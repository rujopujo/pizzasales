import React, { useState, useEffect } from 'react';
import { 
  Boxes, 
  Activity, 
  AlertTriangle, 
  CheckCircle2, 
  Sparkles, 
  Clock, 
  TrendingUp, 
  Wheat, 
  Flame,
  Layers,
  ChefHat
} from 'lucide-react';
import { AreaChart, Area, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

export default function KitchenDemandForecaster() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/inventory/forecast')
      .then((res) => {
        if (!res.ok) {
          return fetch('/api/predict/inventory');
        }
        return res;
      })
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then((d) => {
        if (d && d.timeline && Array.isArray(d.ingredients)) {
          setData(d);
        }
        setLoading(false);
      })
      .catch((err) => {
        console.error('Failed to load inventory forecast', err);
        setLoading(false);
      });
  }, []);

  if (loading || !data) {
    return (
      <div className="flex items-center justify-center min-h-[400px]">
        <div className="flex flex-col items-center gap-3 bg-white/80 backdrop-blur-xl p-8 rounded-3xl border border-slate-200/80 shadow-lg">
          <div className="w-10 h-10 border-4 border-amber-500/20 border-t-amber-600 rounded-full animate-spin" />
          <p className="text-slate-500 text-xs font-semibold">Running Temporal Demand Clustering…</p>
        </div>
      </div>
    );
  }

  const { timeline, ingredients, projected_total_pizzas, waste_reduction_savings } = data;

  return (
    <div className="space-y-8 animate-fadeIn">
      {/* Header */}
      <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-orange-50 border border-orange-200 text-orange-700 text-xs font-bold uppercase tracking-wider mb-2">
            <Boxes className="w-3.5 h-3.5" />
            Supply Chain & Perishables Intelligence
          </div>
          <h2 className="text-2xl lg:text-3xl font-extrabold text-slate-900 font-['Outfit']">
            Kitchen Demand & <span className="text-orange-600">Ingredient Forecaster</span>
          </h2>
          <p className="text-slate-500 text-xs">
            Translates hourly sales velocity into raw material burn rates, predicting stockout risks and minimizing food waste.
          </p>
        </div>

        <div className="flex items-center gap-3">
          <div className="px-4 py-2 rounded-2xl bg-slate-50 border border-slate-200 text-right">
            <span className="text-[10px] uppercase font-bold text-slate-500 block">24h Forecasted Volume</span>
            <span className="text-xl font-black text-slate-900 font-['Outfit']">
              {projected_total_pizzas} Pizzas
            </span>
          </div>
        </div>
      </div>

      {/* 24-Hour Production Velocity Chart */}
      <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs">
        <div className="flex items-center justify-between mb-6">
          <div>
            <h3 className="text-base font-bold text-slate-900 flex items-center gap-2">
              <Activity className="w-4 h-4 text-orange-600" />
              Next 24-Hour Production Curve (Hourly Oven Load)
            </h3>
            <p className="text-xs text-slate-500">Predicted pizza throughput by time of day</p>
          </div>
          <span className="text-xs px-3 py-1 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200 font-semibold">
            {waste_reduction_savings}
          </span>
        </div>

        <div className="h-[220px] w-full">
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart data={timeline} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
              <defs>
                <linearGradient id="invGradientLight" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#f59e0b" stopOpacity={0.25} />
                  <stop offset="95%" stopColor="#f59e0b" stopOpacity={0.0} />
                </linearGradient>
              </defs>
              <XAxis dataKey="hour_label" stroke="#94a3b8" fontSize={11} tickLine={false} />
              <YAxis stroke="#94a3b8" fontSize={11} tickLine={false} />
              <Tooltip 
                contentStyle={{ backgroundColor: '#ffffff', borderColor: '#fed7aa', borderRadius: '12px', boxShadow: '0 4px 12px rgba(0,0,0,0.06)' }}
                formatter={(val) => [`${val} Pizzas`, 'Projected Prep']}
              />
              <Area 
                type="monotone" 
                dataKey="projected_pizzas" 
                stroke="#f59e0b" 
                strokeWidth={2.5} 
                fillOpacity={1} 
                fill="url(#invGradientLight)" 
              />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Raw Ingredients Burn Rate Cards */}
      <div className="space-y-4">
        <h3 className="text-base font-bold text-slate-900 flex items-center gap-2">
          <Wheat className="w-4 h-4 text-amber-600" />
          Perishable Inventory Depletion & Stockout Risk
        </h3>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {ingredients?.map((ing, idx) => (
            <div
              key={idx}
              className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs space-y-4 hover:border-orange-300 transition-all"
            >
              <div className="flex items-start justify-between">
                <div>
                  <h4 className="text-sm font-extrabold text-slate-900 leading-tight">{ing.name}</h4>
                  <span className="text-xs text-slate-500 mt-1 block">
                    Burn Rate: <strong className="text-orange-600">{ing.needed_24h}</strong> / 24 hrs
                  </span>
                </div>
                <span
                  className={`text-[10px] px-2.5 py-0.5 rounded-full font-bold uppercase tracking-wider ${
                    ing.badge_color === 'emerald'
                      ? 'bg-emerald-50 text-emerald-700 border border-emerald-200'
                      : 'bg-amber-50 text-amber-700 border border-amber-200'
                  }`}
                >
                  {ing.status}
                </span>
              </div>

              {/* Progress Bar */}
              <div className="space-y-1.5">
                <div className="flex justify-between text-xs text-slate-500">
                  <span>Stock Buffer</span>
                  <span className="font-bold text-slate-800">{ing.current_stock} available</span>
                </div>
                <div className="w-full bg-slate-100 rounded-full h-2 overflow-hidden">
                  <div
                    className={`h-full rounded-full ${
                      ing.stock_pct > 80 ? 'bg-emerald-500' : 'bg-amber-500'
                    }`}
                    style={{ width: `${Math.min(100, ing.stock_pct)}%` }}
                  />
                </div>
              </div>

              <div className="p-3 rounded-xl bg-slate-50 border border-slate-200 text-[11px] text-slate-600">
                📋 <strong>Manager Action:</strong> {ing.action}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}