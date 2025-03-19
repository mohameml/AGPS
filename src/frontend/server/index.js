import express from 'express';
import cors from 'cors';

const app = express();
const port = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

// --- Constantes et fonctions utilitaires ---
const INDICES = {
  ASX200: 'ASX200',
  EUROSTOXX50: 'EUROSTOXX50',
  FTSE100: 'FTSE100',
  SP500: 'SP500',
  TOPIX: 'TOPIX'
};

function formatIndexName(name) {
  switch (name) {
    case INDICES.ASX200: return 'ASX 200';
    case INDICES.EUROSTOXX50: return 'EURO STOXX 50';
    case INDICES.FTSE100: return 'FTSE 100';
    case INDICES.SP500: return 'S&P 500';
    case INDICES.TOPIX: return 'TOPIX';
    default: return name;
  }
}

// --- Données mock statiques pour une date connue ---
const MOCK_DATA = {
  '2009-01-05': {
    portfolio: {
      cash: 150000,
      [INDICES.EUROSTOXX50]: { quantity: 1000, price: 3500.25, foreignPrice: 3500.25 },
      [INDICES.SP500]: { quantity: 500, price: 4200.75, foreignPrice: 4800.50 },
      [INDICES.FTSE100]: { quantity: 750, price: 7100.30, foreignPrice: 6300.20 },
      [INDICES.ASX200]: { quantity: 300, price: 6800.15, foreignPrice: 7200.45 },
      [INDICES.TOPIX]: { quantity: 450, price: 1900.80, foreignPrice: 210000.0 }
    },
    output: {
      pnl: 2.35,
      [INDICES.EUROSTOXX50]: { after: 1050 }, // Seulement les nouvelles quantités
      [INDICES.SP500]: { after: 480 },
      [INDICES.FTSE100]: { after: 770 },
      [INDICES.ASX200]: { after: 320 },
      [INDICES.TOPIX]: { after: 430 }
    }
  }
};

// --- Fonction pour simuler le rééquilibrage ---
function simulateRebalancing(currentPortfolio) {
  return Object.entries(currentPortfolio).reduce((acc, [name, details]) => {
    if (name === 'cash') {
      acc[name] = details; // On ne modifie pas le cash
    } else {
      const change = Math.random() * 0.2 - 0.1; // Changement aléatoire entre -10% et +10%
      acc[name] = {
        ...details,
        quantity: details.quantity * (1 + change) // Appliquer le changement
      };
    }
    return acc;
  }, {});
}

// --- Endpoint POST "/api/hedge" ---
app.post('/api/hedge', (req, res) => {
  const { date = '2009-01-05', compos = {} } = req.body;

  // Récupérer les données mock ou générer des données aléatoires
  const data = MOCK_DATA[date] || {
    portfolio: Object.values(INDICES).reduce((acc, name) => {
      acc[name] = {
        quantity: parseFloat((Math.random() * 1000).toFixed(6)),
        price: parseFloat((Math.random() * 100).toFixed(6)),
        foreignPrice: parseFloat((Math.random() * 100).toFixed(6))
      };
      return acc;
    }, { cash: 1000 }),
    output: {
      pnl: parseFloat((Math.random() * 20 - 10).toFixed(3)),
      ...Object.values(INDICES).reduce((acc, name) => {
        acc[name] = { after: parseFloat((Math.random() * 1000).toFixed(6)) };
        return acc;
      }, {})
    }
  };

  // Si un rééquilibrage est demandé, simuler les changements
  if (Object.keys(compos).length > 0) {
    data.portfolio = simulateRebalancing(data.portfolio);
    data.output = Object.entries(data.portfolio).reduce((acc, [name, details]) => {
      if (name !== 'cash') {
        acc[name] = { after: details.quantity };
      }
      return acc;
    }, { pnl: data.output.pnl });
  }

  // Structure réponse pour le frontend
  const response = {
    data: {
      portfolio: data.portfolio,
      output: data.output
    }
  };

  console.log(`POST /api/hedge - Date: ${date}`, compos);
  res.json(response);
});

// --- Endpoint GET "/api/next-day" ---
app.get('/api/next-day', (req, res) => {
  const date = new Date(req.query.date || '2009-01-05');
  date.setDate(date.getDate() + 1);
  const nextDate = date.toISOString().split('T')[0];

  const data = MOCK_DATA[nextDate] || {
    portfolio: Object.values(INDICES).reduce((acc, name) => {
      acc[name] = {
        quantity: parseFloat((Math.random() * 1000).toFixed(6)),
        price: parseFloat((Math.random() * 100).toFixed(6)),
        foreignPrice: parseFloat((Math.random() * 100).toFixed(6))
      };
      return acc;
    }, { cash: 1000 }),
    output: {
      pnl: parseFloat((Math.random() * 20 - 10).toFixed(3)),
      ...Object.values(INDICES).reduce((acc, name) => {
        acc[name] = { after: parseFloat((Math.random() * 1000).toFixed(6)) };
        return acc;
      }, {})
    }
  };

  const response = {
    data: {
      portfolio: data.portfolio,
      output: data.output
    }
  };

  console.log(`GET /api/next-day - New date: ${nextDate}`);
  res.json(response);
});

app.listen(port, () => {
  console.log(`Mock server running on http://localhost:${port}`);
});