export interface MarketTier {
  tierNumber: number;
  name: string;
  region: string;
  buyerCount: number;
  distanceKm: string;
  transitHours: string;
  highway: string;
  dominantCommodities: string;
  keyBuyers: string[];
}

export const MARKET_TIERS: MarketTier[] = [
  {
    tierNumber: 1,
    name: "Local Quad-Territory",
    region: "Gooty, Guntakal, Pamidi, Ananthapuramu (AP)",
    buyerCount: 141,
    distanceKm: "0 - 50 km",
    transitHours: "20 min - 1.0 hr",
    highway: "NH-44 / NH-67 Corridor",
    dominantCommodities: "Sona Masoori Rice, Toor Dal, Raw Kapas, Groundnut Pods & Oil",
    keyBuyers: ["Gooty Rly Canteens", "Guntakal Junction Commissaries", "Pamidi Ginning Mills", "Anantapur Grain Mandi"]
  },
  {
    tierNumber: 2,
    name: "Northern High-Ticket Corridor",
    region: "Kurnool Metropolis & Mantralayam (AP)",
    buyerCount: 34,
    distanceKm: "92 km",
    transitHours: "1.5 hrs",
    highway: "NH-44 North Corridor",
    dominantCommodities: "Annadhanam Sona Masoori, Broken Rice, Damodara Peanuts, Putnalu",
    keyBuyers: ["Sri Raghavendra Swamy Matha", "IIITDM Kurnool", "Kurnool Medical College", "Damodara Oil Mills"]
  },
  {
    tierNumber: 3,
    name: "Dual Mega-Metros (QSR & Feed)",
    region: "Bengaluru (KA) & Hyderabad (TS)",
    buyerCount: 30,
    distanceKm: "290 - 300 km",
    transitHours: "4.5 hrs (Overnight)",
    highway: "NH-44 Express Haul",
    dominantCommodities: "Aged Sona Masoori (BPT 5204), RNR 15048, Yellow Maize (150k MT Silos)",
    keyBuyers: ["CTR Shri Sagar", "Vidyarthi Bhavan", "Paradise Biryani", "Suguna & Godrej Feed Silos"]
  },
  {
    tierNumber: 4,
    name: "Bengaluru Educational Campuses",
    region: "Yelahanka, Mysore Rd, Electronic City (KA)",
    buyerCount: 35,
    distanceKm: "280 - 320 km",
    transitHours: "4.5 hrs",
    highway: "NH-44 -> NICE Expressway",
    dominantCommodities: "Aged Sona Masoori, Broken Idli Rice, Unpolished Toor Dal, Karnataka Ragi",
    keyBuyers: ["RVCE Hostels", "PES University", "BMS College of Engineering", "Jain International Residential"]
  },
  {
    tierNumber: 5,
    name: "Bengaluru Healthcare Dietary & Cloud Kitchens",
    region: "Bommasandra, Whitefield, Koramangala (KA)",
    buyerCount: 35,
    distanceKm: "290 - 330 km",
    transitHours: "4.5 hrs",
    highway: "NH-44 South Artery",
    dominantCommodities: "Low-GI RNR 15048, High-Starch Broken Rice (iD Fresh), Toor Dal",
    keyBuyers: ["iD Fresh Food Factory", "Narayana Hrudayalaya", "St. John's Medical College", "Rebel Foods"]
  },
  {
    tierNumber: 6,
    name: "Hyderabad Healthcare, Cloud Kitchens & Unis",
    region: "Gachibowli, Hitec City, Shamshabad (TS)",
    buyerCount: 45,
    distanceKm: "280 - 310 km",
    transitHours: "4.5 hrs",
    highway: "NH-44 North Artery",
    dominantCommodities: "Low-GI Telangana Sona, Aged Sona Masoori, Toor Dal, Red Chilies",
    keyBuyers: ["Apollo Health City", "KIMS Hospitals", "CBIT Hostels", "VNR VJIET", "EatFit Commissaries"]
  },
  {
    tierNumber: 7,
    name: "Bengaluru Supermarket DCs & Food Mfg",
    region: "Nelamangala, Peenya, Bidadi, Harohalli (KA)",
    buyerCount: 35,
    distanceKm: "290 - 340 km",
    transitHours: "4.5 hrs",
    highway: "NH-44 -> NH-48 / NICE",
    dominantCommodities: "Packaged Staples (5kg/25kg), Besan-Grade Bengal Gram, Groundnut Kernels",
    keyBuyers: ["DMart Nelamangala DC", "Reliance Retail Hosakote DC", "MTR Foods Harohalli", "Anand Sweets"]
  },
  {
    tierNumber: 8,
    name: "Hyderabad Supermarket DCs & Food Mfg",
    region: "Medchal, Kattedan, Cherlapally, Begum Bazaar (TS)",
    buyerCount: 35,
    distanceKm: "290 - 320 km",
    transitHours: "4.5 hrs",
    highway: "NH-44 North",
    dominantCommodities: "Packaged Rice, Besan, Murmura Broken Rice (Kattedan Mills), Red Chilies",
    keyBuyers: ["Ratnadeep Supermarkets DC", "Vijetha Supermarkets DC", "G. Pulla Reddy Sweets", "Bikanervala"]
  },
  {
    tierNumber: 9,
    name: "Hyderabad Film Production Banners & Studios",
    region: "Film Nagar, Jubilee Hills, Ramoji Film City (TS)",
    buyerCount: 35,
    distanceKm: "300 - 330 km",
    transitHours: "5.0 hrs",
    highway: "NH-44 -> ORR -> NH-65",
    dominantCommodities: "Aged Sona Masoori, Breakfast Broken Rice, Toor Dal, Desi Besan, Peanuts",
    keyBuyers: ["Ramoji Film City Commissaries", "Annapurna Studios", "Suresh Productions", "Mythri Movie Makers"]
  },
  {
    tierNumber: 10,
    name: "Bengaluru Film Production Banners & Studios",
    region: "Basavanagudi, Gandhinagar, Bidadi Film City (KA)",
    buyerCount: 35,
    distanceKm: "290 - 320 km",
    transitHours: "4.5 hrs",
    highway: "NH-44 -> NICE Highway",
    dominantCommodities: "Aged Sona Masoori, Native Ragi (Daily Ragi Mudde), Toor Dal, Shenga Peanuts",
    keyBuyers: ["Hombale Films Catering", "Rockline Studios", "Kanteerava Studios", "Innovative Film City"]
  },
  {
    tierNumber: 11,
    name: "Hyderabad HORECA & Iconic Biryani Empires",
    region: "Old City, Secunderabad, Banjara Hills (TS)",
    buyerCount: 40,
    distanceKm: "300 - 310 km",
    transitHours: "4.5 hrs",
    highway: "NH-44 Direct Expressway",
    dominantCommodities: "Naturally Aged Sona Masoori, High-Protein Toor Dal, Filtered Groundnut Oil",
    keyBuyers: ["Bawarchi RTC X Roads", "Hotel Shadab", "Shah Ghouse Chain", "Chutneys Chain", "Minerva Coffee"]
  },
  {
    tierNumber: 12,
    name: "Bengaluru HORECA & Heritage Food Chains",
    region: "Jayanagar, Indiranagar, Malleshwaram (KA)",
    buyerCount: 40,
    distanceKm: "290 - 310 km",
    transitHours: "4.5 hrs",
    highway: "NH-44 Direct Expressway",
    dominantCommodities: "Aged BPT 5204, High-Gelatinization Broken Rice, Unpolished Toor Dal",
    keyBuyers: ["Nagarjuna Andhra Restaurants", "Meghana Foods Chain", "Udupi Sri Krishna Bhavan", "Maiyas"]
  },
  {
    tierNumber: 13,
    name: "Agricultural EXIM Houses & Merchant Exporters",
    region: "Chennai Port, Krishnapatnam Port, Kakinada (AP/TN)",
    buyerCount: 40,
    distanceKm: "280 - 450 km",
    transitHours: "5.0 - 8.0 hrs",
    highway: "NH-67 / NH-40 Port Trunks",
    dominantCommodities: "Raw Kapas & Cotton Bales, Bold Peanuts (HPS), Red Chilies, Non-Basmati Rice",
    keyBuyers: ["ITC Agri Business Division", "Olam Agri India", "Adani Wilmar Port Silos", "Cargill India"]
  },
  {
    tierNumber: 14,
    name: "Sovereign, Divine & Heavy Industrial Off-Takers",
    region: "Tirumala (TTD), Singareni Collieries, BHEL, DRDO",
    buyerCount: 40,
    distanceKm: "180 - 320 km",
    transitHours: "3.5 - 5.0 hrs",
    highway: "NH-40 / NH-44 Expressways",
    dominantCommodities: "Sacred Annadhanam Sona Masoori, High-Protein Dals, Pure Cooking Oil",
    keyBuyers: ["TTD Nitya Annaprasadam (100k meals/day)", "Singareni Collieries (SCCL)", "BHEL Ramachandrapuram", "DRDO"]
  },
  {
    tierNumber: 15,
    name: "Mega-Conventions, Prisons, Ethanol & SEZs",
    region: "Central Jails, HITEX, BIEC, Ethanol Plants",
    buyerCount: 40,
    distanceKm: "80 - 310 km",
    transitHours: "1.5 - 5.0 hrs",
    highway: "Regional Express Corridors",
    dominantCommodities: "High-Starch Broken Rice (Ethanol/Murmura), Standard Sona Masoori, Yellow Corn",
    keyBuyers: ["Cherlapally Central Prison", "Bengaluru Central Prison (Parappana Agrahara)", "HITEX Exhibition Centre", "Kurnool Distilleries"]
  },
  {
    tierNumber: 16,
    name: "Industrial Starch, Dairy Feed, Breweries & RTE",
    region: "Dharmapuri, Chittoor, Jadcherla, Bengaluru (KA/TN)",
    buyerCount: 40,
    distanceKm: "200 - 320 km",
    transitHours: "3.5 - 5.0 hrs",
    highway: "NH-44 Southern Industrial Belt",
    dominantCommodities: "Industrial Broken Rice (Starch/Brewing), Yellow Feed Maize, Groundnut De-oiled Cake",
    keyBuyers: ["United Breweries (Heineken)", "Amrit Feeds", "Keventer Agro", "TajSATS Flight Kitchens"]
  },
  {
    tierNumber: 17,
    name: "Aquafeed, Snack Giants, Spinning Mills & Pharma",
    region: "Nellore, Bhimavaram, Guntur, Hyderabad (AP/TS)",
    buyerCount: 40,
    distanceKm: "180 - 380 km",
    transitHours: "3.5 - 6.5 hrs",
    highway: "NH-544D / NH-16 Coastal Trunks",
    dominantCommodities: "De-oiled Groundnut Cake (Shrimp Feed), Raw Kapas Bales, Maize Starch, Red Chilies",
    keyBuyers: ["Avanti Feeds Limited", "Haldiram's / Bikaji South", "Guntur Spinning Mills", "Dr. Reddy's Laboratories"]
  },
  {
    tierNumber: 18,
    name: "Defense Depots, Ashrams, Paperboard Starch & Pets",
    region: "ASC Supply Depots, Isha Yoga, Art of Living, ITC",
    buyerCount: 60,
    distanceKm: "90 - 450 km",
    transitHours: "1.5 - 7.5 hrs",
    highway: "Interstate Highway Trunks",
    dominantCommodities: "Destoned Sona Masoori, Unpolished Pulses, Pure Groundnut Oil, Industrial Tapioca/Maize Starch",
    keyBuyers: ["Army Supply Corps (ASC Depot Bengaluru)", "Art of Living Annapoorna", "Isha Foundation Canteens", "ITC Paperboards Bhadrachalam"]
  },
  {
    tierNumber: 19,
    name: "Tirupati Commercial Ecosystem",
    region: "Tirupati Pilgrimage & University Basin (AP)",
    buyerCount: 40,
    distanceKm: "240 km",
    transitHours: "4.0 hrs",
    highway: "NH-716 Direct Artery",
    dominantCommodities: "Naturally Aged Sona Masoori, High-Protein Toor Dal, Filtered Groundnut Oil, Broken Rice",
    keyBuyers: ["Sri Venkateswara University (SVU)", "Mohan Babu University (12k students)", "SVIMS Hospital Kitchen", "Bhimas Deluxe Group"]
  },
  {
    tierNumber: 20,
    name: "Greater Chennai Metropolitan Ecosystem",
    region: "Chennai Urban Agglomeration, Guindy, Koyambedu (TN)",
    buyerCount: 40,
    distanceKm: "370 km",
    transitHours: "6.5 hrs (Overnight)",
    highway: "NH-40 / NH-716 & NH-48",
    dominantCommodities: "High-Amylose Broken Rice (Kurunai Arisi), Urad Dal Gota, Sortex Toor Dal, Besan",
    keyBuyers: ["Hotel Saravana Bhavan Central Commissary", "Murugan Idli Shop Commissary", "IIT Madras Hostels", "Koyambedu KWMC Merchants Guild"]
  },
  {
    tierNumber: 21,
    name: "Kurnool & Nandyal Sacred Twin-District",
    region: "Kurnool Metropolis & Nandyal Agricultural Basin (AP)",
    buyerCount: 40,
    distanceKm: "80 - 90 km",
    transitHours: "1.2 hrs (Rapid Shuttle)",
    highway: "NH-44 & NH-544D",
    dominantCommodities: "Aged Sona Masoori, High-Starch Broken Rice (Uggani Murmura), Desi Chana (Putnalu Roasteries)",
    keyBuyers: ["Rayalaseema University (RU)", "Santhiram Medical College (1,000 beds)", "SPY Agro Industries (300 MT/day)", "Mahanandi Annadhanam"]
  },
  {
    tierNumber: 22,
    name: "Kadapa & Chittoor Sacred Rayalaseema Belt",
    region: "Kadapa Cement Corridor & Chittoor Agro Belt (AP)",
    buyerCount: 40,
    distanceKm: "145 - 240 km",
    transitHours: "2.5 - 4.0 hrs",
    highway: "NH-40 & NH-67",
    dominantCommodities: "Aged Sona Masoori, Sortex Toor Dal, Broken Rice, UltraTech & Dalmia Townships, Temple Prasadam",
    keyBuyers: ["UltraTech Andhra Cement Works (5,000 workers)", "Yogi Vemana University (YVU)", "MITS Madanapalle", "Sri Srikalahasteeswara Temple"]
  },
  {
    tierNumber: 23,
    name: "The 1,000-Buyer Macro-Summit",
    region: "Automotive Plants, Rail Pantries, Big-4 Tech Parks, Hospitals",
    buyerCount: 40,
    distanceKm: "25 - 300 km",
    transitHours: "25 min - 4.5 hrs",
    highway: "NH-44 / NH-67 Expressway Hub",
    dominantCommodities: "100% Destoned Sona Masoori (Zero Stones), Low-GI RNR 15048, High-Gelatinization Broken Rice",
    keyBuyers: ["KIA Motors India (Penukonda - 65 km)", "IRCTC Guntakal Base Kitchen (25 km)", "Sodexo South Corporate Dining", "Apollo Hospitals"]
  },
  {
    tierNumber: 24,
    name: "Bellary & Vijayanagara Strategic Corridor",
    region: "Bellary City, Toranagallu, Sandur & Hampi (KA)",
    buyerCount: 40,
    distanceKm: "75 - 85 km",
    transitHours: "1 hr 15 min",
    highway: "NH-67 Direct Expressway",
    dominantCommodities: "Aged Sona Masoori, Low-GI Rice, High-Starch Broken Rice (Mandakki Bhattis), Sortex Toor Dal, Groundnut Oil",
    keyBuyers: ["JSW Steel Vijayanagar Works (35,000 staff)", "Vijayanagar Institute of Medical Sciences (VIMS)", "Sri Virupaksha Temple Hampi", "Sri Kumaraswamy Temple Sandur"]
  }
];
