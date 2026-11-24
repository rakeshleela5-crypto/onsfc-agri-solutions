import React, { useState } from 'react';
import { Phone, Mail, MapPin, Menu, X, ShieldCheck, Award } from 'lucide-react';

interface HeaderProps {
  onOpenRfq: () => void;
}

export const Header: React.FC<HeaderProps> = ({ onOpenRfq }) => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  return (
    <header className="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-sm">
      {/* Divine Invocations Banner */}
      <div className="bg-gradient-to-r from-amber-700 via-amber-600 to-amber-700 text-amber-50 px-4 py-1.5 text-xs font-medium text-center tracking-wide flex items-center justify-center gap-2 border-b border-amber-800/20">
        <span className="text-amber-200">🔱</span>
        <span>
          <strong>हर हर महादेव, शंभो शंकर!</strong> — Operating with the Divine Grace & Blessings of <strong>Lord Shiva</strong>, <strong>Lord Venkateswara Swamy</strong>, <strong>Lord Murugan</strong>, and <strong>Lord Nandiswara</strong>
        </span>
        <span className="text-amber-200">🔱</span>
      </div>

      {/* Main Nav */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-20">
          {/* Logo & Entity Name */}
          <div className="flex items-center gap-3">
            <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-emerald-700 to-emerald-900 text-white flex items-center justify-center font-bold text-2xl shadow-md border border-emerald-600/30">
              🌾
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-extrabold text-xl sm:text-2xl tracking-tight text-slate-900 font-serif">
                  ONSFC <span className="text-emerald-700 font-sans font-bold">AGRI</span>
                </span>
                <span className="bg-emerald-100 text-emerald-800 text-[10px] font-bold px-2 py-0.5 rounded-full uppercase tracking-wider border border-emerald-200">
                  Private Limited
                </span>
              </div>
              <p className="text-xs text-slate-500 font-medium">
                Rayalaseema First-Mile Dry Agro Hub • NH-44 Gooty Corridor
              </p>
            </div>
          </div>

          {/* Desktop Links */}
          <nav className="hidden lg:flex items-center gap-7 text-sm font-semibold text-slate-700">
            <a href="#about" className="hover:text-emerald-700 transition-colors">About Hub</a>
            <a href="#commodities" className="hover:text-emerald-700 transition-colors flex items-center gap-1">
              <span>100% Dry Produce</span>
              <span className="bg-amber-100 text-amber-800 text-[10px] px-1.5 py-0.5 rounded font-bold">Zero Perishables</span>
            </a>
            <a href="#quality-tech" className="hover:text-emerald-700 transition-colors">Pneumatic De-stoning</a>
            <a href="#network" className="hover:text-emerald-700 transition-colors flex items-center gap-1">
              <span>1,040 Buyer Network</span>
              <span className="bg-emerald-100 text-emerald-800 text-[10px] px-1.5 py-0.5 rounded-full font-bold">24 Tiers</span>
            </a>
            <a href="#villages" className="hover:text-emerald-700 transition-colors">24 Gooty Villages</a>
          </nav>

          {/* Action Button */}
          <div className="hidden sm:flex items-center gap-3">
            <button
              onClick={onOpenRfq}
              className="bg-gradient-to-r from-emerald-700 to-emerald-800 hover:from-emerald-800 hover:to-emerald-900 text-white px-4 py-2.5 rounded-lg text-sm font-bold shadow-sm hover:shadow transition-all flex items-center gap-2"
            >
              <Award className="w-4 h-4 text-amber-300" />
              <span>Request 50kg Trial Lot</span>
            </button>
          </div>

          {/* Mobile Menu Toggle */}
          <div className="flex sm:hidden">
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="text-slate-700 hover:text-emerald-700 p-2"
              aria-label="Toggle Menu"
            >
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Menu Dropdown */}
      {mobileMenuOpen && (
        <div className="lg:hidden border-t border-slate-200 bg-white px-4 pt-3 pb-6 space-y-3">
          <a
            href="#about"
            onClick={() => setMobileMenuOpen(false)}
            className="block py-2 text-slate-800 font-medium hover:text-emerald-700"
          >
            About Hub
          </a>
          <a
            href="#commodities"
            onClick={() => setMobileMenuOpen(false)}
            className="block py-2 text-slate-800 font-medium hover:text-emerald-700"
          >
            100% Dry Commodities (Zero Perishables)
          </a>
          <a
            href="#quality-tech"
            onClick={() => setMobileMenuOpen(false)}
            className="block py-2 text-slate-800 font-medium hover:text-emerald-700"
          >
            Pneumatic Quality Tech
          </a>
          <a
            href="#network"
            onClick={() => setMobileMenuOpen(false)}
            className="block py-2 text-slate-800 font-medium hover:text-emerald-700"
          >
            1,040 Commercial Off-Takers (24 Tiers)
          </a>
          <a
            href="#villages"
            onClick={() => setMobileMenuOpen(false)}
            className="block py-2 text-slate-800 font-medium hover:text-emerald-700"
          >
            24 Gooty Mandal Villages
          </a>
          <div className="pt-2">
            <button
              onClick={() => {
                setMobileMenuOpen(false);
                onOpenRfq();
              }}
              className="w-full bg-emerald-700 text-white py-3 rounded-lg font-bold text-center flex items-center justify-center gap-2"
            >
              <Award className="w-4 h-4 text-amber-300" />
              <span>Request 50kg Trial Lot</span>
            </button>
          </div>
        </div>
      )}
    </header>
  );
};
