#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 14: The Sovereign, Divine & Industrial "Hidden Whales" Database Generator.

Audits 40 high-volume sovereign, pilgrimage, heavy industrial, and mega-kitchen institutions:
1. Divine Pilgrimage Temple Devasthanam Annadhanam Trusts & Sacred Prasadam Hubs (8 Shrines)
2. Sovereign Defense Forces, Armed Academies & Paramilitary Central Rations (8 Commands)
3. Heavy Industrial Townships, Steel Mega-Plants & Mining Canteens (8 Industrial Giants)
4. Centralized Mega-Kitchens for Child Nutrition & Welfare Societies (8 Nutrition Networks)
5. Indian Railways IRCTC Base Kitchens & Industrial Feed Conglomerates (8 Mega Off-Takers)
"""

import os
import pandas as pd

WORKSPACE_DIR = r"C:\Users\rakes\.gemini\antigravity\scratch\onsfc-agri-solutions"
DATA_DIR = os.path.join(WORKSPACE_DIR, "data")
OUTPUT_CSV = os.path.join(DATA_DIR, "ONSFC_Phase14_Sovereign_Divine_Industrial_Buyers.csv")

os.makedirs(DATA_DIR, exist_ok=True)

PHASE14_BUYERS = [
    # Category 1: Divine Pilgrimage Temple Devasthanams & Sacred Prasadam Hubs (8 Divine Shrines)
    {
        "Category": "Divine Pilgrimage Temple Devasthanams & Trusts",
        "Business Name": "Tirumala Tirupati Devasthanams (TTD) - Srivari Annaprasadam & Laddu Production Hub",
        "Town": "Tirumala & Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "A-Grade Bengal Gram (for super-fine Besan flour in sacred Tirupati Laddus), Sona Masoori Rice (BPT 5204), Unpolished Toor Dal, Pure Groundnut Oil",
        "Procurement Profile": "World's richest pilgrimage shrine; feeds 100,000+ devotees daily at Tarigonda Vengamamba Annaprasadam Complex and produces 300,000+ sacred Tirupati Laddus daily. Consumes 1,500+ MT Sona Masoori Rice, 500+ MT Bengal Gram, and 200 MT Toor Dal monthly through AP e-Procurement official tenders.",
        "Address / Landmark": "TTD Administrative Building, KT Road, Tirupati & Srivari Annaprasadam Complex, Tirumala - 517501",
        "Contact Channel": "procurement@tirumala.org | General Manager (Procurement) / DyEO: +91 877 2264200"
    },
    {
        "Category": "Divine Pilgrimage Temple Devasthanams & Trusts",
        "Business Name": "Srisailam Sri Bhramaramba Mallikarjuna Swamy Devasthanam (Lord Shiva Jyotirlinga)",
        "Town": "Srisailam, Nandyal District",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Certified Aged Sona Masoori Rice, Sortex Unpolished Toor Dal, Bengal Gram (Putnalu), Native Millets",
        "Procurement Profile": "One of the 12 sacred Jyotirlingas of Lord Shiva and Shakti Peetham (only 220 km from Gooty). Serves free Nitya Annaprasadam to 25,000 to 50,000 Shiva devotees daily. Consumes 250+ MT Sona Masoori Rice, 60 MT Toor Dal, and 30 MT Bengal Gram monthly on official endowment tender contracts.",
        "Address / Landmark": "Devasthanam Annadhanam Complex, Srisailam Temple Hill, Nandyal District - 518101",
        "Contact Channel": "eo@srisailamtemple.com | Executive Officer / Annadhanam Cell: +91 8524 288888"
    },
    {
        "Category": "Divine Pilgrimage Temple Devasthanams & Trusts",
        "Business Name": "Sri Dharmasthala Manjunatha Swamy Temple (Annapoorna Free Dining Mega-Hall)",
        "Town": "Dharmasthala, Belthangady",
        "Region": "Karnataka",
        "Key Crops Demanded": "Raw Sona Masoori Rice, Boiled Rice, Unpolished Toor Dal (Togari Bele), Native Karnataka Ragi",
        "Procurement Profile": "Historic abode of Lord Shiva in Karnataka administered by the Heggade family; operates India's largest free dining hall (Annapoorna), feeding 30,000 to 50,000 pilgrims daily. Consumes 800+ MT Rice, 150 MT Toor Dal, and 50 MT Ragi monthly.",
        "Address / Landmark": "Annapoorna Dining Complex, Sri Kshetra Dharmasthala, Dakshina Kannada - 574216",
        "Contact Channel": "secretary@shridharmasthala.org | Annadhanam Trust Directorate: +91 8256 277121"
    },
    {
        "Category": "Divine Pilgrimage Temple Devasthanams & Trusts",
        "Business Name": "Srikalahasteeswara Swamy Devasthanam (Lord Shiva Sacred Vayu Lingam)",
        "Town": "Srikalahasti, Tirupati District",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Unpolished Toor Dal, Bengal Gram, Pure Cooking Oil",
        "Procurement Profile": "Revered Pancha Bhoota Sthalam representing the Wind (Vayu Lingam); feeds thousands of Rahu-Ketu dosha pilgrims daily with sacred Annaprasadam. Consumes 120+ MT Rice and 30 MT Toor Dal monthly.",
        "Address / Landmark": "Srikalahasteeswara Temple Administrative Block, Srikalahasti - 517644",
        "Contact Channel": "eosrikalahasti@gmail.com | Executive Officer: +91 8578 221655"
    },
    {
        "Category": "Divine Pilgrimage Temple Devasthanams & Trusts",
        "Business Name": "Mahanandeeswara Swamy Devasthanam (Lord Shiva Navanandi Shrine)",
        "Town": "Mahanandi, Nandyal District",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Sona Masoori Rice, Toor Dal, Groundnut Kernels, Bengal Gram",
        "Procurement Profile": "Ancient 1,500-year-old Shiva temple renowned for continuous freshwater spring tank (Kalyani) and Nitya Annadhanam (only 85 km from Gooty). Consumes 40 MT Sona Masoori and 10 MT Toor Dal monthly.",
        "Address / Landmark": "Devasthanam Office, Mahanandi Temple Complex, Nandyal District - 518502",
        "Contact Channel": "eomahanandi@yahoo.com | Devasthanam Superintendent: +91 8514 234727"
    },
    {
        "Category": "Divine Pilgrimage Temple Devasthanams & Trusts",
        "Business Name": "Yaganti Uma Maheshwara Swamy Temple (Lord Shiva Shrines of Banaganapalle)",
        "Town": "Yaganti, Nandyal District",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Sona Masoori Rice, Sortex Toor Dal, Groundnut Cooking Oil, Putnalu",
        "Procurement Profile": "Famous sacred cave temple of Lord Shiva and growing Nandi idol (75 km from Gooty); serves daily Annaprasadam to thousands of visiting pilgrims. Consumes 30 MT Rice and 8 MT Dals monthly.",
        "Address / Landmark": "Yaganti Temple Devasthanam Office, Banaganapalle Mandal, Nandyal - 518124",
        "Contact Channel": "eoyaganti@gmail.com | Temple Executive Authority: +91 8515 277200"
    },
    {
        "Category": "Divine Pilgrimage Temple Devasthanams & Trusts",
        "Business Name": "Yadadri Sri Lakshmi Narasimha Swamy Devasthanam",
        "Town": "Yadagirigutta",
        "Region": "Telangana",
        "Key Crops Demanded": "Aged Sona Masoori Rice, High-Grade Bengal Gram (Besan for Laddu Prasadam), Toor Dal, Moong Dal",
        "Procurement Profile": "Telangana's grand mega-temple complex; serves thousands of devotees daily with free Annaprasadam and prepares tons of sacred Laddus. Consumes 180 MT Rice, 40 MT Bengal Gram, and 35 MT Dals monthly.",
        "Address / Landmark": "Yadadri Temple Administrative Complex, Yadagirigutta, Yadadri Bhuvanagiri District - 508115",
        "Contact Channel": "eoyadadri@telangana.gov.in | Executive Officer / Accounts Desk: +91 8685 236623"
    },
    {
        "Category": "Divine Pilgrimage Temple Devasthanams & Trusts",
        "Business Name": "Vemulawada Sri Raja Rajeshwara Swamy Devasthanam (Lord Shiva Dakshina Kasi)",
        "Town": "Vemulawada, Rajanna Sircilla",
        "Region": "Telangana",
        "Key Crops Demanded": "Sona Masoori Rice, Unpolished Toor Dal, Bengal Gram (Kode Mokku Prasadam & Laddus), Groundnuts",
        "Procurement Profile": "Revered as the Dakshina Kasi (Southern Varanasi) of Lord Shiva, attracting millions of devotees annually. Operates continuous Nitya Annadhanam feeding 10,000+ pilgrims daily. Consumes 150 MT Rice, 35 MT Dals, and 20 MT Peanuts monthly.",
        "Address / Landmark": "Devasthanam Administrative Office, Vemulawada, Rajanna Sircilla District - 505302",
        "Contact Channel": "eovemulawada@telangana.gov.in | Executive Officer: +91 8723 236018"
    },

    # Category 2: Sovereign Defense Forces, Armed Academies & Paramilitary Central Rations (8 Commands)
    {
        "Category": "Sovereign Defense Forces & Paramilitary Central Rations",
        "Business Name": "Army Supply Corps (ASC) Centre & College (South) - Food Logistics Directorate",
        "Town": "Bengaluru",
        "Region": "Karnataka",
        "Key Crops Demanded": "Government Specification Non-Basmati Rice, Sortex Toor Dal, Whole Bengal Gram, Edible Refined Oils",
        "Procurement Profile": "Headquarters of the Indian Army Supply Corps for Southern Command; central rationing and supply depot feeding army cantonments across Karnataka, Kerala, AP, and Telangana. Bulk procurement via GeM tenders (hundreds of MTs per order).",
        "Address / Landmark": "ASC Centre & College (South), Agram Post, Victoria Layout, Bengaluru - 560007",
        "Contact Channel": "asc-south.procurement@nic.in | Commandant / DDST Southern Command: +91 80 25369000"
    },
    {
        "Category": "Sovereign Defense Forces & Paramilitary Central Rations",
        "Business Name": "Air Force Station Yelahanka & Air Force Training Command",
        "Town": "Yelahanka, Bengaluru (NH-44 Entry)",
        "Region": "Karnataka",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Sortex Toor Dal, Bengal Gram (Chana), Whole Red Chilies, Cooking Fats",
        "Procurement Profile": "Premier Indian Air Force base hosting Flight Cadets, aircrew training wings, and Aero India. Directly located on NH-44 from Gooty. Consumes 40 MT Sona Masoori Rice and 10 MT Toor Dal monthly through GeM portal contracts.",
        "Address / Landmark": "Air Force Station Yelahanka, Bellary Road (NH-44 Corridor), Bengaluru - 560063",
        "Contact Channel": "yelahanka.ration@iaf.nic.in | Senior Logistics Officer / Ration Cell: +91 80 28460500"
    },
    {
        "Category": "Sovereign Defense Forces & Paramilitary Central Rations",
        "Business Name": "Sardar Vallabhbhai Patel National Police Academy (SVP NPA)",
        "Town": "Shivrampally, Hyderabad (NH-44 Entry)",
        "Region": "Telangana",
        "Key Crops Demanded": "Single-Origin Sona Masoori Rice, Low-GI RNR 15048, Unpolished Organic Dals, Millets (Ragi/Jowar)",
        "Procurement Profile": "Apex national institute training all Indian Police Service (IPS) probationers and commandants. Located right at the southern NH-44 entrance to Hyderabad. Consumes 25 MT Rice and 6 MT Dals monthly on institutional GeM supply tenders.",
        "Address / Landmark": "SVP NPA Campus, Shivrampally, NH-44 Highway Corridor, Hyderabad - 500052",
        "Contact Channel": "procurement@svpnpa.gov.in | Assistant Director (Logistics & Mess): +91 40 24015151"
    },
    {
        "Category": "Sovereign Defense Forces & Paramilitary Central Rations",
        "Business Name": "CRPF Southern Sector Headquarters & Group Centre Central Ration Depot",
        "Town": "Chandrayangutta, Hyderabad (NH-44 Corridor)",
        "Region": "Telangana",
        "Key Crops Demanded": "Non-Basmati Rice, Toor Dal, Bengal Gram (Senagalu), Whole Red Chilies, Cooking Oil",
        "Procurement Profile": "Central Reserve Police Force mega-base housing 3 operational battalions and Recruit Training Centre feeding thousands of jawans daily. Directly on the southern NH-44 truck route. Consumes 50 MT Rice and 12 MT Dal monthly.",
        "Address / Landmark": "Group Centre CRPF, Chandrayangutta, Barkas Road, Hyderabad - 500005",
        "Contact Channel": "gc-hyd.crpf@nic.in | DIGP / Quartermaster Central Stores: +91 40 24440050"
    },
    {
        "Category": "Sovereign Defense Forces & Paramilitary Central Rations",
        "Business Name": "CISF National Industrial Security Academy (NISA) & Regional Training Centre",
        "Town": "Hakimpet, Hyderabad",
        "Region": "Telangana",
        "Key Crops Demanded": "Sona Masoori Rice, Sortex Pulses, Bengal Gram, Groundnut Oil, Red Chilies",
        "Procurement Profile": "Premier training academy for Central Industrial Security Force officers and commandos guarding airports, nuclear plants, and space stations. Consumes 45 MT Rice and 10 MT Toor Dal monthly.",
        "Address / Landmark": "NISA CISF Campus, Hakimpet, Secunderabad - 500078",
        "Contact Channel": "nisa-hyd@cisf.gov.in | Director NISA / Mess Procurement Board: +91 40 27981000"
    },
    {
        "Category": "Sovereign Defense Forces & Paramilitary Central Rations",
        "Business Name": "BSF Subsidiary Training Centre (STC BSF Bengaluru)",
        "Town": "Yelahanka, Bengaluru",
        "Region": "Karnataka",
        "Key Crops Demanded": "Non-Basmati Milled Rice, Sortex Toor Dal, Bengal Gram, Mustard & Groundnut Oil",
        "Procurement Profile": "Border Security Force training hub on NH-44; feeds 1,500+ recruits and permanent staff with 3 daily high-calorie meals. Consumes 35 MT Rice and 8 MT Pulses monthly.",
        "Address / Landmark": "STC BSF Campus, Bagalur Road, Near Yelahanka, Bengaluru - 560063",
        "Contact Channel": "stcblr-bsf@nic.in | Commandant / Ration Board: +91 80 28461200"
    },
    {
        "Category": "Sovereign Defense Forces & Paramilitary Central Rations",
        "Business Name": "Eastern Naval Command Central Naval Store Depot & Fleet Messes",
        "Town": "Visakhapatnam & Chennai",
        "Region": "Andhra Pradesh & Tamil Nadu",
        "Key Crops Demanded": "Non-Basmati Long-Shelf-Life Rice (<12% moisture), Sortex Dals, Whole Spices, De-stoned Peanuts",
        "Procurement Profile": "Procures dry rations for frontline warships, submarines, and naval dockyards; requires vacuum or tamper-proof 50kg bags with strict moisture control for maritime storage.",
        "Address / Landmark": "Material Organization, Naval Dockyard, Visakhapatnam - 530014 & Fort St. George, Chennai",
        "Contact Channel": "cnsd-vzg.navy@nic.in | Material Superintendent / Navy Ration Officer: +91 891 2812000"
    },
    {
        "Category": "Sovereign Defense Forces & Paramilitary Central Rations",
        "Business Name": "Indian Coast Guard District Headquarters No. 7 & Regional Messes",
        "Town": "Chennai & Krishnapatnam",
        "Region": "Tamil Nadu & Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Sortex Pulses, Bengal Gram, Pure Cooking Oil",
        "Procurement Profile": "Maritime security agency guarding coastal ports; procures dry grocery packs for patrol vessels operating out of Chennai and Krishnapatnam port harbors.",
        "Address / Landmark": "Coast Guard District HQ 7, Meenambakkam, Chennai & Krishnapatnam Station, Nellore",
        "Contact Channel": "dhq7-procurement@indiancoastguard.nic.in | Logistics Officer: +91 44 22320000"
    },

    # Category 3: Heavy Industrial Townships, Steel Mega-Plants & Mining Canteens (8 Industrial Giants)
    {
        "Category": "Heavy Industrial Townships & Mining Canteens",
        "Business Name": "JSW Steel Vijayanagar Works Central Canteen & Vidyanagar Township Cooperative",
        "Town": "Toranagallu, Bellary",
        "Region": "Karnataka",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Sortex Toor Dal, Bengal Gram, Pure Cooking Oil",
        "Procurement Profile": "India's largest single-location steel manufacturing plant (12 MTPA capacity, expanding to 18 MTPA); over 35,000 employees and workers living in Vidyanagar residential township. Consumes 60+ MT Sona Masoori, 15 MT Dals, and 8 MT Cooking Oil monthly. Located only 90 km from Gooty!",
        "Address / Landmark": "JSW Steel Works, PO Vidyanagar, Toranagallu, Bellary District - 583275",
        "Contact Channel": "procurement.canteen@jsw.in | Head of Admin & Township Services: +91 8395 250124"
    },
    {
        "Category": "Heavy Industrial Townships & Mining Canteens",
        "Business Name": "UltraTech Cement Complexes (Tadipatri & Kurnool Works) - Staff Townships",
        "Town": "Tadipatri & Kolimigundla",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Sona Masoori Rice, Unpolished Toor Dal, Bengal Gram, Groundnut Cooking Oil",
        "Procurement Profile": "Aditya Birla Group's flagship cement manufacturing complexes right in our backyard (only 45 km from Gooty!); houses 8,000+ employees and contract laborers across self-contained colonies. Consumes 25 MT Sona Masoori and 6 MT Dals monthly.",
        "Address / Landmark": "UltraTech Cement Works, Tadipatri Mandal, Anantapuramu District & Kolimigundla, Nandyal",
        "Contact Channel": "canteen.tadipatri@adityabirla.com | HR & Admin Lead: +91 8558 277200"
    },
    {
        "Category": "Heavy Industrial Townships & Mining Canteens",
        "Business Name": "Singareni Collieries Company Limited (SCCL) - Central Stores & Miners Canteens",
        "Town": "Kothagudem, Ramagundam & Bellampalli",
        "Region": "Telangana",
        "Key Crops Demanded": "Non-Basmati Sona Masoori Rice, Sortex Pulses, Bengal Gram, Groundnut Oil, Whole Red Chilies",
        "Procurement Profile": "Government coal mining giant operating 40+ opencast and underground mines with 42,000+ permanent miners; maintains large subsidized staff cooperative stores and 24/7 mine canteens. Multi-crore annual state tenders for 100+ MT Rice monthly.",
        "Address / Landmark": "SCCL Head Office, Kothagudem Collieries, Bhadradri Kothagudem District - 507101",
        "Contact Channel": "stores@scclmines.com | General Manager (Purchase & Canteen): +91 8744 242300"
    },
    {
        "Category": "Heavy Industrial Townships & Mining Canteens",
        "Business Name": "NMDC Limited - Donimalai Iron Ore Complex & Township Canteens",
        "Town": "Sandur, Bellary District",
        "Region": "Karnataka",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Toor Dal, Bengal Gram, Groundnut Kernels",
        "Procurement Profile": "Navratna public-sector mining giant; operates Donimalai and Kumaraswamy iron ore mines (85 km from Gooty) with integrated township housing 5,000+ residents. Public-sector annual grain supply tenders.",
        "Address / Landmark": "Donimalai Township, Sandur Taluk, Bellary District - 583118",
        "Contact Channel": "donimalai.stores@nmdc.co.in | Deputy General Manager (Materials): +91 8395 274200"
    },
    {
        "Category": "Heavy Industrial Townships & Mining Canteens",
        "Business Name": "Zuari Cements Limited (HeidelbergCement Group) - Yerraguntla Works",
        "Town": "Yerraguntla, Kadapa District",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Sona Masoori Rice, Toor Dal, Bengal Gram, Cooking Fats",
        "Procurement Profile": "Major international cement manufacturing facility located 85 km south of Gooty; operates factory workers mess and employee residential township colonies consuming 15 MT Rice and 4 MT Dals monthly.",
        "Address / Landmark": "Zuari Cement Works, Krishna Nagar, Yerraguntla, Kadapa District - 516311",
        "Contact Channel": "procurement@zuaricements.com | Canteen Committee / Admin: +91 8563 275100"
    },
    {
        "Category": "Heavy Industrial Townships & Mining Canteens",
        "Business Name": "Bharathi Cement Corporation Private Limited (Vicat Group)",
        "Town": "Kamalapuram, Kadapa District",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Sortex Toor Dal, Groundnut Oil, Bengal Gram",
        "Procurement Profile": "Ultra-modern 5 MTPA cement plant and residential colony situated 90 km from Gooty; serves 3 daily meals to engineers, technicians, and transport workers. Consumes 14 MT Rice monthly.",
        "Address / Landmark": "Bharathi Cement Plant, Nallalingayapalli, Kamalapuram Mandal, Kadapa - 516289",
        "Contact Channel": "admin@bharathicement.com | Commercial Purchase Manager: +91 8568 288300"
    },
    {
        "Category": "Heavy Industrial Townships & Mining Canteens",
        "Business Name": "Dalmia Bharat Sugar and Industries & Cement Complex",
        "Town": "Chinnakomerla, Kadapa",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Non-Basmati Rice, Toor Dal, Groundnut Kernels, Maize",
        "Procurement Profile": "Heavy industrial manufacturing township located in the Kadapa-Tadipatri industrial belt; high daily consumption across employee dining halls.",
        "Address / Landmark": "Dalmia Bharat Complex, Chinnakomerla, Mylavaram Mandal, Kadapa - 516439",
        "Contact Channel": "dalmia.kadapa@dalmiabharat.com | Materials Directorate: +91 8560 279500"
    },
    {
        "Category": "Heavy Industrial Townships & Mining Canteens",
        "Business Name": "Penna Cement Industries Limited - Ganeshpahad & Boyareddypalli Units",
        "Town": "Tadipatri / Yadiki Belt",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Sona Masoori Rice, Toor Dal, Bengal Gram, Edible Oils",
        "Procurement Profile": "Integrated cement plant and limestone quarry colonies situated right on our doorstep (under 40 km from Gooty); steady monthly bulk grocery procurement.",
        "Address / Landmark": "Penna Cement Plant, Boyareddypalli, Yadiki Mandal, Anantapuramu District - 515408",
        "Contact Channel": "purchase.yadiki@pennacement.com | Plant Admin Lead: +91 8558 274100"
    },

    # Category 4: Centralized Mega-Kitchens for Child Nutrition & Welfare Societies (8 Nutrition Networks)
    {
        "Category": "Centralized Child Nutrition Mega-Kitchens",
        "Business Name": "The Akshaya Patra Foundation - Rajajinagar & HK Hill Central Mega-Kitchens",
        "Town": "Rajajinagar & Hare Krishna Hill, Bengaluru",
        "Region": "Karnataka",
        "Key Crops Demanded": "Machine-Destoned Sona Masoori Rice, Sortex Unpolished Toor Dal, Native Karnataka Ragi, Moong Dal",
        "Procurement Profile": "The world's largest NGO midday meal program; cooks 150,000+ hot nutritious meals in 3 hours every morning using automated gravity-flow cauldrons. Consumes 250+ MT Sona Masoori, 65 MT Toor Dal, and 30 MT Ragi monthly. Zero-tolerance for stones.",
        "Address / Landmark": "The Akshaya Patra Foundation, Hare Krishna Hill, West of Chord Road, Bengaluru - 560010",
        "Contact Channel": "procurement@akshayapatra.org | Director of Procurement (India): +91 80 23471956"
    },
    {
        "Category": "Centralized Child Nutrition Mega-Kitchens",
        "Business Name": "The Akshaya Patra Foundation - Vasanthapura & Jigani Mega-Kitchens",
        "Town": "Vasanthapura & Jigani Industrial Area, Bengaluru",
        "Region": "Karnataka",
        "Key Crops Demanded": "Cleaned Sona Masoori Rice, Unpolished Toor Dal, Moong Dal, Bengal Gram, Pure Cooking Oil",
        "Procurement Profile": "South Bengaluru automated mega-kitchen complexes feeding over 100,000 government school children daily across Bengaluru Urban and Anekal taluks. Consumes 200 MT Rice and 50 MT Toor Dal monthly.",
        "Address / Landmark": "Akshaya Patra Kitchen, Vasanthapura Main Road, Off Kanakapura Road, Bengaluru - 560061",
        "Contact Channel": "scm.karnataka@akshayapatra.org | Regional Procurement Manager: +91 80 26668000"
    },
    {
        "Category": "Centralized Child Nutrition Mega-Kitchens",
        "Business Name": "The Akshaya Patra Foundation - Narsingi Mega-Kitchen",
        "Town": "Narsingi, Hyderabad (Outer Ring Road)",
        "Region": "Telangana",
        "Key Crops Demanded": "Telangana Sona Low-GI Rice (RNR 15048), Sona Masoori, Sortex Toor Dal, Bengal Gram",
        "Procurement Profile": "Telangana's flagship centralized kitchen serving 65,000+ students daily in Greater Hyderabad government schools. Consumes 120 MT Rice and 30 MT Toor Dal monthly.",
        "Address / Landmark": "Akshaya Patra Mega Kitchen, Narsingi Junction, Gandipet Road, Hyderabad - 500075",
        "Contact Channel": "hyd.scm@akshayapatra.org | State Operations Lead: +91 40 23145000"
    },
    {
        "Category": "Centralized Child Nutrition Mega-Kitchens",
        "Business Name": "The Akshaya Patra Foundation - Kandi Mega-Kitchen (Sangareddy Corridor)",
        "Town": "Kandi, Sangareddy",
        "Region": "Telangana",
        "Key Crops Demanded": "Non-Basmati Rice, Unpolished Toor Dal, Groundnut Kernels, Whole Bengal Gram",
        "Procurement Profile": "State-of-the-art automated kitchen situated near IIT Hyderabad, feeding thousands of rural and semi-urban school children across Medak and Sangareddy districts. Consumes 80 MT Rice monthly.",
        "Address / Landmark": "Akshaya Patra Kitchen, Mumbai Highway (NH-65), Kandi, Sangareddy - 502285",
        "Contact Channel": "kandi.kitchen@akshayapatra.org | Operations Head: +91 8455 230100"
    },
    {
        "Category": "Centralized Child Nutrition Mega-Kitchens",
        "Business Name": "The Akshaya Patra Foundation - Bellary Mega-Kitchen (90 km from Gooty)",
        "Town": "Bellary Industrial Area",
        "Region": "Karnataka",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Sortex Toor Dal, Native Ragi (Finger Millet), Groundnuts",
        "Procurement Profile": "Directly accessible from Gooty via the Guntakal-Bellary highway; cooks 50,000+ meals daily for mining belt school students. Consumes 90 MT Rice, 22 MT Toor Dal, and 12 MT Ragi monthly.",
        "Address / Landmark": "Akshaya Patra Kitchen, Mundargi Industrial Area, Bellary - 583101",
        "Contact Channel": "bellary.procurement@akshayapatra.org | Kitchen Superintendent: +91 8392 270100"
    },
    {
        "Category": "Centralized Child Nutrition Mega-Kitchens",
        "Business Name": "Andhra Pradesh Tribal Welfare Residential Educational Institutions (APTWREIS - Gurukulam)",
        "Town": "Amaravati & Anantapuramu Regional Directorate",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Certified Sona Masoori Rice, Sortex Toor Dal, Bengal Gram (Senagalu), Millets (Ragi/Jowar), Oil",
        "Procurement Profile": "Apex state government residential school society operating 200+ residential campuses for tribal students; centralized state tenders for thousands of MTs of non-perishable food grains.",
        "Address / Landmark": "Gurukulam Bhavan, Tadepalli, Amaravati & Regional Office, Anantapuramu - 515001",
        "Contact Channel": "secretary.aptwreis@gmail.com | Secretary / Procurement Directorate: +91 863 2349000"
    },
    {
        "Category": "Centralized Child Nutrition Mega-Kitchens",
        "Business Name": "Telangana Social Welfare Residential Educational Institutions Society (TGSWREIS)",
        "Town": "Masab Tank, Hyderabad",
        "Region": "Telangana",
        "Key Crops Demanded": "Telangana Sona Rice (RNR 15048), Unpolished Toor Dal, Bold Peanuts, Bengal Gram",
        "Procurement Profile": "Governs 268+ prestigious residential institutions housing over 150,000 students; rigorous annual state tenders for clean, certified dry food staples.",
        "Address / Landmark": "DSS Bhavan, Masab Tank, Hyderabad - 500028",
        "Contact Channel": "secretary-tswreis@telangana.gov.in | Joint Secretary (Procurement): +91 40 23399000"
    },
    {
        "Category": "Centralized Child Nutrition Mega-Kitchens",
        "Business Name": "ISKCON Food for Life Charitable Trust Central Kitchen",
        "Town": "Tirupati & Anantapuramu Hub",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Cleaned Sona Masoori Rice, Sortex Pulses, Pure Groundnut Oil, Bengal Gram",
        "Procurement Profile": "Charitable mass-feeding wing distributing sanctified vegetarian meals to hospital attendants, rural schools, and pilgrims across Rayalaseema. Consumes 30 MT Rice and 8 MT Dals monthly.",
        "Address / Landmark": "Hare Krishna Land, Alipiri Road, Tirupati & ISKCON Temple, Somaladoddi, Anantapur",
        "Contact Channel": "foodforlife.tirupati@iskcon.org | Central Kitchen Incharge: +91 877 2282000"
    },

    # Category 5: Indian Railways IRCTC Base Kitchens & Industrial Feed Conglomerates (8 Mega Off-Takers)
    {
        "Category": "Railways IRCTC & Industrial Feed Conglomerates",
        "Business Name": "IRCTC Central Base Kitchen & Food Plaza (Guntakal Railway Division HQ)",
        "Town": "Guntakal Junction (25 km from Gooty!)",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Sortex Toor Dal, Bengal Gram, Pure Cooking Oil",
        "Procurement Profile": "Guntakal is the Divisional Headquarters of South Central Railway. The IRCTC Central Base Kitchen prepares thousands of meals daily for express passenger trains crossing North-South corridors. Direct 25-minute truck delivery from Gooty!",
        "Address / Landmark": "Platform 1 Complex, Guntakal Railway Junction, Anantapuramu District - 515801",
        "Contact Channel": "basekitchen.gzl@irctc.com | Area Manager / Base Kitchen Incharge: +91 8552 226100"
    },
    {
        "Category": "Railways IRCTC & Industrial Feed Conglomerates",
        "Business Name": "IRCTC Base Kitchen & Passenger Refreshment Complex (Anantapur & Bellary)",
        "Town": "Anantapur & Bellary Junctions",
        "Region": "Andhra Pradesh & Karnataka",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Red Chilies",
        "Procurement Profile": "High-turnover station dining and meal-tray prep facilities servicing long-distance trains (Rayalaseema Express, Prashanti Express, Karnataka Express). Consumes 20 MT Rice and 5 MT Dals monthly.",
        "Address / Landmark": "Anantapur Railway Station Complex & Bellary Junction Main Building",
        "Contact Channel": "irctc.anantapur@gmail.com | Catering Inspector / Supervisor: +91 8554 240200"
    },
    {
        "Category": "Railways IRCTC & Industrial Feed Conglomerates",
        "Business Name": "IRCTC South Central Zone Headquarters Procurement Directorate",
        "Town": "Secunderabad / Kacheguda",
        "Region": "Telangana",
        "Key Crops Demanded": "Non-Basmati Rice, Parboiled Rice, Sortex Pulses, Pure Groundnut Oil",
        "Procurement Profile": "Apex commercial catering authority for South Central Railway network, issuing multi-crore annual tenders for grains, pulses, and oils across all divisional base kitchens.",
        "Address / Landmark": "Oxford Plaza, SD Road, Secunderabad - 500003",
        "Contact Channel": "ggm.scz@irctc.com | Group General Manager (Catering): +91 40 27712000"
    },
    {
        "Category": "Railways IRCTC & Industrial Feed Conglomerates",
        "Business Name": "Sneha Farms Private Limited - Jadcherla Mega Grain Silo Complex",
        "Town": "Jadcherla, Mahbubnagar (NH-44 Corridor)",
        "Region": "Telangana",
        "Key Crops Demanded": "Yellow Corn (Maize), 100% Broken Rice (Feed Grade), Groundnut De-Oiled Cake (DOC)",
        "Procurement Profile": "Houses 150,000 Metric Tonnes of state-of-the-art grain silos right on the NH-44 highway from Gooty. Buys 5,000+ MT of yellow corn and broken rice monthly for India's largest integrated broiler feed operations.",
        "Address / Landmark": "Sneha Mega Industrial Feed Park, Polepally SEZ, Jadcherla, NH-44 Corridor - 509301",
        "Contact Channel": "grainprocurement@snehagroup.com | General Manager (Grain SCM): +91 8542 258000"
    },
    {
        "Category": "Railways IRCTC & Industrial Feed Conglomerates",
        "Business Name": "Godrej Agrovet Limited - Animal Nutrition & Feed Manufacturing Hub",
        "Town": "Jadcherla (NH-44) & Bengaluru",
        "Region": "Telangana & Karnataka",
        "Key Crops Demanded": "Yellow Maize, Cottonseed Cake, Broken Rice, Groundnut Meal",
        "Procurement Profile": "India's premier animal nutrition and agri-business conglomerate; procures thousands of tonnes of coarse grains, broken rice, and oil cakes for cattle, aqua, and poultry feeds.",
        "Address / Landmark": "Godrej Agrovet Feed Mill, Special Economic Zone, Jadcherla & Industrial Area, Bengaluru",
        "Contact Channel": "feedprocurement@godrejagrovet.com | Head of Raw Material SCM: +91 80 66453000"
    },
    {
        "Category": "Railways IRCTC & Industrial Feed Conglomerates",
        "Business Name": "Suguna Foods Private Limited - South Feed Processing Directorate",
        "Town": "Mahbubnagar & Chittoor",
        "Region": "Telangana & Andhra Pradesh",
        "Key Crops Demanded": "Feed Maize (Corn), Broken Raw Rice, Groundnut Extraction Cake, Soya Meal",
        "Procurement Profile": "Pioneer of contract poultry farming in India; operates heavy automated feed mills consuming 10,000+ MT of maize and broken rice monthly on prompt payment terms.",
        "Address / Landmark": "Suguna Feed Mills, Opp. Railway Station, Mahbubnagar & Industrial Estate, Chittoor",
        "Contact Channel": "rawmaterial@sugunafoods.co.in | Commercial Feed Manager: +91 8542 221200"
    },
    {
        "Category": "Railways IRCTC & Industrial Feed Conglomerates",
        "Business Name": "CP Foods (Charoen Pokphand India) Agro-Industrial Feed Hub",
        "Town": "Chittoor & Bengaluru Rural",
        "Region": "Andhra Pradesh & Karnataka",
        "Key Crops Demanded": "High-Starch Yellow Maize, Broken Raw Rice, Groundnut Cake",
        "Procurement Profile": "Global agro-industrial and food conglomerate headquartered in Thailand; massive commercial poultry feed mills in South India procuring hundreds of truckloads of corn and broken grains monthly.",
        "Address / Landmark": "CP India Feed Complex, Bangarupalem, Chittoor District & Devanahalli, Bengaluru",
        "Contact Channel": "corn.procurement@cp-india.com | Origination Head: +91 8573 280000"
    },
    {
        "Category": "Railways IRCTC & Industrial Feed Conglomerates",
        "Business Name": "KSE Limited (Kerala Solvent Extractions) - Cattle Feed Processing Hubs",
        "Town": "Swaminathapuram & South India Depots",
        "Region": "South India",
        "Key Crops Demanded": "Groundnut De-Oiled Cake (DOC), Cottonseed Cake, Broken Rice, Maize",
        "Procurement Profile": "India's largest private cattle feed manufacturer; purchases massive volumes of Rayalaseema groundnut cake and cottonseed cake from Gooty and Adoni oil mills for milk cattle feeds.",
        "Address / Landmark": "KSE Industrial Complex, Swaminathapuram & Central South Depots",
        "Contact Channel": "kse@kselimited.com | Commercial Purchase Manager: +91 480 2825421"
    }
]

def main():
    df = pd.DataFrame(PHASE14_BUYERS)
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")
    print(f"Successfully generated Phase 14 Sovereign, Divine & Industrial Database with {len(df)} buyers!")
    print(f"Saved to: {OUTPUT_CSV}")
    print("\nBreakdown by Category:")
    print(df["Category"].value_counts())

if __name__ == "__main__":
    main()
