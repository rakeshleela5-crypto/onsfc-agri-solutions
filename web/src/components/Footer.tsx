import React from 'react';
import { Phone, Mail, MapPin, ShieldCheck, Heart, Sparkles } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer className="bg-slate-950 text-slate-400 text-xs border-t border-slate-800">
      {/* Divine Blessing Banner */}
      <div className="bg-gradient-to-r from-amber-950 via-slate-900 to-amber-950 py-4 px-4 text-center border-b border-amber-900/30">
        <p className="text-amber-200/90 font-medium tracking-wide">
          🔱 <strong>हर हर महादेव, शंभो शंकर!</strong> — Consecrated with the Divine Grace and Blessings of <strong>Lord Shiva</strong>, <strong>Lord Venkateswara Swamy</strong>, <strong>Lord Murugan</strong>, and <strong>Lord Nandiswara</strong> 🔱
        </p>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-14">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {/* Col 1: About */}
          <div className="space-y-3">
            <div className="flex items-center gap-2">
              <span className="text-2xl">🌾</span>
              <span className="font-serif font-extrabold text-white text-lg tracking-tight">
                ONSFC <span className="text-emerald-500 font-sans">AGRI SOLUTIONS</span>
              </span>
            </div>
            <p className="text-slate-400 leading-relaxed text-xs">
              Rayalaseema's premier farmer-first agricultural aggregation, pneumatic de-stoning, and dry godown facility. Dedicated to eliminating middlemen and securing reliable B2B supply for South India.
            </p>
            <div className="text-[11px] text-amber-300 font-semibold">
              100% Dry Agricultural Produce Only • Zero Perishables
            </div>
          </div>

          {/* Col 2: Hub Location */}
          <div className="space-y-3">
            <h4 className="font-bold text-white uppercase tracking-wider text-xs font-serif">
              Central Processing Hub
            </h4>
            <div className="flex items-start gap-2">
              <MapPin className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
              <span>
                1-Acre Facility, NH-44 Expressway Corridor,<br />
                Gooty Mandal, Anantapuramu District,<br />
                Andhra Pradesh - 515401
              </span>
            </div>
            <p className="text-[11px] text-slate-500">
              Proximity: 25 km from Guntakal Jn • 75 km from Bellary • 85 km from JSW Steel Toranagallu.
            </p>
          </div>

          {/* Col 3: Direct Contacts */}
          <div className="space-y-3">
            <h4 className="font-bold text-white uppercase tracking-wider text-xs font-serif">
              Commercial Directorate
            </h4>
            <div className="space-y-2">
              <div className="flex items-center gap-2">
                <Phone className="w-4 h-4 text-emerald-400 shrink-0" />
                <span>+91 8558 277100 / +91 8555 288400</span>
              </div>
              <div className="flex items-center gap-2">
                <Mail className="w-4 h-4 text-emerald-400 shrink-0" />
                <span>procurement@onsfcagri.com</span>
              </div>
              <div className="flex items-center gap-2">
                <Mail className="w-4 h-4 text-emerald-400 shrink-0" />
                <span>commercial@onsfcagri.com</span>
              </div>
            </div>
          </div>

          {/* Col 4: Statutory & ESG */}
          <div className="space-y-3">
            <h4 className="font-bold text-white uppercase tracking-wider text-xs font-serif">
              Statutory Governance
            </h4>
            <div className="space-y-1.5 text-[11px] text-slate-400">
              <p>✓ FSSAI Registered First-Mile Facility</p>
              <p>✓ GST Compliant Invoicing & Weighment</p>
              <p>✓ AP Endowments Audit Compliant</p>
              <p>✓ Direct Farmer Digital Bank Settlements</p>
            </div>
          </div>
        </div>

        {/* Bottom copyright */}
        <div className="mt-12 pt-8 border-t border-slate-900 flex flex-col sm:flex-row items-center justify-between gap-4 text-center text-slate-500 text-[11px]">
          <p>© {new Date().getFullYear()} ONSFC Agri Solutions Private Limited. All Rights Reserved.</p>
          <p className="text-slate-400">
            Rayalaseema Dryland Farmer Empowerment • 24 Villages of Gooty Mandal
          </p>
        </div>
      </div>
    </footer>
  );
};
