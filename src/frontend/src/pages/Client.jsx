import React from 'react';
import { User, Mail, Phone, MapPin } from 'lucide-react';

export function Client() {
  const clientInfo = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    phone: '+33 6 12 34 56 78',
    address: '123 Avenue des Champs-Élysées, Paris',
    accountNumber: 'FR76 3000 1007 1234 5678 9012 345',
    portfolioValue: '€1,245,678.90',
    lastLogin: '2025-01-22 14:30'
  };

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900 mb-6">Client Information</h1>

      <div className="bg-white rounded-xl shadow-sm border border-blue-100 p-6">
        <div className="grid grid-cols-2 gap-6">
          <div className="space-y-4">
            <div className="flex items-center space-x-3">
              <User className="w-5 h-5 text-blue-600" />
              <div>
                <div className="text-sm text-gray-500">Name</div>
                <div className="font-medium">{clientInfo.name}</div>
              </div>
            </div>
            <div className="flex items-center space-x-3">
              <Mail className="w-5 h-5 text-blue-600" />
              <div>
                <div className="text-sm text-gray-500">Email</div>
                <div className="font-medium">{clientInfo.email}</div>
              </div>
            </div>
            <div className="flex items-center space-x-3">
              <Phone className="w-5 h-5 text-blue-600" />
              <div>
                <div className="text-sm text-gray-500">Phone</div>
                <div className="font-medium">{clientInfo.phone}</div>
              </div>
            </div>
            <div className="flex items-center space-x-3">
              <MapPin className="w-5 h-5 text-blue-600" />
              <div>
                <div className="text-sm text-gray-500">Address</div>
                <div className="font-medium">{clientInfo.address}</div>
              </div>
            </div>
          </div>

          <div className="space-y-4">
            <div>
              <div className="text-sm text-gray-500">Account Number</div>
              <div className="font-medium font-mono">{clientInfo.accountNumber}</div>
            </div>
            <div>
              <div className="text-sm text-gray-500">Portfolio Value</div>
              <div className="font-medium">{clientInfo.portfolioValue}</div>
            </div>
            <div>
              <div className="text-sm text-gray-500">Last Login</div>
              <div className="font-medium">{clientInfo.lastLogin}</div>
            </div>
          </div>
        </div>
      </div>

      <div className="bg-white rounded-xl shadow-sm border border-blue-100 p-6">
        <h2 className="text-lg font-medium text-gray-900 mb-4">Account Activity</h2>
        <div className="h-64 bg-gray-50 rounded-lg flex items-center justify-center text-gray-500">
          Activity timeline placeholder
        </div>
      </div>
    </div>
  );
}