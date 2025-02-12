import React from 'react';
import { LineChart } from 'lucide-react';

export function Header() {
  return (
    <header className="bg-gradient-to-r from-blue-600 to-indigo-600 text-white py-4 px-8 shadow-lg">
      <div className="max-w-7xl mx-auto flex justify-between items-center">
        <div className="flex items-center space-x-3">
          <LineChart className="w-8 h-8" />
          <div>
            <h1 className="text-2xl font-bold">Portfolio Management</h1>
            <p className="text-blue-100 text-sm">Real-time market analysis</p>
          </div>
        </div>
        <div className="flex items-center space-x-6">
          <div className="text-sm">
            <span className="text-blue-100">Market Status:</span>
            <span className="ml-2 bg-green-500 text-white px-2 py-1 rounded-full text-xs">
              Open
            </span>
          </div>
          <div className="font-medium">Equipe 6</div>
        </div>
      </div>
    </header>
  );
}