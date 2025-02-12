import React from 'react';
import { Info as InfoIcon, Book, HelpCircle, Mail } from 'lucide-react';

export function Info() {
  return (
    <div className="space-y-6">
      <div className="flex items-center space-x-3 mb-6">
        <InfoIcon className="w-6 h-6 text-blue-600" />
        <h1 className="text-2xl font-bold text-gray-900">Product Information</h1>
      </div>

      <div className="bg-white rounded-xl shadow-sm border border-blue-100 p-6">
        <div className="prose max-w-none">
          <h2 className="flex items-center text-xl font-semibold mb-4">
            <Book className="w-5 h-5 mr-2 text-blue-600" />
            About This Platform
          </h2>
          <p className="text-gray-600">
            This portfolio management platform provides real-time market data and sophisticated tools
            for managing investment portfolios. It features advanced analytics, automated rebalancing,
            and comprehensive reporting capabilities.
          </p>

          <h3 className="flex items-center text-lg font-semibold mt-6 mb-4">
            <HelpCircle className="w-5 h-5 mr-2 text-blue-600" />
            Key Features
          </h3>
          <ul className="list-disc pl-6 text-gray-600">
            <li>Real-time portfolio tracking and analytics</li>
            <li>Automated portfolio rebalancing</li>
            <li>Market data integration</li>
            <li>Performance reporting and analysis</li>
            <li>Risk management tools</li>
          </ul>

          <h3 className="flex items-center text-lg font-semibold mt-6 mb-4">
            <Mail className="w-5 h-5 mr-2 text-blue-600" />
            Support
          </h3>
          <p className="text-gray-600">
            For technical support or questions about the platform, please contact our support team:
            <br />
            Email: support@example.com
            <br />
            Phone: +33 1 23 45 67 89
          </p>
        </div>
      </div>
    </div>
  );
}