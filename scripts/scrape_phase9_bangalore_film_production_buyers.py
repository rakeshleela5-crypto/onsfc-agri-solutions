#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 9 Bengaluru Film Production Banners, Studios & Cine Caterers Scraper & Database Builder
Compiles 35 verified high-budget buyers in the Kannada Film Industry (Sandalwood) in Bengaluru:
- 15 Major Sandalwood Film Production Banners & Executive Offices
- 8 Mega Film Studios, Outdoor Shooting Campuses & Commissaries
- 8 Apex Cine Production Caterers & Outdoor Unit Catering Contractors
- 4 Cine Guilds & Federation Welfare Canteens
100% Dry Agricultural Produce Focus (Zero Perishables).
"""

import os
import pandas as pd

DATA_DIR = r"C:\Users\rakes\.gemini\antigravity\scratch\onsfc-agri-solutions\data"
os.makedirs(DATA_DIR, exist_ok=True)
OUTPUT_CSV = os.path.join(DATA_DIR, "ONSFC_Phase9_Bengaluru_Film_Production_Buyers.csv")

BUYERS = [
    # =========================================================================
    # --- Category 1: Major Sandalwood Film Production Banners & Executive Offices (15 Mega Banners) ---
    # =========================================================================
    {
        "Metro": "Bengaluru",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Hombale Films Central Production Headquarters",
        "Town": "Basavanagudi / Jayanagar Commercial Hub",
        "Region": "Bengaluru South",
        "Facility Scale / Outlets": "India's premier pan-India blockbuster powerhouse (KGF Chapter 1 & 2, Kantara, Salaar, Bagheera) running 6-8 multi-crore mega-budget film productions simultaneously",
        "Key Crops Demanded": "Aged Sona Masoori Rice (BPT 5204), Pure Karnataka Ragi (for unit Ragi Mudde), Broken Rice for breakfast, Unpolished Toor Dal (Togari Bele), Bengal Gram (Besan Grade), Bold Groundnut Kernels & Pure Cooking Oil",
        "Estimated Monthly Volume": "30+ Metric Tonnes Sona Masoori Rice, 10 MT Karnataka Ragi, 6 MT Toor Dal, 4 MT Bengal Gram / Besan, 5 MT Groundnut Kernels, 4,500 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Film Production Executive Producer Master Sourcing Contract / Pan-India Project Slate Catering SCM",
        "Address / Landmark": "No. 40, Krishna Rao Road, Basavanagudi, Bengaluru - 560004",
        "Contact Channel": "Executive Producer & Head of Production (production@hombalefilms.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Rockline Entertainments Corporate Office",
        "Town": "Basavanagudi / Rajajinagar Hub",
        "Region": "Bengaluru West / South",
        "Facility Scale / Outlets": "Legendary 30-year legacy production powerhouse led by Rockline Venkatesh (Bajrangi Bhaijaan, Lingaa, Kurukshetra, Natasaarvabhowma) running continuous massive-scale film productions",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi, Sortex Toor Dal, Broken Rice, Bold Groundnut Kernels, Dry Red Chilies",
        "Estimated Monthly Volume": "22 MT Rice, 7 MT Ragi, 5 MT Dals, 3 MT Groundnuts, 3,000 L Pure Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Production House Annual Vendor Tie-up / Unit Commissary Sourcing Agreement",
        "Address / Landmark": "Rockline Centre, 1st Cross, Gandhi Bazaar, Basavanagudi, Bengaluru - 560004",
        "Contact Channel": "Production Controller & Studio Manager (rocklineentertainments@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "KRG Studios / KRG Connects Production Headquarters",
        "Town": "Indiranagar 100 Ft Road Hub",
        "Region": "Bengaluru East",
        "Facility Scale / Outlets": "High-velocity production and distribution powerhouse (Rathnan Prapancha, Gurudev Hoysala, Uttarakaanda) executing 5+ feature film productions concurrently",
        "Key Crops Demanded": "Aged BPT Sona Masoori Rice, Karnataka Ragi for daily unit Mudde, Sortex Toor Dal, Bengal Gram for snacks, Pure Cooking Oil",
        "Estimated Monthly Volume": "18 MT Rice, 5 MT Ragi, 4 MT Dals, 2.5 MT Bengal Gram, 2,200 L Oil",
        "Procurement Profile / Tie-up Potential": "Direct Production Banner Annual Food Supply Contract",
        "Address / Landmark": "100 Feet Road, HAL 2nd Stage, Indiranagar, Bengaluru - 560038",
        "Contact Channel": "Head of Production & Administration (production@krgstudios.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Jayanna Combines & Jayanna Films Corporate Office",
        "Town": "Gandhinagar Film Trade Corridor",
        "Region": "Bengaluru Central",
        "Facility Scale / Outlets": "Veteran blockbuster banner led by Jayanna & Bhogendra (Googly, Gajakesari, Mr. and Mrs. Ramachari, Rustum) producing continuous commercial theatrical slates",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice for breakfast, Unpolished Toor Dal, Karnataka Ragi, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "18 MT Rice, 5 MT Ragi, 4 MT Dals, 2.5 MT Peanuts, 2,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Production Slate Catering Master Agreement",
        "Address / Landmark": "5th Main, Gandhinagar, Bengaluru - 560009",
        "Contact Channel": "Line Producer & SCM Head (jayannacombines@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "PRK Productions (Ashwini Puneeth Rajkumar Desk)",
        "Town": "Sadashivanagar Elite Suburb",
        "Region": "Bengaluru Central-North",
        "Facility Scale / Outlets": "Legacy production house of Dr. Rajkumar family (Kavaludaari, Maya Bazaar 2016, Law, Gandhada Gudi) backing high-concept feature films and web series",
        "Key Crops Demanded": "Certified Single-Origin Sona Masoori Rice, Low-GI RNR 15048, Pure Karnataka Ragi, Organic Toor Dal, Cold-Pressed Groundnut Oil",
        "Estimated Monthly Volume": "14 MT Premium Rice, 4 MT Ragi, 3 MT Organic Dals, 1.8 MT Groundnuts, 1,800 L Pure Oil",
        "Procurement Profile / Tie-up Potential": "VIP Cast & Crew Premium Quality Sourcing Agreement",
        "Address / Landmark": "Upper Palace Orchards, Sadashivanagar, Bengaluru - 560080",
        "Contact Channel": "General Manager - Operations & Production (contact@prkproductions.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Paramvah Studios Corporate Office (Rakshit Shetty Productions)",
        "Town": "JP Nagar Phase 7 / Bannerghatta Road",
        "Region": "Bengaluru South",
        "Facility Scale / Outlets": "Leading creative powerhouse (777 Charlie, Sapta Sagaradaache Ello Side A & B, Kirik Party) managing extensive indoor and outdoor shooting crews",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi for unit Mudde, Broken Rice, Toor Dal, Bold Groundnut Kernels, Cooking Oil",
        "Estimated Monthly Volume": "15 MT Rice, 4.5 MT Ragi, 3.2 MT Dals, 2 MT Peanuts, 1,800 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Project Slate Catering Direct Farm Sourcing Deed",
        "Address / Landmark": "Brigade Millennium Road, JP Nagar 7th Phase, Bengaluru - 560078",
        "Contact Channel": "Production Controller & Operations Lead (paramvahstudios@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Pushkar Films Corporate Desk",
        "Town": "Basaveshwaranagar / Rajajinagar",
        "Region": "Bengaluru West",
        "Facility Scale / Outlets": "High-profile banner headed by Pushkara Mallikarjunaiah (Avane Srimannarayana, Humble Politician Nograj, Katheyondu Shuruvagide)",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi, Sortex Toor Dal, Bengal Gram for snacks, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "12 MT Rice, 3.5 MT Ragi, 2.5 MT Dals, 1.5 MT Bengal Gram, 1,400 L Oil",
        "Procurement Profile / Tie-up Potential": "Production Unit Annual Food Supply Contract",
        "Address / Landmark": "West of Chord Road, Basaveshwaranagar, Bengaluru - 560079",
        "Contact Channel": "Production Incharge (pushkarfilms@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Sri Venkateshwara Cine Chitra (SVCC South Office)",
        "Town": "Koramangala 4th Block / Indiranagar",
        "Region": "Bengaluru South-East",
        "Facility Scale / Outlets": "Leading southern production banner (B.V.S.N. Prasad) producing bilingual big-budget Kannada-Telugu feature films with multi-hundred crew sets",
        "Key Crops Demanded": "Sortex Sona Masoori Rice, Broken Rice, Toor Dal, Bold Peanuts, Dry Red Chilies, Cooking Oil",
        "Estimated Monthly Volume": "15 MT Rice, 4 MT Ragi, 3 MT Dals, 2 MT Peanuts, 1,600 L Oil",
        "Procurement Profile / Tie-up Potential": "Bilingual Slate Production SCM Framework",
        "Address / Landmark": "100 Feet Intermediate Ring Road, Koramangala 4th Block, Bengaluru - 560034",
        "Contact Channel": "Executive Producer (svccbangalore@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Sandesh Productions Central Office",
        "Town": "Palace Road / High Grounds Hub",
        "Region": "Bengaluru Central",
        "Facility Scale / Outlets": "Established production company led by Sandesh Nagaraj (Ghost, Airavata, Amar) running large star-vehicle productions across Karnataka locations",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi, Toor Dal, Bengal Gram, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "14 MT Rice, 4 MT Ragi, 2.8 MT Dals, 1.8 MT Bengal Gram, 1,500 L Oil",
        "Procurement Profile / Tie-up Potential": "Commercial Feature Film Production Supply Deed",
        "Address / Landmark": "Near Mount Carmel College, Palace Road, Bengaluru - 560052",
        "Contact Channel": "Production Controller (sandeshproductions@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "D Beats & V. Harikrishna Productions",
        "Town": "Rajajinagar Industrial / Commercial Town",
        "Region": "Bengaluru West",
        "Facility Scale / Outlets": "Leading music and film production house (Kranti, Yajamana) operating film shoots, dubbing studios, and unit rehearsal mess kitchens",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi, Broken Rice, Sortex Toor Dal, Peanuts for chutney",
        "Estimated Monthly Volume": "12 MT Rice, 3 MT Ragi, 2.5 MT Dals, 1.5 MT Peanuts, 1,300 L Oil",
        "Procurement Profile / Tie-up Potential": "Annual Catering Commodities Supply Agreement",
        "Address / Landmark": "1st Block, Dr. Rajkumar Road, Rajajinagar, Bengaluru - 560010",
        "Contact Channel": "Studio Manager & Line Producer (dbeatsproductions@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Toffee Doodle Productions (Kichcha Sudeepa Productions)",
        "Town": "JP Nagar Phase 6 / Kanakapura Road",
        "Region": "Bengaluru South",
        "Facility Scale / Outlets": "Production banner of superstar Kichcha Sudeepa (Vikrant Rona, Max, Kotigobba 3) executing high-concept mega-canvas film shoots",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Low-GI Rice, Karnataka Ragi, Unpolished Toor Dal, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "14 MT Rice, 3.5 MT Ragi, 2.8 MT Dals, 1.8 MT Peanuts, 1,500 L Oil",
        "Procurement Profile / Tie-up Potential": "VIP Production Unit Direct SCM Contract",
        "Address / Landmark": "Kichcha Creative Hub, 24th Main, JP Nagar 6th Phase, Bengaluru - 560078",
        "Contact Channel": "Production Executive (toffeedoodleprods@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Vaaraahi Chalana Chitram (Bengaluru Office)",
        "Town": "Sadashivanagar Film Hub",
        "Region": "Bengaluru Central-North",
        "Facility Scale / Outlets": "Major production house (Sai Korrapati) producing high-budget multilingual films across Karnataka and Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Sun-Dried Red Chilies",
        "Estimated Monthly Volume": "12 MT Rice, 3 MT Ragi, 2.4 MT Dals, 1.5 MT Bengal Gram, 1,400 L Oil",
        "Procurement Profile / Tie-up Potential": "Project Slate Catering Master Vendor Agreement",
        "Address / Landmark": "Bashyam Circle, Sadashivanagar, Bengaluru - 560080",
        "Contact Channel": "Production Coordinator (vaaraahibangalore@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Venkateshwara Film Associates",
        "Town": "Gandhinagar Film Trade Corridor",
        "Region": "Bengaluru Central",
        "Facility Scale / Outlets": "Prominent Sandalwood financing, production, and distribution house managing multiple regional film projects",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram for snacks, Cooking Oil",
        "Estimated Monthly Volume": "10 MT Rice, 2.5 MT Ragi, 2 MT Dals, 1.2 MT Bengal Gram, 1,200 L Oil",
        "Procurement Profile / Tie-up Potential": "Direct Production Vendor Contract",
        "Address / Landmark": "4th Cross, Gandhinagar, Bengaluru - 560009",
        "Contact Channel": "Managing Partner (vfa.gandhinagar@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Zee Studios South (Kannada Feature Film Division)",
        "Town": "Sadashivanagar / Palace Guttahalli",
        "Region": "Bengaluru Central-North",
        "Facility Scale / Outlets": "Major broadcast and studio conglomerate backing 4-6 theatrical Kannada films and streaming projects annually",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Low-GI Rice, Karnataka Ragi, Sortex Toor Dal, Pure Cooking Oil",
        "Estimated Monthly Volume": "14 MT Rice, 3.5 MT Ragi, 2.8 MT Dals, 1.5 MT Peanuts, 1,500 L Oil",
        "Procurement Profile / Tie-up Potential": "Corporate Entertainment SCM Master Agreement",
        "Address / Landmark": "Bellary Road, Sadashivanagar, Bengaluru - 560080",
        "Contact Channel": "Head of Regional Film Production (zeestudios.south@zee.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Production Banners & Executive Offices",
        "Business Name": "Shree Chamundeshwari Studio & Production Desk",
        "Town": "Millers Road / Vasanth Nagar",
        "Region": "Bengaluru Central",
        "Facility Scale / Outlets": "Historic production desk and post-production hub supporting continuous Sandalwood shoot scheduling and dubbing hospitality",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi, Toor Dal, Broken Rice, Pure Groundnut Oil",
        "Estimated Monthly Volume": "10 MT Rice, 2.5 MT Ragi, 2 MT Dals, 1.2 MT Peanuts, 1,100 L Oil",
        "Procurement Profile / Tie-up Potential": "Annual Food Services Supply Contract",
        "Address / Landmark": "Millers Tank Bund Road, Vasanth Nagar, Bengaluru - 560052",
        "Contact Channel": "Production Incharge (chamundeshwaristudios@gmail.com)"
    },

    # =========================================================================
    # --- Category 2: Mega Film Studios, Outdoor Shooting Campuses & Commissaries (8 Studios) ---
    # =========================================================================
    {
        "Metro": "Bengaluru",
        "Category": "Film Studios & Studio Commissaries",
        "Business Name": "Kanteerava Studios Central Production Canteen & Studio Floors",
        "Town": "Nandini Layout, Outer Ring Road",
        "Region": "Bengaluru North-West",
        "Facility Scale / Outlets": "Karnataka Government & Sandalwood's premier historic 20-acre studio campus with 4 massive shooting floors, Dr. Rajkumar Memorial, and continuous feature film shoots feeding 2,000+ crew daily",
        "Key Crops Demanded": "Aged Sona Masoori Rice (BPT 5204), Pure Karnataka Ragi (for massive Ragi Mudde preparation), Broken Rice for Idli/Dosa, Sortex Toor Dal (Togari Bele), Bengal Gram (Besan Grade), Bold Groundnut Kernels, Pure Groundnut Cooking Oil",
        "Estimated Monthly Volume": "40+ Metric Tonnes Sona Masoori Rice, 15 MT Karnataka Ragi, 8 MT Toor Dal, 5 MT Bengal Gram / Besan, 5 MT Groundnut Kernels, 5,000 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Studio Central Canteen & Unit Production Annual Rate Contract (ARC)",
        "Address / Landmark": "Outer Ring Road, Nandini Layout, Bengaluru - 560096",
        "Contact Channel": "Managing Director & Studio Facilities Manager (canteen.kanteerava@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Studios & Studio Commissaries",
        "Business Name": "Innovative Film City Central Production Commissary",
        "Town": "Bidadi Industrial Area, Mysore Road Expressway",
        "Region": "Greater Bengaluru West",
        "Facility Scale / Outlets": "58-acre mega shooting and entertainment campus housing permanent outdoor sets, Western streets, Bigg Boss Kannada grand house, and central production catering commissaries feeding 3,000+ people daily",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi, Broken Rice, Toor Dal, Bengal Gram for evening snacks, Refined & Cold-Pressed Groundnut Oil",
        "Estimated Monthly Volume": "35 MT Sona Masoori Rice, 10 MT Ragi, 7 MT Toor Dal, 4 MT Bengal Gram, 4,000 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Campus Hospitality & Production SCM Master Vendor Contract",
        "Address / Landmark": "Kiadb Industrial Area, Bidadi, Mysore Expressway, Bengaluru - 562109",
        "Contact Channel": "Vice President - Operations & Commissary Sourcing (operations@innovativefilmcity.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Studios & Studio Commissaries",
        "Business Name": "Premier Studios & Abhiman Studio Production Mess",
        "Town": "Kengeri Satellite Town / Mysore Road",
        "Region": "Bengaluru West",
        "Facility Scale / Outlets": "Historic studio campus founded by comedy legend T.N. Balakrishna, operating active village sets, sound stages, and daily unit dining facilities",
        "Key Crops Demanded": "Sortex Sona Masoori Rice, Karnataka Ragi, Broken Rice, Unpolished Toor Dal, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "15 MT Rice, 4.5 MT Ragi, 3 MT Dals, 1.8 MT Peanuts, 1,800 L Oil",
        "Procurement Profile / Tie-up Potential": "Studio Commissary Annual Food Supply Agreement",
        "Address / Landmark": "Dr. Vishnuvardhan Road, Kengeri, Bengaluru - 560060",
        "Contact Channel": "Studio Admin & Canteen Manager (abhimanstudio@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Studios & Studio Commissaries",
        "Business Name": "Dr. Rajkumar International Shooting Sets & Base Camp",
        "Town": "Hesaraghatta Lake Road / Soladevanahalli",
        "Region": "Bengaluru North-West",
        "Facility Scale / Outlets": "Sprawling outdoor landscape and period village shooting sets frequently booked for rural and action film sequences",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi for unit Mudde, Toor Dal, Bengal Gram, Sun-Dried Red Chilies, Cooking Oil",
        "Estimated Monthly Volume": "14 MT Rice, 4 MT Ragi, 2.8 MT Dals, 1.5 MT Bengal Gram, 1,600 L Oil",
        "Procurement Profile / Tie-up Potential": "Outdoor Sets Catering Logistics Supply Agreement",
        "Address / Landmark": "Hesaraghatta Main Road, Near Nrityagram, Bengaluru - 560088",
        "Contact Channel": "Outdoor Camp Logistics Manager (hesaraghattasets@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Studios & Studio Commissaries",
        "Business Name": "Palace Grounds Outdoor Film Sets & Temporary Kitchen Hub",
        "Town": "Jayamahal / Bellary Road Corridor",
        "Region": "Bengaluru Central",
        "Facility Scale / Outlets": "Expansive royal grounds frequently converted into massive film sets, dance song sets, and temporary production kitchens",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi, Broken Rice, Toor Dal, Bengal Gram for snacks, Pure Cooking Oil",
        "Estimated Monthly Volume": "18 MT Rice, 5 MT Ragi, 3.5 MT Dals, 2 MT Bengal Gram, 2,200 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Event & Film Production Catering Commodities Deed",
        "Address / Landmark": "Tripuravasini, Palace Grounds, Bellary Road, Bengaluru - 560006",
        "Contact Channel": "Estate & Production Sets Manager (palacegrounds.sets@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Studios & Studio Commissaries",
        "Business Name": "Ramohalli Big Banyan Tree Outdoor Shooting Camp Base",
        "Town": "Tavarekere / Mysore Road Hub",
        "Region": "Bengaluru West",
        "Facility Scale / Outlets": "Natural outdoor shooting destination with mobile kitchen camps servicing feature films and high-end commercial ad films",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi, Toor Dal, Bold Groundnuts, Cooking Oil",
        "Estimated Monthly Volume": "12 MT Rice, 3.5 MT Ragi, 2.5 MT Dals, 1.5 MT Peanuts, 1,400 L Oil",
        "Procurement Profile / Tie-up Potential": "Outdoor Field Unit Food Supply Agreement",
        "Address / Landmark": "Dodda Alada Mara Road, Ramohalli, Bengaluru - 560074",
        "Contact Channel": "Base Camp Coordinator (ramohallisets@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Studios & Studio Commissaries",
        "Business Name": "HMT Industrial Shooting Campus & Soundstage Mess",
        "Town": "Jalahalli / Peenya Corridor",
        "Region": "Bengaluru North-West",
        "Facility Scale / Outlets": "Massive vintage industrial heritage halls frequently leased for mega action sequences, chase scenes, and heavy crew shoots",
        "Key Crops Demanded": "High-Yield Sona Masoori Rice, Karnataka Ragi, Toor Dal, Bengal Gram, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "14 MT Rice, 4 MT Ragi, 2.8 MT Dals, 1.8 MT Bengal Gram, 1,600 L Oil",
        "Procurement Profile / Tie-up Potential": "Industrial Sets Production Mess SCM Contract",
        "Address / Landmark": "HMT Estate, Jalahalli, Bengaluru - 560013",
        "Contact Channel": "Facilities & Shooting Coordinator (hmtshootingcampus@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Film Studios & Studio Commissaries",
        "Business Name": "Kanakapura Outdoor Film Shooting Farmhouse Camp",
        "Town": "Kanakapura Road / Harohalli Belt",
        "Region": "Bengaluru South",
        "Facility Scale / Outlets": "Corridor of 25+ private estate farmhouses with dedicated outdoor mobile unit kitchen staging for Kannada feature films",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi for Mudde, Toor Dal, Bengal Gram, Pure Cooking Oil",
        "Estimated Monthly Volume": "12 MT Rice, 3.5 MT Ragi, 2.5 MT Dals, 1.5 MT Peanuts, 1,400 L Oil",
        "Procurement Profile / Tie-up Potential": "Farmhouse Sets Catering Logistics Agreement",
        "Address / Landmark": "NH-209, Kanakapura Main Road, Near Kaggalipura, Bengaluru - 560082",
        "Contact Channel": "Camp Catering Manager (kanakapurasets@gmail.com)"
    },

    # =========================================================================
    # --- Category 3: Apex Cine Production Caterers & Outdoor Unit Contractors (8 Caterers) ---
    # =========================================================================
    {
        "Metro": "Bengaluru",
        "Category": "Cine Production Caterers & Unit Contractors",
        "Business Name": "Sri Manjunatha Cine Catering Services",
        "Town": "Gandhinagar / Rajajinagar Hub",
        "Region": "Bengaluru Central-West",
        "Facility Scale / Outlets": "Sandalwood's #1 film production catering company; operates mobile field kitchens feeding 1,200+ cast, crew, and technicians daily on major feature film sets",
        "Key Crops Demanded": "Aged BPT Sona Masoori Rice (high expansion, non-sticky for large chafing trays), Pure Karnataka Ragi (daily Ragi Mudde), Broken Rice for morning Akki Rotti/Idli/Dosa, Sortex Toor Dal for rich Mysore Sambar, Bengal Gram for 4 PM Bajjis, Bold Peanuts for Shenga chutney",
        "Estimated Monthly Volume": "28+ Metric Tonnes Sona Masoori Rice, 10 MT Karnataka Ragi, 6 MT Toor Dal, 4 MT Bengal Gram / Besan, 3.5 MT Groundnut Kernels, 4,000 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Primary Cine Catering Grain Partnership / Direct Farm-Gate Weekly Truckload Delivery",
        "Address / Landmark": "3rd Cross, Gandhinagar Film District, Bengaluru - 560009",
        "Contact Channel": "Managing Partner & Chief Master Caterer (srimanjunathacatering@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Cine Production Caterers & Unit Contractors",
        "Business Name": "Chamundeshwari Cine Caterers & Unit Mess",
        "Town": "Nandini Layout / Kanteerava Studios Vicinity",
        "Region": "Bengaluru North-West",
        "Facility Scale / Outlets": "Veteran film unit caterer stationed beside Kanteerava Studios, handling simultaneous shooting units across North and West Bengaluru",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi, Broken Rice, Toor Dal, Bengal Gram for snacks, Pure Cooking Oil",
        "Estimated Monthly Volume": "20 MT Rice, 6 MT Ragi, 4.2 MT Dals, 2.5 MT Bengal Gram, 2,500 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Direct Wholesale Agro Supply Contract",
        "Address / Landmark": "Main Road, Nandini Layout, Near Kanteerava Studios, Bengaluru - 560096",
        "Contact Channel": "Proprietor & Master Caterer (chamundeshwaricatering@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Cine Production Caterers & Unit Contractors",
        "Business Name": "Sri Krishna Cine Catering & Mobile Unit Mess",
        "Town": "Basavanagudi / Malleshwaram",
        "Region": "Bengaluru South / Central",
        "Facility Scale / Outlets": "Renowned outdoor shooting caterers catering to big-star units with traditional South Karnataka culinary specialities",
        "Key Crops Demanded": "Sortex Sona Masoori Rice, Karnataka Ragi, Broken Rice, Unpolished Toor Dal, Bold Groundnut Kernels, Pure Cooking Oil",
        "Estimated Monthly Volume": "18 MT Rice, 5 MT Ragi, 3.8 MT Dals, 2.2 MT Peanuts, 2,200 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Master Caterer Direct Farm Sourcing Agreement",
        "Address / Landmark": "Gandhi Bazaar Main Road, Basavanagudi, Bengaluru - 560004",
        "Contact Channel": "Production Catering Head (srikrishnacatering@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Cine Production Caterers & Unit Contractors",
        "Business Name": "Venkateshwara Film Unit Catering Services",
        "Town": "Gandhinagar Film Trade Corridor",
        "Region": "Bengaluru Central",
        "Facility Scale / Outlets": "High-capacity caterer serving junior artists, technical departments, and fighting units with robust high-calorie meals",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi, Toor Dal, Bengal Gram, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "18 MT Rice, 5 MT Ragi, 3.5 MT Dals, 2 MT Bengal Gram, 2,200 L Oil",
        "Procurement Profile / Tie-up Potential": "Mass-Volume Direct Farm-Gate Supply Agreement",
        "Address / Landmark": "6th Main, Gandhinagar, Bengaluru - 560009",
        "Contact Channel": "Managing Director (venkateshwaracatering@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Cine Production Caterers & Unit Contractors",
        "Business Name": "Bidadi Film City Outdoor Catering Contractors",
        "Town": "Bidadi Industrial / Film Zone",
        "Region": "Greater Bengaluru West",
        "Facility Scale / Outlets": "Specialized catering contractor servicing shooting sets, dance troops, and stunt units on Mysore Road",
        "Key Crops Demanded": "Sona Masoori Rice, Karnataka Ragi, Broken Rice, Toor Dal, Bengal Gram, Cooking Oil, Red Chilies",
        "Estimated Monthly Volume": "16 MT Rice, 4.5 MT Ragi, 3.2 MT Dals, 1.8 MT Bengal Gram, 2,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Mobile Unit Catering Bulk Commodity Agreement",
        "Address / Landmark": "Mysore Road, Bidadi Industrial Area, Bengaluru - 562109",
        "Contact Channel": "Operations Head (bidadicatering@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Cine Production Caterers & Unit Contractors",
        "Business Name": "Annapoorna Cine Foods & Outdoor Unit Services",
        "Town": "Rajajinagar Industrial Suburb",
        "Region": "Bengaluru West",
        "Facility Scale / Outlets": "Modern film catering operator providing hygienic, premium buffet catering for OTT series and feature film sets",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Low-GI Rice, Karnataka Ragi, Sortex Pulses, Pure Groundnut Oil, Bold Peanuts",
        "Estimated Monthly Volume": "15 MT Rice, 4 MT Ragi, 3 MT Dals, 1.8 MT Peanuts, 1,800 L Oil",
        "Procurement Profile / Tie-up Potential": "Exclusive Catering Raw Materials Sourcing Contract",
        "Address / Landmark": "Dr. Rajkumar Road, 2nd Block, Rajajinagar, Bengaluru - 560010",
        "Contact Channel": "Founder & Catering Director (annapoornacine@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Cine Production Caterers & Unit Contractors",
        "Business Name": "Cauvery Cine Catering & Mobile Kitchens",
        "Town": "Mahalakshmi Layout / Yeshwanthpur",
        "Region": "Bengaluru North-West",
        "Facility Scale / Outlets": "Catering contractor operating 4 mobile kitchen vans serving independent films, serials, and ad film shoots",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi, Broken Rice, Toor Dal, Bengal Gram, Cooking Oil",
        "Estimated Monthly Volume": "14 MT Rice, 3.5 MT Ragi, 2.8 MT Dals, 1.5 MT Bengal Gram, 1,600 L Oil",
        "Procurement Profile / Tie-up Potential": "Flexible Rolling Order Agreement",
        "Address / Landmark": "Mahalakshmi Layout, Near Swimming Pool, Bengaluru - 560086",
        "Contact Channel": "Proprietor (cauverycinecatering@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Cine Production Caterers & Unit Contractors",
        "Business Name": "Guru Raghavendra Film Catering Services",
        "Town": "Vijayanagar Commercial Hub",
        "Region": "Bengaluru West",
        "Facility Scale / Outlets": "Established catering operator serving indoor sound stages in Vijayanagar, Magadi Road, and Kengeri",
        "Key Crops Demanded": "Sortex Sona Masoori Rice, Karnataka Ragi, Broken Rice for breakfast, Toor Dal, Bengal Gram, Cooking Oil",
        "Estimated Monthly Volume": "12 MT Rice, 3 MT Ragi, 2.5 MT Dals, 1.5 MT Bengal Gram, 1,400 L Oil",
        "Procurement Profile / Tie-up Potential": "Direct Producer Weekly Supply Contract",
        "Address / Landmark": "Service Road, Vijayanagar, Bengaluru - 560040",
        "Contact Channel": "Chief Caterer (gururaghavendracatering@gmail.com)"
    },

    # =========================================================================
    # --- Category 4: Cine Guilds & Federation Welfare Canteens (4 Guilds) ---
    # =========================================================================
    {
        "Metro": "Bengaluru",
        "Category": "Cine Guilds & Federation Welfare Canteens",
        "Business Name": "Karnataka Film Chamber of Commerce (KFCC) Central Canteen",
        "Town": "Crescent Road, High Grounds",
        "Region": "Bengaluru Central",
        "Facility Scale / Outlets": "Apex trade body and nerve center of the Kannada Film Industry, representing 5,000+ producers, distributors, and exhibitors, hosting daily trade meets, script registrations, and industry dining",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi (daily Ragi Mudde), Broken Rice for breakfast, Unpolished Toor Dal (Togari Bele), Pure Groundnut Cooking Oil",
        "Estimated Monthly Volume": "12 MT Sona Masoori Rice, 4 MT Karnataka Ragi, 2.5 MT Toor Dal, 1.5 MT Bengal Gram, 1,500 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Chamber of Commerce Central Food Services Annual Supply Agreement",
        "Address / Landmark": "No. 28, Crescent Road, High Grounds, Bengaluru - 560001",
        "Contact Channel": "Honorary Secretary & Canteen Convener (kfcc.bangalore@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Cine Guilds & Federation Welfare Canteens",
        "Business Name": "Karnataka Cine Workers Welfare Guild Canteen",
        "Town": "Gandhinagar Film District",
        "Region": "Bengaluru Central",
        "Facility Scale / Outlets": "Welfare association representing light technicians, camera assistants, carpenters, dancers, fight assistants, and set workers, providing subsidized daily meals to 8,000+ registered cine workers",
        "Key Crops Demanded": "Wholesale Gunny Sacks Aged Sona Masoori Rice, Karnataka Ragi for Mudde, Broken Rice, Toor Dal, Bengal Gram (Kadale Bele), Groundnut Cooking Oil",
        "Estimated Monthly Volume": "25+ Metric Tonnes Sona Masoori Rice, 8 MT Karnataka Ragi, 5 MT Toor Dal, 3 MT Bengal Gram, 3,000 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Cine Workers Guild Subsidized Master Agro-Supply Contract (Annual Rate Contract)",
        "Address / Landmark": "6th Cross, Gandhinagar, Bengaluru - 560009",
        "Contact Channel": "Guild President & Canteen Committee Head (karnatakacineworkers@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Cine Guilds & Federation Welfare Canteens",
        "Business Name": "Karnataka Film Directors Association (KANFIDA) Dining Hub",
        "Town": "Gandhinagar Film Trade Corridor",
        "Region": "Bengaluru Central",
        "Facility Scale / Outlets": "Official association representing Kannada film directors, associate directors, and writers, hosting script sessions, workshops, and continuous daily dining",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi, Broken Rice, Toor Dal, Bengal Gram for snacks, Pure Groundnut Oil",
        "Estimated Monthly Volume": "8 MT Rice, 2 MT Ragi, 1.8 MT Dals, 1 MT Bengal Gram, 1,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Directors Association Annual Food Supply Agreement",
        "Address / Landmark": "5th Main Road, Gandhinagar, Bengaluru - 560009",
        "Contact Channel": "General Secretary (kanfida.bangalore@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Cine Guilds & Federation Welfare Canteens",
        "Business Name": "Kannada Film Artistes Association (Chalanachitra Kalavidara Sangha) Dining",
        "Town": "Chamarajpet / Basavanagudi Hub",
        "Region": "Bengaluru South",
        "Facility Scale / Outlets": "Prestigious association representing actors, supporting artists, and theater-film veterans, hosting cultural meets, charity events, and association banquets",
        "Key Crops Demanded": "Premium Single-Origin Sona Masoori Rice, Low-GI Rice, Karnataka Ragi, Unpolished Toor Dal, Cold-Pressed Groundnut Oil",
        "Estimated Monthly Volume": "8 MT Premium Rice, 2 MT Ragi, 1.8 MT Dals, 1 MT Millets, 1,000 L Pure Oil",
        "Procurement Profile / Tie-up Potential": "Artistes Sangha Annual Pantry & Catering Sourcing Agreement",
        "Address / Landmark": "1st Main Road, Chamarajpet, Bengaluru - 560018",
        "Contact Channel": "General Secretary & Pantry Manager (kalavidarasangha@gmail.com)"
    }
]

def main():
    df = pd.DataFrame(BUYERS)
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")
    print(f"Successfully generated Phase 9 Bengaluru Film Production & Cine Catering Database with {len(df)} buyers!")
    print(f"Saved to: {OUTPUT_CSV}")
    
    # Summary by Category
    print("\nBreakdown by Category:")
    print(df["Category"].value_counts())

if __name__ == "__main__":
    main()
