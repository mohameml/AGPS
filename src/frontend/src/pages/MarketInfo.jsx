import React from 'react';
import { LineChart, TrendingUp, TrendingDown } from 'lucide-react';

export function MarketInfo() {
  const marketData = [
    {
      name: 'Eurostoxx 50',
      value: '4,521.13',
      change: '+1.2%',
      trend: 'up'
    },
    {
      name: 'S&P 500',
      value: '4,783.45',
      change: '-0.3%',
      trend: 'down'
    },
    {
      name: 'Hang Seng',
      value: '16,624.84',
      change: '+2.1%',
      trend: 'up'
    }
  ];

  return (
    <div className="space-y-6">
      <div className="flex items-center space-x-3 mb-6">
        <LineChart className="w-6 h-6 text-blue-600" />
        <h1 className="text-2xl font-bold text-gray-900">Market Information</h1>
      </div>

      <div className="grid grid-cols-3 gap-6">
        {marketData.map((item, index) => (
          <div key={index} className="bg-white rounded-xl shadow-sm border border-blue-100 p-6">
            <h3 className="text-lg font-medium text-gray-900 mb-4">{item.name}</h3>
            <div className="text-2xl font-bold mb-2">{item.value}</div>
            <div className={`flex items-center ${
              item.trend === 'up' ? 'text-green-600' : 'text-red-600'
            }`}>
              {item.trend === 'up' ? (
                <TrendingUp className="w-5 h-5 mr-2" />
              ) : (
                <TrendingDown className="w-5 h-5 mr-2" />
              )}
              {item.change}
            </div>
          </div>
        ))}
      </div>

      <div className="bg-white rounded-xl shadow-sm border border-blue-100 p-6">
        <h2 className="text-lg font-medium text-gray-900 mb-4">Market Overview</h2>
        <div className="h-96 bg-gray-50 rounded-lg flex items-center justify-center text-gray-500">
          Chart placeholder
        </div>
      </div>
    </div>
  );
}