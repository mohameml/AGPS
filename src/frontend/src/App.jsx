import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Header } from './components/Header';
import { Sidebar } from './components/Sidebar';
import { Portfolio } from './pages/Portfolio';
import { MarketInfo } from './pages/MarketInfo';
import { Client } from './pages/Client';
import { Info } from './pages/Info';

function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-50">
        <Header />
        <div className="flex">
          <Sidebar />
          <main className="flex-1 p-8">
            <div className="max-w-7xl mx-auto">
              <Routes>
                <Route path="/" element={<Portfolio />} />
                <Route path="/market" element={<MarketInfo />} />
                <Route path="/client" element={<Client />} />
                <Route path="/info" element={<Info />} />
              </Routes>
            </div>
          </main>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;