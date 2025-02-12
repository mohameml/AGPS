import React, { useState, useEffect } from 'react';
import { TrendingUp, TrendingDown, DollarSign } from 'lucide-react';
import { api } from '../lib/api';

export function Stats({ date }) {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchStats() {
      try {
        setLoading(true);
        const data = await api.getStats(date);
        setStats(data);
        setError(null);
      } catch (err) {
        setError('Failed to fetch statistics');
        console.error('Error:', err);
      } finally {
        setLoading(false);
      }
    }

    fetchStats();
  }, [date]);

  if (loading) {
    return (
      <div className="grid grid-cols-3 gap-6">
        {[1, 2, 3].map((i) => (
          <div key={i} className="bg-white rounded-xl shadow-sm border border-blue-100 p-6 animate-pulse">
            <div className="h-4 bg-gray-200 rounded w-1/3 mb-4"></div>
            <div className="h-8 bg-gray-200 rounded w-1/2"></div>
          </div>
        ))}
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-red-50 text-red-600 p-4 rounded-lg">
        {error}
      </div>
    );
  }

  if (!stats) return null;

  return (
    <div className="space-y-6">
      <div className="grid grid-cols-3 gap-6">
        <div className="bg-white rounded-xl shadow-sm border border-blue-100 p-6">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-gray-500 font-medium">P&L</h3>
            {stats.pnl >= 0 ? (
              <TrendingUp className="w-5 h-5 text-green-500" />
            ) : (
              <TrendingDown className="w-5 h-5 text-red-500" />
            )}
          </div>
          <div className={`text-2xl font-bold ${
            stats.pnl >= 0 ? 'text-green-600' : 'text-red-600'
          }`}>
            {stats.pnl}%
          </div>
        </div>

        <div className="bg-white rounded-xl shadow-sm border border-blue-100 p-6">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-gray-500 font-medium">Portfolio Value</h3>
            <DollarSign className="w-5 h-5 text-blue-500" />
          </div>
          <div className="text-2xl font-bold">
            {stats.portfolioValue.toLocaleString('fr-FR', {
              style: 'currency',
              currency: 'EUR'
            })}
          </div>
        </div>

        <div className="bg-white rounded-xl shadow-sm border border-blue-100 p-6">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-gray-500 font-medium">Liquidative Value</h3>
            <DollarSign className="w-5 h-5 text-blue-500" />
          </div>
          <div className="text-2xl font-bold">
            {stats.liquidativeValue.toLocaleString('fr-FR', {
              style: 'currency',
              currency: 'EUR'
            })}
          </div>
        </div>
      </div>

      <div className="bg-white rounded-xl shadow-sm border border-blue-100 p-6">
        <h3 className="text-lg font-semibold text-gray-900 mb-6">Cash Flows History</h3>
        <div className="relative h-64">
          <div className="absolute inset-0">
            {stats.flows.map((flow, index) => {
              const maxValue = Math.max(...stats.flows.map(f => Math.abs(f.value)));
              const scale = 200 / maxValue; // 200px max height
              const height = Math.abs(flow.value) * scale;
              const left = `${(index / (stats.flows.length - 1)) * 100}%`;

              return (
                <div
                  key={index}
                  className="absolute bottom-0 transform -translate-x-1/2"
                  style={{ left }}
                >
                  <div
                    className={`w-12 ${flow.value >= 0 ? 'bg-blue-500' : 'bg-red-500'}`}
                    style={{ height: `${height}px` }}
                  >
                    <div className="absolute bottom-0 left-1/2 transform -translate-x-1/2 text-white text-sm pb-1">
                      {flow.value}
                    </div>
                  </div>
                  <div className="absolute top-full mt-2 left-1/2 transform -translate-x-1/2 text-sm text-gray-600">
                    {flow.date}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}