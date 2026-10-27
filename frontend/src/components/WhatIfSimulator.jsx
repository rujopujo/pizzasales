import React, { useState, useEffect } from 'react';
import { 
  TrendingUp, 
  TrendingDown, 
  Sliders
} from 'lucide-react';

export default function WhatIfSimulator() {
  const [priceDelta, setPriceDelta] = useState(5.0);
  const [peakDiscount, setPeakDiscount] = useState(10.0);
  const [marketingBoost, setMarketingBoost] = useState(15.0);
  const [costInflation, setCostInflation] = useState(3.0);

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const runSimulation = async () => {
    setLoading(true);
    try {
      const res = await fetch('/api/predict/what-if', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          price_delta_pct: parseFloat(priceDelta),
          peak_discount_pct: parseFloat(peakDiscount),
          marketing_boost_pct: parseFloat(marketingBoost),
          cost_inflation_pct: parseFloat(costInflation),
        }),
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    runSimulation();
  }, [priceDelta, peakDiscount, marketingBoost, costInflation]);

  return (
    <div className="space-y-8 animate-fadeIn">
      {/* Header */}
      <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-orange-50 border border-orange-200 text-orange-700 text-xs font-bold uppercase tracking-wider mb-2">
            <Sliders className="w-3.5 h-3.5" />
            Pricing Elasticity & Scenario Modeling
          </div>
          <h2 className="text-2xl lg:text-3xl font-extrabold text-slate-900 font-['Outfit']">
            Executive <span className="text-orange-600">'What-If' Scenario Simulator</span>
          </h2>
          <p className="text-slate-500 text-xs">
            Test business strategies before deploying them in the real world: simulate price changes, inflation, marketing campaigns, and happy hour discounts.
          </p>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={() => {
              setPriceDelta(0);
              setPeakDiscount(0);
              setMarketingBoost(0);
              setCostInflation(0);
            }}
            className="px-3 py-2 rounded-xl text-xs font-bold bg-slate-50 border border-slate-200 text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition-all cursor-pointer"
          >
            Reset to Baseline
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
        {/* Sliders Input Panel (5 Cols) */}
        <div className="lg:col-span-5 bg-white p-6 rounded-2xl border border-slate-200 shadow-xs space-y-6">
          <h3 className="text-base font-bold text-slate-900 flex items-center gap-2 border-b border-slate-100 pb-4">
            <Sliders className="w-4 h-4 text-orange-600" />
            Macroeconomic & Strategy Levers
          </h3>

          {/* Price Change */}
          <div className="space-y-2">
            <div className="flex justify-between items-center text-xs">
              <label className="font-semibold text-slate-700">Base Menu Price Adjustment</label>
              <span className={`font-bold px-2 py-0.5 rounded-lg border ${
                priceDelta >= 0 
                  ? 'text-emerald-700 bg-emerald-50 border-emerald-200' 
                  : 'text-rose-700 bg-rose-50 border-rose-200'
              }`}>
                {priceDelta > 0 ? `+${priceDelta}%` : `${priceDelta}%`}
              </span>
            </div>
            <input
              type="range"
              min="-25"
              max="25"
              step="1"
              value={priceDelta}
              onChange={(e) => setPriceDelta(e.target.value)}
              className="w-full accent-orange-600 bg-slate-200 h-2 rounded-lg cursor-pointer"
            />
            <p className="text-[10px] text-slate-400">Fast-casual elasticity coefficient: -1.35</p>
          </div>

          {/* Peak Discount */}
          <div className="space-y-2">
            <div className="flex justify-between items-center text-xs">
              <label className="font-semibold text-slate-700">Peak Lunch Special Discount</label>
              <span className="font-bold text-amber-700 bg-amber-50 px-2 py-0.5 rounded-lg border border-amber-200">
                {peakDiscount}% Off
              </span>
            </div>
            <input
              type="range"
              min="0"
              max="30"
              step="1"
              value={peakDiscount}
              onChange={(e) => setPeakDiscount(e.target.value)}
              className="w-full accent-amber-500 bg-slate-200 h-2 rounded-lg cursor-pointer"
            />
            <p className="text-[10px] text-slate-400">Stimulates off-peak volume (+0.8x traffic multiplier)</p>
          </div>

          {/* Marketing Boost */}
          <div className="space-y-2">
            <div className="flex justify-between items-center text-xs">
              <label className="font-semibold text-slate-700">Marketing & Local Ad Boost</label>
              <span className="font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-lg border border-emerald-200">
                +{marketingBoost}% Demand
              </span>
            </div>
            <input
              type="range"
              min="0"
              max="50"
              step="5"
              value={marketingBoost}
              onChange={(e) => setMarketingBoost(e.target.value)}
              className="w-full accent-emerald-600 bg-slate-200 h-2 rounded-lg cursor-pointer"
            />
          </div>

          {/* Cost Inflation */}
          <div className="space-y-2">
            <div className="flex justify-between items-center text-xs">
              <label className="font-semibold text-slate-700">Ingredient Cost Inflation (COGS)</label>
              <span className="font-bold text-rose-700 bg-rose-50 px-2 py-0.5 rounded-lg border border-rose-200">
                +{costInflation}%
              </span>
            </div>
            <input
              type="range"
              min="0"
              max="20"
              step="1"
              value={costInflation}
              onChange={(e) => setCostInflation(e.target.value)}
              className="w-full accent-rose-500 bg-slate-200 h-2 rounded-lg cursor-pointer"
            />
          </div>
        </div>

        {/* Projection Results (7 Cols) */}
        <div className="lg:col-span-7 space-y-6">
          {/* Executive Verdict Badge */}
          <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs space-y-3">
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold uppercase tracking-wider text-slate-500">
                AI Scenario Strategy Assessment
              </span>
              <span className={`text-xs px-3 py-1 rounded-full font-bold uppercase tracking-wider ${
                result?.badge_color === 'emerald'
                  ? 'bg-emerald-50 text-emerald-700 border border-emerald-200'
                  : result?.badge_color === 'amber'
                  ? 'bg-amber-50 text-amber-700 border border-amber-200'
                  : 'bg-rose-50 text-rose-700 border border-rose-200'
              }`}>
                {result?.verdict}
              </span>
            </div>

            <p className="text-sm font-semibold text-slate-800">
              {result?.executive_comment}
            </p>
          </div>

          {/* Big Delta Metrics */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
            {/* Projected Revenue */}
            <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs">
              <span className="text-xs text-slate-500 font-semibold uppercase tracking-wider block">
                Projected Total Revenue
              </span>
              <div className="flex items-baseline gap-2 mt-2">
                <h4 className="text-3xl font-black text-slate-900 font-['Outfit']">
                  ${result?.projected_revenue?.toLocaleString()}
                </h4>
              </div>
              <div className="mt-2 flex items-center gap-1.5 text-xs font-bold">
                {result?.revenue_delta >= 0 ? (
                  <span className="text-emerald-600 flex items-center gap-0.5">
                    <TrendingUp className="w-3.5 h-3.5" /> +${result?.revenue_delta?.toLocaleString()} (+{result?.revenue_delta_pct}%)
                  </span>
                ) : (
                  <span className="text-rose-600 flex items-center gap-0.5">
                    <TrendingDown className="w-3.5 h-3.5" /> -${Math.abs(result?.revenue_delta)?.toLocaleString()} ({result?.revenue_delta_pct}%)
                  </span>
                )}
                <span className="text-slate-400">vs baseline</span>
              </div>
            </div>

            {/* Projected Gross Profit */}
            <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs">
              <span className="text-xs text-slate-500 font-semibold uppercase tracking-wider block">
                Projected Net Gross Profit
              </span>
              <div className="flex items-baseline gap-2 mt-2">
                <h4 className="text-3xl font-black text-amber-600 font-['Outfit']">
                  ${result?.projected_gross_profit?.toLocaleString()}
                </h4>
              </div>
              <div className="mt-2 flex items-center gap-1.5 text-xs font-bold">
                {result?.profit_delta >= 0 ? (
                  <span className="text-emerald-600 flex items-center gap-0.5">
                    <TrendingUp className="w-3.5 h-3.5" /> +${result?.profit_delta?.toLocaleString()} profit gain
                  </span>
                ) : (
                  <span className="text-rose-600 flex items-center gap-0.5">
                    <TrendingDown className="w-3.5 h-3.5" /> -${Math.abs(result?.profit_delta)?.toLocaleString()} margin hit
                  </span>
                )}
              </div>
            </div>
          </div>

          {/* Volume Delta & Baseline Comparison */}
          <div className="p-4 rounded-xl bg-slate-50 border border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs">
            <span className="text-slate-700">
              📦 Order Velocity: <strong>{result?.projected_orders?.toLocaleString()} orders</strong> ({result?.orders_delta_pct > 0 ? `+${result?.orders_delta_pct}%` : `${result?.orders_delta_pct}%`})
            </span>
            <span className="text-slate-500">
              Baseline: ${result?.base_revenue?.toLocaleString()} across {result?.base_orders?.toLocaleString()} orders
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}
