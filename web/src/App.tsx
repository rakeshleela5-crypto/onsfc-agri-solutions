import React, { useState } from 'react';
import { Header } from './components/Header';
import { Hero } from './components/Hero';
import { CommoditiesSection } from './components/CommoditiesSection';
import { FirstMileHub } from './components/FirstMileHub';
import { NetworkExplorer } from './components/NetworkExplorer';
import { LogisticsSection } from './components/LogisticsSection';
import { VillagesSection } from './components/VillagesSection';
import { RfqModal } from './components/RfqModal';
import { Footer } from './components/Footer';
import { Commodity } from './data/commodities';

export function App() {
  const [isRfqOpen, setIsRfqOpen] = useState(false);
  const [selectedCommodity, setSelectedCommodity] = useState<Commodity | null>(null);

  const handleOpenRfq = (commodity?: Commodity) => {
    setSelectedCommodity(commodity || null);
    setIsRfqOpen(true);
  };

  const handleCloseRfq = () => {
    setIsRfqOpen(false);
    setSelectedCommodity(null);
  };

  return (
    <div className="min-h-screen flex flex-col bg-white text-slate-900 font-sans selection:bg-emerald-600 selection:text-white">
      {/* Sticky Header */}
      <Header onOpenRfq={() => handleOpenRfq()} />

      {/* Main Content */}
      <main className="flex-grow">
        {/* Hero Section */}
        <Hero onOpenRfq={() => handleOpenRfq()} />

        {/* 100% Dry Commodities Catalog */}
        <CommoditiesSection onSelectCommodity={(c) => handleOpenRfq(c)} />

        {/* 1-Acre First Mile Processing Hub at Gooty */}
        <FirstMileHub />

        {/* 1,040 Verified Commercial Off-Takers Explorer */}
        <NetworkExplorer />

        {/* Highway Arteries & Logistics Advantage */}
        <LogisticsSection />

        {/* 24 Gooty Mandal Dryland Villages */}
        <VillagesSection />
      </main>

      {/* Footer */}
      <Footer />

      {/* RFQ / Sample Request Modal */}
      <RfqModal
        isOpen={isRfqOpen}
        onClose={handleCloseRfq}
        selectedCommodity={selectedCommodity}
      />
    </div>
  );
}

export default App;
