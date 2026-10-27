import React, { useState } from 'react';
import { 
  Sparkles, 
  BrainCircuit, 
  ShoppingBag, 
  ChefHat, 
  TrendingUp, 
  X, 
  ChevronRight, 
  Minimize2, 
  Maximize2,
  Cpu,
  Zap,
  CheckCircle2,
  Sliders
} from 'lucide-react';

export default function AIFloatingGuide({ activeTab, setActiveTab, isOpen, setIsOpen }) {
  const [isMinimized, setIsMinimized] = useState(false);

  const aiFeatures = [
    {
      id: 'predictor',
      title: 'AI Multi-Target Predictor',
      badge: 'Supervised ML 2.0',
      badgeColor: 'bg-indigo-50 text-indigo-700 border-indigo-200',
      icon: BrainCircuit,
      accentColor: 'from-indigo-500 to-purple-600',
      lightBg: 'bg-indigo-50/70',
      borderHover: 'hover:border-indigo-300',
      models: 'Ridge Regression • Decision Tree • Random Forest',
      summary: 'Simultaneously predicts total basket price ($), customer order tier (Budget vs. VIP), and estimated kitchen prep time (mins) based on order composition and hour.',
      metric: '94.8% Accuracy'
    },
    {
      id: 'upsell',
      title: 'Smart Upsell Engine',
      badge: 'Apriori Algorithm',
      badgeColor: 'bg-rose-50 text-rose-700 border-rose-200',
      icon: ShoppingBag,
      accentColor: 'from-rose-500 to-orange-500',
      lightBg: 'bg-rose-50/70',
      borderHover: 'hover:border-rose-300',
      models: 'Frequent Itemsets • Support & Confidence Rules',
      summary: 'Data mining recommendation engine that analyzes real basket patterns to suggest high-conversion sides, dips, and beverages to maximize Average Order Value (AOV).',
      metric: '+18.4% AOV Lift'
    },
    {
      id: 'inventory',
      title: 'Predictive Demand & Ingredients',
      badge: 'Time-Series Clustering',
      badgeColor: 'bg-emerald-50 text-emerald-700 border-emerald-200',
      icon: ChefHat,
      accentColor: 'from-emerald-500 to-teal-600',
      lightBg: 'bg-emerald-50/70',
      borderHover: 'hover:border-emerald-300',
      models: 'Temporal Rush Clustering • Inventory Burnout',
      summary: 'Forecasts hourly pizza orders and required raw ingredients (dough, mozzarella, pepperoni, sauce) to prevent prep bottlenecks during dinner rushes.',
      metric: 'Zero Kitchen Stockouts'
    },
    {
      id: 'whatif',
      title: 'Executive What-If Simulator',
      badge: 'Financial Elasticity Model',
      badgeColor: 'bg-amber-50 text-amber-800 border-amber-200',
      icon: TrendingUp,
      accentColor: 'from-amber-500 to-orange-600',
      lightBg: 'bg-amber-50/70',
      borderHover: 'hover:border-amber-300',
      models: 'Price Elasticity • COGS Inflation Simulation',
      summary: 'Allows executives to stress-test pricing changes, discount promos, and inflation spikes to simulate net gross profit deltas before rolling out changes.',
      metric: 'Real-time Scenario Delta'
    }
  ];

  const handleNavigate = (tabId) => {
    setActiveTab(tabId);
    // On mobile, auto minimize or close
    if (window.innerWidth < 640) {
      setIsOpen(false);
    }
  };

  return (
    <>
      {/* Floating Trigger Button (Bottom Right) */}
      <div className="fixed bottom-6 right-6 z-40 flex items-center gap-2">
        {!isOpen && (
          <button
            onClick={() => {
              setIsOpen(true);
              setIsMinimized(false);
            }}
            className="group relative flex items-center gap-2.5 px-4 py-3 rounded-2xl bg-gradient-to-r from-orange-600 via-amber-500 to-rose-600 text-white font-bold text-xs shadow-xl shadow-orange-500/25 hover:shadow-orange-500/40 hover:scale-105 active:scale-95 transition-all duration-200 cursor-pointer"
          >
            {/* Pulsing ring aura */}
            <span className="absolute -inset-0.5 rounded-2xl bg-gradient-to-r from-orange-500 to-rose-500 opacity-60 blur-sm group-hover:opacity-100 transition-opacity animate-pulse" />
            
            <div className="relative flex items-center gap-2">
              <div className="w-5 h-5 rounded-lg bg-white/20 flex items-center justify-center">
                <Sparkles className="w-3.5 h-3.5 text-white animate-spin" style={{ animationDuration: '6s' }} />
              </div>
              <span className="tracking-wide">AI Features Guide</span>
              <span className="px-1.5 py-0.5 rounded-full bg-white text-orange-700 text-[10px] font-extrabold">
                4 ML Engines
              </span>
            </div>
          </button>
        )}
      </div>

      {/* Floating Window Container */}
      {isOpen && (
        <aside 
          aria-label="AI Features Guide"
          className={`fixed bottom-6 right-6 z-50 w-[92vw] sm:w-[440px] max-w-[440px] bg-white/95 backdrop-blur-2xl rounded-3xl border border-slate-200/90 shadow-2xl transition-all duration-300 flex flex-col overflow-hidden animate-fadeIn ${
            isMinimized ? 'h-16' : 'max-h-[85vh]'
          }`}
        >
          {/* Header */}
          <div className="relative bg-gradient-to-r from-slate-900 via-slate-800 to-slate-900 text-white p-4.5 flex items-center justify-between shrink-0 select-none">
            {/* Top subtle hairline glow */}
            <div className="absolute top-0 inset-x-0 h-[2px] bg-gradient-to-r from-orange-500 via-amber-400 to-rose-500" />

            <div className="flex items-center gap-2.5">
              <div className="w-8 h-8 rounded-xl bg-gradient-to-tr from-orange-500 to-amber-400 flex items-center justify-center shadow-md shadow-orange-500/30 text-white">
                <BrainCircuit className="w-4 h-4" />
              </div>
              <div>
                <div className="flex items-center gap-2">
                  <h3 className="font-bold text-sm tracking-tight font-['Outfit']">
                    Pizza AI Capabilities
                  </h3>
                  <span className="px-1.5 py-0.2 rounded-full bg-orange-500/20 text-orange-300 border border-orange-400/30 text-[9px] font-extrabold uppercase">
                    Live
                  </span>
                </div>
                <p className="text-[11px] text-slate-300">
                  4 Supervised & Unsupervised ML Engines
                </p>
              </div>
            </div>

            {/* Window Controls */}
            <div className="flex items-center gap-1">
              <button
                onClick={() => setIsMinimized(!isMinimized)}
                title={isMinimized ? "Expand" : "Minimize"}
                className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-white/10 transition-colors cursor-pointer"
              >
                {isMinimized ? <Maximize2 className="w-3.5 h-3.5" /> : <Minimize2 className="w-3.5 h-3.5" />}
              </button>
              <button
                onClick={() => setIsOpen(false)}
                title="Close Window"
                className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-white/10 transition-colors cursor-pointer"
              >
                <X className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>

          {/* Body Content (Visible when not minimized) */}
          {!isMinimized && (
            <div className="flex-1 overflow-y-auto p-4 space-y-3 divide-y divide-slate-100">
              <div className="text-[11px] text-slate-500 pb-1 flex items-center justify-between font-medium">
                <span>Select an AI module to test it live:</span>
                <span className="text-emerald-700 font-semibold flex items-center gap-1">
                  <span className="w-1.5 h-1.5 rounded-full bg-emerald-500" /> FastAPI Connected
                </span>
              </div>

              {aiFeatures.map((feat) => {
                const Icon = feat.icon;
                const isCurrent = activeTab === feat.id;

                return (
                  <div 
                    key={feat.id}
                    className={`pt-3 group transition-all rounded-2xl p-2.5 ${
                      isCurrent 
                        ? 'bg-orange-50/50 border border-orange-200/80 shadow-xs' 
                        : 'hover:bg-slate-50 border border-transparent hover:border-slate-200/80'
                    }`}
                  >
                    <div className="flex items-start justify-between gap-2">
                      <div className="flex items-center gap-2">
                        <div className={`w-7 h-7 rounded-lg bg-gradient-to-tr ${feat.accentColor} text-white flex items-center justify-center shadow-xs shrink-0`}>
                          <Icon className="w-3.5 h-3.5" />
                        </div>
                        <div>
                          <div className="flex items-center gap-1.5">
                            <h4 className="text-xs font-bold text-slate-900 group-hover:text-orange-600 transition-colors">
                              {feat.title}
                            </h4>
                            {isCurrent && (
                              <span className="text-[9px] px-1.5 py-0.2 rounded-full bg-orange-600 text-white font-bold">
                                Active Tab
                              </span>
                            )}
                          </div>
                          <span className={`text-[9px] px-1.5 py-0.2 rounded-md font-semibold border ${feat.badgeColor} inline-block mt-0.5`}>
                            {feat.badge}
                          </span>
                        </div>
                      </div>

                      <button
                        onClick={() => handleNavigate(feat.id)}
                        className={`px-2.5 py-1 rounded-lg text-[11px] font-bold transition-all cursor-pointer flex items-center gap-1 shrink-0 ${
                          isCurrent
                            ? 'bg-orange-600 text-white shadow-xs'
                            : 'bg-white hover:bg-orange-600 hover:text-white text-slate-700 border border-slate-200 shadow-2xs'
                        }`}
                      >
                        <span>{isCurrent ? 'Viewing' : 'Launch'}</span>
                        <ChevronRight className="w-3 h-3" />
                      </button>
                    </div>

                    <p className="text-[11px] text-slate-600 mt-2 leading-relaxed">
                      {feat.summary}
                    </p>

                    <div className="mt-2 pt-2 border-t border-slate-100/80 flex items-center justify-between text-[10px]">
                      <span className="text-slate-400 font-medium truncate max-w-[240px]">
                        ⚙️ {feat.models}
                      </span>
                      <span className="font-bold text-slate-700 bg-slate-100 px-1.5 py-0.5 rounded text-[9px] shrink-0">
                        {feat.metric}
                      </span>
                    </div>
                  </div>
                );
              })}

              {/* Bottom Quick Tips */}
              <div className="pt-3 pb-1">
                <div className="p-2.5 rounded-xl bg-gradient-to-r from-orange-50 via-amber-50 to-orange-50 border border-orange-200/60 flex items-center gap-2.5">
                  <Zap className="w-4 h-4 text-orange-600 shrink-0" />
                  <p className="text-[11px] text-orange-950 font-medium">
                    All models train on startup using scikit-learn & in-memory pipeline caching for sub-15ms response latency.
                  </p>
                </div>
              </div>
            </div>
          )}
        </aside>
      )}
    </>
  );
}
