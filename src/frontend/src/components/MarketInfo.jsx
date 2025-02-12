import React from 'react';
import { LineChart } from 'lucide-react';

const IndexCard = ({ name, dailyPerf, sixMonthPerf, yearPerf }) => (
  <div className="bg-blue-100 p-4 rounded-lg">
    <h3 className="font-medium mb-2">Index name</h3>
    <p>{name}</p>
    <div className="space-y-1 mt-2">
      <div>
        <div className="text-sm text-gray-600">Daily performance (in %)</div>
        <div className={`font-medium ${dailyPerf >= 0 ? 'text-green-600' : 'text-red-600'}`}>
          {dailyPerf}
        </div>
      </div>
      <div>
        <div className="text-sm text-gray-600">6-months performance (in %)</div>
        <div className={`font-medium ${sixMonthPerf >= 0 ? 'text-green-600' : 'text-red-600'}`}>
          {sixMonthPerf}
        </div>
      </div>
      <div>
        <div className="text-sm text-gray-600">Year performance (in %)</div>
        <div className={`font-medium ${yearPerf >= 0 ? 'text-green-600' : 'text-red-600'}`}>
          {yearPerf}
        </div>
      </div>
    </div>
  </div>
);

export function MarketInfo() {
  const indices = [
    {
      name: 'Eurostoxx 50',
      dailyPerf: 0.67,
      sixMonthPerf: -18.75,
      yearPerf: -31.98
    },
    {
      name: 'S&P 500',
      dailyPerf: -0.47,
      sixMonthPerf: -23.66,
      yearPerf: -29.23
    },
    {
      name: 'Hang Seng',
      dailyPerf: 3.46,
      sixMonthPerf: -26.50,
      yearPerf: -28.47
    }
  ];

  return (
    <div className="bg-white rounded-lg shadow p-6 mb-6">
      <div className="flex items-center gap-2 mb-4">
        <LineChart className="w-5 h-5 text-blue-600" />
        <h2 className="text-xl font-semibold">Market Information</h2>
      </div>
      <div className="grid grid-cols-3 gap-4">
        {indices.map((index, i) => (
          <IndexCard key={i} {...index} />
        ))}
      </div>
    </div>
  );
}