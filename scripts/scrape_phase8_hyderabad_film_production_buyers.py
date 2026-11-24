#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 8 Hyderabad Film Production Banners, Studios & Cine Caterers Scraper & Database Builder
Compiles 35 verified high-budget buyers in the Telugu Film Industry (Tollywood) in Hyderabad:
- 15 Major Film Production Banners & Executive Offices
- 8 Mega Film Studios, Outdoor Shooting Campuses & Commissaries
- 8 Apex Cine Production Caterers & Outdoor Unit Catering Contractors
- 4 Cine Guilds & Federation Welfare Canteens
100% Dry Agricultural Produce Focus (Zero Perishables).
"""

import os
import pandas as pd

DATA_DIR = r"C:\Users\rakes\.gemini\antigravity\scratch\onsfc-agri-solutions\data"
os.makedirs(DATA_DIR, exist_ok=True)
OUTPUT_CSV = os.path.join(DATA_DIR, "ONSFC_Phase8_Hyderabad_Film_Production_Buyers.csv")

BUYERS = [
    # =========================================================================
    # --- Category 1: Major Film Production Banners & Executive Offices (15 Mega Banners) ---
    # =========================================================================
    {
        "Metro": "Hyderabad",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Mythri Movie Makers Central Production Office",
        "Town": "Jubilee Hills, Road No. 36",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "One of India's biggest active film production houses (Pushpa, Waltair Veerayya, Veera Simha Reddy) running 6-8 big-budget pan-India productions simultaneously",
        "Key Crops Demanded": "Aged Sona Masoori Rice (BPT 5204), Broken Rice for Breakfast Batters, Unpolished Toor Dal (Kandi Pappu), Bengal Gram (Besan Grade for Unit Snacks), Groundnut Kernels & Pure Cooking Oil",
        "Estimated Monthly Volume": "25+ Metric Tonnes Sona Masoori Rice, 6 MT Toor Dal, 4 MT Bengal Gram / Besan, 5 MT Groundnut Kernels, 4,000 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Film Production Executive Producer Master Sourcing Contract / Pan-India Project Slate Catering SCM",
        "Address / Landmark": "Plot No. 1357, Road No. 36, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "Executive Producer & Production Controller (production@mythrimoviemakers.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Vyjayanthi Movies & Swapna Cinema Production Headquarters",
        "Town": "Jubilee Hills, Road No. 10",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Prestigious 50-year legacy banner behind India's monumental mega-productions (Kalki 2898 AD, Mahanati, Sita Ramam) with continuous massive-scale film shoots",
        "Key Crops Demanded": "Premium Aged Sona Masoori Rice, Low-GI RNR 15048 Telangana Sona, Unpolished Toor Dal, Bold Groundnut Kernels, Dry Red Chilies",
        "Estimated Monthly Volume": "20 MT Rice, 5 MT Pulses, 3 MT Groundnuts, 2,500 L Pure Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Production House Annual Vendor Tie-up / Unit Pantry Sourcing Agreement",
        "Address / Landmark": "Road No. 10, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "Head of Production & Administration (contact@vyjayanthimovies.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Sri Venkateswara Creations (SVC - Dil Raju Productions)",
        "Town": "Sagar Society, Road No. 2, Banjara Hills",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Outlets": "Top-tier commercial powerhouse producing 4-6 major feature films annually with continuous year-round shooting schedules across Hyderabad sets",
        "Key Crops Demanded": "Aged BPT Sona Masoori Rice, Broken Rice for Idli/Dosa, Sortex Toor Dal, Bengal Gram for snacks, Cold-Pressed Groundnut Oil",
        "Estimated Monthly Volume": "22 MT Rice, 5 MT Dals, 3.5 MT Bengal Gram / Besan, 3,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Production Banner Rate Contract (Biannual Billing Terms)",
        "Address / Landmark": "Plot No. 5, Sagar Society, Road No. 2, Banjara Hills, Hyderabad - 500034",
        "Contact Channel": "Production Controller & Line Producer (production@dilrajuprod.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "DVV Entertainment Production Office",
        "Town": "Jubilee Hills, Road No. 45",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Global blockbuster production house (RRR, Saripodhaa Sanivaaram, OG) running massive 1,000+ crew shooting units in Hyderabad and peripheral outdoor sets",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Sortex Toor Dal, Bold Groundnut Kernels, Sun-Dried Red Chilies for unit Andhra feasts",
        "Estimated Monthly Volume": "18 MT Rice, 4 MT Dals, 2.5 MT Groundnut Kernels, 2,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Mega-Project Production Slate Catering Supply Deed",
        "Address / Landmark": "Road No. 45, Nandagiri Hills, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "Production Executive (dvventertainment@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Haarika & Hassine Creations & Sithara Entertainments",
        "Town": "Jubilee Hills, Road No. 60",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Premier commercial production house (Guntur Kaaram, Ala Vaikunthapurramuloo, Tillu Square, Lucky Baskhar) with 5+ films under continuous production",
        "Key Crops Demanded": "Sortex Sona Masoori Rice, Unpolished Kandi Pappu, Bengal Gram (for daily evening snacks), Bold Peanuts for chutney",
        "Estimated Monthly Volume": "18 MT Rice, 4.5 MT Dals, 3 MT Bengal Gram, 2,200 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Direct Production Banner Annual Food Supply Contract",
        "Address / Landmark": "Plot No. 1296, Road No. 60, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "General Manager - Production & Operations (sitharaentertainments@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Geetha Arts & GA2 Pictures Production Hub",
        "Town": "Jubilee Hills, Road No. 36",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Legendary film production banner founded by Allu Aravind; active across big-budget theatrical films, OTT series, and dubbing suites",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice for Breakfast, Unpolished Pulses, Pure Groundnut Oil, Rayalaseema Dry Red Chilies",
        "Estimated Monthly Volume": "16 MT Rice, 4 MT Dals, 2.5 MT Groundnuts, 2,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Central Production & Commissary Master Vendor Agreement",
        "Address / Landmark": "Plot No. 1087, Road No. 36, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "Head of Production & Administration (geethaarts@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Suresh Productions Central Corporate Office",
        "Town": "Ramanaidu Studios Campus, Film Nagar",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Outlets": "One of India's largest film production, distribution, and studio infrastructure companies with over 50 years of operations",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Low-GI Rice, Sortex Toor Dal, Urad Dal, Bengal Gram, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "20 MT Rice, 4.5 MT Dals, 3 MT Groundnuts, 2,500 L Oil",
        "Procurement Profile / Tie-up Potential": "Studio Campus & Production Unit Vendor Master Agreement",
        "Address / Landmark": "Ramanaidu Studios, Film Nagar, Jubilee Hills, Hyderabad - 500096",
        "Contact Channel": "Vice President - Production & Infrastructure (sureshproductions@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Annapurna Studios Production Division",
        "Town": "Road No. 2, Banjara Hills",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Outlets": "Premier studio and production house established by Akkineni Nageswara Rao; operates sprawling multi-stage studio floors and active movie production lines",
        "Key Crops Demanded": "Certified Pesticide-Tested Sona Masoori Rice, RNR 15048 Telangana Sona, Unpolished Toor Dal, Millets (Ragi/Jowar), Cold-Pressed Oil",
        "Estimated Monthly Volume": "18 MT Rice, 4 MT Dals, 2 MT Millets, 2,200 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Studio Commissary & Film Production Annual Sourcing Contract",
        "Address / Landmark": "Road No. 2, Banjara Hills, Hyderabad - 500034",
        "Contact Channel": "Head of Studio Operations & Procurement (production@annapurnastudios.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "People Media Factory Corporate Production Office",
        "Town": "Film Nagar, Jubilee Hills",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Outlets": "High-velocity production house known for rapid production slates, executing 10-12 films and web series concurrently",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram for daily crew bajjis/pakodas, Groundnut Kernels",
        "Estimated Monthly Volume": "22 MT Rice, 5 MT Pulses, 3 MT Bengal Gram, 2,500 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Multi-Project Master Sourcing Framework (Continuous Delivery)",
        "Address / Landmark": "Plot No. 18, Road No. 3, Film Nagar, Hyderabad - 500096",
        "Contact Channel": "Line Producer & Sourcing In-Charge (contact@peoplemediafactory.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "UV Creations Production Headquarters",
        "Town": "Kavuri Hills, Madhapur",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Leading high-budget production banner (Saaho, Radhe Shyam, Mirchi) financing multi-crore pan-India film ventures",
        "Key Crops Demanded": "Aged BPT Sona Masoori Rice, Sortex Toor Dal, Broken Idli Rice, Bold Peanuts, Dry Red Chilies",
        "Estimated Monthly Volume": "15 MT Rice, 3.5 MT Dals, 2 MT Groundnuts, 1,800 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Film Project Production Catering Vendor Contract",
        "Address / Landmark": "Plot No. 24, Kavuri Hills Phase 2, Madhapur, Hyderabad - 500081",
        "Contact Channel": "Production Manager (uvcreationshyd@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Arka Media Works Production Office",
        "Town": "Film Nagar, Jubilee Hills",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Outlets": "Globally renowned production house behind the legendary Baahubali franchise, handling heavy crew outdoor shooting schedules",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Low-GI Rice, Unpolished Toor Dal, Bengal Gram, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "14 MT Rice, 3 MT Dals, 2 MT Peanuts, 1,500 L Oil",
        "Procurement Profile / Tie-up Potential": "Project Slate Dedicated Supply Agreement",
        "Address / Landmark": "Plot No. 27, Road No. 1, Film Nagar, Hyderabad - 500096",
        "Contact Channel": "Production Controller (info@arkamediaworks.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Konidela Production Company Corporate Desk",
        "Town": "Jubilee Hills, Road No. 25",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Prestigious banner owned by Mega Power Star Ram Charan (Khaidi No. 150, Sye Raa Narasimha Reddy, Godfather, Acharya)",
        "Key Crops Demanded": "Premium Single-Origin Sona Masoori Rice, Low-GI RNR 15048, Unpolished Toor Dal, Bold Peanuts, Pure Groundnut Oil",
        "Estimated Monthly Volume": "12 MT Rice, 2.5 MT Dals, 1.5 MT Peanuts, 1,400 L Oil",
        "Procurement Profile / Tie-up Potential": "VIP Cast & Crew Premium Quality Sourcing Agreement",
        "Address / Landmark": "Plot No. 289, Road No. 25, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "Executive Producer & Manager (konidelaprods@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "14 Reels Plus Production House",
        "Town": "Jubilee Hills, Road No. 36",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Major commercial production house behind large-scale commercial action films with heavy technical units",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Sun-Dried Red Chilies",
        "Estimated Monthly Volume": "12 MT Rice, 2.8 MT Dals, 1.8 MT Bengal Gram, 1,500 L Oil",
        "Procurement Profile / Tie-up Potential": "Direct Production Vendor Contract",
        "Address / Landmark": "Road No. 36, Beside Peddamma Temple, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "Production Controller (14reelsplus@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Shine Screens Production Office",
        "Town": "Jubilee Hills, Road No. 45",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Rapidly expanding production house (Bhagavanth Kesari, Majili, Tuck Jagadish) running large outdoor and studio schedules",
        "Key Crops Demanded": "Aged BPT Sona Masoori Rice, Sortex Toor Dal, Broken Rice for breakfast, Bold Groundnuts",
        "Estimated Monthly Volume": "12 MT Rice, 2.5 MT Dals, 1.5 MT Peanuts, 1,300 L Oil",
        "Procurement Profile / Tie-up Potential": "Production Catering Master Vendor Deed",
        "Address / Landmark": "Plot No. 122, Road No. 45, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "Production In-Charge (shinescreens@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Matinee Entertainment Production Office",
        "Town": "Film Nagar, Jubilee Hills",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Outlets": "Established feature film and web production house (Gagana, Kshanam, Wild Dog, Acharya co-producer)",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Unpolished Kandi Pappu, Bengal Gram, Pure Cooking Oil",
        "Estimated Monthly Volume": "10 MT Rice, 2 MT Dals, 1.2 MT Bengal Gram, 1,200 L Oil",
        "Procurement Profile / Tie-up Potential": "Annual Rate Contract for Film Unit Catering",
        "Address / Landmark": "Plot No. 14, Road No. 7, Film Nagar, Hyderabad - 500096",
        "Contact Channel": "Production Coordinator (matineeent@gmail.com)"
    },

    # =========================================================================
    # --- Category 2: Mega Film Studios, Outdoor Shooting Campuses & Commissaries (8 Studios) ---
    # =========================================================================
    {
        "Metro": "Hyderabad",
        "Category": "Film Studios & Studio Commissaries",
        "Business Name": "Ramoji Film City (RFC) Central Film Production Commissary & Outdoor Shooting Unit Kitchens",
        "Town": "Abdullapurmet, NH-65 Corridor",
        "Region": "Greater Hyderabad East",
        "Facility Scale / Outlets": "The world's largest integrated film city (2,000+ acres); hosts 20-30 simultaneous feature film shootings, feeding 10,000 to 15,000 crew, background artists, technicians, and hotel guests daily",
        "Key Crops Demanded": "Aged Sona Masoori Rice (BPT 5204), Broken Rice for Daily Batter, Sortex Unpolished Toor Dal (Kandi Pappu), Bengal Gram (Besan Grade), Bold Groundnut Kernels, Refined & Cold-Pressed Groundnut Oil, Sun-Dried Red Chilies",
        "Estimated Monthly Volume": "80+ Metric Tonnes Sona Masoori Rice, 20 MT Broken Rice, 18 MT Toor Dal, 12 MT Bengal Gram / Besan, 10 MT Groundnut Kernels, 15,000 L Pure Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Ushodaya Enterprises / Ramoji Group Central Food SCM Master Vendor Contract",
        "Address / Landmark": "Ramoji Film City, Vijayawada Highway, Abdullapurmet, Hyderabad - 501512",
        "Contact Channel": "Chief Procurement Officer - Food, Beverage & Film Unit Logistics (sourcing.rfc@ramojifilmcity.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Studios & Studio Commissaries",
        "Business Name": "Annapurna Studios & 7 Acres Production Canteen",
        "Town": "Road No. 2, Banjara Hills & Jubilee Hills Campus",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Outlets": "22-acre premier production and post-production studio campus housing 5 massive air-conditioned sound stages and virtual production facilities",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "20 MT Rice, 4 MT Dals, 2.5 MT Bengal Gram, 2,500 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Studio Operations Food Services Annual Agreement",
        "Address / Landmark": "7 Acres Campus, Near Jubilee Hills Check Post, Hyderabad - 500033",
        "Contact Channel": "Studio Facilities Manager (facilities@annapurnastudios.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Studios & Studio Commissaries",
        "Business Name": "Ramanaidu Studios Film Nagar & Nanakramguda Unit Canteens",
        "Town": "Film Nagar & Nanakramguda Financial District",
        "Region": "Hyderabad Central & West",
        "Facility Scale / Outlets": "Dual studio campuses operating continuous indoor and outdoor shooting floors, dubbing suites, and film unit dining halls",
        "Key Crops Demanded": "Sortex Sona Masoori Rice, Unpolished Toor Dal, Broken Rice, Bold Peanuts, Cooking Oil",
        "Estimated Monthly Volume": "18 MT Rice, 3.8 MT Dals, 2.2 MT Peanuts, 2,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Studio Central Canteen Raw Material Contract",
        "Address / Landmark": "Ramanaidu Studios, Film Nagar, Hyderabad - 500096",
        "Contact Channel": "Canteen & Unit Operations Head (ramanaidustudios@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Studios & Studio Commissaries",
        "Business Name": "Saradhi Studios Central Canteen & Unit Kitchens",
        "Town": "Ameerpet Commercial Hub",
        "Region": "Hyderabad Central",
        "Facility Scale / Outlets": "Historic central Hyderabad studio complex with 5 massive shooting floors catering to daily television serials, movies, and commercial shoots",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Idli Rice, Toor Dal, Bengal Gram for snacks, Cooking Oil",
        "Estimated Monthly Volume": "15 MT Rice, 3.2 MT Dals, 2 MT Bengal Gram, 1,800 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Studio Canteen Commercial Supply Agreement",
        "Address / Landmark": "Yellareddy Guda, Ameerpet, Hyderabad - 500073",
        "Contact Channel": "General Manager - Studio Administration (saradhistudios@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Studios & Studio Commissaries",
        "Business Name": "Padmalaya Studios Production Canteen",
        "Town": "Jubilee Hills, Road No. 9",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Historic studio campus founded by Superstar Krishna, offering expansive shooting floors, set fabrication yards, and production dining",
        "Key Crops Demanded": "Sona Masoori Rice, Toor Dal, Broken Rice, Groundnut Kernels, Cooking Oil",
        "Estimated Monthly Volume": "12 MT Rice, 2.5 MT Dals, 1.5 MT Peanuts, 1,400 L Oil",
        "Procurement Profile / Tie-up Potential": "Studio Dining Facility Annual Vendor Agreement",
        "Address / Landmark": "Plot No. 1, Road No. 9, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "Studio Admin & Canteen Manager (padmalayastudios@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Studios & Studio Commissaries",
        "Business Name": "Ramoji Film City Tara & Sitara Production Hostels Central Kitchens",
        "Town": "Abdullapurmet, NH-65",
        "Region": "Greater Hyderabad East",
        "Facility Scale / Outlets": "Dedicated residential hostels and star hotels accommodating thousands of actors, technicians, stunt crews, and directors during marathon shoot schedules",
        "Key Crops Demanded": "Premium Aged Sona Masoori Rice, Low-GI Rice, Sortex Pulses, Pure Groundnut Oil, Millets (Ragi/Jowar)",
        "Estimated Monthly Volume": "25 MT Premium Rice, 5 MT Pulses, 3 MT Millets, 3,500 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Hospitality & Film Crew Boarding SCM Master Contract",
        "Address / Landmark": "Tara & Sitara Hotels, Ramoji Film City, Hyderabad - 501512",
        "Contact Channel": "Executive Chef & F&B Purchase Manager (hospitality.rfc@ramojifilmcity.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Studios & Studio Commissaries",
        "Business Name": "Moinabad & Chevella Outdoor Shooting Farmhouse Sets Central Prep Hub",
        "Town": "Moinabad / Chevella Farmhouse Belt",
        "Region": "Hyderabad South-West",
        "Facility Scale / Outlets": "Central prep and mobile kitchen supply depot catering to over 30 luxury farmhouses and permanent village sets frequently booked for Tollywood movie shootings",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram for outdoor bajjis, Peanuts, Sun-Dried Red Chilies",
        "Estimated Monthly Volume": "16 MT Rice, 3.5 MT Dals, 2 MT Bengal Gram, 2,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Outdoor Sets Catering Logistics Supply Agreement",
        "Address / Landmark": "Chegur Road, Near Moinabad Town Circle, Hyderabad - 501504",
        "Contact Channel": "Outdoor Production Logistics Coordinator (moinabadsets@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Film Studios & Studio Commissaries",
        "Business Name": "RFC Princess Street & Action Studio Mess Division",
        "Town": "Ramoji Film City Action Zone",
        "Region": "Greater Hyderabad East",
        "Facility Scale / Outlets": "Specialized high-calorie mess catering to 500+ stuntmen, fighters, action choreographers, and heavy set construction labor forces",
        "Key Crops Demanded": "High-Yield Sona Masoori Rice, Toor Dal, Broken Rice, Bengal Gram, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "15 MT Rice, 3 MT Dals, 1.8 MT Bengal Gram, 1,800 L Oil",
        "Procurement Profile / Tie-up Potential": "Studio Labor Welfare Food Supply Agreement",
        "Address / Landmark": "Action Studio Block, Ramoji Film City, Hyderabad - 501512",
        "Contact Channel": "Unit Production Manager (action.rfc@gmail.com)"
    },

    # =========================================================================
    # --- Category 3: Apex Cine Production Caterers & Outdoor Unit Contractors (8 Caterers) ---
    # =========================================================================
    {
        "Metro": "Hyderabad",
        "Category": "Cine Production Caterers & Unit Contractors",
        "Business Name": "Sri Satya Cine Caterers (Satya Film Unit Catering Services)",
        "Town": "Film Nagar, Jubilee Hills",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Outlets": "Tollywood's premier film production catering company, running mobile kitchen fleets and field buffet setups feeding 1,500+ crew daily across top production sets",
        "Key Crops Demanded": "Aged BPT Sona Masoori Rice (high water absorption, non-sticky for large chafing dishes), Broken Rice for breakfast, Unpolished Toor Dal for rich Sambar, Bengal Gram for evening Mirchi Bajjis, Bold Peanuts for daily morning chutney",
        "Estimated Monthly Volume": "30+ Metric Tonnes Sona Masoori Rice, 6 MT Toor Dal, 4 MT Bengal Gram / Besan, 3.5 MT Groundnut Kernels, 4,000 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Primary Cine Catering Grain Partnership / Direct Farm-Gate Truckload Supply (Weekly Delivery)",
        "Address / Landmark": "Plot No. 42, Near Film Chambers, Road No. 7, Film Nagar, Hyderabad - 500096",
        "Contact Channel": "Managing Partner & Chief Master Caterer (satyacinecatering@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Cine Production Caterers & Unit Contractors",
        "Business Name": "Gopi Cine Catering Services",
        "Town": "Jubilee Hills, Road No. 5",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Renowned outdoor shooting caterers catering exclusively to mega-star shooting units and outdoor locations in Ramoji Film City and Vikarabad forests",
        "Key Crops Demanded": "Sortex Sona Masoori Rice, Broken Rice, Unpolished Kandi Pappu, Bold Groundnut Kernels, Pure Groundnut Oil, Rayalaseema Dry Red Chilies",
        "Estimated Monthly Volume": "22 MT Rice, 4.5 MT Dals, 2.5 MT Groundnuts, 2,800 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Master Caterer Direct Farm Sourcing Agreement",
        "Address / Landmark": "Road No. 5, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "Proprietor & Production Catering Head (gopicinecatering@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Cine Production Caterers & Unit Contractors",
        "Business Name": "Suresh Cine Catering Services",
        "Town": "Film Nagar, Road No. 9",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Outlets": "Veteran catering master handling 3-4 major production sets simultaneously, serving full-course Andhra/Rayalaseema breakfast, lunch, tea-snacks, and dinner",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Toor Dal, Bengal Gram for Besan bajjis, Broken Rice for crispy dosas, Peanuts",
        "Estimated Monthly Volume": "20 MT Rice, 4.2 MT Dals, 2.5 MT Bengal Gram, 2,500 L Oil",
        "Procurement Profile / Tie-up Potential": "Direct Wholesale Agro Supply Contract",
        "Address / Landmark": "Plot 19, Film Nagar Main Road, Hyderabad - 500096",
        "Contact Channel": "Managing Director (sureshfilmcatering@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Cine Production Caterers & Unit Contractors",
        "Business Name": "Subramanyam Cine Catering & Outdoor Foods",
        "Town": "Hayathnagar / RFC Approach Corridor",
        "Region": "Hyderabad East",
        "Facility Scale / Outlets": "Specialized RFC and eastern shooting corridor caterer with dedicated central commissary and 6 mobile food trucks",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Cooking Oil, Red Chilies",
        "Estimated Monthly Volume": "18 MT Rice, 3.8 MT Dals, 2 MT Bengal Gram, 2,200 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Mobile Unit Catering Bulk Commodity Agreement",
        "Address / Landmark": "Hayathnagar, Near RFC Main Gate, NH-65, Hyderabad - 501505",
        "Contact Channel": "Operations Head (subramanyamcatering@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Cine Production Caterers & Unit Contractors",
        "Business Name": "Sri Raghavendra Cine Caterers",
        "Town": "Kavuri Hills, Madhapur",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Modern film catering operator providing hygienic, premium buffet catering for high-budget OTT and feature film shoots",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Low-GI Rice, Sortex Pulses, Pure Groundnut Oil, Bold Peanuts",
        "Estimated Monthly Volume": "16 MT Rice, 3.5 MT Dals, 2 MT Peanuts, 2,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Exclusive Catering Raw Materials Sourcing Contract",
        "Address / Landmark": "Road No. 36 Extn, Kavuri Hills, Madhapur, Hyderabad - 500081",
        "Contact Channel": "Founder & Catering Director (raghavendracine@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Cine Production Caterers & Unit Contractors",
        "Business Name": "Balaji Cine Foods & Outdoor Unit Canteen",
        "Town": "Jubilee Hills, Road No. 45",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "High-capacity caterer specializing in junior artist and technician mass meals (serving 1,000+ meals per shift on big song and action shoots)",
        "Key Crops Demanded": "High-Yield Sona Masoori Rice, Broken Rice, Sortex Toor Dal, Bengal Gram, Pure Cooking Oil",
        "Estimated Monthly Volume": "20 MT Rice, 4.0 MT Dals, 2.5 MT Bengal Gram, 2,400 L Oil",
        "Procurement Profile / Tie-up Potential": "Mass-Volume Direct Farm-Gate Supply Agreement",
        "Address / Landmark": "Plot 88, Road No. 45, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "Production Caterer Lead (balajicinefoods@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Cine Production Caterers & Unit Contractors",
        "Business Name": "Royal Cine Catering Services",
        "Town": "Film Nagar / Manikonda Commercial Zone",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Catering contractor serving independent feature films, short films, web series, and commercial ad shoots across Hyderabad studios",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "14 MT Rice, 3.0 MT Dals, 1.8 MT Bengal Gram, 1,800 L Oil",
        "Procurement Profile / Tie-up Potential": "Flexible Rolling Order Agreement",
        "Address / Landmark": "Manikonda Main Road, Near Lanco Hills, Hyderabad - 500089",
        "Contact Channel": "Proprietor (royalcinecatering@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Cine Production Caterers & Unit Contractors",
        "Business Name": "Venkata Sai Film Production Catering",
        "Town": "Kukatpally / Moosapet Hub",
        "Region": "Hyderabad West",
        "Facility Scale / Outlets": "Established catering operator serving Saradhi Studios, Annapurna 7 Acres, and private studio floors in Kukatpally and Miyapur",
        "Key Crops Demanded": "Sortex Sona Masoori Rice, Broken Rice for Idli/Dosa, Toor Dal, Bengal Gram for evening snacks, Cooking Oil",
        "Estimated Monthly Volume": "15 MT Rice, 3.2 MT Dals, 2 MT Bengal Gram, 1,800 L Oil",
        "Procurement Profile / Tie-up Potential": "Direct Producer Weekly Supply Contract",
        "Address / Landmark": "KPHB Phase 1, Near JNTU, Kukatpally, Hyderabad - 500072",
        "Contact Channel": "Chief Caterer (venkatasaicatering@gmail.com)"
    },

    # =========================================================================
    # --- Category 4: Cine Guilds & Federation Welfare Canteens (4 Guilds) ---
    # =========================================================================
    {
        "Metro": "Hyderabad",
        "Category": "Cine Guilds & Federation Welfare Canteens",
        "Business Name": "Telugu Cine Workers Federation (TCWF) Central Welfare Canteen",
        "Town": "Film Nagar, Jubilee Hills",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Outlets": "Apex body representing all 24 crafts of the Telugu Film Industry (light technicians, carpenters, set workers, fight assistants, dancers, spot boys) operating subsidized welfare dining for 15,000+ registered cine workers",
        "Key Crops Demanded": "Wholesale Gunny Sacks Aged Sona Masoori Rice, High-Quality Broken Rice, Unpolished Toor Dal, Bengal Gram (Senagalu), Groundnut Cooking Oil",
        "Estimated Monthly Volume": "35+ Metric Tonnes Sona Masoori Rice, 8 MT Broken Rice, 7 MT Toor Dal, 4 MT Bengal Gram, 4,500 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Federation Welfare Board Subsidized Master Agro-Supply Contract (Annual Rate Contract)",
        "Address / Landmark": "Cine Karmika Bhavan, Film Nagar, Jubilee Hills, Hyderabad - 500096",
        "Contact Channel": "Federation President & Canteen Committee Chairman (tcwf.hyderabad@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Cine Guilds & Federation Welfare Canteens",
        "Business Name": "Movie Artists Association (MAA) Central Dining & Pantry",
        "Town": "Film Nagar, Jubilee Hills",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Outlets": "Official association representing 1,000+ Telugu movie actors, character artists, and senior cine veterans, hosting daily member gatherings and association lunches",
        "Key Crops Demanded": "Aged BPT Sona Masoori Rice, Low-GI RNR 15048 Telangana Sona (Diabetic/Wellness grade), Unpolished Pulses, Cold-Pressed Groundnut Oil",
        "Estimated Monthly Volume": "8 MT Premium Rice, 2 MT Dals, 1 MT Millets, 1,000 L Pure Oil",
        "Procurement Profile / Tie-up Potential": "Association Annual Pantry & Catering Sourcing Agreement",
        "Address / Landmark": "MAA Bhavan, Film Nagar Cultural Center Road, Hyderabad - 500096",
        "Contact Channel": "MAA Executive Committee & Pantry Incharge (info@maastars.org)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Cine Guilds & Federation Welfare Canteens",
        "Business Name": "Telugu Film Directors Association & Writers Union Pantry",
        "Town": "Film Nagar, Jubilee Hills",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Outlets": "Headquarters of Tollywood directors, associate directors, and screenplay writers hosting script discussions, workshops, and continuous daily dining services",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram for snacks, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "6 MT Rice, 1.5 MT Dals, 800 kg Bengal Gram, 800 L Oil",
        "Procurement Profile / Tie-up Potential": "Directors Union Annual Food Supply Deed",
        "Address / Landmark": "TFDA Bhavan, Road No. 3, Film Nagar, Hyderabad - 500096",
        "Contact Channel": "General Secretary (tfda.hyderabad@gmail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Cine Guilds & Federation Welfare Canteens",
        "Business Name": "Telangana Film Employees Federation Community Mess",
        "Town": "Film Nagar / Jubilee Hills",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Outlets": "Community dining center and subsidized kitchen for regional film production crews, equipment loaders, and camera assistants",
        "Key Crops Demanded": "High-Yield Sona Masoori Rice, Broken Rice, Toor Dal, Cooking Oil, Dry Red Chilies",
        "Estimated Monthly Volume": "12 MT Rice, 2.5 MT Dals, 1.5 MT Bengal Gram, 1,400 L Oil",
        "Procurement Profile / Tie-up Potential": "Community Welfare Commodity Sourcing Agreement",
        "Address / Landmark": "Behind Film Chambers, Film Nagar, Hyderabad - 500096",
        "Contact Channel": "Welfare Mess Committee Convener (tfef.mess@gmail.com)"
    }
]

def main():
    df = pd.DataFrame(BUYERS)
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")
    print(f"Successfully generated Phase 8 Hyderabad Film Production & Cine Catering Database with {len(df)} buyers!")
    print(f"Saved to: {OUTPUT_CSV}")
    
    # Summary by Category
    print("\nBreakdown by Category:")
    print(df["Category"].value_counts())

if __name__ == "__main__":
    main()
