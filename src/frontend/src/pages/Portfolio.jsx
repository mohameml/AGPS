import React, { useState, useEffect } from 'react';
import { DateSelector } from '../components/DateSelector';
import { PortfolioTable } from '../components/PortfolioTable';
import { Stats } from '../components/Stats';
import { api } from '../lib/api';

export function Portfolio() {
  const [date, setDate] = useState('2010-01-04');
  const [portfolioData, setPortfolioData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchData() {
      try {
        setLoading(true);
        const response = await api.getPortfolio(date);
        setPortfolioData(response.portfolio.data || []);
        setError(null);
      } catch (err) {
        setError('Failed to fetch portfolio data');
        console.error('Error:', err);
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, [date]);

  const handleDateChange = (newDate) => {
    setDate(newDate);
  };

  return (
    <div className="space-y-6">
      <DateSelector date={date} onDateChange={handleDateChange} />
      {error && (
        <div className="bg-red-50 text-red-600 p-4 rounded-lg">
          {error}
        </div>
      )}
      {loading ? (
        <div className="text-center py-12">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4 text-gray-600">Loading portfolio data...</p>
        </div>
      ) : (
        <>
          <PortfolioTable data={portfolioData} currentDate={date} setPortfolioData={setPortfolioData}/>
          <Stats date={date} />
        </>
      )}
    </div>
  );
}