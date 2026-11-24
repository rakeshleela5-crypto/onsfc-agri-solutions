import React, { useState } from 'react';
import { COMMODITIES, Commodity } from '../data/commodities';
import { Check, Info, Sparkles, Filter, PackageCheck } from 'lucide-react';

interface CommoditiesSectionProps {
  onSelectCommodity: (commodity: Commodity) => void;
}

export const CommoditiesSection: React.FC<CommoditiesSectionProps> = ({ onSelectCommodity }) => {
  const [selectedCategory, setSelectedCategory] = useState<string>('All');

  const categories = [
    'All',
    'Paddy & Rice',
    'Pulses & Dals',
    'Oilseeds & Oils',
    'Commercial Cash Crops',
    'Millets & Feed'
  ];

  const filteredCommodities = selectedCategory === 'All'
    ? COMMODITIES
    : COMMODITIES.filter(c => c.category === selectedCategory);

  return (
    <section id="commodities" className="py-20 bg-slate-50 border-b border-slate-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center max-w-3xl mx-auto mb-12">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 text-xs font-bold uppercase tracking-wider mb-3">
            <PackageCheck className="w-4 h-4 text-emerald-700" />
            <span>100% Dry Agricultural Produce</span>
          </div>
          <h2 className="text-3xl sm:text-4xl font-bold font-serif text-slate-900 tracking-tight">
            Commercial Commodity Portfolio
          </h2>
          <p className="text-slate-600 mt-3 text-base">
            Every grain, pulse, oilseed, and fiber is directly aggregated from Gooty Mandal dryland farms, graded via optical sortex machinery, and pneumatically de-stoned to guarantee zero physical defects.
          </p>
        </div>

        {/* Category Filters */}
        <div className="flex flex-wrap items-center justify-center gap-2 mb-12">
          {categories.map((cat) => (
            <button
              key={cat}
              onClick={() => setSelectedCategory(cat)}
              className={`px-4 py-2 rounded-xl text-sm font-semibold transition-all ${
                selectedCategory === cat
                  ? 'bg-emerald-700 text-white shadow-md'
                  : 'bg-white text-slate-700 border border-slate-200 hover:bg-slate-100'
              }`}
            >
              {cat}
            </button>
          ))}
        </div>

        {/* Commodity Cards Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredCommodities.map((item) => (
            <div
              key={item.id}
              className="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-md transition-shadow flex flex-col justify-between"
            >
              <div className="p-6">
                {/* Header row */}
                <div className="flex items-start justify-between gap-3 mb-3">
                  <div className="flex items-center gap-3">
                    <span className="text-3xl p-2 bg-slate-100 rounded-xl">{item.icon}</span>
                    <div>
                      <span className="text-xs font-semibold text-emerald-700 uppercase tracking-wider block">
                        {item.category}
                      </span>
                      <h3 className="font-bold text-slate-900 text-lg leading-snug">
                        {item.name}
                      </h3>
                      <p className="text-xs text-slate-500 font-medium">
                        {item.teluguName}
                      </p>
                    </div>
                  </div>
                  {item.isPopular && (
                    <span className="bg-amber-100 text-amber-800 text-[10px] font-bold px-2 py-0.5 rounded-full shrink-0 flex items-center gap-1">
                      <Sparkles className="w-3 h-3 text-amber-600" />
                      Whale Staple
                    </span>
                  )}
                </div>

                {/* Badge Pills */}
                <div className="flex flex-wrap gap-2 my-4">
                  <span className="bg-slate-100 text-slate-700 text-xs px-2.5 py-1 rounded-md font-medium">
                    {item.grade}
                  </span>
                  <span className="bg-emerald-50 text-emerald-800 text-xs px-2.5 py-1 rounded-md font-medium border border-emerald-200">
                    {item.cookingExpansion}
                  </span>
                  <span className="bg-amber-50 text-amber-900 text-xs px-2.5 py-1 rounded-md font-medium border border-amber-200">
                    {item.aging}
                  </span>
                </div>

                {/* Specs List */}
                <div className="space-y-1.5 pt-2 border-t border-slate-100">
                  <h4 className="text-xs font-bold text-slate-800 uppercase tracking-wide">Technical Specs:</h4>
                  {item.specifications.map((spec, idx) => (
                    <div key={idx} className="flex items-center gap-2 text-xs text-slate-600">
                      <Check className="w-3.5 h-3.5 text-emerald-600 shrink-0" />
                      <span>{spec}</span>
                    </div>
                  ))}
                </div>

                {/* Packaging & Sectors */}
                <div className="mt-4 pt-3 border-t border-slate-100 text-xs space-y-1 text-slate-500">
                  <p><strong>Packing:</strong> {item.packaging.join(', ')}</p>
                  <p><strong>Primary Off-Takers:</strong> {item.targetSectors.slice(0, 2).join(', ')}</p>
                </div>
              </div>

              {/* Action Button */}
              <div className="px-6 pb-6 pt-2 bg-slate-50/50 border-t border-slate-100">
                <button
                  onClick={() => onSelectCommodity(item)}
                  className="w-full bg-slate-900 hover:bg-emerald-700 text-white font-semibold py-2.5 px-4 rounded-xl text-xs transition-colors flex items-center justify-center gap-2"
                >
                  <span>Request Specifications & Pricing</span>
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};
