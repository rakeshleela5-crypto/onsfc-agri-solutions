import React, { useState } from 'react';
import { MARKET_TIERS, MarketTier } from '../data/tiers';
import { Search, MapPin, Building, Clock, ChevronRight, Layers, Users } from 'lucide-react';

export const NetworkExplorer: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedTier, setSelectedTier] = useState<MarketTier | null>(null);

  const filteredTiers = MARKET_TIERS.filter((tier) => {
    const term = searchTerm.toLowerCase();
    return (
      tier.name.toLowerCase().includes(term) ||
      tier.region.toLowerCase().includes(term) ||
      tier.dominantCommodities.toLowerCase().includes(term) ||
      tier.keyBuyers.some((b) => b.toLowerCase().includes(term))
    );
  });

  const totalBuyers = MARKET_TIERS.reduce((acc, t) => acc + t.buyerCount, 0);

  return (
    <section id="network" className="py-20 bg-slate-900 text-white border-b border-slate-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center max-w-3xl mx-auto mb-12">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-900/60 border border-emerald-500/30 text-emerald-300 text-xs font-bold uppercase tracking-wider mb-3">
            <Layers className="w-4 h-4 text-emerald-400" />
            <span>Audited Commercial Pipeline</span>
          </div>
          <h2 className="text-3xl sm:text-4xl font-bold font-serif text-white tracking-tight">
            1,040 Verified Commercial Off-Takers
          </h2>
          <p className="text-slate-300 mt-3 text-base">
            Exploring 24 strategic market tiers spanning automotive plants, railway pantries, tech parks, hospitals, universities, temples, and grain mandis across South India.
          </p>

          {/* Search Input */}
          <div className="mt-8 max-w-xl mx-auto relative">
            <Search className="w-5 h-5 text-slate-400 absolute left-4 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              placeholder="Search by city, sector (e.g. KIA, JSW Steel, IRCTC, Sodexo, Apollo, VIMS)..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full bg-slate-800/90 border border-slate-700 rounded-xl pl-12 pr-4 py-3.5 text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 text-sm"
            />
          </div>
        </div>

        {/* Tiers Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {filteredTiers.map((tier) => (
            <div
              key={tier.tierNumber}
              onClick={() => setSelectedTier(tier)}
              className="bg-slate-800/60 hover:bg-slate-800 border border-slate-700/80 hover:border-emerald-500/50 rounded-2xl p-5 cursor-pointer transition-all flex flex-col justify-between group shadow-sm"
            >
              <div>
                {/* Top Badge */}
                <div className="flex items-center justify-between gap-2 mb-3">
                  <span className="bg-emerald-950 text-emerald-300 border border-emerald-700/40 text-[11px] font-bold px-2.5 py-0.5 rounded-full">
                    Tier {tier.tierNumber}
                  </span>
                  <div className="flex items-center gap-1.5 text-amber-400 font-extrabold text-sm">
                    <Users className="w-4 h-4" />
                    <span>{tier.buyerCount} Buyers</span>
                  </div>
                </div>

                {/* Title */}
                <h3 className="text-base font-bold text-white group-hover:text-emerald-300 transition-colors">
                  {tier.name}
                </h3>
                <p className="text-xs text-slate-400 flex items-center gap-1 mt-1">
                  <MapPin className="w-3.5 h-3.5 text-slate-500 shrink-0" />
                  <span>{tier.region}</span>
                </p>

                {/* Highway & Distance */}
                <div className="grid grid-cols-2 gap-2 mt-4 pt-3 border-t border-slate-700/60 text-xs">
                  <div>
                    <span className="text-slate-400 block text-[10px] uppercase font-semibold">Highway / Route:</span>
                    <span className="text-slate-200 font-medium">{tier.highway}</span>
                  </div>
                  <div>
                    <span className="text-slate-400 block text-[10px] uppercase font-semibold">Distance & Transit:</span>
                    <span className="text-slate-200 font-medium">{tier.distanceKm} ({tier.transitHours})</span>
                  </div>
                </div>

                {/* Key Whale Buyers */}
                <div className="mt-3 pt-3 border-t border-slate-700/60">
                  <span className="text-[10px] uppercase tracking-wider text-amber-400/90 font-bold block mb-1">
                    Anchor Off-Takers:
                  </span>
                  <div className="flex flex-wrap gap-1.5">
                    {tier.keyBuyers.slice(0, 3).map((buyer, bIdx) => (
                      <span
                        key={bIdx}
                        className="bg-slate-700/60 text-slate-300 text-[11px] px-2 py-0.5 rounded font-normal"
                      >
                        {buyer}
                      </span>
                    ))}
                    {tier.keyBuyers.length > 3 && (
                      <span className="text-[11px] text-slate-400 self-center">
                        +{tier.keyBuyers.length - 3} more
                      </span>
                    )}
                  </div>
                </div>
              </div>

              {/* Commodities list */}
              <div className="mt-4 pt-3 border-t border-slate-700/60 text-[11px] text-slate-400">
                <span className="font-semibold text-slate-300">Staples: </span>
                <span>{tier.dominantCommodities}</span>
              </div>
            </div>
          ))}
        </div>

        {/* Total Summary Footer */}
        <div className="mt-12 bg-slate-800/80 border border-slate-700 p-6 rounded-2xl flex flex-col sm:flex-row items-center justify-between gap-4 text-center sm:text-left">
          <div>
            <div className="text-xs font-bold text-emerald-400 uppercase tracking-wider">
              Cumulative Pipeline Architecture
            </div>
            <div className="text-xl sm:text-2xl font-bold font-serif text-white">
              Total Audited Commercial Demand: {totalBuyers} Verified Buyers
            </div>
            <p className="text-xs text-slate-400 mt-0.5">
              Across Andhra Pradesh, Telangana, Karnataka, and Tamil Nadu via direct highway corridors.
            </p>
          </div>
          <div className="bg-emerald-700 text-white font-bold px-5 py-2.5 rounded-xl text-sm shrink-0">
            100% Non-Perishables
          </div>
        </div>
      </div>
    </section>
  );
};
