import React from 'react';
import { Truck, Navigation, Clock, ShieldCheck, MapPin } from 'lucide-react';

export const LogisticsSection: React.FC = () => {
  const arteries = [
    {
      route: "Gooty -> Bellary / JSW Steel Complex",
      distance: "75 - 85 km",
      time: "1 hr 15 min",
      highway: "NH-67 Direct Expressway",
      type: "High-Frequency Daily Shuttles (2-3 runs/day)",
      keyHighlights: "Toranagallu JSW Steel township, VIMS hospital, Bellary Mandakki cluster, Hampi"
    },
    {
      route: "Gooty -> Guntakal Railway Divisional HQ",
      distance: "25 km",
      time: "25 minutes",
      highway: "NH-67 Direct West Link",
      type: "Same-Day Platform Shuttle",
      keyHighlights: "South Central Railway Division HQ, IRCTC base kitchens & train pantry stocking"
    },
    {
      route: "Gooty -> Kurnool & Nandyal Sacred Basin",
      distance: "80 - 90 km",
      time: "1 hr 15 min",
      highway: "NH-44 North / NH-544D East",
      type: "Rapid Highway Shuttle",
      keyHighlights: "Rayalaseema Univ, Santhiram Medical 1,000 beds, SPY Agro, Putnalu roasteries"
    },
    {
      route: "Gooty -> Kadapa & Tadipatri Cement Belt",
      distance: "145 km",
      time: "2.5 hours",
      highway: "NH-40 / NH-67 Southeast",
      type: "Intra-State Heavy Truckloads",
      keyHighlights: "UltraTech Andhra Cement Works, Dalmia Bharat, Yogi Vemana Univ, Srikalahasti"
    },
    {
      route: "Gooty -> Bengaluru Metropolitan Corridor",
      distance: "290 km",
      time: "4.5 hours (Overnight)",
      highway: "NH-44 South Trunk -> NICE Ring",
      type: "Dedicated Closed Freight (16 - 30 MT)",
      keyHighlights: "5:00 AM delivery to Manyata Tech Park, Electronic City, Bidadi & Hosur TVS"
    },
    {
      route: "Gooty -> Hyderabad Metropolitan Corridor",
      distance: "300 km",
      time: "4.5 hours (Overnight)",
      highway: "NH-44 North Straight Artery",
      type: "Dedicated Closed Freight (16 - 30 MT)",
      keyHighlights: "4:30 AM arrival at Hitec City, Gachibowli, Begum Bazaar & Kattedan mills"
    },
    {
      route: "Gooty -> Greater Chennai Agglomeration",
      distance: "370 km",
      time: "6.5 hours (Overnight)",
      highway: "NH-40 / NH-716 & NH-48",
      type: "Heavy Interstate Container Trucks",
      keyHighlights: "Hotel Saravana Bhavan commissaries, Koyambedu KWMC, Irungattukottai Hyundai"
    }
  ];

  return (
    <section id="logistics" className="py-20 bg-slate-50 border-b border-slate-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center max-w-3xl mx-auto mb-16">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-100 text-blue-800 text-xs font-bold uppercase tracking-wider mb-3">
            <Truck className="w-4 h-4 text-blue-700" />
            <span>Dedicated Highway Arteries</span>
          </div>
          <h2 className="text-3xl sm:text-4xl font-bold font-serif text-slate-900 tracking-tight">
            The Gooty Highway Corridor Advantage
          </h2>
          <p className="text-slate-600 mt-3 text-base">
            Located at the premier transit crossroads of Andhra Pradesh, Karnataka, and Tamil Nadu. Overnight dedicated transit guarantees morning deliveries before urban traffic congestion sets in.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {arteries.map((art, idx) => (
            <div
              key={idx}
              className="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm hover:shadow-md transition-shadow flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between gap-2 mb-3">
                  <span className="bg-slate-100 text-slate-700 text-[11px] font-bold px-2.5 py-0.5 rounded-full">
                    {art.highway}
                  </span>
                  <div className="flex items-center gap-1 text-emerald-700 font-extrabold text-xs">
                    <Clock className="w-3.5 h-3.5" />
                    <span>{art.time}</span>
                  </div>
                </div>

                <h3 className="text-base font-bold text-slate-900 leading-snug">
                  {art.route}
                </h3>
                <div className="text-xs text-slate-500 font-medium mt-1">
                  Distance: <strong>{art.distance}</strong> • {art.type}
                </div>

                <p className="text-xs text-slate-600 mt-3 pt-3 border-t border-slate-100 leading-relaxed">
                  <strong>Servicing:</strong> {art.keyHighlights}
                </p>
              </div>

              <div className="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between text-[11px] text-slate-500 font-medium">
                <span>GPS Tracked Closed Trucks</span>
                <span className="text-emerald-700 font-bold">Zero Spoilage</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};
