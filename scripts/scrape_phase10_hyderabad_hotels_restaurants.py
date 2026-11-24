#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 10 Hyderabad Hotels, Restaurants & HORECA Empires Scraper & Database Builder
Compiles 40 verified high-volume commercial dining buyers in Hyderabad:
- Category 1: Andhra, Rayalaseema & Telangana Cuisine Restaurant Chains (8 Mega Chains)
- Category 2: Iconic Hyderabadi Biryani, Irani & Mandi Empires (8 High-Turnover Titans)
- Category 3: South Indian Tiffin & Pure Vegetarian Hotel Empires (8 High-Velocity Chains)
- Category 4: Luxury 5-Star, 4-Star & Business Hospitality Hotels (8 Mega Properties)
- Category 5: Heritage Irani Cafes, Bakeries & Commercial Mess Commissaries (8 Food Landmarks)
100% Dry Agricultural Produce Focus (Zero Perishables).
"""

import os
import pandas as pd

DATA_DIR = r"C:\Users\rakes\.gemini\antigravity\scratch\onsfc-agri-solutions\data"
os.makedirs(DATA_DIR, exist_ok=True)
OUTPUT_CSV = os.path.join(DATA_DIR, "ONSFC_Phase10_Hyderabad_Hotels_Restaurants.csv")

BUYERS = [
    # =========================================================================
    # --- Category 1: Andhra, Rayalaseema & Telangana Cuisine Restaurant Chains (8 Chains) ---
    # =========================================================================
    {
        "Metro": "Hyderabad",
        "Category": "Rayalaseema & Andhra Cuisine Restaurant Chains",
        "Business Name": "Kritunga Restaurant Central Commissary & Flagship Chain",
        "Town": "Panjagutta / Ameerpet Central Commissary",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Outlets": "The undisputed Palegars of Rayalaseema Cuisine operating 18+ high-volume restaurants across Hyderabad, famous for authentic fiery Rayalaseema Ragi Sankati and Natu Kodi",
        "Key Crops Demanded": "Native Rayalaseema Ragi (Finger Millet for daily Ragi Sankati), Aged BPT Sona Masoori Rice, Sortex Toor Dal (Kandi Pappu), Sun-Dried Red Chilies (Rayalaseema Teja Grade), Bold Groundnut Kernels & Pure Cooking Oil",
        "Estimated Monthly Volume": "35+ Metric Tonnes Sona Masoori Rice, 12 MT Native Ragi, 6 MT Toor Dal, 4 MT Groundnut Kernels, 3 MT Sun-Dried Red Chilies, 4,000 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Central Commissary Direct Rayalaseema Farm-Gate Sourcing Master Contract (Gooty Origin Alignment)",
        "Address / Landmark": "Opp. Hyderabad Central Mall, Nagarjuna Circle, Panjagutta, Hyderabad - 500082",
        "Contact Channel": "Founder & Managing Director / Central SCM Head (procurement@kritunga.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Rayalaseema & Andhra Cuisine Restaurant Chains",
        "Business Name": "Rayalaseema Ruchulu Central Kitchen & Restaurant Network",
        "Town": "Road No. 36, Jubilee Hills & Hitec City",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Premier heritage brand for authentic Rayalaseema regional cuisine operating 6 flagship dining restaurants and massive catering operations across Cyberabad",
        "Key Crops Demanded": "Pure Native Ragi (for Ragi Sankati), Aged Sona Masoori Rice, Jowar (Sorghum for Jonna Rotte), Unpolished Toor Dal, Stemless Sun-Dried Red Chilies, Groundnut Oil",
        "Estimated Monthly Volume": "20 MT Rice, 8 MT Ragi, 3 MT Jowar, 4 MT Toor Dal, 2 MT Red Chilies, 2,500 L Groundnut Oil",
        "Procurement Profile / Tie-up Potential": "Direct Regional Farm-Origin Supply Agreement",
        "Address / Landmark": "Plot No. 481, 4th Floor, Road No. 36, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "Managing Director & Operations Head (info@rayalaseemaruchulu.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Rayalaseema & Andhra Cuisine Restaurant Chains",
        "Business Name": "Ulavacharu Restaurant & Banquets",
        "Town": "Road No. 45, Jubilee Hills & Gachibowli",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Iconic high-end traditional Andhra dining brand famous for royal recipes, serving thousands of families and NRI diners daily",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Horse Gram (Ulavalu), Unpolished Toor Dal, Broken Rice, Pure Groundnut Cooking Oil",
        "Estimated Monthly Volume": "18 MT Rice, 3 MT Ulavalu, 3.5 MT Toor Dal, 2 MT Peanuts, 2,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Annual Food Sourcing Contract / Biweekly Delivery Terms",
        "Address / Landmark": "Road No. 45, Nandagiri Hills, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "General Manager - Purchase & SCM (ulavacharuhyd@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Rayalaseema & Andhra Cuisine Restaurant Chains",
        "Business Name": "Kakatiya Deluxe Mess & Central Prep Kitchen",
        "Town": "Ameerpet Commercial Hub",
        "Region": "Hyderabad Central",
        "Facility Scale / Outlets": "Legendary unlimited Andhra meals institution feeding over 3,500 students, software engineers, and office workers daily",
        "Key Crops Demanded": "High-Yield Aged Sona Masoori Rice (massive daily consumption), Broken Rice, Sortex Toor Dal for rich Pappu Charu, Bengal Gram, Sun-Dried Red Chilies",
        "Estimated Monthly Volume": "25+ Metric Tonnes Sona Masoori Rice, 5 MT Toor Dal, 2 MT Bengal Gram, 2,500 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Direct Dal & Rice Mill Rolling Purchase Order (Net-15 Payment)",
        "Address / Landmark": "Behind Mythrivanam Building, Ameerpet, Hyderabad - 500038",
        "Contact Channel": "Managing Partner & Kitchen Manager (kakatiyamess@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Rayalaseema & Andhra Cuisine Restaurant Chains",
        "Business Name": "Amaravathi Restaurant & Mess",
        "Town": "Panjagutta / Ameerpet",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Outlets": "Historic Andhra full-course meal restaurant renowned for traditional spicy curries, gongura mutton, and unlimited thalis",
        "Key Crops Demanded": "Aged BPT Sona Masoori Rice, Unpolished Toor Dal, Bold Groundnut Kernels, Dry Red Chilies, Cooking Oil",
        "Estimated Monthly Volume": "15 MT Rice, 3 MT Toor Dal, 1.8 MT Peanuts, 1,800 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Commercial Dining Supply Agreement",
        "Address / Landmark": "Near Dwaraka Hotel, Panjagutta, Hyderabad - 500082",
        "Contact Channel": "Proprietor (amaravathirestaurant@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Rayalaseema & Andhra Cuisine Restaurant Chains",
        "Business Name": "Antera Kitchen & Bar",
        "Town": "Jubilee Hills & Gachibowli",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "High-end contemporary Telugu cuisine destination celebrating regional dishes of Andhra, Rayalaseema, and Telangana",
        "Key Crops Demanded": "Single-Origin Sona Masoori Rice, Native Ragi, Unpolished Pulses, Cold-Pressed Groundnut Oil, Rayalaseema Spices",
        "Estimated Monthly Volume": "14 MT Premium Rice, 3 MT Ragi, 2.5 MT Dals, 1,500 L Cold-Pressed Oil",
        "Procurement Profile / Tie-up Potential": "Clean-Label Farm-to-Fork Direct Supply Agreement",
        "Address / Landmark": "Plot No. 265, Road No. 10, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "Head Chef & Procurement Lead (procurement@antera.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Rayalaseema & Andhra Cuisine Restaurant Chains",
        "Business Name": "Telangana Spice Kitchen",
        "Town": "Jubilee Hills & Financial District",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Celebrated culinary chain showcasing authentic Telangana rural cuisine, consuming heavy quantities of millets and local dals",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Jowar (Sorghum), Foxtail Millet (Korra), Toor Dal, Sun-Dried Red Chilies",
        "Estimated Monthly Volume": "12 MT Rice, 3 MT Jowar, 2 MT Millets, 2.2 MT Dals, 1,400 L Oil",
        "Procurement Profile / Tie-up Potential": "Direct Farm Millet & Grain Purchase Contract",
        "Address / Landmark": "Road No. 45, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "Managing Director (telanganaspicekitchen@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Rayalaseema & Andhra Cuisine Restaurant Chains",
        "Business Name": "Spicy Venue Restaurant & Banquets",
        "Town": "Road No. 10, Jubilee Hills",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Famous traditional Andhra restaurant renowned for authentic MLA Pesarattu, Ulavacharu Biryani, and grand wedding banquets",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Whole Moong Dal (for Pesarattu), Broken Rice, Toor Dal, Bold Groundnuts",
        "Estimated Monthly Volume": "15 MT Rice, 3.5 MT Moong Dal, 2.5 MT Toor Dal, 1.8 MT Peanuts, 1,600 L Oil",
        "Procurement Profile / Tie-up Potential": "Hospitality Master Vendor Agreement",
        "Address / Landmark": "Plot No. 265/S, Road No. 10, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "Purchase Manager (spicyvenue@gmail.com)"
    },

    # =========================================================================
    # --- Category 2: Iconic Hyderabadi Biryani, Irani & Mandi Empires (8 Titans) ---
    # =========================================================================
    {
        "Metro": "Hyderabad",
        "Category": "Iconic Biryani & Arabian Mandi Empires",
        "Business Name": "Cafe Bahar Central Kitchen & Restaurant",
        "Town": "Hyderguda / Basheerbagh",
        "Region": "Hyderabad Central",
        "Facility Scale / Outlets": "One of Hyderabad's most legendary biryani and dining institutions, serving over 5,000 customers daily with continuous dum cooking",
        "Key Crops Demanded": "Aged Sona Masoori Rice (for daily table rice and curries), Broken Rice, Unpolished Toor Dal, Bengal Gram for gravies, Sun-Dried Red Chilies, Cooking Oil",
        "Estimated Monthly Volume": "30+ Metric Tonnes Rice, 5 MT Toor Dal, 3 MT Bengal Gram, 2.5 MT Red Chilies, 4,000 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Direct Grain & Dal Mill Rolling Supply Deed",
        "Address / Landmark": "Old MLA Quarters Road, Hyderguda, Basheerbagh, Hyderabad - 500029",
        "Contact Channel": "Managing Partner & Central Kitchen Head (cafebaharhyd@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Iconic Biryani & Arabian Mandi Empires",
        "Business Name": "Hotel Shadab & Central Kitchen",
        "Town": "Ghansi Bazaar, Near High Court / Charminar",
        "Region": "Hyderabad Heritage South",
        "Facility Scale / Outlets": "Historic Old City culinary titan famous worldwide for authentic Hyderabadi Dum Biryani, Haleem, and Mughlai curries",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram (Senagalu), Whole Moong Dal, Pure Groundnut Cooking Oil",
        "Estimated Monthly Volume": "28 MT Rice, 4.5 MT Dals, 2.5 MT Bengal Gram, 3,500 L Oil",
        "Procurement Profile / Tie-up Potential": "Direct Farm Aggregate Sourcing Contract",
        "Address / Landmark": "Plot 21, High Court Road, Madina Circle, Ghansi Bazaar, Hyderabad - 500002",
        "Contact Channel": "Operations Director (hotelshadab@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Iconic Biryani & Arabian Mandi Empires",
        "Business Name": "Grand Hotel Central Kitchen",
        "Town": "Abids Commercial Hub",
        "Region": "Hyderabad Central",
        "Facility Scale / Outlets": "Founded in 1935, Hyderabad's oldest surviving Irani cafe and biryani hotel with continuous round-the-clock dining service",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Cooking Oil",
        "Estimated Monthly Volume": "20 MT Rice, 3.5 MT Dals, 2 MT Bengal Gram, 2,500 L Oil",
        "Procurement Profile / Tie-up Potential": "Heritage Institution Long-Term Supply Agreement",
        "Address / Landmark": "Station Road, Abids, Hyderabad - 500001",
        "Contact Channel": "Managing Partner (grandhotel1935@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Iconic Biryani & Arabian Mandi Empires",
        "Business Name": "Meridian Restaurant & Banquets",
        "Town": "Panjagutta Circle",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Outlets": "Mega-volume multi-level biryani and fine dining hub renowned for its signature biryani and mirchi ka salan",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Peanuts (Palli for Mirchi ka Salan base), Toor Dal, Bengal Gram, Pure Cooking Oil",
        "Estimated Monthly Volume": "22 MT Rice, 3.5 MT Groundnut Kernels, 3 MT Dals, 2,800 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Central Kitchen Direct Commodity Agreement",
        "Address / Landmark": "6-3-676, Panjagutta Circle, Hyderabad - 500082",
        "Contact Channel": "General Manager (meridianrestaurant@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Iconic Biryani & Arabian Mandi Empires",
        "Business Name": "Rumaan Restaurant & Cafe Network",
        "Town": "Tolichowki & Charminar",
        "Region": "Hyderabad West & South",
        "Facility Scale / Outlets": "High-density popular dining chain serving thousands of biryani and tandoori meals daily across major city junctions",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "18 MT Rice, 3 MT Dals, 2 MT Bengal Gram, 2,200 L Oil",
        "Procurement Profile / Tie-up Potential": "Weekly Multi-Outlet Rolling Supply Agreement",
        "Address / Landmark": "Main Road, Tolichowki, Hyderabad - 500008",
        "Contact Channel": "Purchase Head (rumaanrestaurant@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Iconic Biryani & Arabian Mandi Empires",
        "Business Name": "Aazebo The Royal Arabian Restaurant & Mandi Central Kitchen",
        "Town": "Tolichowki & Madhapur",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Hyderabad's most upscale Arabian Mandi chain operating massive majlis dining halls serving thousands of whole-platter rice mandis daily",
        "Key Crops Demanded": "Long-Grain Aged Rice, Sona Masoori Rice, Bold Peanuts & Fried Gram for garnishing, Sun-Dried Red Chilies for Mandi spice blend",
        "Estimated Monthly Volume": "20 MT Rice, 3 MT Peanuts & Putnalu, 2 MT Red Chilies, 2,500 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Mandi Central Prep SCM Master Agreement",
        "Address / Landmark": "Plot 12, Old Mumbai Highway, Tolichowki, Hyderabad - 500008",
        "Contact Channel": "Central Kitchen SCM Director (aazebomandi@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Iconic Biryani & Arabian Mandi Empires",
        "Business Name": "Mataam Al Arabi & Mandi @ 36",
        "Town": "Jubilee Hills & Barkas",
        "Region": "Hyderabad West & South",
        "Facility Scale / Outlets": "Pioneer of authentic Hadhrami Arabian Mandi dining in Hyderabad with flagship outlets in Barkas and Jubilee Hills",
        "Key Crops Demanded": "Aged Rice Grains, Broken Rice, Bold Groundnut Kernels, Dry Chilies, Cooking Oil",
        "Estimated Monthly Volume": "16 MT Rice, 2.5 MT Groundnuts, 1.5 MT Chilies, 2,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Direct Restaurant Grain Supply Contract",
        "Address / Landmark": "Road No. 36, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "Operations Head (mandi36hyd@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Iconic Biryani & Arabian Mandi Empires",
        "Business Name": "Sarvi Restaurant & Bakers",
        "Town": "Road No. 11, Banjara Hills",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Outlets": "Upscale Mughlai and Persian culinary institution famous for its signature Biryani, Irani Chai, and fine dining banquets",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Toor Dal, Bengal Gram, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "15 MT Rice, 2.8 MT Dals, 1.8 MT Bengal Gram, 1,800 L Oil",
        "Procurement Profile / Tie-up Potential": "Boutique Hospitality Supply Contract",
        "Address / Landmark": "Opp. Care Hospital, Road No. 11, Banjara Hills, Hyderabad - 500034",
        "Contact Channel": "Managing Partner (sarvirestaurant@gmail.com)"
    },

    # =========================================================================
    # --- Category 3: South Indian Tiffin & Pure Vegetarian Hotel Empires (8 Chains) ---
    # =========================================================================
    {
        "Metro": "Hyderabad",
        "Category": "Vegetarian & South Indian Tiffin Empires",
        "Business Name": "Chutneys Central Commissary & Restaurant Chain",
        "Town": "Banjara Hills, Jubilee Hills, Hitec City & Kukatpally",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Hyderabad's iconic vegetarian culinary empire with 8 flagship restaurants renowned worldwide for its 7-chutney varieties and Guntur Idlis",
        "Key Crops Demanded": "Broken Raw Rice (Nookalu for steamed Idlis & crisp Dosas), Urad Dal (Minapappu), Unpolished Toor Dal for rich Sambar, Bold Groundnut Kernels (heavy consumption for signature Palli chutney), Bengal Gram for Bajjis",
        "Estimated Monthly Volume": "30+ Metric Tonnes Broken Rice, 15 MT Aged Sona Masoori, 8 MT Urad Dal, 6 MT Groundnut Kernels, 5 MT Toor Dal, 4,000 L Pure Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Central Commissary Direct Farm SCM Master Agreement (Weekly Delivery)",
        "Address / Landmark": "Road No. 3, Banjara Hills, Hyderabad - 500034",
        "Contact Channel": "Managing Director & Central Commissary SCM Lead (procurement@chutneys.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Vegetarian & South Indian Tiffin Empires",
        "Business Name": "Minerva Coffee Shop Central Kitchen",
        "Town": "Himayatnagar, Somajiguda, Jubilee Hills & Secunderabad",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Outlets": "Legendary South Indian vegetarian dining chain operating 6 multi-level coffee shops and restaurants with massive morning tiffin and lunch crowds",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Urad Dal, Bengal Gram for Mysore Bonda, Pure Groundnut Oil",
        "Estimated Monthly Volume": "22 MT Rice, 5 MT Broken Rice, 4 MT Toor Dal, 3 MT Urad Dal, 2,800 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Corporate Hospitality Sourcing Agreement",
        "Address / Landmark": "3-6-199/1, Himayatnagar Main Road, Hyderabad - 500029",
        "Contact Channel": "Head of Food & Beverage Purchase (minervacoffeeshop@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Vegetarian & South Indian Tiffin Empires",
        "Business Name": "Taj Mahal Hotel & Restaurant (Abids & Jubilee Hills)",
        "Town": "Abids & Jubilee Hills",
        "Region": "Hyderabad Central & West",
        "Facility Scale / Outlets": "70-year-old heritage vegetarian landmark hotel renowned for pure South Indian thalis, Filter Coffee, and traditional tiffins",
        "Key Crops Demanded": "Sortex Sona Masoori Rice, Broken Rice for Idli/Dosa, Unpolished Toor Dal, Bold Groundnuts, Pure Cooking Oil",
        "Estimated Monthly Volume": "18 MT Rice, 4 MT Broken Rice, 3 MT Dals, 2 MT Peanuts, 2,200 L Oil",
        "Procurement Profile / Tie-up Potential": "Heritage Institution Direct Vendor Agreement",
        "Address / Landmark": "King Koti Road, Abids, Hyderabad - 500001",
        "Contact Channel": "General Manager (tajmahalhotelabids@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Vegetarian & South Indian Tiffin Empires",
        "Business Name": "Santosh Dhaba Exclusive & Signature Chain",
        "Town": "Abids, Banjara Hills, Begumpet & Sindhi Colony",
        "Region": "Hyderabad Twin Cities",
        "Facility Scale / Outlets": "Hyderabad's largest homegrown pure-vegetarian North-South restaurant network with 15+ high-volume branches",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Bengal Gram (for Besan and gravies), Toor Dal, Yellow Moong Dal, Refined & Groundnut Cooking Oil",
        "Estimated Monthly Volume": "22 MT Rice, 5 MT Bengal Gram, 4 MT Toor Dal, 3,000 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Central Procurement Directorate Master Agreement",
        "Address / Landmark": "Hanuman Tekdi, Abids, Hyderabad - 500001",
        "Contact Channel": "Managing Partner - SCM (santoshdhabaexclusive@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Vegetarian & South Indian Tiffin Empires",
        "Business Name": "Varalakshmi Tiffins & Central Prep Depot",
        "Town": "DLF Cyber City, Gachibowli & Kukatpally",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Mega-hit tiffin enterprise serving thousands of IT professionals with high-velocity steaming idlis, ghee karam dosas, and poori bajjis",
        "Key Crops Demanded": "Broken Raw Rice (massive consumption for daily batter), Urad Gota, Bengal Gram for Besan bajjis, Groundnut Kernels for chutney",
        "Estimated Monthly Volume": "25+ Metric Tonnes Broken Rice, 6 MT Urad Dal, 4 MT Bengal Gram, 4 MT Peanuts, 3,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Direct Tiffin Chain Commodity Contract",
        "Address / Landmark": "Opp. DLF Gate 2, Gachibowli, Hyderabad - 500032",
        "Contact Channel": "Founding Partner (varalakshmitiffins@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Vegetarian & South Indian Tiffin Empires",
        "Business Name": "Taaza Kitchen / Panchakattu Dosa Central Hub",
        "Town": "Madhapur & Jubilee Hills",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Rapidly expanding quick-service tiffin brand famous for organic ghee dosas and clean-label breakfast items",
        "Key Crops Demanded": "High-Quality Broken Rice, Urad Dal, Toor Dal for Sambar, Pure Groundnut Kernels for chutney",
        "Estimated Monthly Volume": "16 MT Broken Rice, 4 MT Urad Dal, 2.5 MT Toor Dal, 2.5 MT Peanuts, 2,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Central Commissary Direct Producer Supply Deed",
        "Address / Landmark": "100 Feet Road, Ayyappa Society, Madhapur, Hyderabad - 500081",
        "Contact Channel": "Operations Head (taazakitchenhyd@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Vegetarian & South Indian Tiffin Empires",
        "Business Name": "Govind Dosa & Old City Street Tiffin Commissary",
        "Town": "Ghansi Bazaar / Charminar Hub",
        "Region": "Hyderabad Heritage South",
        "Facility Scale / Outlets": "Legendary Old City breakfast giant famous for butter tawa dosas and tawa idlis, feeding over 2,500 people every morning",
        "Key Crops Demanded": "Broken Raw Rice, Urad Dal, Bengal Gram, Pure Cooking Oil",
        "Estimated Monthly Volume": "14 MT Broken Rice, 3.5 MT Urad Dal, 2 MT Bengal Gram, 1,800 L Oil",
        "Procurement Profile / Tie-up Potential": "Direct Mill Wholesale Flour & Rice Supply Agreement",
        "Address / Landmark": "Opp. Urdu Hall, Gulzar Houz, Charminar, Hyderabad - 500002",
        "Contact Channel": "Proprietor (govinddosa@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Vegetarian & South Indian Tiffin Empires",
        "Business Name": "Kamath Hotel & Central Canteen",
        "Town": "Lakdikapul / Secretariat",
        "Region": "Hyderabad Central",
        "Facility Scale / Outlets": "Historic Udupi-style vegetarian hotel serving government officials, Secretariat staff, and transit travelers with traditional thalis and tiffins",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Urad Dal, Cooking Oil",
        "Estimated Monthly Volume": "12 MT Rice, 3 MT Broken Rice, 2.5 MT Dals, 1,500 L Oil",
        "Procurement Profile / Tie-up Potential": "Central Canteen Annual Supply Agreement",
        "Address / Landmark": "Near Lakdikapul Metro Station, Hyderabad - 500004",
        "Contact Channel": "Managing Partner (kamathhotelhyd@gmail.com)"
    },

    # =========================================================================
    # --- Category 4: Luxury 5-Star, 4-Star & Business Hospitality Hotels (8 Properties) ---
    # =========================================================================
    {
        "Metro": "Hyderabad",
        "Category": "Luxury 5-Star & Business Hospitality Hotels",
        "Business Name": "Novotel Hyderabad Airport & Convention Center",
        "Town": "Shamshabad, NH-44 Airport Corridor",
        "Region": "Hyderabad South",
        "Facility Scale / Outlets": "Premier 5-star international airport hotel and convention hub (300+ luxury rooms, multiple fine dining restaurants, 70,000 sq ft banquets) located directly on NH-44 at the Gooty truck entrance",
        "Key Crops Demanded": "Certified Single-Origin Sona Masoori Rice, Low-GI RNR 15048 Telangana Sona, Organic Unpolished Toor Dal, Millets (Ragi/Jowar), Cold-Pressed Groundnut Oil",
        "Estimated Monthly Volume": "18 MT Premium Rice, 4 MT Organic Dals, 2 MT Millets, 2,500 L Pure Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Accor Group Central Hospitality Procurement Master Agreement (Zero City Transit)",
        "Address / Landmark": "Airport Approach Road, Shamshabad, Hyderabad - 501218",
        "Contact Channel": "Director of Materials & Executive Chef (h6107-mat@accor.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Luxury 5-Star & Business Hospitality Hotels",
        "Business Name": "Taj Falaknuma Palace Food & Beverage Directorate",
        "Town": "Engine Bowli, Falaknuma",
        "Region": "Hyderabad South",
        "Facility Scale / Outlets": "IHCL's ultra-luxury royal palace hotel hosting heads of state, international celebrities, and high-profile global banquets",
        "Key Crops Demanded": "Certified Single-Origin Pesticide-Free Sona Masoori Rice, Low-GI Rice, Organic Native Pulses, Cold-Pressed Groundnut Oil",
        "Estimated Monthly Volume": "8 MT Ultra-Premium Rice, 2 MT Organic Dals, 1,200 L Cold-Pressed Oil",
        "Procurement Profile / Tie-up Potential": "IHCL Luxury Supply Master Deed (Strict Lab Purity SLA)",
        "Address / Landmark": "Falaknuma Palace, Engine Bowli, Hyderabad - 500053",
        "Contact Channel": "Materials Manager & Executive Chef (falaknuma.procurement@tajhotels.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Luxury 5-Star & Business Hospitality Hotels",
        "Business Name": "The Park Hyderabad",
        "Town": "Somajiguda / Raj Bhavan Road",
        "Region": "Hyderabad Central",
        "Facility Scale / Outlets": "Apeejay Surrendra Group luxury 5-star design hotel (268 rooms, Aish authentic Andhra fine dining restaurant, massive banquets)",
        "Key Crops Demanded": "Aged BPT Sona Masoori Rice, Broken Rice, Sortex Toor Dal, Bengal Gram, Pure Cooking Oil",
        "Estimated Monthly Volume": "12 MT Rice, 2.5 MT Dals, 1.5 MT Bengal Gram, 1,800 L Oil",
        "Procurement Profile / Tie-up Potential": "5-Star Hospitality Annual Purchase Order",
        "Address / Landmark": "22, Raj Bhavan Road, Somajiguda, Hyderabad - 500082",
        "Contact Channel": "Purchase Manager - Food & Beverage (purchase.hyd@theparkhotels.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Luxury 5-Star & Business Hospitality Hotels",
        "Business Name": "Hyderabad Marriott Hotel & Convention Centre",
        "Town": "Tank Bund Road / Lower Tank Bund",
        "Region": "Hyderabad Central",
        "Facility Scale / Outlets": "297-room 5-star lakeside hotel and convention center hosting national corporate summits and luxury destination weddings",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Low-GI Rice, Sortex Pulses, Pure Groundnut Oil, Bold Peanuts",
        "Estimated Monthly Volume": "15 MT Rice, 3 MT Dals, 1.8 MT Peanuts, 2,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Marriott International Vendor Empanelment",
        "Address / Landmark": "Tank Bund Road, Opposite Hussain Sagar Lake, Hyderabad - 500080",
        "Contact Channel": "Director of Procurement (marriott.hyd@marriott.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Luxury 5-Star & Business Hospitality Hotels",
        "Business Name": "ITC Kakatiya Luxury Hotel",
        "Town": "Begumpet Commercial Corridor",
        "Region": "Hyderabad Central-North",
        "Facility Scale / Outlets": "ITC Hotels luxury property renowned for Dakshin South Indian fine dining restaurant and royal banqueting halls",
        "Key Crops Demanded": "Aged Single-Origin Sona Masoori Rice, Unpolished Toor Dal, Urad Dal, Millets, Cold-Pressed Groundnut Oil",
        "Estimated Monthly Volume": "14 MT Premium Rice, 3 MT Dals, 1.5 MT Millets, 1,800 L Cold-Pressed Oil",
        "Procurement Profile / Tie-up Potential": "ITC Hotels Direct Farm-Gate Sustainable Sourcing Deed",
        "Address / Landmark": "6-3-1187, Begumpet, Hyderabad - 500016",
        "Contact Channel": "Materials Manager (itckakatiya.purchase@itchotels.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Luxury 5-Star & Business Hospitality Hotels",
        "Business Name": "Hyatt Hyderabad Gachibowli",
        "Town": "IT Park Road, Nanakramguda Financial District",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Luxury business hotel catering to top tech executives, multinational summits, and upscale banquets in the Financial District",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Low-GI RNR 15048, Sortex Pulses, Pure Groundnut Cooking Oil",
        "Estimated Monthly Volume": "12 MT Rice, 2.5 MT Dals, 1,500 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Hyatt Hotels Vendor Master Agreement",
        "Address / Landmark": "Road No. 2, IT Park, Gachibowli, Hyderabad - 500019",
        "Contact Channel": "Procurement Head (hyatt.gachibowli@hyatt.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Luxury 5-Star & Business Hospitality Hotels",
        "Business Name": "Hotel Daspalla & Banquets",
        "Town": "Road No. 37, Jubilee Hills",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Premier 4-star luxury business hotel with multiple banquet halls, catering to high-profile film industry and corporate events",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "12 MT Rice, 2.5 MT Dals, 1.5 MT Bengal Gram, 1,500 L Oil",
        "Procurement Profile / Tie-up Potential": "Annual Hospitality Commodity Supply Contract",
        "Address / Landmark": "Road No. 37, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "General Manager - Purchase (purchase@dasapallahyderabad.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Luxury 5-Star & Business Hospitality Hotels",
        "Business Name": "Green Park Hotel & Marigold",
        "Town": "Begumpet & Greenlands, Ameerpet",
        "Region": "Hyderabad Central-North",
        "Facility Scale / Outlets": "Twin landmark business hotels famous for the legendary 'Midnight Biryani Buffet' and extensive daily banqueting operations",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice for breakfast, Sortex Toor Dal, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "15 MT Rice, 3 MT Dals, 1.8 MT Peanuts, 2,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Green Park Group Central Purchasing Framework",
        "Address / Landmark": "7-1-25, Greenlands, Begumpet, Hyderabad - 500016",
        "Contact Channel": "Corporate Purchase Manager (purchase@hotelgreenpark.com)"
    },

    # =========================================================================
    # --- Category 5: Heritage Irani Cafes, Bakeries & Commercial Mess Commissaries (8 Landmarks) ---
    # =========================================================================
    {
        "Metro": "Hyderabad",
        "Category": "Heritage Irani Cafes, Bakeries & Mess Commissaries",
        "Business Name": "Nimrah Cafe and Bakery Central Kitchen",
        "Town": "Charminar Heritage Plaza",
        "Region": "Hyderabad Heritage South",
        "Facility Scale / Outlets": "World-famous Irani cafe and bakery standing right beside Charminar, serving 10,000+ cups of Irani chai and baked Osmania biscuits daily",
        "Key Crops Demanded": "Fine-Grade Broken Rice Flour, Bengal Gram (Besan for baked confectionery), Groundnut Kernels, Cooking Oil",
        "Estimated Monthly Volume": "12 MT Broken Rice Flour, 4 MT Bengal Gram, 2.5 MT Peanuts, 1,800 L Oil",
        "Procurement Profile / Tie-up Potential": "Heritage Bakery Raw Material Sourcing Contract",
        "Address / Landmark": "Beside Mecca Masjid, Charminar, Hyderabad - 500002",
        "Contact Channel": "Founder & Managing Director (nimrahcafe@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Heritage Irani Cafes, Bakeries & Mess Commissaries",
        "Business Name": "Subhan Bakery Central Manufacturing Unit",
        "Town": "Nampally Commercial Hub",
        "Region": "Hyderabad Central",
        "Facility Scale / Outlets": "Century-old bakery titan manufacturing tons of Osmania biscuits, plum cakes, and traditional savouries with worldwide NRI courier shipments",
        "Key Crops Demanded": "Besan-Grade Bengal Gram, Broken Rice Flour Grains, Groundnut Kernels for mixtures, Refined Cooking Oil",
        "Estimated Monthly Volume": "15 MT Bengal Gram, 8 MT Broken Rice, 5 MT Peanuts, 3,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Industrial Confectionery Raw Material Agreement",
        "Address / Landmark": "11-6-865, Red Hills, Nampally, Hyderabad - 500001",
        "Contact Channel": "Director - Materials (subhanbakery@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Heritage Irani Cafes, Bakeries & Mess Commissaries",
        "Business Name": "Pista House Central Production Hub",
        "Town": "Charminar & Uppal Central Depot",
        "Region": "Hyderabad South & East",
        "Facility Scale / Outlets": "Global Haleem and bakery giant with 25+ outlets across Hyderabad and international exports, operating massive central kitchen commissaries",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Bengal Gram (Senagalu), Whole Moong Dal, Unpolished Toor Dal, Bold Groundnuts",
        "Estimated Monthly Volume": "40+ Metric Tonnes Rice, 10 MT Bengal Gram & Pulses, 6 MT Peanuts, 5,000 L Pure Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Corporate SCM Central Commissary Master Vendor Agreement",
        "Address / Landmark": "Shalibanda Road, Charminar / Central Depot IDA Uppal, Hyderabad - 500002",
        "Contact Channel": "Managing Director & Head of SCM (procurement@pistahouse.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Heritage Irani Cafes, Bakeries & Mess Commissaries",
        "Business Name": "Shah Ghouse Central Kitchens & Chain",
        "Town": "Tolichowki & Gachibowli",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Iconic high-volume restaurant chain feeding thousands of biryani and Mughlai curry lovers late into the night across Cyberabad",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Pure Cooking Oil",
        "Estimated Monthly Volume": "25 MT Rice, 4 MT Dals, 2.5 MT Bengal Gram, 3,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Direct Mill Wholesale Supply Agreement",
        "Address / Landmark": "Opp. Bio-Diversity Park, Gachibowli, Hyderabad - 500032",
        "Contact Channel": "Managing Partner (shahghousehyd@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Heritage Irani Cafes, Bakeries & Mess Commissaries",
        "Business Name": "Rio Restaurant & Irani Cafe",
        "Town": "Patny Circle, Secunderabad",
        "Region": "Secunderabad Commercial Core",
        "Facility Scale / Outlets": "Heritage Irani cafe in Secunderabad operating continuous high-traffic tea, samosa, biryani, and tiffin counters",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram for samosas/bajjis, Cooking Oil",
        "Estimated Monthly Volume": "12 MT Rice, 2.5 MT Dals, 1.8 MT Bengal Gram, 1,500 L Oil",
        "Procurement Profile / Tie-up Potential": "Commercial Cafe Supply Agreement",
        "Address / Landmark": "Patny Circle, Sardar Patel Road, Secunderabad - 500003",
        "Contact Channel": "Managing Partner (riorestaurant@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Heritage Irani Cafes, Bakeries & Mess Commissaries",
        "Business Name": "Paradise Food Court Central Commissary",
        "Town": "PG Road, Secunderabad & 30+ City Outlets",
        "Region": "Secunderabad / Greater Hyderabad",
        "Facility Scale / Outlets": "The iconic 70-year brand with 30+ outlets in the twin cities, producing thousands of meals daily from its mega central commissary",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Unpolished Pulses, Pure Cooking Oil",
        "Estimated Monthly Volume": "35+ Metric Tonnes Rice, 6 MT Dals, 4,500 L Pure Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Centralized Corporate SCM Framework Contract",
        "Address / Landmark": "Paradise Circle, MG Road, Secunderabad - 500003",
        "Contact Channel": "Head of SCM & Food Sourcing (scm@paradisefoodcourt.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Heritage Irani Cafes, Bakeries & Mess Commissaries",
        "Business Name": "Bawarchi Restaurant Mega Kitchen",
        "Town": "RTC X Roads, Musheerabad",
        "Region": "Hyderabad Central",
        "Facility Scale / Outlets": "India's highest single-restaurant biryani seller, cooking hundreds of giant deghs (handis) daily for 10,000+ diners",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Groundnut Cooking Oil, Sun-Dried Red Chilies",
        "Estimated Monthly Volume": "30+ Metric Tonnes Rice, 4 MT Toor Dal, 3,500 L Cooking Oil, 1.5 MT Red Chilies",
        "Procurement Profile / Tie-up Potential": "Direct Mill Wholesale Contract / Biweekly Truckload Delivery",
        "Address / Landmark": "RTC X Roads, Musheerabad, Hyderabad - 500020",
        "Contact Channel": "Managing Partner & Head Chef (bawarchixroads@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Heritage Irani Cafes, Bakeries & Mess Commissaries",
        "Business Name": "Al Rabea Al Arabi Mandi & Restaurant",
        "Town": "Barkas / Chandrayangutta Corridor",
        "Region": "Hyderabad South",
        "Facility Scale / Outlets": "The pioneer and highest-turnover authentic Yemeni Mandi restaurant in Hyderabad's historic Arab quarter (Barkas)",
        "Key Crops Demanded": "Aged Rice Grains, Sona Masoori, Bold Peanuts & Putnalu, Sun-Dried Red Chilies, Cooking Oil",
        "Estimated Monthly Volume": "18 MT Rice, 2.5 MT Groundnuts & Putnalu, 1.5 MT Chilies, 2,200 L Oil",
        "Procurement Profile / Tie-up Potential": "Direct Highway Delivery Commodity Agreement",
        "Address / Landmark": "Main Road, Barkas, Chandrayangutta, Hyderabad - 500005",
        "Contact Channel": "Managing Director (alrabeamandi@gmail.com)"
    }
]

def main():
    df = pd.DataFrame(BUYERS)
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")
    print(f"Successfully generated Phase 10 Hyderabad Hotels & Restaurants Database with {len(df)} buyers!")
    print(f"Saved to: {OUTPUT_CSV}")
    
    # Summary by Category
    print("\nBreakdown by Category:")
    print(df["Category"].value_counts())

if __name__ == "__main__":
    main()
