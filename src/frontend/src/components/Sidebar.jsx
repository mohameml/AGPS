import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Building2, LineChart, Users, Info, Settings } from 'lucide-react';

export function Sidebar() {
  const location = useLocation();

  const menuItems = [
    {
      icon: Building2,
      title: 'Portfolio',
      description: 'Main page to access your portfolio',
      path: '/'
    },
    {
      icon: Info,
      title: 'Info',
      description: 'Information about this product',
      path: '/info'
    }
  ];

  return (
    <aside className="w-72 bg-white border-r border-gray-200">
      <div className="p-6">
        <div className="mb-8">
          <h2 className="text-xs font-semibold text-gray-400 uppercase tracking-wider">
            Navigation
          </h2>
        </div>
        <nav className="space-y-2">
          {menuItems.map((item, index) => {
            const Icon = item.icon;
            const isActive = location.pathname === item.path;
            return (
              <Link
                key={index}
                to={item.path}
                className={`w-full flex items-start space-x-4 p-3 rounded-lg transition-colors ${
                  isActive
                    ? 'bg-blue-50 text-blue-600'
                    : 'text-gray-600 hover:bg-gray-50'
                }`}
              >
                <Icon className="w-5 h-5 mt-0.5" />
                <div className="flex-1 text-left">
                  <div className="font-medium">{item.title}</div>
                  <div className="text-sm text-gray-500">{item.description}</div>
                </div>
              </Link>
            );
          })}
        </nav>

        <div className="mt-8 pt-8 border-t">
          <button className="w-full flex items-center space-x-3 px-3 py-2 text-gray-600 hover:bg-gray-50 rounded-lg transition-colors">
            <Settings className="w-5 h-5" />
            <span>Settings</span>
          </button>
        </div>
      </div>
    </aside>
  );
}