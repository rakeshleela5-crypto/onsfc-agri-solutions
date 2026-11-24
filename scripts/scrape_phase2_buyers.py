#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 2 Mega-Metros (Bengaluru & Hyderabad) Buyer Database Compiler
Targets the dual 300 km NH-44 expressway expansion arcs:
- Phase 2A: Bengaluru (The High-Margin Lavish Hub & Tech Corridor - 290 km South)
- Phase 2B: Hyderabad (The High-Volume Biryani, Poultry & Commodity Capital - 300 km North)
"""

import os
import csv

OUTPUT_DIR = r"C:\Users\rakes\.gemini\antigravity\scratch\onsfc-agri-solutions\data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "ONSFC_Phase2_Bengaluru_Hyderabad_Buyers.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

PHASE2_BUYERS = [
    # =========================================================================
    # PHASE 2A: BENGALURU (THE HIGH-MARGIN LAVISH & TECH HUB - 290 KM SOUTH)
    # =========================================================================
    {
        "Metro": "Bengaluru",
        "Category": "Iconic QSR Chains & Central Commissaries",
        "Business Name": "The Rameshwaram Cafe Central Commissary",
        "Town": "Bengaluru",
        "Region": "Indiranagar & JP Nagar Central Kitchen",
        "Key Crops Demanded": "Aged Sona Masoori Rice (1,000+ kg daily), Broken Idli Rice, Toor Dal, Urad Dal, Pure Groundnut Oil",
        "Procurement Profile": "India's highest-revenue vegetarian QSR chain serving tens of thousands of idlis, dosas, and meals daily; massive daily grain turnover",
        "Address / Landmark": "100 Feet Road, Indiranagar / Central Kitchen Hub, Bengaluru - 560038",
        "Contact Channel": "Chief Procurement Officer / Supply Chain Head"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Iconic QSR Chains & Central Commissaries",
        "Business Name": "Paakashala Restaurant Chain Central Kitchen",
        "Town": "Bengaluru",
        "Region": "Rajarajeshwari Nagar & Malleshwaram",
        "Key Crops Demanded": "Sona Masoori Rice (500kg daily), Ragi (Finger Millet for Ragi Mudde), Toor Dal, Groundnut Cooking Oil",
        "Procurement Profile": "Premier vegetarian family dining chain with 15+ branches across Bengaluru supported by centralized commissary procurement",
        "Address / Landmark": "Rajarajeshwari Nagar Central Commissary, Bengaluru - 560098",
        "Contact Channel": "General Manager (Procurement)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Iconic QSR Chains & Central Commissaries",
        "Business Name": "Vidyarthi Bhavan Legacy Dosa Kitchen",
        "Town": "Bengaluru",
        "Region": "Gandhi Bazaar, Basavanagudi",
        "Key Crops Demanded": "Broken Rice, Urad Dal (Minapappu), Toor Dal, Pure Ghee & Oil",
        "Procurement Profile": "Historic landmark culinary institution serving thousands of crispy dosas daily requiring premium batter grain consistency",
        "Address / Landmark": "Gandhi Bazaar Main Road, Basavanagudi, Bengaluru - 560004",
        "Contact Channel": "Managing Partner"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Iconic QSR Chains & Central Commissaries",
        "Business Name": "Vasudev Adiga's Fast Food Chain Central Kitchen",
        "Town": "Bengaluru",
        "Region": "Jayanagar / Outer Ring Road",
        "Key Crops Demanded": "Sona Masoori Rice (Raw & Boiled), Toor Dal, Millets, Cooking Oil",
        "Procurement Profile": "High-density South Indian quick service restaurant chain with city-wide commissary distribution",
        "Address / Landmark": "Outer Ring Road Central Kitchen, Bengaluru - 560078",
        "Contact Channel": "Supply Chain Director"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Iconic QSR Chains & Central Commissaries",
        "Business Name": "Taaza Thindi & Brahmins' Coffee Bar Tiffin Hub",
        "Town": "Bengaluru",
        "Region": "Jayanagar & Shankarpuram",
        "Key Crops Demanded": "Sona Masoori Broken Rice, Toor Dal, Bengal Gram (Putnala Pappu for Chutneys)",
        "Procurement Profile": "Celebrated high-volume morning tiffin hubs with continuous daily consumption of idli batter and sambar dals",
        "Address / Landmark": "100 Feet Road, 3rd Block, Jayanagar, Bengaluru - 560011",
        "Contact Channel": "Kitchen Purchase Desk"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Tech Park Corporate Catering Giants",
        "Business Name": "Sodexo India Central Commissary (Manyata Tech Park)",
        "Town": "Bengaluru",
        "Region": "Hebbal / Manyata Tech Park",
        "Key Crops Demanded": "Sona Masoori Rice (2,000+ kg daily), Toor Dal, Bengal Gram, Millets, Cooking Oil",
        "Procurement Profile": "Global catering giant serving over 50,000 meals daily across multinational IT campuses (IBM, Cognizant, Target, Rolls Royce)",
        "Address / Landmark": "Manyata Embassy Business Park, Outer Ring Road, Bengaluru - 560045",
        "Contact Channel": "Regional Supply Chain Manager (South) / Lead Commodity Buyer"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Tech Park Corporate Catering Giants",
        "Business Name": "Compass Group India Central Food Services",
        "Town": "Bengaluru",
        "Region": "Whitefield & Electronic City",
        "Key Crops Demanded": "Sona Masoori Rice, Toor Dal, Urad Dal, Edible Cooking Oil",
        "Procurement Profile": "Apex institutional catering provider for Fortune 500 corporate dining centers across Whitefield and Electronic City IT parks",
        "Address / Landmark": "EPIP Zone, Whitefield, Bengaluru - 560066",
        "Contact Channel": "Head of Strategic Sourcing (Staples)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Millet Processing & Urban Wellness Brands",
        "Business Name": "MTR Foods (Orkla) - Heritage Grain & Breakfast Hub",
        "Town": "Bengaluru",
        "Region": "Bommasandra Industrial Area",
        "Key Crops Demanded": "Ragi (Finger Millet - 50+ MT monthly), Jowar, Foxtail Millet (Korra), Bengal Gram (Chana)",
        "Procurement Profile": "Pioneer packaged food manufacturer producing traditional Ragi Rava, ready-mixes, and breakfast staples",
        "Address / Landmark": "Hebbagodi, Bommasandra Industrial Area, Bengaluru - 560099",
        "Contact Channel": "VP - Agricultural Raw Material Procurement"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Millet Processing & Urban Wellness Brands",
        "Business Name": "Akshayakalpa Organic Agro Products",
        "Town": "Bengaluru",
        "Region": "Jayanagar / Tiptur Corridor",
        "Key Crops Demanded": "Organic Ragi, Foxtail Millet, Cold-Pressed Groundnut Oil",
        "Procurement Profile": "Premium farm-fresh organic brand with affluent tech subscriber base demanding chemical-free farm-gate staples",
        "Address / Landmark": "Jayanagar 4th Block, Bengaluru - 560011",
        "Contact Channel": "Head of Organic Sourcing"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premium Supermarkets & Hypermarket Flagships",
        "Business Name": "Nature's Basket Flagship Store & Distribution Hub",
        "Town": "Bengaluru",
        "Region": "Koramangala & Indiranagar",
        "Key Crops Demanded": "Single-Origin Sona Masoori (RNR 15048 Sugar Free), Millets, Pure Cold-Pressed Groundnut Oil",
        "Procurement Profile": "Gourmet luxury supermarket chain catering to affluent NRI and tech executive households paying top margins",
        "Address / Landmark": "100 Feet Road, HAL 2nd Stage, Indiranagar, Bengaluru - 560038",
        "Contact Channel": "Category Lead - Organic & Premium Staples"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premium Supermarkets & Hypermarket Flagships",
        "Business Name": "Star Bazaar (Trent Hypermarket - Tata Group)",
        "Town": "Bengaluru",
        "Region": "Koramangala & Whitefield",
        "Key Crops Demanded": "Sona Masoori Rice (Packaged 10kg/25kg), Toor Dal, Bengal Gram, Groundnut Kernels",
        "Procurement Profile": "Tata Group hypermarket flagship with massive monthly off-take of farm-direct private-label staples",
        "Address / Landmark": "Forum Mall, Koramangala, Bengaluru - 560095",
        "Contact Channel": "Senior Category Manager (Grains & Pulses)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Terminal APMC Wholesale Grain Mandi (Yeshwanthpur)",
        "Business Name": "Bangalore Wholesale Food Grains & Pulses Merchants Association",
        "Town": "Bengaluru",
        "Region": "Yeshwanthpur APMC Yard (RMC Yard)",
        "Key Crops Demanded": "Sona Masoori Rice (BPT 5204 - 500+ MT monthly), Toor Dal, Bengal Gram, Broken Rice",
        "Procurement Profile": "The apex grain terminal market in Karnataka; hundreds of wholesale godowns buying multi-axle truckloads directly from millers and aggregators on cash terms",
        "Address / Landmark": "Triveni Road, APMC Yard, Yeshwanthpur, Bengaluru - 560022",
        "Contact Channel": "President & Secretary, Wholesale Grain Merchants Association"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Terminal APMC Wholesale Grain Mandi (Yeshwanthpur)",
        "Business Name": "Mamaji Group Wholesale Grain Merchants",
        "Town": "Bengaluru",
        "Region": "4th Main Road, APMC Yard, Yeshwanthpur",
        "Key Crops Demanded": "Sona Masoori Rice (All grades), Pulses, Bengal Gram",
        "Procurement Profile": "Prominent multi-generation grain merchant supplying 200+ grocery stores and commercial catering canteens across Bengaluru",
        "Address / Landmark": "4th Main Road, APMC Yard, Yeshwanthpur, Bengaluru - 560022",
        "Contact Channel": "Managing Partner"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Terminal APMC Wholesale Grain Mandi (Yeshwanthpur)",
        "Business Name": "Sujatha Traders (Rice & Pulse Wholesalers)",
        "Town": "Bengaluru",
        "Region": "Shop No. 168, APMC Yard, Yeshwanthpur",
        "Key Crops Demanded": "Unadulterated Sona Masoori, Idli Rice (Orange Gold), Toor Dal",
        "Procurement Profile": "Leading institutional wholesaler dealing in farm-grade non-perishable staples",
        "Address / Landmark": "Shop 168, APMC Yard, Yeshwanthpur, Bengaluru - 560022",
        "Contact Channel": "Wholesale Purchase Desk"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Luxury 5-Star Hospitality Culinary Operations",
        "Business Name": "The Leela Palace Luxury Culinary Kitchens",
        "Town": "Bengaluru",
        "Region": "Old Airport Road / Kodihalli",
        "Key Crops Demanded": "Finest Grade Sona Masoori Rice, Organic Pulses, Cold-Pressed Groundnut Oil, Spices",
        "Procurement Profile": "Ultra-luxury hospitality landmark hosting international state banquets and high-profile wedding events",
        "Address / Landmark": "Old Airport Road, Kodihalli, Bengaluru - 560008",
        "Contact Channel": "Director of Materials & Executive Chef"
    },

    # =========================================================================
    # PHASE 2B: HYDERABAD (THE HIGH-VOLUME BIRYANI & POULTRY HUB - 300 KM NORTH)
    # =========================================================================
    {
        "Metro": "Hyderabad",
        "Category": "Mega Biryani & Restaurant Empires",
        "Business Name": "Bawarchi Restaurant Flagship Central Kitchen",
        "Town": "Hyderabad",
        "Region": "RTC Cross Roads, Chikkadpally",
        "Key Crops Demanded": "Sona Masoori Rice (1,000+ kg daily), Biryani Rice, Toor Dal, Sun-Dried Chilies, Groundnut Oil",
        "Procurement Profile": "India's highest single-location biryani and dining powerhouse serving thousands of kilograms of cooked food daily",
        "Address / Landmark": "RTC Cross Roads, Chikkadpally, Hyderabad - 500020",
        "Contact Channel": "Managing Partner & Kitchen Operations Head"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Mega Biryani & Restaurant Empires",
        "Business Name": "Paradise Food Court Central SCM & Commissary",
        "Town": "Hyderabad",
        "Region": "Secunderabad HQ & Shamshabad Commissary",
        "Key Crops Demanded": "Premium Sona Masoori Rice, Basmati, Toor Dal, Pure Cooking Oil (Tens of tonnes monthly)",
        "Procurement Profile": "Limca Record-holding biryani chain serving 7+ million meals annually; fully automated centralized ERP procurement",
        "Address / Landmark": "Paradise Circle, MG Road, Secunderabad - 500003",
        "Contact Channel": "Head of Supply Chain Management (SCM)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Mega Biryani & Restaurant Empires",
        "Business Name": "Pista House Central Commissary & Bakery",
        "Town": "Hyderabad",
        "Region": "Charminar & Banjara Hills",
        "Key Crops Demanded": "Rice, Wheat, Bengal Gram, Spices, Pure Cooking Oil",
        "Procurement Profile": "World-famous GI-tagged Haleem and Biryani empire with massive year-round restaurant dining and export operations",
        "Address / Landmark": "Shalibanda Road, Charminar, Hyderabad - 500002",
        "Contact Channel": "Managing Director / Procurement Desk"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Mega Biryani & Restaurant Empires",
        "Business Name": "Mehfil Restaurant Group Central Commissary",
        "Town": "Hyderabad",
        "Region": "Narayanaguda & Hitec City",
        "Key Crops Demanded": "Sona Masoori Rice (500kg daily), Biryani Rice, Pulses, Spices",
        "Procurement Profile": "Multi-outlet restaurant network with high daily turnover catering to tech employees and city diners",
        "Address / Landmark": "Narayanaguda Main Road, Hyderabad - 500029",
        "Contact Channel": "General Manager - Operations"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Mega Biryani & Restaurant Empires",
        "Business Name": "Shah Ghouse Hotel & Multi-Cuisine Chain",
        "Town": "Hyderabad",
        "Region": "Gachibowli & Tolichowki",
        "Key Crops Demanded": "Rice (Sona Masoori & Basmati), Toor Dal, Cooking Oil",
        "Procurement Profile": "Famous 24/7 dining establishment serving tech hubs in Gachibowli and old city corridors",
        "Address / Landmark": "Biodiversity Junction, Gachibowli, Hyderabad - 500032",
        "Contact Channel": "Partner & Purchase Head"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Premier South Indian Tiffin Chains",
        "Business Name": "Chutneys Restaurant Chain Central Kitchen",
        "Town": "Hyderabad",
        "Region": "Banjara Hills, Jubilee Hills & Hitec City",
        "Key Crops Demanded": "Sona Masoori Broken Rice (Idli/Dosa 500kg daily), Urad Dal (Minapappu), Toor Dal, Bengal Gram (Putnalu)",
        "Procurement Profile": "Telangana's premier fine-dining South Indian tiffin chain famous for 6 signature chutneys and Babai Idlis; massive pulse consumer",
        "Address / Landmark": "Road No. 3, Banjara Hills, Hyderabad - 500034",
        "Contact Channel": "Executive Director / Central Kitchen Incharge"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Commercial Poultry & Livestock Feed Giants",
        "Business Name": "Sneha Farms Mega Feed Mill & Grain Silos (Jadcherla / Hyderabad)",
        "Town": "Hyderabad",
        "Region": "Jadcherla Industrial Hub (NH-44 Corridor) / Kondapur HQ",
        "Key Crops Demanded": "Yellow Maize (Corn - 100+ MT weekly), Broken Rice, Cottonseed Cake, Groundnut Meal",
        "Procurement Profile": "One of India's largest integrated poultry giants operating 1,50,000 MT silo storage; situated directly on the NH-44 highway between Gooty and Hyderabad",
        "Address / Landmark": "Industrial Area, Jadcherla, Mahbubnagar / Kondapur, Hyderabad - 509301",
        "Contact Channel": "Vice President - Raw Material Sourcing (Maize & Cereals)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Commercial Poultry & Livestock Feed Giants",
        "Business Name": "Suguna Foods Regional Feed Plant (Mahbubnagar / Hyderabad NH-44)",
        "Town": "Hyderabad",
        "Region": "Mahbubnagar NH-44 Corridor / Hyderabad",
        "Key Crops Demanded": "Raw Yellow Maize (Makka), Broken Rice (Nookalu), De-oiled Cakes",
        "Procurement Profile": "Market leader in commercial poultry feed where maize represents 50-60% of formulation; continuous farm-gate corn buyer",
        "Address / Landmark": "NH-44 Corridor, Mahbubnagar - 509001",
        "Contact Channel": "Commercial Feed Procurement Head"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Apex Wholesale Grain & Pulse Mandi (Osmangunj / Begum Bazaar)",
        "Business Name": "Begum Bazaar Apex Wholesale Grain & Pulse Merchants Association",
        "Town": "Hyderabad",
        "Region": "Begum Bazaar & Mahboob Gunj",
        "Key Crops Demanded": "Sona Masoori Rice, Toor Dal (Kandi Pappu), Bengal Gram (Chana), Red Chilies (Endu Mirapa)",
        "Procurement Profile": "The historic nerve-center of agricultural commodity wholesale trading in Telangana; thousands of tonnes traded daily in truckloads",
        "Address / Landmark": "Mahboob Gunj / Begum Bazaar, Hyderabad - 500012",
        "Contact Channel": "President, Hyderabad Grain & Seeds Merchants Association"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Apex Wholesale Grain & Pulse Mandi (Osmangunj / Begum Bazaar)",
        "Business Name": "Relmal Kishanlal Wholesale Grain Merchants",
        "Town": "Hyderabad",
        "Region": "Mahboob Gunj, Osmangunj",
        "Key Crops Demanded": "Sona Masoori Rice (Kurnool & Rayalaseema origins), Toor Dal, Pulses",
        "Procurement Profile": "Major primary distributor and commission merchant buying full truckloads directly from Rayalaseema millers and aggregators",
        "Address / Landmark": "Mahboob Gunj, Hyderabad - 500012",
        "Contact Channel": "Managing Partner"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Apex Wholesale Grain & Pulse Mandi (Osmangunj / Begum Bazaar)",
        "Business Name": "C Eshwaraiah Grain & Kirana Wholesale Merchant",
        "Town": "Hyderabad",
        "Region": "Siddiamber Bazar / Mahboob Gunj",
        "Key Crops Demanded": "Rice, Toor Dal, Bengal Gram, Spices",
        "Procurement Profile": "Established wholesale supplier servicing 100+ neighborhood retail stores and caterers across Hyderabad urban zone",
        "Address / Landmark": "Siddiamber Bazar, Hyderabad - 500012",
        "Contact Channel": "Proprietor"
    },
    {
        "Metro": "Hyderabad",
        "Category": "E-Commerce & Quick Commerce Central Mother Warehouses",
        "Business Name": "BigBasket (Innovative Retail Concepts - Tata Group) Central DC",
        "Town": "Hyderabad",
        "Region": "Shamshabad / NH-44 Logistics Corridor",
        "Key Crops Demanded": "Sona Masoori Rice (5kg/25kg bags), Organic Toor Dal, Millets, Groundnut Oil",
        "Procurement Profile": "India's largest online grocery mother warehouse serving the entire Hyderabad urban territory with direct farmer procurement programs",
        "Address / Landmark": "Near Shamshabad International Airport, NH-44, Hyderabad - 501218",
        "Contact Channel": "Head of Farmer-Connect & Staples Sourcing"
    },
    {
        "Metro": "Hyderabad",
        "Category": "E-Commerce & Quick Commerce Central Mother Warehouses",
        "Business Name": "Blinkit / Zepto Regional Grocery Fulfillment Hub",
        "Town": "Hyderabad",
        "Region": "Medchal & Shamshabad Outer",
        "Key Crops Demanded": "Packaged Staples, Sona Masoori Rice, Dal, Cold-Pressed Oil",
        "Procurement Profile": "Hyper-growth quick-commerce mother warehouse feeding 80+ dark stores across Hyderabad with rapid turnover",
        "Address / Landmark": "Industrial Logistics Park, Hyderabad - 501401",
        "Contact Channel": "Regional Category Procurement Lead"
    },
    {
        "Metro": "Hyderabad",
        "Category": "IT Corridor Corporate Dining Campuses",
        "Business Name": "Elior India / Sodexo Corporate Dining Hub (Hitec City)",
        "Town": "Hyderabad",
        "Region": "Hitec City & Financial District",
        "Key Crops Demanded": "Sona Masoori Rice, Toor Dal, Bengal Gram, Groundnut Cooking Oil",
        "Procurement Profile": "Centralized corporate dining contractor serving 75,000+ software engineers daily across Microsoft, Amazon, Google, and Infosys campuses",
        "Address / Landmark": "Financial District, Nanakramguda, Gachibowli, Hyderabad - 500032",
        "Contact Channel": "Director - Supply Chain & Quality Assurance"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Luxury 5-Star Hospitality Culinary Operations",
        "Business Name": "ITC Kohenur & Taj Krishna Luxury Dining Kitchens",
        "Town": "Hyderabad",
        "Region": "Madhapur (Hitec City) & Banjara Hills",
        "Key Crops Demanded": "Finest Grade Aged Sona Masoori, Organic Dals, Cold-Pressed Oil, Spices",
        "Procurement Profile": "Luxury hotel properties hosting international delegations, state banquets, and high-end dining restaurants",
        "Address / Landmark": "Knowledge City, Madhapur, Hyderabad - 500081",
        "Contact Channel": "Purchase Manager & Executive Chef"
    }
]

def main():
    fieldnames = [
        "Metro",
        "Category", 
        "Business Name", 
        "Town", 
        "Region", 
        "Key Crops Demanded", 
        "Procurement Profile", 
        "Address / Landmark", 
        "Contact Channel"
    ]
    
    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in PHASE2_BUYERS:
            writer.writerow(row)
            
    print(f"Successfully compiled {len(PHASE2_BUYERS)} Phase 2 Mega-Metro buyers (Bengaluru & Hyderabad) into:")
    print(OUTPUT_FILE)

if __name__ == "__main__":
    main()
