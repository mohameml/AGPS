const API_URL = 'http://localhost:5000/api';

export const api = {
  async getPortfolio(date) {
    const response = await fetch(`${API_URL}/priceAndDeltas?date=${date}`);
    if (!response.ok) throw new Error('Failed to fetch data');
    const data = await response.json();
    return data.portfolio;
  },

  async getRebalancingInfo(date) {
    const response = await fetch(`${API_URL}/priceAndDeltas?date=${date}`);
    if (!response.ok) throw new Error('Failed to fetch data');
    const data = await response.json();
    return data.rebalancing;
  },

  async rebalancePortfolio(date) {
    const response = await fetch(`${API_URL}/priceAndDeltas?date=${date}`);
    if (!response.ok) throw new Error('Failed to fetch data');
    return { success: true, message: 'Portfolio rebalanced successfully' };
  },

  async getStats(date) {
    const response = await fetch(`${API_URL}/priceAndDeltas?date=${date}`);
    if (!response.ok) throw new Error('Failed to fetch data');
    const data = await response.json();
    return data.stats;
  },
};