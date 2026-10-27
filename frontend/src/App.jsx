import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import LoginPage from './components/LoginPage';
import ExecutiveOverview from './components/ExecutiveOverview';
import MultiTargetPredictor from './components/MultiTargetPredictor';
import SmartUpsellEngine from './components/SmartUpsellEngine';
import KitchenDemandForecaster from './components/KitchenDemandForecaster';
import WhatIfSimulator from './components/WhatIfSimulator';
import AIFloatingGuide from './components/AIFloatingGuide';
import { Database, Cpu, Lock, Crown } from 'lucide-react';

export default function App() {
  const [currentUser, setCurrentUser] = useState(() => {
    const saved = localStorage.getItem('pizza_auth_user');
    if (!saved) return null;
    try {
      const parsed = JSON.parse(saved);
      if (parsed.role === 'admin' || (parsed.name && parsed.name.includes('Alex'))) {
        parsed.name = 'Admin';
        localStorage.setItem('pizza_auth_user', JSON.stringify(parsed));
      }
      return parsed;
    } catch {
      return null;
    }
  });

  const [activeTab, setActiveTab] = useState('overview');
  const [analyticsData, setAnalyticsData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [isAIGuideOpen, setIsAIGuideOpen] = useState(false);

  useEffect(() => {
    if (currentUser) {
      fetch('/api/analytics/kpis')
        .then((res) => res.json())
        .then((data) => {
          setAnalyticsData(data);
          setLoading(false);
        })
        .catch((err) => {
          console.error('Failed to load analytics', err);
          setLoading(false);
        });
    }
  }, [currentUser]);

  const handleLogout = () => {
    localStorage.removeItem('pizza_auth_user');
    localStorage.removeItem('pizza_auth_token');
    setCurrentUser(null);
    setActiveTab('overview');
  };

  // If not logged in, render the login page
  if (!currentUser) {
    return <LoginPage onLoginSuccess={(user) => setCurrentUser(user)} />;
  }

  const isAdmin = currentUser.role === 'admin';

  return (
    <div className="min-h-screen flex flex-col justify-between bg-[#f8fafc] text-slate-900">
      <div>
        <Navbar 
          activeTab={activeTab} 
          setActiveTab={setActiveTab} 
          currentUser={currentUser} 
          onLogout={handleLogout} 
          onOpenAIGuide={() => setIsAIGuideOpen((prev) => !prev)}
        />

        <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-16">
          {activeTab === 'overview' && (
            <ExecutiveOverview data={analyticsData} loading={loading} />
          )}

          {activeTab === 'predictor' && <MultiTargetPredictor />}

          {activeTab === 'upsell' && <SmartUpsellEngine />}

          {activeTab === 'inventory' && <KitchenDemandForecaster />}

          {activeTab === 'whatif' && (
            isAdmin ? (
              <WhatIfSimulator />
            ) : (
              <div className="bg-white p-12 rounded-3xl border border-slate-200 shadow-sm text-center max-w-xl mx-auto space-y-4 my-8">
                <div className="w-14 h-14 rounded-2xl bg-amber-50 border border-amber-200 text-amber-600 flex items-center justify-center mx-auto">
                  <Lock className="w-7 h-7" />
                </div>
                <h3 className="text-2xl font-bold text-slate-900 font-['Outfit']">
                  Executive Admin Access Required
                </h3>
                <p className="text-xs text-slate-500 leading-relaxed">
                  The 'What-If' Pricing & Margin Elasticity Simulator contains sensitive strategic financial controls reserved for store executives and decision makers.
                </p>
                <div className="pt-2">
                  <button
                    onClick={handleLogout}
                    className="px-5 py-2.5 rounded-xl bg-orange-600 hover:bg-orange-700 text-white text-xs font-bold shadow-md shadow-orange-500/20 hover:scale-105 transition-all cursor-pointer flex items-center gap-2 mx-auto"
                  >
                    <Crown className="w-4 h-4" /> Switch to Admin Account
                  </button>
                </div>
              </div>
            )
          )}
        </main>
      </div>

      {/* Footer */}
      <footer className="border-t border-slate-200 py-8 mt-12 bg-white">
        <div className="max-w-7xl mx-auto px-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-500">
          <div className="flex items-center gap-2">
            <span className="font-bold text-slate-800">Pizza MDW Intelligence Suite</span>
            <span>•</span>
            <span>Logged in as <strong className="text-slate-800">{currentUser.name}</strong> ({currentUser.role})</span>
          </div>

          <div className="flex items-center gap-4">
            <span className="flex items-center gap-1.5 text-slate-600">
              <Database className="w-3.5 h-3.5 text-orange-600" /> Star Schema Fact Grain
            </span>
            <span className="flex items-center gap-1.5 text-slate-600">
              <Cpu className="w-3.5 h-3.5 text-emerald-600" /> Random Forest & Apriori
            </span>
          </div>
        </div>
      </footer>

      {/* Floating AI Features Guide Widget */}
      <AIFloatingGuide 
        activeTab={activeTab} 
        setActiveTab={setActiveTab} 
        isOpen={isAIGuideOpen} 
        setIsOpen={setIsAIGuideOpen} 
      />
    </div>
  );
}
