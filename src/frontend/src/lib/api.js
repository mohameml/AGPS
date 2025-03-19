const API_URL = 'http://localhost:3000';

// Enum des indices correspondant au backend
const INDICES = {
  ASX200: 'ASX200',
  EUROSTOXX50: 'EUROSTOXX50',
  FTSE100: 'FTSE100',
  SP500: 'SP500',
  TOPIX: 'TOPIX'
};

// Fonction utilitaire pour formater les noms des indices
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
      const response = await fetch(`${API_URL}/hedge`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          date: date,
          isFirstTime: false,
          currDate: date,
          cash: 1000,
          compos: {}
        })
      });

    const data = await response.json();
    if (data.status !== "success") throw new Error("API error");
    
    // Adapté à la structure de l'API réelle
    return {
      portfolio: {
        data: Object.entries(data.data.portfolio.compositions).map(([name, quantity]) => ({
          name: formatIndexName(name), 
          quantity,
          price: 0, // À récupérer depuis dict_index_price
          total: quantity * price
        })),
        cash: data.data.portfolio.cash
      }
    };
  },

  async getRebalancingInfo(date) {
    try {
          // {
          //   date: date,
          //   isFirstTime: false,
          //   currDate: date,
          //   cash: 1000,
          //   compos: {}
          // }

      const response = await fetch(`${API_URL}/hedge`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          cash : 0 , 
          compos :  {"EUROSTOXX50": 0.0, "SP500": 0.0, "FTSE100": 0.0, "TOPIX": 0.0, "ASX200": 0.0 , "USD": 0.0, "GBP": 0.0, "JPY": 0.0, "AUD": 0.0},
          date : "2009-05-01T00:00:00",
          isFirstTime : true ,
          currDate : "2009-05-01T00:00:00"
      
      })
      });

      if (!response.ok) throw new Error('Failed to fetch rebalancing data');
      const data = await response.json();

      // Transform the output data to match the frontend structure
      const rebalancingData = {
        rebalancing: Object.entries(data.data.output)
          .filter(([key]) => key !== 'pnl') // Exclude pnl from rebalancing data
          .map(([name, details]) => ({
            name: formatIndexName(name), // Formater le nom de l'indice
            previousQuantity: details.before || 0,
            newQuantity: details.after || 0
          }))
      };

      return rebalancingData;
    } catch (error) {
      console.error('API Error:', error);
      throw error;
    }
  },

  async rebalancePortfolio(date, currentPortfolio) {
    try {
      // Convertir les noms formatés en noms d'indices backend
      const backendCompos = currentPortfolio.reduce((acc, item) => {
        const backendName = Object.entries(INDICES).find(
          ([_, value]) => formatIndexName(value) === item.name
        )?.[1] || item.name;
        
        acc[backendName] = item.quantity;
        return acc;
      }, {});

      const response = await fetch(`${API_URL}/hedge`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          date: date,
          isFirstTime: false,
          currDate: date,
          cash: 1000,
          compos: backendCompos
        })
      });

      if (!response.ok) throw new Error('Failed to rebalance portfolio');
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('API Error:', error);
      throw error;
    }
  },

  async getStats(date) {
    try {
      const response = await fetch(`${API_URL}/hedge`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          date: date,
          isFirstTime: false,
          currDate: date,
          cash: 1000,
          compos: {}
        })
      });

      if (!response.ok) throw new Error('Failed to fetch stats data');
      const data = await response.json();

      // Calculate portfolio value from the portfolio data
      const portfolioValue = Object.entries(data.data.portfolio)
        .filter(([key]) => key !== 'cash')
        .reduce((sum, [_, details]) => sum + (details.quantity || 0) * (details.price || 0), 0);

      // Get cash value
      const cash = data.data.portfolio.cash || 0;

      // Get PnL from output
      const pnl = data.data.output.pnl || 0;

      return {
        pnl: pnl,
        portfolioValue: portfolioValue,
        liquidativeValue: portfolioValue + cash
      };
    } catch (error) {
      console.error('API Error:', error);
      throw error;
    }
  }
};