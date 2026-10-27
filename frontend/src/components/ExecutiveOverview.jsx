import React, { useState } from 'react';
import { 
  DollarSign, 
  ShoppingBag, 
  Pizza, 
  TrendingUp, 
  Award, 
  PieChart as PieIcon,
  Sparkles,
  Download,
  Search,
  Filter,
  CheckCircle2,
  Calendar,
  Layers,
  Activity,
  ArrowUpRight,
  Flame,
  ChevronRight
} from 'lucide-react';
import { 
  AreaChart, 
  Area, 
  XAxis, 
  YAxis, 
  Tooltip, 
  ResponsiveContainer, 
  BarChart, 
  Bar, 
  Cell 
} from 'recharts';

const CATEGORY_COLORS = {
  Classic: '#ea580c', // Warm Ember Orange
  Supreme: '#ef4444', // Red Ruby
  Veggie: '#10b981',  // Emerald Mint
  Chicken: '#f59e0b', // Saffron Amber
};

export default function ExecutiveOverview({ data, loading }) {
  const [selectedCategory, setSelectedCategory] = useState('ALL');
  const [searchQuery, setSearchQuery] = useState('');
  const [timeRange, setTimeRange] = useState('30D');

  if (loading || !data) {
    return (
      <div className="flex items-center justify-center min-h-[500px]">
        <div className="flex flex-col items-center gap-4 bg-white/80 backdrop-blur-xl p-8 rounded-3xl border border-slate-200/80 shadow-lg">
          <div className="relative">
            <div className="w-12 h-12 border-4 border-orange-500/20 border-t-orange-600 rounded-full animate-spin" />
            <div className="absolute inset-0 flex items-center justify-center text-sm font-bold">🍕</div>
          </div>
          <div className="text-center">
            <h4 className="text-sm font-bold text-slate-800">Processing Star Schema OLAP Fact Grain</h4>
            <p className="text-xs text-slate-400 mt-1">Aggregating dimensional cubes & KPI distributions…</p>
          </div>
        </div>
      </div>
    );
  }

  const { kpis, categories, sizes, top_pizzas, daily_trend, recent_transactions } = data;

  // Normalize daily trend so AreaChart reliably finds revenue data
  const chartData = (daily_trend || []).map((d) => ({
    ...d,
    revenue: Number(d.daily_revenue ?? d.revenue ?? 0),
    daily_revenue: Number(d.daily_revenue ?? d.revenue ?? 0),
  }));

  // Normalize top pizzas so total revenue and category render properly
  const normalizedTopPizzas = (top_pizzas || []).map((p) => ({
    ...p,
    revenue: Number(p.total_revenue ?? p.revenue ?? 0),
    category: p.pizza_category ?? p.category,
    unit_price: Number(p.avg_unit_price ?? p.unit_price ?? 0).toFixed(2),
  }));

  // Normalize sizes to compute percentage share
  const totalPizzasInSizes = (sizes || []).reduce((acc, s) => acc + (s.pizzas_sold || 0), 0);
  const normalizedSizes = (sizes || []).map((s) => ({
    ...s,
    orders_count: s.pizzas_sold || 0,
    pct: totalPizzasInSizes > 0 ? Number(((s.pizzas_sold / totalPizzasInSizes) * 100).toFixed(1)) : 0,
  }));

  // Filter transactions
  const filteredTransactions = recent_transactions?.filter((tx) => {
    const matchesCat = selectedCategory === 'ALL' || tx.pizza_category === selectedCategory;
    const matchesSearch = 
      tx.order_id.toLowerCase().includes(searchQuery.toLowerCase()) ||
      tx.pizza_name.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesCat && matchesSearch;
  });

  const exportCSV = () => {
    if (!recent_transactions?.length) return;
    const headers = ["Order ID", "Date", "Time", "Pizza Name", "Category", "Size", "Quantity", "Unit Price", "Total Price", "Tier"];
    const rows = recent_transactions.map(t => [
      t.order_id, t.date_str, t.order_time, `"${t.pizza_name}"`, t.pizza_category, t.pizza_size, t.quantity, t.unit_price, t.total_price, t.order_tier
    ]);
    const csvContent = "data:text/csv;charset=utf-8," + [headers.join(","), ...rows.map(e => e.join(","))].join("\n");
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", `pizza_sales_report_${new Date().toISOString().slice(0, 10)}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const kpiCards = [
    {
      title: 'Gross Revenue',
      subtitle: 'Star Schema Fact Grain',
      value: `$${kpis.total_revenue?.toLocaleString()}`,
      delta: '+14.2%',
      trendLabel: 'vs prior 30d',
      icon: DollarSign,
      gradient: 'from-orange-500 via-amber-500 to-orange-600',
      tagColor: 'text-orange-700 bg-orange-50 border-orange-200/80',
    },
    {
      title: 'Order Velocity',
      subtitle: 'Unique Checkouts',
      value: kpis.total_orders?.toLocaleString(),
      delta: '+8.1%',
      trendLabel: 'conversion rate',
      icon: ShoppingBag,
      gradient: 'from-amber-500 via-orange-500 to-amber-600',
      tagColor: 'text-amber-700 bg-amber-50 border-amber-200/80',
    },
    {
      title: 'Pizzas Baked',
      subtitle: 'Oven Production Volume',
      value: kpis.total_pizzas_sold?.toLocaleString(),
      delta: '3,000+',
      trendLabel: 'unit records analyzed',
      icon: Pizza,
      gradient: 'from-emerald-500 via-teal-500 to-emerald-600',
      tagColor: 'text-emerald-700 bg-emerald-50 border-emerald-200/80',
    },
    {
      title: 'Average Order Value',
      subtitle: 'Basket Revenue Density',
      value: `$${kpis.avg_order_value}`,
      delta: '+$4.85',
      trendLabel: 'smart upsell lift',
      icon: TrendingUp,
      gradient: 'from-indigo-500 via-purple-500 to-indigo-600',
      tagColor: 'text-indigo-700 bg-indigo-50 border-indigo-200/80',
    },
  ];

  return (
    <div className="space-y-7 animate-fadeIn">
      {/* Top Filter & Action Bar */}
      <div className="bg-white rounded-2xl border border-slate-200 shadow-xs p-4 flex flex-col md:flex-row md:items-center justify-between gap-4">
        {/* Category Segmented Control */}
        <div className="flex items-center gap-1.5 flex-wrap">
          <span className="text-[11px] font-bold text-slate-400 uppercase tracking-widest flex items-center gap-1.5 mr-1.5">
            <Filter className="w-3.5 h-3.5 text-orange-600" /> Category:
          </span>
          {['ALL', 'Classic', 'Supreme', 'Veggie', 'Chicken'].map((cat) => (
            <button
              key={cat}
              onClick={() => setSelectedCategory(cat)}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                selectedCategory === cat
                  ? 'bg-gradient-to-r from-orange-600 to-amber-600 text-white shadow-xs shadow-orange-500/20'
                  : 'bg-slate-100/80 text-slate-600 hover:text-slate-900 hover:bg-slate-200/70'
              }`}
            >
              {cat}
            </button>
          ))}
        </div>

        {/* Time Filter & Export */}
        <div className="flex items-center gap-3">
          <div className="flex items-center bg-slate-100/90 p-1 rounded-xl border border-slate-200/70 text-xs font-semibold">
            {['7D', '30D', '90D', 'YTD'].map((t) => (
              <button
                key={t}
                onClick={() => setTimeRange(t)}
                className={`px-2.5 py-1 rounded-lg transition-all cursor-pointer ${
                  timeRange === t ? 'bg-white text-slate-900 shadow-xs font-bold' : 'text-slate-500 hover:text-slate-800'
                }`}
              >
                {t}
              </button>
            ))}
          </div>

          <button
            onClick={exportCSV}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-white hover:bg-slate-50 text-slate-700 border border-slate-200/90 text-xs font-bold shadow-2xs hover:shadow-xs transition-all cursor-pointer"
          >
            <Download className="w-3.5 h-3.5 text-slate-500" />
            <span>Export CSV</span>
          </button>
        </div>
      </div>

      {/* 4 Bento KPI Metric Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {kpiCards.map((kpi, index) => {
          const Icon = kpi.icon;
          return (
            <div 
              key={index} 
              className="bg-white rounded-2xl border border-slate-200 shadow-xs p-5 flex flex-col justify-between"
            >
              <div className="flex items-start justify-between">
                <div>
                  <span className="text-[10px] font-bold tracking-wider uppercase text-slate-400 block mb-0.5">
                    {kpi.subtitle}
                  </span>
                  <h4 className="text-xs font-bold text-slate-700">{kpi.title}</h4>
                </div>
                <div className={`w-8 h-8 rounded-xl bg-gradient-to-tr ${kpi.gradient} text-white flex items-center justify-center shadow-sm`}>
                  <Icon className="w-4 h-4" />
                </div>
              </div>

              <div className="mt-4">
                <div className="text-3xl font-extrabold tracking-tight text-slate-900 font-['Outfit']">
                  {kpi.value}
                </div>
                <div className="flex items-center gap-1.5 mt-2">
                  <span className={`text-[10px] font-extrabold px-1.5 py-0.5 rounded-md border flex items-center gap-0.5 ${kpi.tagColor}`}>
                    <ArrowUpRight className="w-3 h-3" />
                    {kpi.delta}
                  </span>
                  <span className="text-[11px] text-slate-400 font-medium">
                    {kpi.trendLabel}
                  </span>
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {/* Analytics Mid Grid: Area Trend + Category Distribution */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Sales Volume Curve (7 Cols) */}
        <div className="lg:col-span-7 bg-white rounded-2xl border border-slate-200 shadow-xs p-6 flex flex-col justify-between">
          <div className="flex items-center justify-between mb-5">
            <div>
              <div className="flex items-center gap-2">
                <h3 className="text-base font-extrabold text-slate-900 font-['Outfit']">
                  Daily Sales Velocity & Revenue
                </h3>
                <span className="px-2 py-0.5 rounded-full text-[9px] font-extrabold uppercase bg-orange-50 text-orange-700 border border-orange-200">
                  Star Schema Aggregated
                </span>
              </div>
              <p className="text-xs text-slate-400 mt-0.5">
                Time-series revenue fluctuations across 2015 historical transactions
              </p>
            </div>

            <div className="hidden sm:flex items-center gap-3 text-xs text-slate-500 font-semibold">
              <span className="flex items-center gap-1.5">
                <span className="w-2.5 h-2.5 rounded-full bg-orange-500" /> Daily Revenue ($)
              </span>
            </div>
          </div>

          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={chartData}>
                <defs>
                  <linearGradient id="revenueGradient" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stopColor="#ea580c" stopOpacity={0.35} />
                    <stop offset="60%" stopColor="#f59e0b" stopOpacity={0.08} />
                    <stop offset="100%" stopColor="#f59e0b" stopOpacity={0} />
                  </linearGradient>
                </defs>
                <XAxis 
                  dataKey="date_str" 
                  tickLine={false} 
                  axisLine={{ stroke: '#e2e8f0' }} 
                  tick={{ fill: '#94a3b8', fontSize: 10 }}
                />
                <YAxis 
                  tickLine={false} 
                  axisLine={{ stroke: '#e2e8f0' }} 
                  tick={{ fill: '#94a3b8', fontSize: 10 }}
                  tickFormatter={(val) => `$${val}`}
                />
                <Tooltip
                  content={({ active, payload }) => {
                    if (active && payload && payload.length) {
                      const d = payload[0].payload;
                      return (
                        <div className="bg-white/95 backdrop-blur-md p-3 rounded-xl border border-slate-200 shadow-xl text-xs space-y-1">
                          <p className="font-bold text-slate-900">{d.date_str}</p>
                          <p className="text-orange-600 font-extrabold text-sm">${d.revenue?.toLocaleString()}</p>
                          <p className="text-slate-500 text-[11px]">{d.orders} orders processed</p>
                        </div>
                      );
                    }
                    return null;
                  }}
                />
                <Area 
                  type="monotone" 
                  dataKey="revenue" 
                  stroke="#ea580c" 
                  strokeWidth={2.5} 
                  fillOpacity={1} 
                  fill="url(#revenueGradient)" 
                />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Category Revenue Share (5 Cols) */}
        <div className="lg:col-span-5 bg-white rounded-2xl border border-slate-200 shadow-xs p-6 flex flex-col justify-between">
          <div className="flex items-center justify-between mb-4">
            <div>
              <h3 className="text-base font-extrabold text-slate-900 font-['Outfit']">
                Category Revenue Breakdown
              </h3>
              <p className="text-xs text-slate-400 mt-0.5">Share of total enterprise sales volume</p>
            </div>
            <span className="p-2 rounded-xl bg-orange-50 border border-orange-100 text-orange-600">
              <PieIcon className="w-4 h-4" />
            </span>
          </div>

          <div className="h-44 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={categories || []} layout="vertical" barSize={16}>
                <XAxis type="number" hide />
                <YAxis 
                  type="category" 
                  dataKey="pizza_category" 
                  axisLine={false} 
                  tickLine={false} 
                  tick={{ fill: '#475569', fontSize: 11, fontWeight: 600 }}
                  width={75}
                />
                <Tooltip 
                  formatter={(val) => [`$${val.toLocaleString()}`, 'Revenue']}
                  contentStyle={{ backgroundColor: '#ffffff', borderRadius: '0.75rem', border: '1px solid #e2e8f0', fontSize: '12px' }}
                />
                <Bar dataKey="revenue" radius={[0, 6, 6, 0]}>
                  {(categories || []).map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={CATEGORY_COLORS[entry.pizza_category] || '#ea580c'} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>

          {/* Category Chips */}
          <div className="grid grid-cols-2 gap-2 mt-4 pt-4 border-t border-slate-100">
            {(categories || []).map((cat) => (
              <div key={cat.pizza_category} className="flex items-center justify-between p-2 rounded-xl bg-slate-50 border border-slate-100">
                <div className="flex items-center gap-1.5">
                  <span className="w-2.5 h-2.5 rounded-full" style={{ backgroundColor: CATEGORY_COLORS[cat.pizza_category] }} />
                  <span className="text-xs font-bold text-slate-700">{cat.pizza_category}</span>
                </div>
                <span className="text-xs font-extrabold text-slate-900 font-['Outfit']">{cat.revenue_pct}%</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Crust Size Distribution & Top Pizzas Bento */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Crust Size Distribution (5 Cols) */}
        <div className="lg:col-span-5 bg-white rounded-2xl border border-slate-200 shadow-xs p-6 flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between mb-4">
              <div>
                <h3 className="text-base font-extrabold text-slate-900 font-['Outfit']">
                  Crust Size Grain
                </h3>
                <p className="text-xs text-slate-400 mt-0.5">Distribution across S, M, L, XL, XXL portions</p>
              </div>
              <span className="p-2 rounded-xl bg-amber-50 border border-amber-100 text-amber-600">
                <Layers className="w-4 h-4" />
              </span>
            </div>

            {/* Segmented Bar */}
            <div className="w-full h-4 rounded-full bg-slate-100 flex overflow-hidden border border-slate-200/80 mb-5">
              {(normalizedSizes || []).map((s, idx) => {
                const colors = ['#ea580c', '#f59e0b', '#10b981', '#6366f1', '#ec4899'];
                return (
                  <div
                    key={s.pizza_size}
                    title={`${s.pizza_size}: ${s.pct}%`}
                    style={{ width: `${s.pct}%`, backgroundColor: colors[idx % colors.length] }}
                    className="h-full transition-all duration-500 hover:opacity-85"
                  />
                );
              })}
            </div>

            {/* Size legend */}
            <div className="space-y-2">
              {(normalizedSizes || []).map((s, idx) => {
                const colors = ['#ea580c', '#f59e0b', '#10b981', '#6366f1', '#ec4899'];
                return (
                  <div key={s.pizza_size} className="flex items-center justify-between py-1 border-b border-slate-100 text-xs">
                    <div className="flex items-center gap-2">
                      <span className="w-2.5 h-2.5 rounded-full" style={{ backgroundColor: colors[idx % colors.length] }} />
                      <span className="font-bold text-slate-800">Size {s.pizza_size}</span>
                      <span className="text-[10px] text-slate-400 font-medium">({s.orders_count} pies)</span>
                    </div>
                    <span className="font-extrabold text-slate-900">{s.pct}%</span>
                  </div>
                );
              })}
            </div>
          </div>
        </div>

        {/* Top 5 Best-Selling Pizza Menu Leaderboard (7 Cols) */}
        <div className="lg:col-span-7 bg-white rounded-2xl border border-slate-200 shadow-xs p-6">
          <div className="flex items-center justify-between mb-4">
            <div>
              <div className="flex items-center gap-2">
                <h3 className="text-base font-extrabold text-slate-900 font-['Outfit']">
                  Top Performing Menu Items
                </h3>
                <span className="px-2 py-0.5 rounded-full text-[9px] font-extrabold uppercase bg-amber-50 text-amber-800 border border-amber-200">
                  Pareto Leaderboard
                </span>
              </div>
              <p className="text-xs text-slate-400 mt-0.5">Highest grossing pizza recipes by revenue</p>
            </div>
            <Award className="w-5 h-5 text-amber-500" />
          </div>

          <div className="space-y-2.5">
            {(normalizedTopPizzas || []).slice(0, 5).map((p, idx) => {
              const ranks = ['🥇', '🥈', '🥉', '4', '5'];
              return (
                <div 
                  key={p.pizza_name} 
                  className="flex items-center justify-between p-3 rounded-2xl bg-slate-50/70 border border-slate-100 hover:border-orange-200 hover:bg-orange-50/20 transition-all group"
                >
                  <div className="flex items-center gap-3">
                    <span className="w-7 h-7 rounded-lg bg-white border border-slate-200 flex items-center justify-center font-bold text-xs shadow-2xs">
                      {ranks[idx]}
                    </span>
                    <div>
                      <div className="flex items-center gap-2">
                        <span className="text-xs font-bold text-slate-900 group-hover:text-orange-600 transition-colors">
                          {p.pizza_name}
                        </span>
                        <span className="text-[9px] px-1.5 py-0.2 rounded font-semibold bg-white border border-slate-200 text-slate-600">
                          {p.category}
                        </span>
                      </div>
                      <span className="text-[10px] text-slate-400 font-medium block mt-0.5">
                        {p.quantity_sold} pies sold
                      </span>
                    </div>
                  </div>

                  <div className="text-right">
                    <span className="text-sm font-black text-slate-900 font-['Outfit'] block">
                      ${p.revenue?.toLocaleString()}
                    </span>
                    <span className="text-[10px] text-emerald-600 font-bold">
                      ${p.unit_price} / unit
                    </span>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>

      {/* Star Schema Live Transaction Explorer */}
      <div className="bg-white rounded-2xl border border-slate-200 shadow-xs p-6">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-5 border-b border-slate-100 pb-4">
          <div>
            <div className="flex items-center gap-2">
              <h3 className="text-base font-extrabold text-slate-900 font-['Outfit']">
                Fact_Sales Transaction Grain
              </h3>
              <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 border border-slate-200">
                {filteredTransactions?.length || 0} Records
              </span>
            </div>
            <p className="text-xs text-slate-400 mt-0.5">
              Live star schema joined table showing Fact_Sales linked with Dim_Pizza & Dim_Date
            </p>
          </div>

          <div className="relative w-full sm:w-64">
            <Search className="w-3.5 h-3.5 text-slate-400 absolute left-3 top-3" />
            <input
              type="text"
              placeholder="Search by order or recipe…"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-8 pr-3 py-1.5 rounded-xl bg-slate-50 border border-slate-200 text-xs focus:outline-none focus:border-orange-500 focus:bg-white transition-all"
            />
          </div>
        </div>

        {/* Transaction Table */}
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b border-slate-200 text-slate-400 font-bold uppercase tracking-wider text-[10px]">
                <th className="pb-3 pl-2">Order ID</th>
                <th className="pb-3">Timestamp</th>
                <th className="pb-3">Recipe</th>
                <th className="pb-3">Category</th>
                <th className="pb-3">Size</th>
                <th className="pb-3 text-right">Qty</th>
                <th className="pb-3 text-right">Price</th>
                <th className="pb-3 text-right">Total</th>
                <th className="pb-3 text-center pr-2">Order Tier</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {(filteredTransactions || []).slice(0, 10).map((tx, idx) => {
                const tierStyles = {
                  'VIP Feast': 'bg-purple-50 text-purple-700 border-purple-200',
                  Premium: 'bg-orange-50 text-orange-700 border-orange-200',
                  Standard: 'bg-emerald-50 text-emerald-700 border-emerald-200',
                  Budget: 'bg-slate-100 text-slate-600 border-slate-200',
                };

                return (
                  <tr key={idx} className="hover:bg-slate-50/80 transition-colors">
                    <td className="py-3 pl-2 font-mono font-bold text-slate-800">{tx.order_id}</td>
                    <td className="py-3 text-slate-500">{tx.date_str} {tx.order_time}</td>
                    <td className="py-3 font-semibold text-slate-800">{tx.pizza_name}</td>
                    <td className="py-3">
                      <span className="px-2 py-0.5 rounded-md text-[10px] font-bold border" style={{ color: CATEGORY_COLORS[tx.pizza_category], borderColor: `${CATEGORY_COLORS[tx.pizza_category]}40`, backgroundColor: `${CATEGORY_COLORS[tx.pizza_category]}10` }}>
                        {tx.pizza_category}
                      </span>
                    </td>
                    <td className="py-3 font-bold text-slate-700">{tx.pizza_size}</td>
                    <td className="py-3 text-right font-semibold">{tx.quantity}</td>
                    <td className="py-3 text-right text-slate-500">${tx.unit_price}</td>
                    <td className="py-3 text-right font-extrabold text-slate-900">${tx.total_price}</td>
                    <td className="py-3 text-center pr-2">
                      <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold border ${tierStyles[tx.order_tier] || 'bg-slate-100'}`}>
                        {tx.order_tier}
                      </span>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
