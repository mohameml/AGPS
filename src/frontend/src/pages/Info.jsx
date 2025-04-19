// ====== File: ./pages/Info.jsx ======
import React from 'react';
import { Info as InfoIcon, Book, TrendingUp, AlertTriangle, Gift } from 'lucide-react';

export function Info() {
  return (
    <div className="space-y-6">
      <div className="flex items-center space-x-3 mb-6">
        <InfoIcon className="w-6 h-6 text-blue-600" />
        <h1 className="text-2xl font-bold text-gray-900">Structured Product Details</h1>
      </div>

      <div className="bg-white rounded-xl shadow-sm border border-blue-100 p-6">
        <div className="prose max-w-none">
          <h2 className="flex items-center text-xl font-semibold mb-4">
            <Book className="w-5 h-5 mr-2 text-blue-600" />
            Performance Mechanism
          </h2>
          
          <div className="space-y-4">
            <div className="p-4 bg-blue-50 rounded-lg">
              <h3 className="font-medium text-blue-800 mb-2">Reference Indices</h3>
              <ul className="list-disc pl-6">
                <li>ASX 200 (Australia)</li>
                <li>Euro Stoxx 50 (Eurozone)</li>
                <li>FTSE 100 (United Kingdom)</li>
                <li>S&P 500 (United States)</li>
                <li>TOPIX (Japan)</li>
              </ul>
            </div>

            <h3 className="flex items-center text-lg font-semibold mt-6">
              <TrendingUp className="w-5 h-5 mr-2 text-blue-600" />
              Calculation Formula
            </h3>
            <ol className="list-decimal pl-6 space-y-4">
              <li>
                <strong>Initial Net Asset Value (NAV):</strong> €1000 at T0
                <div className="text-sm text-gray-600 mt-1">(Closing prices of indices at T0)</div>
              </li>
              
              <li>
                <strong>Annual Selection:</strong>
                <ul className="list-disc pl-6 mt-2">
                  <li>At each Ti (T1 to Tc), keep the index with best performance</li>
                  <li>Performance capped at +15% and floored at -15%</li>
                </ul>
              </li>

              <li>
                <strong>Final Value at Tc:</strong>
                <div className="bg-gray-50 p-3 rounded-md mt-2 font-mono">
                  Final NAV = 1000 × (1 + 60% × Σ Selected Performances)
                </div>
                <div className="text-red-600 text-sm mt-2">
                  <AlertTriangle className="inline w-4 h-4 mr-1" />
                  Capital Protection: Minimum 80% of Initial NAV (€800)
                </div>
              </li>
            </ol>

            <div className="p-4 bg-green-50 rounded-lg mt-6">
              <h3 className="flex items-center font-medium text-green-800 mb-2">
                <Gift className="w-5 h-5 mr-2" />
                Dividend Mechanism
              </h3>
              <p>
                At each Ti (T1 to T4):<br/>
                If the <strong>worst performing</strong> remaining index has positive performance:<br/>
                <span className="font-bold text-green-700">Dividend = 100 × Performance (%)</span>
              </p>
            </div>
          </div>

          <h3 className="flex items-center text-lg font-semibold mt-8 mb-4">
            <AlertTriangle className="w-5 h-5 mr-2 text-blue-600" />
            Key Features
          </h3>
          <ul className="list-disc pl-6 space-y-2">
            <li>Total duration: 5 years (T0 to T5)</li>
            <li>Annual rebalancing with index elimination</li>
            <li>Maximum exposure: 60% of global performance</li>
            <li>Capital protection at 80% at maturity</li>
          </ul>
        </div>
      </div>
    </div>
  );
}