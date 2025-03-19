import React, { useState } from 'react';
import { Eye, ArrowRight, X, AlertCircle } from 'lucide-react';
import { api } from '../lib/api';

export function PortfolioTable({ data, currentDate }) {
  const [showRebalancing, setShowRebalancing] = useState(false);
  const [rebalancingData, setRebalancingData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);


  const saveCurrentPortfolio = () => {
    localStorage.setItem('previousPortfolio', JSON.stringify(data));
  };

  const handleRebalanceInfo = async () => {
    try {
      setLoading(true);
  
      // Récupérer les données de rééquilibrage depuis le backend
      const response = await api.getRebalancingInfo(currentDate);
  
      // Récupérer les quantités précédentes depuis le localStorage
      const previousPortfolio = JSON.parse(localStorage.getItem('previousPortfolio')) || [];
  
      // Combiner les données du backend avec les quantités précédentes
      const updatedRebalancing = response.rebalancing.map(item => ({
        ...item,
        previousQuantity: previousPortfolio.find(p => p.name === item.name)?.quantity || 0
      }));
  
      // Mettre à jour l'état avec les données combinées
      setRebalancingData(updatedRebalancing);
      setShowRebalancing(true);
      setError(null);
    } catch (err) {
      setError('Failed to fetch rebalancing information');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleRebalance = async () => {
    try {
      const response = await api.rebalancePortfolio(date, data);
      // Utiliser response.data.output.deltas pour les changements
      window.location.reload();
    } catch (err) {
      setError("Failed to rebalance portfolio");
    }
  };

  const previousPortfolio = JSON.parse(localStorage.getItem('previousPortfolio')) || [];


  

  return (
    <div className="bg-white rounded-xl shadow-sm border border-blue-100 overflow-hidden">
      <div className="p-6">
        <h2 className="text-xl font-semibold text-gray-900 mb-6">Portfolio Information</h2>
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead>
              <tr className="bg-gray-50">
                <th className="px-6 py-3 text-left text-sm font-semibold text-gray-600">Product</th>
                <th className="px-6 py-3 text-left text-sm font-semibold text-gray-600">Quantity</th>
                <th className="px-6 py-3 text-left text-sm font-semibold text-gray-600">Price (€)</th>
                <th className="px-6 py-3 text-left text-sm font-semibold text-gray-600">Foreign Price</th>
                <th className="px-6 py-3 text-left text-sm font-semibold text-gray-600">Total</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200">
              {data.map((item, index) => (
                <tr key={index} className="hover:bg-gray-50 transition-colors">
                  <td className="px-6 py-4 text-sm">{item.name}</td>
                  <td className="px-6 py-4 text-sm font-mono">{item.quantity.toFixed(2)}</td>
                  <td className="px-6 py-4 text-sm font-mono">{item.price.toFixed(2)}</td>
                  <td className="px-6 py-4 text-sm font-mono">{item.foreignPrice.toFixed(2)}</td>
                  <td className="px-6 py-4 text-sm font-mono">{(item.quantity * item.price).toFixed(2)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {error && (
          <div className="mt-4 p-4 bg-red-50 text-red-600 rounded-lg flex items-center">
            <AlertCircle className="w-5 h-5 mr-2" />
            {error}
          </div>
        )}

        <div className="mt-6 flex gap-4">
          <button
            onClick={handleRebalanceInfo}
            disabled={loading}
            className="btn btn-primary flex items-center"
          >
            <Eye className="w-4 h-4 mr-2" />
            Rebalancing Info
          </button>
          <button
            onClick={handleRebalance}
            disabled={loading}
            className="btn btn-secondary flex items-center"
          >
            Rebalance
            <ArrowRight className="w-4 h-4 ml-2" />
          </button>
        </div>
      </div>

      {showRebalancing && rebalancingData && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center p-4">
          <div className="bg-white rounded-xl shadow-xl max-w-3xl w-full max-h-[90vh] overflow-y-auto">
            <div className="p-6">
              <div className="flex justify-between items-center mb-6">
                <h3 className="text-xl font-semibold text-gray-900">
                  Rebalancing Information
                </h3>
                <button
                  onClick={() => setShowRebalancing(false)}
                  className="text-gray-400 hover:text-gray-600"
                >
                  <X className="w-6 h-6" />
                </button>
              </div>
              <table className="w-full">
                <thead>
                  <tr className="bg-gray-50">
                    <th className="px-6 py-3 text-left text-sm font-semibold text-gray-600">Product</th>
                    <th className="px-6 py-3 text-left text-sm font-semibold text-gray-600">Previous Qty</th>
                    <th className="px-6 py-3 text-left text-sm font-semibold text-gray-600">New Qty</th>
                    <th className="px-6 py-3 text-left text-sm font-semibold text-gray-600">Change</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-200">
                  {rebalancingData.map((item, index) => (
                    <tr key={index} className="hover:bg-gray-50">
                      <td className="px-6 py-4 text-sm">{item.name}</td>
                      <td className="px-6 py-4 text-sm font-mono">{item.previousQuantity.toFixed(2)}</td>
                      <td className="px-6 py-4 text-sm font-mono">{item.newQuantity.toFixed(2)}</td>
                      <td className="px-6 py-4 text-sm font-mono">
                        <span className={item.newQuantity - item.previousQuantity >= 0 ? 'text-green-600' : 'text-red-600'}>
                          {(item.newQuantity - item.previousQuantity).toFixed(2)}
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}