import React, { useState } from 'react';
import { 
  Sparkles, 
  Plus, 
  Check, 
  ShoppingCart, 
  TrendingUp, 
  Flame, 
  Zap, 
  ShoppingBag,
  ArrowRight,
  Layers,
  Cpu
} from 'lucide-react';

const CATEGORIES = ['Classic', 'Supreme', 'Veggie', 'Chicken'];

const MOCK_RULES = {
  Classic: {
    base_item: 'Classic Pepperoni Pizza',
    recommendations: [
      { item: 'Garlic Herb Dipping Sauce', category: 'Dips & Sauces', price: 2.50, lift: 2.8, confidence: 78, reason: 'Frequently ordered with thick crispy crusts to soften crust edge bites.' },
      { item: 'Cheesy Garlic Breadsticks', category: 'Sides', price: 6.99, lift: 2.1, confidence: 64, reason: 'Strong pairing affinity in family-sized Friday evening baskets.' },
      { item: 'Cold Mexican Cola (Glass)', category: 'Beverages', price: 3.50, lift: 1.9, confidence: 61, reason: 'High-lift pairing with salty pepperoni and mozzarella profile.' },
    ]
  },
  Supreme: {
    base_item: 'Deluxe Supreme Feast',
    recommendations: [
      { item: 'Spicy Buffalo Wings (6pcs)', category: 'Appetizers', price: 9.99, lift: 3.1, confidence: 82, reason: 'Highest margin combo attachment in weekend game-day orders.' },
      { item: 'Truffle Parmesan Fries', category: 'Sides', price: 5.50, lift: 2.4, confidence: 69, reason: 'Premium item synergy observed with high-tier supreme buyers.' },
      { item: 'House Ranch Dip Double', category: 'Dips', price: 2.00, lift: 1.8, confidence: 60, reason: 'Popular complement to balance bold peppers and olives.' },
    ]
  },
  Veggie: {
    base_item: 'Garden Harvest Veggie',
    recommendations: [
      { item: 'Mediterranean Greek Salad', category: 'Salads', price: 7.50, lift: 3.4, confidence: 86, reason: 'Health-conscious customer affinity: 86% attach rate on lunch orders.' },
      { item: 'Basil Pesto Swirl Dip', category: 'Dips', price: 2.75, lift: 2.2, confidence: 67, reason: 'Enhances roasted mushrooms, bell peppers, and artichoke hearts.' },
      { item: 'Sparkling San Pellegrino', category: 'Beverages', price: 3.25, lift: 1.7, confidence: 62, reason: 'Light zero-sugar complement frequently bought with veggie bases.' },
    ]
  },
  Chicken: {
    base_item: 'BBQ Chicken Feast',
    recommendations: [
      { item: 'Smoky BBQ Extra Sauce Cup', category: 'Dips', price: 1.75, lift: 2.9, confidence: 80, reason: 'Direct brand match: 80% of BBQ chicken lovers order dipping cups.' },
      { item: 'Jalapeño Poppers (4pcs)', category: 'Appetizers', price: 6.50, lift: 2.3, confidence: 71, reason: 'Adds heat balance to sweet caramelized BBQ onion base.' },
      { item: 'Warm Cinnamon Dough Knots', category: 'Desserts', price: 5.99, lift: 2.0, confidence: 65, reason: 'High sweet-tooth conversion when savory chicken is in the cart.' },
    ]
  }
};

export default function SmartUpsellEngine() {
  const [selectedCategory, setSelectedCategory] = useState('Classic');
  const [cartItems, setCartItems] = useState([
    { name: 'Classic Pepperoni Pizza (Large)', price: 18.50, type: 'base' },
  ]);

  const data = MOCK_RULES[selectedCategory];

  const addUpsellToCart = (item) => {
    setCartItems([...cartItems, { name: item.item, price: item.price, type: 'upsell' }]);
  };
  const removeCartItem = (index) => {
    setCartItems(cartItems.filter((_, i) => i !== index));
  };

  const totalCart = cartItems.reduce((acc, curr) => acc + curr.price, 0);

  return (
    <div className="space-y-8 animate-fadeIn">
      {/* Header */}
      <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-xs flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-orange-50 border border-orange-200 text-orange-700 text-xs font-bold uppercase tracking-wider mb-2">
            <Zap className="w-3.5 h-3.5" />
            Data Mining Association Rules
          </div>
          <h2 className="text-2xl lg:text-3xl font-extrabold text-slate-900 font-['Outfit']">
            Smart Menu <span className="text-orange-600">Upsell Engine</span>
          </h2>
          <p className="text-slate-500 text-xs">
            Powered by Market Basket Analysis (Apriori Algorithm). Uncovers high-lift pairings to maximize Average Basket Value.
          </p>
        </div>

        <div className="flex items-center gap-2">
          {CATEGORIES.map((cat) => (
            <button
              key={cat}
              onClick={() => setSelectedCategory(cat)}
              className={`px-3 py-2 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                selectedCategory === cat
                  ? 'bg-orange-600 text-white font-bold shadow-xs'
                  : 'bg-slate-50 border border-slate-200 text-slate-600 hover:bg-slate-100'
              }`}
            >
              {cat}
            </button>
          ))}
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
        {/* Recommended Upsell Rules (8 Cols) */}
        <div className="lg:col-span-8 space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-base font-bold text-slate-900 flex items-center gap-2">
              <Sparkles className="w-4 h-4 text-amber-600" />
              Highest Lift Complements for {selectedCategory} Pies
            </h3>
            <span className="text-xs text-slate-400 font-mono">
              Min Support: 3% • Min Confidence: 60%
            </span>
          </div>

          <div className="space-y-4">
            {data?.recommendations?.map((rule, idx) => {
              const inCart = cartItems.some(c => c.name === rule.item);
              return (
                <div
                  key={idx}
                  className="bg-white p-5 rounded-2xl border border-slate-200 shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4 hover:border-orange-300 transition-all"
                >
                  <div className="space-y-2">
                    <div className="flex items-center gap-2">
                      <span className="text-xs font-bold px-2.5 py-0.5 rounded-lg bg-orange-50 text-orange-700 border border-orange-200">
                        {rule.category}
                      </span>
                      <h4 className="text-base font-extrabold text-slate-900">{rule.item}</h4>
                    </div>

                    <p className="text-xs text-slate-600 leading-relaxed max-w-lg">
                      {rule.reason}
                    </p>

                    <div className="flex items-center gap-4 text-xs font-medium pt-1">
                      <span className="text-emerald-700 font-bold bg-emerald-50 px-2 py-0.5 rounded-md border border-emerald-200">
                        {rule.confidence}% Confidence
                      </span>
                      <span className="text-amber-700 font-bold bg-amber-50 px-2 py-0.5 rounded-md border border-amber-200">
                        {rule.lift}x Lift Multiplier
                      </span>
                      <span className="text-slate-800 font-bold">
                        +${rule.price.toFixed(2)}
                      </span>
                    </div>
                  </div>

                  <button
                    onClick={() => addUpsellToCart(rule)}
                    disabled={inCart}
                    className={`px-4 py-2.5 rounded-xl text-xs font-bold transition-all flex items-center justify-center gap-2 cursor-pointer shrink-0 shadow-xs ${
                      inCart
                        ? 'bg-emerald-50 text-emerald-700 border border-emerald-200 cursor-default'
                        : 'bg-orange-600 text-white font-bold hover:bg-orange-700'
                    }`}
                  >
                    {inCart ? (
                      <>
                        <Check className="w-3.5 h-3.5" /> Added to Order
                      </>
                    ) : (
                      <>
                        <Plus className="w-3.5 h-3.5" /> Add to Order (+${rule.price.toFixed(2)})
                      </>
                    )}
                  </button>
                </div>
              );
            })}
          </div>
        </div>

        {/* Live Cart Simulator & Basket Value Impact (4 Cols) */}
        <div className="lg:col-span-4 bg-white p-6 rounded-2xl border border-slate-200 shadow-xs flex flex-col justify-between space-y-6">
          <div>
            <div className="flex items-center justify-between border-b border-slate-100 pb-4 mb-4">
              <h3 className="text-base font-bold text-slate-900 flex items-center gap-2">
                <ShoppingCart className="w-4 h-4 text-orange-600" />
                Live POS Basket Simulator
              </h3>
              <span className="text-xs text-orange-700 font-bold bg-orange-50 px-2 py-0.5 rounded-md border border-orange-200">
                {cartItems.length} Items
              </span>
            </div>

            <div className="space-y-2.5 max-h-[250px] overflow-y-auto pr-1">
              {cartItems.map((item, idx) => (
                <div
                  key={idx}
                  className="flex items-center justify-between p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs"
                >
                  <div className="flex items-center gap-2 truncate">
                    <span className="w-1.5 h-1.5 rounded-full bg-orange-500" />
                    <span className="text-slate-800 font-semibold truncate">{item.name}</span>
                  </div>
                  <div className="flex items-center gap-2 shrink-0">
                    <span className="font-bold text-slate-900">${item.price.toFixed(2)}</span>
                    {item.type === 'upsell' && (
                      <button
                        onClick={() => removeCartItem(idx)}
                        className="text-slate-400 hover:text-rose-600 text-xs px-1 cursor-pointer font-bold"
                      >
                        ✕
                      </button>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="space-y-4 pt-4 border-t border-slate-100">
            <div className="flex justify-between items-baseline">
              <span className="text-xs font-semibold text-slate-500">Total Basket Value</span>
              <span className="text-2xl font-black text-slate-900 font-['Outfit']">
                ${totalCart.toFixed(2)}
              </span>
            </div>

            <div className="p-3.5 rounded-xl bg-emerald-50 border border-emerald-200 text-xs text-emerald-800">
              📈 <strong>Upsell Impact:</strong> Cross-selling rules increased basket value by +
              {(((totalCart - 18.5) / 18.5) * 100).toFixed(0)}%!
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
