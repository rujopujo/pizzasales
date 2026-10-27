import React from 'react';
import { 
  BarChart3, 
  BrainCircuit, 
  Sparkles, 
  Boxes, 
  TrendingUp, 
  LogOut,
  Crown,
  ChefHat,
  Lock,
  Flame,
  Cpu
} from 'lucide-react';

export default function Navbar({ activeTab, setActiveTab, currentUser, onLogout, onOpenAIGuide }) {
  const tabs = [
    { 
      id: 'overview', 
      label: 'Insights', 
      icon: BarChart3, 
      activeColor: 'text-orange-600', 
      bgActive: 'bg-orange-500',
      badge: null, 
      adminOnly: false 
    },
    { 
      id: 'predictor', 
      label: 'Predictor', 
      icon: BrainCircuit, 
      activeColor: 'text-indigo-600', 
      bgActive: 'bg-indigo-500',
      badge: 'ML 2.0', 
      badgeClass: 'bg-indigo-50 text-indigo-700 border-indigo-200/80',
      adminOnly: false 
    },
    { 
      id: 'upsell', 
      label: 'Smart Upsell', 
      icon: Sparkles, 
      activeColor: 'text-rose-600', 
      bgActive: 'bg-rose-500',
      badge: '🔥 HOT', 
      badgeClass: 'bg-gradient-to-r from-rose-500 to-orange-500 text-white font-black shadow-xs',
      adminOnly: false 
    },
    { 
      id: 'inventory', 
      label: 'Kitchen Demand', 
      icon: Boxes, 
      activeColor: 'text-emerald-600', 
      bgActive: 'bg-emerald-500',
      badge: 'AI FORECAST', 
      badgeClass: 'bg-emerald-50 text-emerald-700 border-emerald-200/80 font-bold',
      adminOnly: false 
    },
    { 
      id: 'whatif', 
      label: 'Simulator', 
      icon: TrendingUp, 
      activeColor: 'text-amber-600', 
      bgActive: 'bg-amber-500',
      badge: 'ADMIN AI', 
      badgeClass: 'bg-amber-50 text-amber-800 border-amber-200/90 font-bold',
      adminOnly: true 
    },
  ];

  const isAdmin = currentUser?.role === 'admin';
  const displayName = isAdmin ? 'Admin' : (currentUser?.name?.replace(/Alex.*/i, 'Admin')?.split(' ')[0] || 'User');

  return (
    <header className="sticky top-0 z-50 bg-white/90 backdrop-blur-xl border-b border-slate-200/70 px-4 sm:px-6 py-2.5 mb-7 shadow-[0_4px_20px_-4px_rgba(15,23,42,0.04)]">
      {/* Top Hairline Glowing Gradient Accent */}
      <div className="absolute top-0 inset-x-0 h-[2px] bg-gradient-to-r from-orange-500 via-amber-400 to-rose-500 opacity-90" />

      <div className="max-w-7xl mx-auto flex items-center justify-between gap-3">
        {/* Brand */}
        <div className="flex items-center gap-2.5 shrink-0 group cursor-pointer" onClick={() => setActiveTab('overview')}>
          <div className="relative">
            <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-orange-600 via-orange-500 to-amber-400 flex items-center justify-center shadow-md shadow-orange-500/25 ring-2 ring-orange-100 group-hover:scale-105 group-hover:rotate-3 transition-all duration-200 text-white text-base font-bold">
              🍕
            </div>
            <span className="absolute -bottom-0.5 -right-0.5 w-2.5 h-2.5 bg-emerald-500 border-2 border-white rounded-full shadow-2xs" />
          </div>

          <div className="flex items-center gap-2">
            <span className="font-extrabold text-lg tracking-tight text-slate-900 font-['Outfit']">
              PIZZA<span className="bg-gradient-to-r from-orange-600 to-amber-500 bg-clip-text text-transparent font-black">MDW</span>
            </span>
            <div className="hidden sm:flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-bold tracking-wider uppercase bg-gradient-to-r from-orange-500/10 via-amber-500/10 to-orange-500/10 text-orange-700 border border-orange-200/70 shadow-2xs">
              <Sparkles className="w-2.5 h-2.5 text-orange-500" />
              <span>AI Suite</span>
            </div>
          </div>
        </div>

        {/* Center Modern Navigation Tabs */}
        <nav 
          className="flex items-center gap-1 bg-slate-100/80 p-1.5 rounded-2xl border border-slate-200/70 shadow-inner overflow-x-auto max-w-full [&::-webkit-scrollbar]:hidden"
          style={{ scrollbarWidth: 'none', msOverflowStyle: 'none' }}
        >
          {tabs.map((tab) => {
            const Icon = tab.icon;
            const isActive = activeTab === tab.id;
            const isLocked = tab.adminOnly && !isAdmin;

            return (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`group relative flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold transition-all duration-200 whitespace-nowrap cursor-pointer ${
                  isActive
                    ? 'bg-white text-slate-900 shadow-[0_2px_8px_-1px_rgba(0,0,0,0.08),0_1px_3px_0_rgba(0,0,0,0.04)] border border-slate-200/90 font-bold scale-[1.01]'
                    : 'text-slate-600 hover:text-slate-900 hover:bg-white/60 hover:shadow-2xs'
                }`}
              >
                {/* Active bottom micro-indicator */}
                {isActive && (
                  <span className={`absolute bottom-0 inset-x-3 h-[2px] rounded-full ${tab.bgActive} transition-all duration-300`} />
                )}

                <Icon 
                  className={`w-3.5 h-3.5 transition-colors duration-200 ${
                    isActive ? tab.activeColor : 'text-slate-400 group-hover:text-slate-600'
                  }`} 
                />
                
                <span className={isActive ? 'text-slate-900 font-bold' : ''}>
                  {tab.label}
                </span>

                {isLocked && <Lock className="w-3 h-3 text-slate-400 ml-0.5" />}

                {tab.badge && !isLocked && (
                  <span
                    className={`text-[9px] px-1.5 py-0.2 rounded-full font-bold uppercase tracking-wider border border-transparent ${tab.badgeClass}`}
                  >
                    {tab.badge}
                  </span>
                )}
              </button>
            );
          })}
        </nav>

        {/* Right Section: AI Guide Trigger, Live Status & User Profile */}
        <div className="flex items-center gap-2.5 shrink-0">
          {/* Quick AI Explainer Guide Trigger Button */}
          <button
            onClick={onOpenAIGuide}
            className="hidden md:flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-gradient-to-r from-orange-500/10 via-amber-500/15 to-rose-500/10 hover:from-orange-500/20 hover:to-rose-500/20 border border-orange-300/80 text-orange-800 text-xs font-bold shadow-2xs hover:shadow-xs transition-all hover:scale-105 active:scale-95 cursor-pointer"
            title="Open AI Capabilities Matrix & Guide"
          >
            <Sparkles className="w-3.5 h-3.5 text-orange-600 animate-spin" style={{ animationDuration: '6s' }} />
            <span>AI Guide</span>
          </button>

          {/* Live System Pulsing Status */}
          <div className="hidden lg:flex items-center gap-2 px-2.5 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-800 text-[11px] font-semibold shadow-2xs">
            <span className="relative flex h-2 w-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75" />
              <span className="relative inline-flex rounded-full h-2 w-2 bg-emerald-500" />
            </span>
            <span className="tracking-tight">FastAPI Live</span>
          </div>

          {/* Luxury Executive Profile Pill */}
          <div className="flex items-center gap-2.5 px-3 py-1.5 rounded-xl bg-gradient-to-b from-white to-slate-50/90 border border-slate-200/90 shadow-xs hover:border-orange-200 hover:shadow-sm transition-all duration-200">
            <div className={`w-7 h-7 rounded-lg flex items-center justify-center text-xs font-bold shadow-2xs ${
              isAdmin
                ? 'bg-gradient-to-tr from-amber-500 via-orange-500 to-amber-300 text-white ring-2 ring-amber-100'
                : 'bg-emerald-100 text-emerald-700 ring-2 ring-emerald-100'
            }`}>
              {isAdmin ? <Crown className="w-3.5 h-3.5 drop-shadow-xs" /> : <ChefHat className="w-3.5 h-3.5" />}
            </div>

            <div className="text-left hidden sm:block">
              <div className="flex items-center gap-1">
                <span className="text-xs font-extrabold text-slate-900 block leading-tight">
                  {displayName}
                </span>
                {isAdmin && (
                  <span className="w-1.5 h-1.5 rounded-full bg-orange-500" title="Super Admin" />
                )}
              </div>
              <span className="text-[10px] font-semibold text-slate-500 block leading-tight">
                {isAdmin ? '👑 Executive' : '🍕 Staff'}
              </span>
            </div>

            <button
              onClick={onLogout}
              title="Sign Out"
              className="ml-1 p-1 rounded-lg text-slate-400 hover:text-rose-600 hover:bg-rose-50 transition-all hover:scale-105 active:scale-95 cursor-pointer"
            >
              <LogOut className="w-3.5 h-3.5" />
            </button>
          </div>
        </div>
      </div>
    </header>
  );
}
