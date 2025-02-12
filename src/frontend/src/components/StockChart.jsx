import React from 'react';
import { Glasses as MagnifyingGlass, Home, Settings } from 'lucide-react';

export function StockChart() {
  return (
    <div className="bg-white rounded-lg shadow p-6">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-xl font-semibold">EUROSTOXX 50</h2>
        <div className="flex items-center gap-2">
          <span className="text-sm text-gray-500">Stock Price Movement</span>
          <div className="flex gap-1">
            <button className="p-1 hover:bg-gray-100 rounded">
              <MagnifyingGlass className="w-4 h-4 text-gray-600" />
            </button>
            <button className="p-1 hover:bg-gray-100 rounded">
              <Home className="w-4 h-4 text-gray-600" />
            </button>
            <button className="p-1 hover:bg-gray-100 rounded">
              <Settings className="w-4 h-4 text-gray-600" />
            </button>
          </div>
        </div>
      </div>
      <div className="h-[400px] relative">
        {/* Ici, vous pouvez intégrer une bibliothèque de graphiques comme Chart.js ou Recharts */}
        <img 
          src="https://images.unsplash.com/photo-1642790106117-e829e14a795f?auto=format&fit=crop&w=800&h=400"
          alt="Stock chart"
          className="w-full h-full object-cover rounded"
        />
      </div>
    </div>
  );
}