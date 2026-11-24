import React from 'react';
import { Shield, Sparkles, Filter, Scale, CheckCircle, Truck, Building2 } from 'lucide-react';

export const FirstMileHub: React.FC = () => {
  return (
    <section id="quality-tech" className="py-20 bg-white border-b border-slate-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-100 text-amber-800 text-xs font-bold uppercase tracking-wider mb-3">
            <Building2 className="w-4 h-4 text-amber-700" />
            <span>1-Acre First-Mile Infrastructure</span>
          </div>
          <h2 className="text-3xl sm:text-4xl font-bold font-serif text-slate-900 tracking-tight">
            The Gooty Processing Hub Advantage
          </h2>
          <p className="text-slate-600 mt-3 text-base">
            Located directly on the <strong>NH-44 Expressway Corridor at Gooty (Anantapuramu District)</strong>, our automated pre-cleaning and de-stoning hub eliminates multi-tier broker markups while delivering factory-grade quality consistency.
          </p>
        </div>

        {/* 4 Pillars Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {/* Pillar 1 */}
          <div className="bg-slate-50 p-6 rounded-2xl border border-slate-200 flex flex-col justify-between">
            <div>
              <div className="w-12 h-12 bg-emerald-100 text-emerald-800 rounded-xl flex items-center justify-center font-bold text-xl mb-4">
                0.00%
              </div>
              <h3 className="font-bold text-slate-900 text-lg mb-2">
                Pneumatic De-stoning
              </h3>
              <p className="text-xs text-slate-600 leading-relaxed">
                Multi-stage mechanical gravity tables separate 100% of silica stones, gravel, and field sand, preventing commercial steam kettle jams and dining hall complaints.
              </p>
            </div>
            <div className="mt-4 pt-3 border-t border-slate-200 text-[11px] font-semibold text-emerald-800">
              ✓ Guaranteed Stone-Free Deliveries
            </div>
          </div>

          {/* Pillar 2 */}
          <div className="bg-slate-50 p-6 rounded-2xl border border-slate-200 flex flex-col justify-between">
            <div>
              <div className="w-12 h-12 bg-amber-100 text-amber-800 rounded-xl flex items-center justify-center font-bold text-xl mb-4">
                Sortex
              </div>
              <h3 className="font-bold text-slate-900 text-lg mb-2">
                Optical Color Grading
              </h3>
              <p className="text-xs text-slate-600 leading-relaxed">
                High-speed cameras and monochromatic optical sorting detect and eject chalky, damaged, or discolored grains, ensuring uniform cosmetic appearance.
              </p>
            </div>
            <div className="mt-4 pt-3 border-t border-slate-200 text-[11px] font-semibold text-amber-800">
              ✓ 99.8% Grain Purity Index
            </div>
          </div>

          {/* Pillar 3 */}
          <div className="bg-slate-50 p-6 rounded-2xl border border-slate-200 flex flex-col justify-between">
            <div>
              <div className="w-12 h-12 bg-blue-100 text-blue-800 rounded-xl flex items-center justify-center font-bold text-xl mb-4">
                &lt; 12%
              </div>
              <h3 className="font-bold text-slate-900 text-lg mb-2">
                Dry Godown Storage
              </h3>
              <p className="text-xs text-slate-600 leading-relaxed">
                Ventilated, moisture-tested Rayalaseema godowns keep paddy aged naturally for 12+ months. Eliminates damp spoilage, mold, and grain breakage during milling.
              </p>
            </div>
            <div className="mt-4 pt-3 border-t border-slate-200 text-[11px] font-semibold text-blue-800">
              ✓ High-Expansion Cooked Yield (1:2.8)
            </div>
          </div>

          {/* Pillar 4 */}
          <div className="bg-slate-50 p-6 rounded-2xl border border-slate-200 flex flex-col justify-between">
            <div>
              <div className="w-12 h-12 bg-purple-100 text-purple-800 rounded-xl flex items-center justify-center font-bold text-xl mb-4">
                100 MT
              </div>
              <h3 className="font-bold text-slate-900 text-lg mb-2">
                Digital Weighbridge
              </h3>
              <p className="text-xs text-slate-600 leading-relaxed">
                Full-length electronic weighbridges with computerized gross/tare ticketing ensure transparent settlement for dryland farmers and zero quantity disputes for buyers.
              </p>
            </div>
            <div className="mt-4 pt-3 border-t border-slate-200 text-[11px] font-semibold text-purple-800">
              ✓ Instant Digital Direct Farmer Payouts
            </div>
          </div>
        </div>

        {/* Quality Flow Banner */}
        <div className="mt-12 bg-gradient-to-r from-slate-900 to-emerald-950 text-white rounded-2xl p-6 sm:p-8 flex flex-col lg:flex-row items-center justify-between gap-6 shadow-md">
          <div className="space-y-1">
            <div className="text-amber-400 font-bold text-xs uppercase tracking-wider">
              Quality Assurance Protocol
            </div>
            <h4 className="text-xl sm:text-2xl font-bold font-serif">
              Statutory FSSAI & Corporate ESG Compliance
            </h4>
            <p className="text-slate-300 text-xs sm:text-sm max-w-2xl">
              Every shipment is accompanied by lot-level moisture certificates, computerized weighment slips, FSSAI quality verification, and GST tax invoices.
            </p>
          </div>
          <div className="flex flex-wrap gap-3 shrink-0">
            <span className="bg-emerald-900/80 border border-emerald-500/30 text-emerald-200 px-3 py-1.5 rounded-lg text-xs font-semibold">
              FSSAI Standard
            </span>
            <span className="bg-emerald-900/80 border border-emerald-500/30 text-emerald-200 px-3 py-1.5 rounded-lg text-xs font-semibold">
              GST Invoiced
            </span>
            <span className="bg-emerald-900/80 border border-emerald-500/30 text-emerald-200 px-3 py-1.5 rounded-lg text-xs font-semibold">
              AP Endowments Compliant
            </span>
          </div>
        </div>
      </div>
    </section>
  );
};
