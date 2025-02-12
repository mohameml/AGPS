import React, { useState } from 'react';
import { ChevronRight, Calendar } from 'lucide-react';

export function DateSelector({ date, onDateChange }) {
  const [inputDate, setInputDate] = useState(date);

  const handleNextDay = () => {
    const nextDay = new Date(date);
    nextDay.setDate(nextDay.getDate() + 1);
    const formattedDate = nextDay.toISOString().split('T')[0];
    onDateChange(formattedDate);
  };

  const handleDateSubmit = () => {
    if (inputDate && inputDate.match(/^\d{4}-\d{2}-\d{2}$/)) {
      onDateChange(inputDate);
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-blue-100 p-6">
      <div className="flex justify-between items-center">
        <div className="flex items-center space-x-3">
          <Calendar className="w-5 h-5 text-blue-600" />
          <span className="text-lg font-medium text-gray-900">
            Current date: {date}
          </span>
        </div>
        <div className="flex items-center space-x-4">
          <button
            onClick={handleNextDay}
            className="flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
          >
            Next Day
            <ChevronRight className="w-4 h-4 ml-1" />
          </button>
          <div className="flex items-center space-x-2">
            <input
              type="text"
              value={inputDate}
              onChange={(e) => setInputDate(e.target.value)}
              placeholder="YYYY-MM-DD"
              className="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            />
            <button
              onClick={handleDateSubmit}
              className="px-4 py-2 bg-gray-800 text-white rounded-lg hover:bg-gray-900 transition-colors"
            >
              Go
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}