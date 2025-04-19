const API_URL = 'http://localhost:3000';

const INDICES = {
  ASX200: 'ASX200',
  EUROSTOXX50: 'EUROSTOXX50',
  FTSE100: 'FTSE100',
  SP500: 'SP500',
  TOPIX: 'TOPIX'
};

const formatIndexName = (name) => {
  switch (name) {
    case INDICES.ASX200: return 'ASX 200';
    case INDICES.EUROSTOXX50: return 'EURO STOXX 50';
    case INDICES.FTSE100: return 'FTSE 100';
    case INDICES.SP500: return 'S&P 500';
    case INDICES.TOPIX: return 'TOPIX';
    default: return name;
  }
};

export const api = {
  async getPortfolio(date) {
    try {
      // 1. Récupérer les données du portefeuille
      const hedgeResponse = await fetch(`${API_URL}/hedge`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          date: `${date}T00:00:00`,
          isFirstTime: false,
          currDate: `${date}T00:00:00`,
          cash: 1000,
          compos: {}
        })
      });
      const hedgeData = await hedgeResponse.json();
      if (!hedgeResponse.ok) throw new Error(hedgeData.message);

      // 2. Récupérer les prix
      const nextDayResponse = await fetch(`${API_URL}/next-day`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ date: `${date}T00:00:00` })
      });
      const nextDayData = await nextDayResponse.json();
      if (!nextDayResponse.ok || !nextDayData.data) {
        throw new Error('Données de prix invalides');
      }

      // 3. Formater les données avec conversion des devises
      return {
        portfolio: {
          data: Object.entries(hedgeData.data.portfolio.compositions)
            .filter(([key]) => Object.keys(INDICES).includes(key))
            .map(([backendName, quantity]) => {
              const indexData = nextDayData.data.dict_index_price[backendName] || {};
              const currency = indexData.currency || 'EUR';
              const localPrice = indexData.price || 0;
              const exchangeRate = nextDayData.data.dict_exchange_rate[currency]?.rate || 1;
              const eurPrice = localPrice * exchangeRate;

              return {
                name: formatIndexName(backendName),
                quantity,
                price: eurPrice,
                foreignPrice: localPrice,
                total: quantity * eurPrice
              };
            }),
          cash: hedgeData.data.portfolio.cash
        }
      };

    } catch (error) {
      console.error('Erreur Portfolio:', error);
      throw new Error('Échec du chargement : ' + error.message);
    }
  },

  async rebalancePortfolio(date, currentPortfolio) {
    try {
      // Convertir les noms frontend -> backend
      if (!currentPortfolio || typeof currentPortfolio !== 'object') {
        throw new Error('Portfolio data format invalide');
      }
  
      // Conversion corrigée
      const backendCompos = Object.keys(currentPortfolio).reduce((acc, name) => {
        const backendName = Object.keys(INDICES).find(k => 
          formatIndexName(k) === name
        );
        if (backendName) acc[backendName] = currentPortfolio[name];
        return acc;
      }, {});

      // Exécuter le rééquilibrage
      const hedgeResponse = await fetch(`${API_URL}/hedge`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          date: `${date}T00:00:00`,
          isFirstTime: false,
          currDate: `${date}T00:00:00`,
          cash: 1000,
          compos: backendCompos
        })
      });
      const hedgeData = await hedgeResponse.json();
      if (!hedgeResponse.ok) throw new Error(hedgeData.message);

      return { status: "success", message: "Portfolio rebalanced successfully" };

    } catch (error) {
      console.error('Erreur Rééquilibrage:', error);
      throw new Error('Échec : ' + error.message);
    }
  },

  // ====== Fichier : ./lib/api.js ======
async getRebalancingInfo(date) {
    try {
      const response = await fetch(`${API_URL}/hedge`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          date: `${date}T00:00:00`,
          isFirstTime: false,
          currDate: `${date}T00:00:00`,
          cash: 1000,
          compos: {}
        })
      });
      const data = await response.json();
      
      // Extraction corrigée des données
      return {
        rebalancing: Object.entries(INDICES).map(([backendName]) => ({
          name: formatIndexName(backendName),
          previousQuantity: data.data?.portfolio?.compositions?.[backendName] || 0,
          newQuantity: data.data?.output?.deltas?.[backendName] || 0
        }))
      };
    } catch (error) {
      console.error('Erreur Rebalancing Info:', error);
      throw error;
    }
  },

  async getStats(date) {
    try {
      // Récupération des prix
      const priceResponse = await fetch(`${API_URL}/next-day`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ date: `${date}T00:00:00` })
      });
      const priceData = await priceResponse.json();
      if (!priceData.data) throw new Error('Données de prix manquantes');

      // Récupération du portefeuille
      const portfolioResponse = await fetch(`${API_URL}/hedge`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          date: `${date}T00:00:00`,
          isFirstTime: false,
          currDate: `${date}T00:00:00`,
          cash: 1000,
          compos: {}
        })
      });
      const portfolioData = await portfolioResponse.json();

      // Calculs
      const portfolioValue = Object.entries(portfolioData.data.portfolio.compositions)
        .reduce((sum, [name, qty]) => {
          const indexData = priceData.data.dict_index_price[name] || {};
          const currency = indexData.currency || 'EUR';
          const localPrice = indexData.price || 0;
          const exchangeRate = priceData.data.dict_exchange_rate[currency]?.rate || 1;
          return sum + (qty * localPrice * exchangeRate);
        }, 0);

      return {
        pnl: portfolioData.data.output?.pnl || 0,
        portfolioValue,
        liquidativeValue: portfolioValue + portfolioData.data.portfolio.cash
      };

    } catch (error) {
      console.error('Erreur Statistiques:', error);
      throw new Error('Statistiques indisponibles : ' + error.message);
    }
  }
};