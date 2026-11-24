import React, { useState } from 'react';
import { GOOTY_VILLAGES, GootyVillage } from '../data/villages';
import { MapPin, Users, Sprout, Landmark, Search } from 'lucide-react';

export const VillagesSection: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState('');

  const filteredVillages = GOOTY_VILLAGES.filter((v) => {
    const term = searchTerm.toLowerCase();
    return (
      v.name.toLowerCase().includes(term) ||
      v.teluguName.toLowerCase().includes(term) ||
      v.primaryCrops.some((c) => c.toLowerCase().includes(term)) ||
      v.soilType.toLowerCase().includes(term)
    );
  });

  const totalFamilies = GOOTY_VILLAGES.reduce((acc, v) => acc + v.activeFarmingFamilies, 0);

  return (
    <section id="villages" className="py-20 bg-white border-b border-slate-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center max-w-3xl mx-auto mb-12">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 text-xs font-bold uppercase tracking-wider mb-3">
            <Sprout className="w-4 h-4 text-emerald-700" />
            <span>Direct Dryland Farmer Origin</span>
          </div>
          <h2 className="text-3xl sm:text-4xl font-bold font-serif text-slate-900 tracking-tight">
            All 24 Villages of Gooty Mandal
          </h2>
          <p className="text-slate-600 mt-3 text-base">
            Every grain in our inventory is harvested by <strong>{totalFamilies}+ dryland farming families</strong> across all 24 revenue villages of Gooty Mandal (Anantapuramu District). We eliminate middlemen by providing direct gate collection, digital weighbridge ticketing, and instant bank settlements.
          </p>

          <div className="mt-8 max-w-md mx-auto relative">
            <Search className="w-5 h-5 text-slate-400 absolute left-4 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              placeholder="Search village name or crop (e.g. Basinepalle, Groundnut, Cotton)..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full bg-slate-50 border border-slate-300 rounded-xl pl-12 pr-4 py-3 text-slate-900 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-emerald-500 text-sm"
            />
          </div>
        </div>

        {/* Village Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          {filteredVillages.map((v) => (
            <div
              key={v.id}
              className="bg-slate-50 rounded-xl border border-slate-200 p-4 hover:border-emerald-500/50 hover:bg-emerald-50/20 transition-all flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between gap-1 mb-1.5">
                  <span className="text-xs font-bold text-slate-400">#{v.id}</span>
                  <span className="text-[11px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-full">
                    {v.activeFarmingFamilies} Farmers
                  </span>
                </div>

                <h3 className="font-bold text-slate-900 text-base">
                  {v.name}
                </h3>
                <p className="text-xs text-slate-500 font-medium">
                  {v.teluguName} • <span className="text-emerald-700 font-semibold">{v.distanceFromHubKm}</span>
                </p>

                <div className="mt-3 pt-2 border-t border-slate-200/80 text-xs space-y-1">
                  <p className="text-slate-600">
                    <strong>Crops:</strong> {v.primaryCrops.join(', ')}
                  </p>
                  <p className="text-slate-500 text-[11px]">
                    <strong>Soil:</strong> {v.soilType}
                  </p>
                </div>
              </div>

              <div className="mt-3 pt-2 border-t border-slate-200 text-[11px] text-slate-500 flex items-center gap-1">
                <Landmark className="w-3 h-3 text-slate-400 shrink-0" />
                <span className="truncate">{v.aggregationCenter}</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};
