import express from 'express';
import cors from 'cors';

const app = express();
const port = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

// Mock data for different dates
const mockData = {
  '2009-01-05': {
    portfolio: {
      data: [
        { name: 'REUR', quantity: '1000.000000', price: '0.028300', foreignPrice: '0.028300', total: '1000.000000' },
        { name: 'RUSD', quantity: '0.000000', price: '0.010879', foreignPrice: '0.014800', total: '0.000000' },
        { name: 'RHKD', quantity: '0.000000', price: '0.001295', foreignPrice: '0.013650', total: '0.000000' },
        { name: 'Eurotaxa50', quantity: '0.000000', price: '2553.410000', foreignPrice: '2553.410000', total: '0.000000' },
      ]
    },
    stats: {
      pnl: -8.451,
      portfolioValue: 1104.287,
      liquidativeValue: 1206.225,
      flows: [
        { date: '2009-01-05', value: 1000 },
        { date: '2010-01-04', value: -20 },
        { date: '2011-01-04', value: -30 },
        { date: '2012-01-04', value: -25 },
        { date: '2013-01-04', value: -20 }
      ]
    },
    rebalancing: {
      rebalancing: [
        { name: 'Eurostoxx50', previousQuantity: '0.000000', newQuantity: '0.08376319082136002' },
        { name: 'HANGSENG', previousQuantity: '0.000000', newQuantity: '0.153208856188453' },
        { name: 'S&P500', previousQuantity: '0.000000', newQuantity: '0.31622078747820914' },
        { name: 'RHKD', previousQuantity: '0.000000', newQuantity: '-2414.7621401627403' },
        { name: 'RUSD', previousQuantity: '0.000000', newQuantity: '-297.18579654286276' },
      ]
    }
  },
  '2009-01-06': {
    portfolio: {
      data: [
        { name: 'REUR', quantity: '800.000000', price: '0.029100', foreignPrice: '0.029100', total: '800.000000' },
        { name: 'RUSD', quantity: '200.000000', price: '0.011200', foreignPrice: '0.015200', total: '200.000000' },
        { name: 'RHKD', quantity: '100.000000', price: '0.001350', foreignPrice: '0.014100', total: '100.000000' },
        { name: 'Eurotaxa50', quantity: '0.100000', price: '2600.000000', foreignPrice: '2600.000000', total: '260.000000' },
      ]
    },
    stats: {
      pnl: -5.321,
      portfolioValue: 1360.000,
      liquidativeValue: 1400.225,
      flows: [
        { date: '2009-01-05', value: 1000 },
        { date: '2009-01-06', value: 300 }
      ]
    },
    rebalancing: {
      rebalancing: [
        { name: 'Eurostoxx50', previousQuantity: '0.100000', newQuantity: '0.150000' },
        { name: 'HANGSENG', previousQuantity: '0.000000', newQuantity: '0.200000' },
        { name: 'S&P500', previousQuantity: '0.000000', newQuantity: '0.400000' },
        { name: 'RHKD', previousQuantity: '100.000000', newQuantity: '-2000.000000' },
        { name: 'RUSD', previousQuantity: '200.000000', newQuantity: '-250.000000' },
      ]
    }
  },
  '2009-01-07': {
    portfolio: {
      data: [
        { name: 'REUR', quantity: '1000.000000', price: '0.028300', foreignPrice: '0.028300', total: '1000.000000' },
        { name: 'RUSD', quantity: '0.000000', price: '0.010879', foreignPrice: '0.014800', total: '0.000000' },
        { name: 'RHKD', quantity: '0.000000', price: '0.001295', foreignPrice: '0.013650', total: '0.000000' },
        { name: 'Eurotaxa50', quantity: '0.000000', price: '2553.410000', foreignPrice: '2553.410000', total: '0.000000' },
      ]
    },
    stats: {
      pnl: +7.00,
      portfolioValue: 1104.287,
      liquidativeValue: 1206.225,
      flows: [
        { date: '2009-01-05', value: 1000 },
        { date: '2010-01-04', value: -20 },
        { date: '2011-01-04', value: -30 },
        { date: '2012-01-04', value: -25 },
        { date: '2013-01-04', value: -20 }
      ]
    },
    rebalancing: {
      rebalancing: [
        { name: 'Eurostoxx50', previousQuantity: '0.0005', newQuantity: '0.08376319082136002' },
        { name: 'HANGSENG', previousQuantity: '0.09', newQuantity: '0.153208856188453' },
        { name: 'S&P500', previousQuantity: '0.05', newQuantity: '0.31622078747820914' },
        { name: 'RHKD', previousQuantity: '0.000000', newQuantity: '-2414.7621401627403' },
        { name: 'RUSD', previousQuantity: '-285.00005555', newQuantity: '-297.18579654286276' },
      ]
    }
  }
};

// Single endpoint that returns all data for a given date
app.get('/api/priceAndDeltas', (req, res) => {
  const date = req.query.date || '2009-01-05';
  const data = mockData[date] || mockData['2009-01-05']; // Fallback to default date if not found
  res.json(data);
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});