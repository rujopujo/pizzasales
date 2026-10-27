import React, { useState } from 'react';
import { 
  User, 
  Lock, 
  Sparkles, 
  ChefHat, 
  ArrowRight, 
  Eye, 
  EyeOff, 
  AlertCircle,
  Crown
} from 'lucide-react';
import confetti from 'canvas-confetti';

export default function LoginPage({ onLoginSuccess }) {
  const [activeRoleTab, setActiveRoleTab] = useState('admin');
  const [username, setUsername] = useState('admin');
  const [password, setPassword] = useState('admin123');
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleRoleTabChange = (role) => {
    setActiveRoleTab(role);
    setError('');
    if (role === 'admin') {
      setUsername('admin');
      setPassword('admin123');
    } else {
      setUsername('user');
      setPassword('pizza123');
    }
  };

  const handleSubmit = async (e) => {
    e?.preventDefault();
    setError('');
    setLoading(true);

    try {
      const res = await fetch('/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          username,
          password,
          requested_role: activeRoleTab,
        }),
      });

      const data = await res.json();

      if (!res.ok) {
        throw new Error(data.detail || 'Authentication failed');
      }

      localStorage.setItem('pizza_auth_user', JSON.stringify(data.user));
      localStorage.setItem('pizza_auth_token', data.token);

      confetti({
        particleCount: 40,
        spread: 60,
        origin: { y: 0.6 },
        colors: activeRoleTab === 'admin' ? ['#ea580c', '#f59e0b', '#dc2626'] : ['#059669', '#2563eb'],
      });

      onLoginSuccess(data.user);
    } catch (err) {
      setError(err.message || 'Login error occurred');
    } finally {
      setLoading(false);
    }
  };

  const quickLogin = (role) => {
    if (role === 'admin') {
      setUsername('admin');
      setPassword('admin123');
      setActiveRoleTab('admin');
    } else {
      setUsername('user');
      setPassword('pizza123');
      setActiveRoleTab('user');
    }
    setTimeout(() => {
      handleSubmit();
    }, 100);
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-4 relative overflow-hidden bg-[#f8fafc]">
      {/* Subtle Background Glows */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-orange-200/40 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-amber-200/30 rounded-full blur-3xl pointer-events-none" />

      <div className="w-full max-w-md relative z-10 space-y-6">
        {/* Brand Header */}
        <div className="text-center space-y-2">
          <div className="inline-flex w-14 h-14 rounded-2xl bg-gradient-to-tr from-orange-600 to-amber-500 items-center justify-center shadow-lg shadow-orange-500/20 text-3xl mb-2 text-white">
            🍕
          </div>
          <h1 className="text-3xl font-extrabold text-slate-900 tracking-tight font-['Outfit']">
            PIZZA<span className="text-orange-600">MDW</span>
          </h1>
          <p className="text-xs text-slate-500 font-medium">
            Artisanal Warehouse & Multi-Target Predictive Suite
          </p>
        </div>

        {/* Main Login Card */}
        <div className="bg-white p-8 rounded-3xl border border-slate-200/90 shadow-xl shadow-slate-200/60 space-y-6">
          {/* Portal Switcher Tabs */}
          <div className="grid grid-cols-2 p-1.5 rounded-2xl bg-slate-100 border border-slate-200">
            <button
              type="button"
              onClick={() => handleRoleTabChange('admin')}
              className={`flex items-center justify-center gap-2 py-2.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                activeRoleTab === 'admin'
                  ? 'bg-white text-orange-600 shadow-sm font-black border border-slate-200/80'
                  : 'text-slate-600 hover:text-slate-950'
              }`}
            >
              <Crown className="w-4 h-4 text-orange-600" />
              Admin Portal
            </button>

            <button
              type="button"
              onClick={() => handleRoleTabChange('user')}
              className={`flex items-center justify-center gap-2 py-2.5 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                activeRoleTab === 'user'
                  ? 'bg-white text-emerald-600 shadow-sm font-black border border-slate-200/80'
                  : 'text-slate-600 hover:text-slate-950'
              }`}
            >
              <ChefHat className="w-4 h-4 text-emerald-600" />
              Staff / User Portal
            </button>
          </div>

          {/* Role Description Banner */}
          <div className={`p-3 rounded-2xl border text-xs flex items-center gap-2.5 ${
            activeRoleTab === 'admin'
              ? 'bg-orange-50 border-orange-200 text-orange-800'
              : 'bg-emerald-50 border-emerald-200 text-emerald-800'
          }`}>
            <Sparkles className="w-4 h-4 shrink-0 text-orange-600" />
            <span>
              {activeRoleTab === 'admin'
                ? 'Executive access: Full OLAP analytics, ML models, pricing levers & What-If simulator.'
                : 'Frontline access: Real-time AI basket predictions, Apriori upsell, and kitchen queue.'}
            </span>
          </div>

          {/* Error Message */}
          {error && (
            <div className="p-3.5 rounded-2xl bg-rose-50 border border-rose-200 text-rose-700 text-xs flex items-center gap-2">
              <AlertCircle className="w-4 h-4 shrink-0 text-rose-600" />
              <span>{error}</span>
            </div>
          )}

          {/* Login Form */}
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="space-y-1.5">
              <label className="text-xs font-semibold text-slate-700 flex items-center gap-1.5">
                <User className="w-3.5 h-3.5 text-orange-600" />
                Username
              </label>
              <input
                type="text"
                required
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Enter username"
                className="w-full px-4 py-2.5 rounded-xl bg-slate-50 border border-slate-300 text-slate-900 text-sm focus:outline-none focus:bg-white focus:border-orange-500 focus:ring-2 focus:ring-orange-500/20 transition-all"
              />
            </div>

            <div className="space-y-1.5">
              <label className="text-xs font-semibold text-slate-700 flex items-center gap-1.5">
                <Lock className="w-3.5 h-3.5 text-amber-600" />
                Password
              </label>
              <div className="relative">
                <input
                  type={showPassword ? 'text' : 'password'}
                  required
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="Enter password"
                  className="w-full px-4 py-2.5 pr-10 rounded-xl bg-slate-50 border border-slate-300 text-slate-900 text-sm focus:outline-none focus:bg-white focus:border-orange-500 focus:ring-2 focus:ring-orange-500/20 transition-all"
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 cursor-pointer"
                >
                  {showPassword ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                </button>
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className={`w-full py-3 rounded-xl font-bold text-xs uppercase tracking-wider text-white transition-all duration-200 flex items-center justify-center gap-2 cursor-pointer shadow-md ${
                activeRoleTab === 'admin'
                  ? 'bg-gradient-to-r from-orange-600 to-amber-600 shadow-orange-500/25 hover:from-orange-700 hover:to-amber-700'
                  : 'bg-gradient-to-r from-emerald-600 to-teal-600 shadow-emerald-500/25 hover:from-emerald-700 hover:to-teal-700'
              }`}
            >
              {loading ? (
                <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin" />
              ) : (
                <>
                  Authenticate & Launch <ArrowRight className="w-4 h-4" />
                </>
              )}
            </button>
          </form>

          {/* Quick Demo Login Helpers */}
          <div className="pt-2 border-t border-slate-200 space-y-2.5">
            <span className="text-[11px] font-bold text-slate-500 uppercase tracking-wider block text-center">
              Quick 1-Click Demo Login
            </span>
            <div className="grid grid-cols-2 gap-2">
              <button
                type="button"
                onClick={() => quickLogin('admin')}
                className="py-2 px-3 rounded-xl bg-orange-50 border border-orange-200 text-[11px] font-bold text-orange-700 hover:bg-orange-100 transition-all cursor-pointer flex items-center justify-center gap-1.5"
              >
                👑 Demo Admin
              </button>
              <button
                type="button"
                onClick={() => quickLogin('user')}
                className="py-2 px-3 rounded-xl bg-emerald-50 border border-emerald-200 text-[11px] font-bold text-emerald-700 hover:bg-emerald-100 transition-all cursor-pointer flex items-center justify-center gap-1.5"
              >
                👤 Demo Staff
              </button>
            </div>
          </div>
        </div>

        {/* Credentials footnote */}
        <div className="p-3 rounded-2xl bg-white border border-slate-200 text-[11px] text-center text-slate-500 shadow-xs">
          🔑 Admin: <code className="text-orange-600 font-bold">admin / admin123</code> &bull; User: <code className="text-emerald-600 font-bold">user / pizza123</code>
        </div>
      </div>
    </div>
  );
}
