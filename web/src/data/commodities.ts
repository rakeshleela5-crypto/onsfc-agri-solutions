export interface Commodity {
  id: string;
  name: string;
  teluguName: string;
  category: 'Paddy & Rice' | 'Pulses & Dals' | 'Oilseeds & Oils' | 'Commercial Cash Crops' | 'Millets & Feed';
  grade: string;
  aging: string;
  cookingExpansion: string;
  specifications: string[];
  packaging: string[];
  targetSectors: string[];
  icon: string;
  isPopular?: boolean;
}

export const COMMODITIES: Commodity[] = [
  {
    id: "sona-masoori-aged",
    name: "Naturally Aged Sona Masoori Rice (BPT 5204)",
    teluguName: "నిల్వ ఉంచిన సోనా మసూరి బియ్యం (BPT 5204)",
    category: "Paddy & Rice",
    grade: "Grade-A Sortex Cleaned",
    aging: "12 to 14 Months Naturally Stored",
    cookingExpansion: "1:2.8 Volumetric Yield",
    specifications: [
      "Moisture Content: < 12.0%",
      "Purity: 100% Sortex Optical Graded",
      "Stones & Silica: 0.00% (Pneumatically Destoned)",
      "Grain Texture: Non-sticky, long, distinct grain structure"
    ],
    packaging: ["25 kg HDPE Bags", "50 kg Non-woven Bags", "1,000 kg Jumbo Silo Bags"],
    targetSectors: ["Automotive Plant Commissaries", "University Campus Hostels", "Premier Hotels & Banquets", "Temple Annadhanam Halls"],
    icon: "🌾",
    isPopular: true
  },
  {
    id: "low-gi-telangana-sona",
    name: "Low-GI Telangana Sona Rice (RNR 15048)",
    teluguName: "తక్కువ గ్లైసెమిక్ తెలంగాణ సోనా (RNR 15048)",
    category: "Paddy & Rice",
    grade: "Diabetic-Friendly Certified",
    aging: "10 to 12 Months Naturally Aged",
    cookingExpansion: "1:2.6 Volumetric Yield",
    specifications: [
      "Glycemic Index: < 55 (Clinically Tested)",
      "High Dietary Fiber & Complex Carbohydrates",
      "Broken Percentage: < 2.0%",
      "100% Chemical & Polish Residue Free"
    ],
    packaging: ["5 kg Retail Pouches", "25 kg Consumer Bags", "50 kg Hospital Packs"],
    targetSectors: ["Corporate Multi-Specialty Hospitals", "Big-4 Tech Park Wellness Canteens", "Premium Supermarket Retail"],
    icon: "🍚",
    isPopular: true
  },
  {
    id: "idli-broken-rice",
    name: "High-Gelatinization Idli Broken Rice (Nookalu / Kurunai)",
    teluguName: "ఇడ్లీ నూకలు / గుండు నూకలు",
    category: "Paddy & Rice",
    grade: "Triple-Screened Uniform Granules",
    aging: "Naturally Aged Raw Paddy Milled",
    cookingExpansion: "Superior Batter Puff & Fluff",
    specifications: [
      "Particle Sizing: Uniform 1.2mm - 1.5mm Granules",
      "Fermentation Acceleration: Active Natural Starch",
      "De-dusted: Zero Fine Flour Dust",
      "Puffing Quality: Premium for Mandakki Bhattis"
    ],
    packaging: ["25 kg Bags", "50 kg Gunny / HDPE Bags"],
    targetSectors: ["Bellary Mandakki Bhattis (Puffed Rice)", "Train Pantry Car Guilds", "QSR & Tiffin Centers", "Batter Factories"],
    icon: "🥣",
    isPopular: true
  },
  {
    id: "unpolished-toor-dal",
    name: "Sortex Unpolished Toor Dal (Red Gram / Kandi Pappu)",
    teluguName: "పాలిష్ లేని నాటు కంది పప్పు",
    category: "Pulses & Dals",
    grade: "Premium Desi Bold Split",
    aging: "Fresh Kharif Dryland Crop",
    cookingExpansion: "High Water Absorption & Emulsion",
    specifications: [
      "Processing: Unpolished, Chemically Untreated, Water-washed",
      "Protein Content: > 22.5% Crude Protein",
      "Cooking Speed: Melts into thick golden sambar without sediment separation",
      "Foreign Matter: < 0.05%"
    ],
    packaging: ["25 kg PP Bags", "50 kg Heavy Woven Sacks"],
    targetSectors: ["Hospital Dietary Kitchens", "Railway Pantries", "College Hostels", "Military Messes"],
    icon: "🍲",
    isPopular: true
  },
  {
    id: "desi-bengal-gram",
    name: "Desi Bengal Gram & Roasted Chana (Senagalu & Putnalu)",
    teluguName: "దేశీ శనగలు మరియు వేయించిన పుట్నాలు",
    category: "Pulses & Dals",
    grade: "Bold Dryland Desi Chana / Besan Grade",
    aging: "Current Rabi Season Stored",
    cookingExpansion: "Maximum Aroma and Crispiness",
    specifications: [
      "Moisture: < 9.5%",
      "Besan Yield: Ultra-fine silky flour for traditional Mysore Pak & Sweets",
      "Putnalu Roasting: Crisp, golden, oil-free roasted split gram",
      "Purity: Machine Cleaned & Graded"
    ],
    packaging: ["25 kg Bags", "50 kg Bags"],
    targetSectors: ["Nandyal & Kurnool Putnalu Mills", "Traditional Sweet Manufacturers", "Wedding Caterers Guild", "Snack Giants"],
    icon: "🧆"
  },
  {
    id: "urad-dal-gota",
    name: "Pure White Urad Dal Gota (Whole Black Gram Skinned)",
    teluguName: "మినప గుండ్లు (ఉద్ది బేడలు)",
    category: "Pulses & Dals",
    grade: "Grade-1 Round Gota",
    aging: "Cool Godown Preserved",
    cookingExpansion: "High Batter Volume & Elasticity",
    specifications: [
      "Batter Yield: 1:3.2 Expansion in Wet Grinding",
      "Whiteness Index: Naturally pristine white, unbleached",
      "Admixture: < 0.1%",
      "Texture: Ideal for fluffy Chennai Medu Vadas & Idlis"
    ],
    packaging: ["25 kg Bags", "50 kg Bags"],
    targetSectors: ["Chennai HORECA & Hotel Saravana Bhavan", "Bengaluru Darshini Chains", "Cloud Kitchens"],
    icon: "🥟"
  },
  {
    id: "filtered-groundnut-oil",
    name: "Filtered Pure Groundnut Oil (Wood-Pressed / Expeller)",
    teluguName: "స్వచ్ఛమైన గానుగ వేరుశనగ నూనె",
    category: "Oilseeds & Oils",
    grade: "Food-Grade Double Filtered",
    aging: "Cold Processed from Bold Kernels",
    cookingExpansion: "High Smoke Point (> 225°C)",
    specifications: [
      "Extracted from: 100% Rayalaseema Bold Groundnut Kernels",
      "Chemicals & Solvents: Zero Added Chemicals or Preservatives",
      "Natural Aroma: Rich nutty flavor without oily aftertaste",
      "Free Fatty Acids: < 1.0%"
    ],
    packaging: ["15 Litre Food-Grade Tins", "15 Kg Metal Containers", "200 Litre Food-Grade Drums"],
    targetSectors: ["Industrial Plant Cafeterias", "Luxury Banquets & Wedding Caterers", "Namkeen & Farsan Manufacturers"],
    icon: "🫗",
    isPopular: true
  },
  {
    id: "groundnut-kernels",
    name: "Bold Groundnut Kernels (Palli / Shenga)",
    teluguName: "వేరుశనగ పప్పు (పల్లీలు / గుళ్ళు)",
    category: "Oilseeds & Oils",
    grade: "Count 50/60 & 60/70 Bold",
    aging: "Moisture Tested & Machine Decorticated",
    cookingExpansion: "High Oil Content (> 48%)",
    specifications: [
      "Aflatoxin: Certified Negative (< 4 ppb)",
      "Moisture: < 7.0%",
      "Damage / Shrivelled: < 1.5%",
      "Flavor: Sweet, crunchy, ideal for Chikki & snack roasting"
    ],
    packaging: ["50 kg Jute Bags", "50 kg Vacuum PP Bags"],
    targetSectors: ["Kovilpatti & Chittoor Chikki Manufacturers", "EXIM Export Houses", "Snack Conglomerates"],
    icon: "🥜"
  },
  {
    id: "karnataka-ragi-millets",
    name: "Karnataka Ragi & Ancient Millets (Jowar / Foxtail Korra)",
    teluguName: "రాగులు (తైదలు), జొన్నలు మరియు కొర్రలు",
    category: "Millets & Feed",
    grade: "Cleaned Native Desi Seed",
    aging: "Dry Season Harvest",
    cookingExpansion: "High Dietary Fiber & Mineral Density",
    specifications: [
      "Ragi Calcium: > 340mg per 100g",
      "Zero Grit: Multi-deck destoned and aspirator cleaned",
      "Foxtail Millet (Korra): High protein diabetic staple",
      "Jowar: Bold white grain for authentic North Karnataka rotis"
    ],
    packaging: ["25 kg Bags", "50 kg Bags"],
    targetSectors: ["Automotive Worker Dining (Toyota / TVS)", "Bengaluru Health & Wellness Brands", "Ayurvedic Ashrams"],
    icon: "🥣"
  },
  {
    id: "guntur-teja-chilies",
    name: "Sun-Dried Red Chilies (Guntur Teja & Byadgi)",
    teluguName: "ఎండబెట్టిన ఎర్ర మిరపకాయలు (తేజ / బ్యాడగి)",
    category: "Commercial Cash Crops",
    grade: "Stemless & With Stem Sortex Selected",
    aging: "Sun-Dried under Rayalaseema Sun",
    cookingExpansion: "Intense Heat & Deep Natural Color",
    specifications: [
      "Capsaicin Level: 70,000 - 90,000 SHU (High Heat Teja)",
      "Color Value (ASTA): 120 - 160 ASTA (Deep Red Byadgi)",
      "Moisture: < 10.0%",
      "Foreign Matter: < 0.5%"
    ],
    packaging: ["10 kg Compressed Cartons", "25 kg Jute Bales"],
    targetSectors: ["Oleoresin & Spice Extraction Plants", "Pickle & Masala Giants", "HORECA Chains", "EXIM Exporters"],
    icon: "🌶️"
  },
  {
    id: "raw-kapas-cotton",
    name: "Raw Seed Cotton (Kapas) & Ginning Bales",
    teluguName: "నాటు ప్రత్తి (కపాస్) మరియు బేళ్లు",
    category: "Commercial Cash Crops",
    grade: "Medium & Long Staple (29mm - 31mm)",
    aging: "Dry Farm Gate Harvest",
    cookingExpansion: "High Micronaire 3.8 - 4.2",
    specifications: [
      "Staple Length: 29mm to 31.5mm",
      "Trash Content: < 2.5%",
      "Moisture: < 8.0%",
      "Strength: 28 to 30 g/tex"
    ],
    packaging: ["170 kg Standard Compressed Bales"],
    targetSectors: ["Spinning Mills (Coimbatore, Guntur, Bellary)", "Textile Conglomerates", "Cotton Corporation of India"],
    icon: "☁️"
  },
  {
    id: "yellow-maize-feed",
    name: "Yellow Industrial & Feed Maize (Corn)",
    teluguName: "పసుపు పచ్చ మొక్కజొన్న",
    category: "Millets & Feed",
    grade: "Feed & Starch Grade #1",
    aging: "Silo Dry Stored",
    cookingExpansion: "High Starch Content (> 68%)",
    specifications: [
      "Moisture: < 13.5%",
      "Foreign Matter: < 1.0%",
      "Broken Grains: < 3.0%",
      "Aflatoxin: < 20 ppb"
    ],
    packaging: ["50 kg Bags", "Bulk Tipping Trailers (25 MT)"],
    targetSectors: ["Jadcherla & Hosur Starch Refineries", "Aquafeed & Poultry Feed Compounders", "Snack Extruders"],
    icon: "🌽"
  }
];
