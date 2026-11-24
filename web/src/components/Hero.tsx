import React from 'react';
import { ShieldCheck, Truck, Users, CheckCircle2, ChevronRight, Warehouse, ArrowDown } from 'lucide-react';

interface HeroProps {
  onOpenRfq: () => void;
}

export const Hero: React.FC<HeroProps> = ({ onOpenRfq }) => {
  return (
    <section className="relative overflow-hidden bg-gradient-to-b from-emerald-950 via-slate-900 to-slate-900 text-white pt-16 pb-20 lg:pt-24 lg:pb-28 border-b border-slate-800">
      {/* Decorative Grid Pattern */}
      <div className="absolute inset-0 opacity-10 bg-[radial-gradient(#10b981_1px,transparent_1px)] [background-size:20px_20px] pointer-events-none" />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div className="text-center max-w-4xl mx-auto space-y-6">
          {/* Badge */}
          <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-emerald-900/60 border border-emerald-500/30 text-emerald-300 text-xs sm:text-sm font-semibold shadow-inner">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
            <span>Direct Dryland Farmer Origin • 1-Acre First-Mile Processing Hub at Gooty (NH-44)</span>
          </div>

          {/* Main Headline */}
          <h1 className="text-3xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight font-serif leading-tight">
            Eliminating Middlemen. <br />
            <span className="bg-gradient-to-r from-emerald-300 via-amber-300 to-amber-200 bg-clip-text text-transparent">
              100% Pure Dry Agricultural Produce & Cash Crops.
            </span>
          </h1>

          {/* Subheading */}
          <p className="text-base sm:text-xl text-slate-300 max-w-3xl mx-auto font-normal leading-relaxed">
            Directly aggregating from <strong>5,000+ dryland farming families across all 24 villages of Gooty Mandal</strong>. Mechanically cleaned, pneumatically de-stoned, and sortex graded at our central NH-44 highway hub to feed <strong>1,040 verified commercial B2B buyers</strong> across South India.
          </p>

          {/* Zero Perishables Mandate Banner */}
          <div className="inline-block bg-amber-950/70 border border-amber-500/40 rounded-xl px-5 py-3 text-amber-200 text-xs sm:text-sm font-medium">
            🛡️ <strong>Strict Commodity Mandate:</strong> 100% Dry Non-Perishable Staples & Commercial Cash Crops Only (Zero Perishable Fruits, Zero Vegetables).
          </div>

          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-4">
            <button
              onClick={onOpenRfq}
              className="w-full sm:w-auto bg-gradient-to-r from-emerald-500 to-emerald-600 hover:from-emerald-600 hover:to-emerald-700 text-slate-950 font-bold px-7 py-3.5 rounded-xl shadow-lg hover:shadow-emerald-500/20 transition-all flex items-center justify-center gap-2 text-base"
            >
              <span>Submit Commercial RFP / 50kg Trial</span>
              <ChevronRight className="w-5 h-5 text-slate-950" />
            </button>
            <a
              href="#commodities"
              className="w-full sm:w-auto bg-slate-800/80 hover:bg-slate-700/80 border border-slate-700 text-white font-semibold px-6 py-3.5 rounded-xl transition-all flex items-center justify-center gap-2 text-base"
            >
              <span>Explore 100% Dry Commodities</span>
              <ArrowDown className="w-4 h-4 text-slate-400" />
            </a>
          </div>
        </div>

        {/* Live Metrics Grid */}
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4 mt-16 pt-10 border-t border-slate-800/80">
          <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700/60 p-5 rounded-2xl text-center">
            <div className="text-3xl sm:text-4xl font-extrabold text-amber-400 font-serif">1,040</div>
            <div className="text-xs uppercase tracking-wider text-slate-400 font-semibold mt-1">Verified B2B Whales</div>
            <div className="text-[11px] text-emerald-400 font-medium mt-1">24 Strategic Tiers</div>
          </div>

          <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700/60 p-5 rounded-2xl text-center">
            <div className="text-3xl sm:text-4xl font-extrabold text-emerald-400 font-serif">24</div>
            <div className="text-xs uppercase tracking-wider text-slate-400 font-semibold mt-1">Gooty Mandal Villages</div>
            <div className="text-[11px] text-slate-300 font-medium mt-1">5,000+ Farming Families</div>
          </div>

          <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700/60 p-5 rounded-2xl text-center">
            <div className="text-3xl sm:text-4xl font-extrabold text-amber-400 font-serif">1 Acre</div>
            <div className="text-xs uppercase tracking-wider text-slate-400 font-semibold mt-1">First-Mile Hub</div>
            <div className="text-[11px] text-emerald-400 font-medium mt-1">NH-44 Expressway Corridor</div>
          </div>

          <div className="bg-slate-800/50 backdrop-blur-sm border border-slate-700/60 p-5 rounded-2xl text-center">
            <div className="text-3xl sm:text-4xl font-extrabold text-emerald-400 font-serif">0.00%</div>
            <div className="text-xs uppercase tracking-wider text-slate-400 font-semibold mt-1">Stones & Silica</div>
            <div className="text-[11px] text-slate-300 font-medium mt-1">Pneumatic Gravity Tables</div>
          </div>

          <div className="col-span-2 md:col-span-1 bg-slate-800/50 backdrop-blur-sm border border-slate-700/60 p-5 rounded-2xl text-center">
            <div className="text-3xl sm:text-4xl font-extrabold text-amber-400 font-serif">1:2.8</div>
            <div className="text-xs uppercase tracking-wider text-slate-400 font-semibold mt-1">Cooking Yield</div>
            <div className="text-[11px] text-emerald-400 font-medium mt-1">12-Mo. Aged Sona Masoori</div>
          </div>
        </div>
      </div>
    </section>
  );
};
