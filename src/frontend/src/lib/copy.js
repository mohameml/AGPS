// Modifiez le fichier ./lib/api.js pour ajouter le mode mock

const API_URL = 'http://localhost:5000/api';
const USE_MOCK = true; // Activer le mode mock

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

// Données mock pour les tests
const MOCK_DATA = {
  portfolio: {
    cash: 150000,
    EUROSTOXX50: {
      quantity: 1000,
      price: 3500.25,
      foreignPrice: 3500.25
    },
    SP500: {
      quantity: 500,
      price: 4200.75,
      foreignPrice: 4800.50
    },
    FTSE100: {
      quantity: 750,
      price: 7100.30,
      foreignPrice: 6300.20
    },
    ASX200: {
      quantity: 300,
      price: 6800.15,
      foreignPrice: 7200.45
    },
    TOPIX: {
      quantity: 450,
      price: 1900.80,
      foreignPrice: 210000.0
    }
  },
  output: {
    pnl: 2.35,
    EUROSTOXX50: {
      before: 1000,
      after: 1050
    },
    SP500: {
      before: 500,
      after: 480
    },
    FTSE100: {
      before: 750,
      after: 770
    },
    ASX200: {
      before: 300,
      after: 320
    },
    TOPIX: {
      before: 450,
      after: 430
    }
  }
};

export const api = {
  async getPortfolio(date) {
    if (USE_MOCK) {
      // Version mock
      return {
        portfolio: {
          data: Object.entries(MOCK_DATA.portfolio)
            .filter(([key]) => key !== 'cash')
            .map(([name, details]) => ({
              name: formatIndexName(name),
              quantity: details.quantity || 0,
              price: details.price || 0,
              foreignPrice: details.foreignPrice || 0,
              total: (details.quantity || 0) * (details.price || 0)
            }))
        }
      };
    }
    
    try {
      // Version originale
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

      if (!response.ok) throw new Error('Failed to fetch portfolio data');
      const data = await response.json();

      // Transform the portfolio data to match the frontend structure
      const portfolioData = {
        portfolio: {
          data: Object.entries(data.data.portfolio)
            .filter(([key]) => key !== 'cash')
            .map(([name, details]) => ({
              name: formatIndexName(name),
              quantity: details.quantity || 0,
              price: details.price || 0,
              foreignPrice: details.foreignPrice || 0,
              total: (details.quantity || 0) * (details.price || 0)
            }))
        }
      };

      return portfolioData;
    } catch (error) {
      console.error('API Error:', error);
      throw error;
    }
  },

  async getRebalancingInfo(date) {
    if (USE_MOCK) {
      // Version mock
      return {
        rebalancing: Object.entries(MOCK_DATA.output)
          .filter(([key]) => key !== 'pnl')
          .map(([name, details]) => ({
            name: formatIndexName(name),
            previousQuantity: details.before || 0,
            newQuantity: details.after || 0
          }))
      };
    }
    
    try {
      // Version originale
      const response = await fetch(`${API_URL}/hedge`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          date: date,
          isFirstTime: false,
          currDate: date,
          cash: 1000000,
          compos: {}
        })
      });

      if (!response.ok) throw new Error('Failed to fetch rebalancing data');
      const data = await response.json();

      // Transform the output data to match the frontend structure
      const rebalancingData = {
        rebalancing: Object.entries(data.data.output)
          .filter(([key]) => key !== 'pnl')
          .map(([name, details]) => ({
            name: formatIndexName(name),
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
    if (USE_MOCK) {
      // Version mock - simuler une réussite
      return { status: "success", message: "Portfolio rebalanced successfully" };
    }
    
    try {
      // Version originale
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
    if (USE_MOCK) {
      // Version mock
      const portfolioValue = Object.entries(MOCK_DATA.portfolio)
        .filter(([key]) => key !== 'cash')
        .reduce((sum, [_, details]) => sum + (details.quantity || 0) * (details.price || 0), 0);

      return {
        pnl: MOCK_DATA.output.pnl || 0,
        portfolioValue: portfolioValue,
        liquidativeValue: portfolioValue + MOCK_DATA.portfolio.cash
      };
    }
    
    try {
      // Version originale
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