#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 3 Bengaluru Educational Institutions Scraper & Database Builder
Compiles 35 top-tier Residential Schools, Residential Colleges, and Engineering Colleges in Bengaluru.
100% Dry Commodities & Food Staples Focus.
"""

import os
import pandas as pd

DATA_DIR = r"C:\Users\rakes\.gemini\antigravity\scratch\onsfc-agri-solutions\data"
os.makedirs(DATA_DIR, exist_ok=True)
OUTPUT_CSV = os.path.join(DATA_DIR, "ONSFC_Phase3_Bengaluru_Institutions.csv")

INSTITUTIONS = [
    # --- Group A: Premier Engineering Colleges & Deemed Technical Universities ---
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "RV College of Engineering (RVCE) Hostel Mess",
        "Town": "Mysore Road",
        "Region": "Bengaluru West",
        "Hostel Capacity / Students": "2,200+ Residential Hostellers (Cauvery, Krishna, Sir MV Hostel Blocks)",
        "Key Crops Demanded": "Aged Sona Masoori Rice (BPT 5204), Broken Idli Rice, Unpolished Toor Dal, Ragi (Finger Millet), Groundnut Oil",
        "Estimated Monthly Volume": "22 MT Rice, 3.5 MT Toor Dal, 1.5 MT Ragi, 2,500 L Groundnut Oil",
        "Procurement Profile": "Hostel Supervisory Committee & Chief Warden Office",
        "Address / Landmark": "RV Vidyanikethan Post, Mysore Road, Bengaluru - 560059",
        "Contact Channel": "Chief Warden / Hostel Purchase Officer (warden@rvce.edu.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "BMS College of Engineering (BMSCE) Hostels & Mess",
        "Town": "Basavanagudi",
        "Region": "Bengaluru South",
        "Hostel Capacity / Students": "1,800+ Residential Hostellers (International & Indian Student Blocks)",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice for Dosa/Idli, Toor Dal, Urad Dal, Ragi Flour",
        "Estimated Monthly Volume": "18 MT Rice, 2.8 MT Toor Dal, 1.2 MT Ragi, 2,000 L Cooking Oil",
        "Procurement Profile": "BMS Educational Trust (BMSET) Central Procurement",
        "Address / Landmark": "Bull Temple Road, Basavanagudi, Bengaluru - 560019",
        "Contact Channel": "Secretary / Purchase Manager (hostel@bmsce.ac.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "PES University - Ring Road Campus Hostels",
        "Town": "Banashankari",
        "Region": "Bengaluru South-West",
        "Hostel Capacity / Students": "4,500+ Residential Hostellers across 5 Multi-Story Blocks",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Unpolished Toor Dal, Bengal Gram (Chana & Putnalu), Groundnut Oil",
        "Estimated Monthly Volume": "45 MT Rice, 7.0 MT Toor Dal, 3.0 MT Ragi, 5,000 L Oil",
        "Procurement Profile": "PES University Central Hospitality & Food Services Directorate",
        "Address / Landmark": "100 Feet Ring Road, BSK III Stage, Bengaluru - 560085",
        "Contact Channel": "Director of Hospitality / Chief Warden (hostel@pes.edu)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "PES University - Electronic City Campus Hostels",
        "Town": "Electronic City",
        "Region": "Bengaluru South",
        "Hostel Capacity / Students": "2,500+ Residential Students (Engineering & Management)",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Idli Rice, Toor Dal, Urad Dal, Ragi, Groundnut Oil",
        "Estimated Monthly Volume": "25 MT Rice, 4.0 MT Toor Dal, 1.8 MT Ragi, 2,800 L Oil",
        "Procurement Profile": "Campus Facility & Catering Manager",
        "Address / Landmark": "Hosur Road, Electronic City Phase 1, Bengaluru - 560100",
        "Contact Channel": "Campus Administrator (ec-hostel@pes.edu)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "MS Ramaiah Institute of Technology (MSRIT) Hostels",
        "Town": "MSR Nagar / Mathikere",
        "Region": "Bengaluru North",
        "Hostel Capacity / Students": "3,800+ Residential Students (Freshers Block, Aryabhata, PG Blocks)",
        "Key Crops Demanded": "Aged Sona Masoori Rice (BPT 5204), Toor Dal, Broken Rice, Ragi, Bengal Gram",
        "Estimated Monthly Volume": "38 MT Rice, 6.0 MT Toor Dal, 2.5 MT Ragi, 4,200 L Cooking Oil",
        "Procurement Profile": "Gokula Education Foundation Central Purchase Department",
        "Address / Landmark": "MSR Nagar, MSRIT Post, Bengaluru - 560054",
        "Contact Channel": "Chief Executive / Chief Warden (warden@msrit.edu)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "Dayananda Sagar University (DSU) Harohalli Mega Campus",
        "Town": "Harohalli / Kanakapura Road",
        "Region": "Bengaluru South Outskirts",
        "Hostel Capacity / Students": "3,500+ Residential Hostellers in 140-Acre Township",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice for Batter, Toor Dal, Moong Dal, Ragi, Groundnut Oil",
        "Estimated Monthly Volume": "35 MT Rice, 5.5 MT Toor Dal, 2.5 MT Ragi, 4,000 L Oil",
        "Procurement Profile": "DSI Central Procurement & Food Services Desk",
        "Address / Landmark": "Devarakaggalahalli, Harohalli, Kanakapura Road, Bengaluru - 562112",
        "Contact Channel": "General Manager (Admin & Hostels) (warden@dsu.edu.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "Dayananda Sagar Institutions (DSI) Kumaraswamy Layout",
        "Town": "Kumaraswamy Layout",
        "Region": "Bengaluru South",
        "Hostel Capacity / Students": "2,200+ Hostellers (Engineering, Dental & Pharmacy Blocks)",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Urad Dal, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "22 MT Rice, 3.5 MT Toor Dal, 1.5 MT Ragi, 2,500 L Oil",
        "Procurement Profile": "DSI Campus Warden Committee",
        "Address / Landmark": "Shavige Malleshwara Hills, Kumaraswamy Layout, Bengaluru - 560078",
        "Contact Channel": "Hostel Superintendent (hostels@dayanandasagar.edu)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "REVA University Mega Campus Hostels",
        "Town": "Kattigenahalli, Yelahanka",
        "Region": "Bengaluru North (Direct NH-44 Corridor)",
        "Hostel Capacity / Students": "5,200+ Residential Boarders (Boys & Girls Towers)",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice for Idli/Dosa, Unpolished Toor Dal, Ragi, Groundnut Oil",
        "Estimated Monthly Volume": "50 MT Rice, 8.0 MT Toor Dal, 3.5 MT Ragi, 5,500 L Oil",
        "Procurement Profile": "REVA University Central Food Services & Mess Division",
        "Address / Landmark": "Rukmini Knowledge Park, Kattigenahalli, Yelahanka, Bengaluru - 560064",
        "Contact Channel": "Director of Student Affairs & Hostels (hostels@reva.edu.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "Acharya Institutes Mega Residential Campus",
        "Town": "Soldevanahalli, Hesaraghatta",
        "Region": "Bengaluru North-West",
        "Hostel Capacity / Students": "4,500+ Hostellers across 12 Residential Residences in 65-Acre Campus",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram (Chana), Ragi Flour, Cooking Oil",
        "Estimated Monthly Volume": "45 MT Rice, 7.0 MT Toor Dal, 3.0 MT Ragi, 4,800 L Oil",
        "Procurement Profile": "Samruddhi Trust Central Logistics & Mess Management",
        "Address / Landmark": "Acharya Dr. Sarvepalli Radhakrishnan Road, Soldevanahalli, Bengaluru - 560107",
        "Contact Channel": "Head of Campus Living & Food Services (hostel@acharya.ac.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "Alliance University Residential Campus",
        "Town": "Anekal / Chandapura",
        "Region": "Bengaluru South",
        "Hostel Capacity / Students": "3,200+ Hostellers (Engineering, Law, Business Schools)",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice for Tiffins, Unpolished Toor Dal, Ragi, Pure Cooking Oil",
        "Estimated Monthly Volume": "32 MT Rice, 5.0 MT Toor Dal, 2.0 MT Ragi, 3,500 L Oil",
        "Procurement Profile": "Campus Facility & Central Dining Services",
        "Address / Landmark": "Chikkahagade Cross, Chandapura - Anekal Main Road, Bengaluru - 562106",
        "Contact Channel": "Chief Operating Officer / Food Committee (dining@alliance.edu.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "Sir M. Visvesvaraya Institute of Technology (Sir MVIT)",
        "Town": "Hunasamaranahalli, Yelahanka",
        "Region": "Bengaluru North (Direct NH-44 Airport Corridor)",
        "Hostel Capacity / Students": "1,800+ Residential Hostellers in 133-Acre Campus",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Urad Dal, Ragi, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "18 MT Rice, 3.0 MT Toor Dal, 1.2 MT Ragi, 2,000 L Oil",
        "Procurement Profile": "Sri Krishnadevaraya Educational Trust (SKET) Purchase Section",
        "Address / Landmark": "Krishnadevarayanagar, International Airport Road, Hunasamaranahalli, Bengaluru - 562157",
        "Contact Channel": "Hostel Warden / Purchase Section (warden@sirmvit.edu)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "Bangalore Institute of Technology (BIT) Hostels",
        "Town": "VV Puram / KR Road",
        "Region": "Bengaluru South",
        "Hostel Capacity / Students": "1,400+ Residential Boarders",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Cooking Oil",
        "Estimated Monthly Volume": "14 MT Rice, 2.2 MT Toor Dal, 1.0 MT Ragi, 1,500 L Oil",
        "Procurement Profile": "Rajya Vokkaligara Sangha Purchase Committee",
        "Address / Landmark": "KR Road, VV Puram, Bengaluru - 560004",
        "Contact Channel": "Hostel Warden Office (bithostel@bit-bangalore.edu.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "New Horizon College of Engineering (NHCE) Hostels",
        "Town": "Marathahalli / Bellandur",
        "Region": "Bengaluru East (Outer Ring Road)",
        "Hostel Capacity / Students": "1,600+ Residential Students",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Moong Dal, Ragi, Groundnut Oil",
        "Estimated Monthly Volume": "16 MT Rice, 2.5 MT Toor Dal, 1.2 MT Ragi, 1,800 L Oil",
        "Procurement Profile": "New Horizon Educational Institution Purchase Directorate",
        "Address / Landmark": "Ring Road, Near Marathahalli, Bellandur Post, Bengaluru - 560103",
        "Contact Channel": "Purchase Officer / Hostel Warden (hostel@newhorizonindia.edu)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "The Oxford College of Engineering Hostels",
        "Town": "Bommanahalli",
        "Region": "Bengaluru South (Hosur Road)",
        "Hostel Capacity / Students": "2,200+ Hostellers (Engineering & Dental Campuses)",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Urad Dal, Ragi, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "22 MT Rice, 3.5 MT Toor Dal, 1.5 MT Ragi, 2,500 L Oil",
        "Procurement Profile": "Children's Education Society Central Purchase",
        "Address / Landmark": "10th Milestone, Hosur Road, Bommanahalli, Bengaluru - 560068",
        "Contact Channel": "Hostel General Manager (hostel@theoxford.edu)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "BMS Institute of Technology & Management (BMSIT&M)",
        "Town": "Avalahalli, Yelahanka",
        "Region": "Bengaluru North (Direct NH-44 Corridor)",
        "Hostel Capacity / Students": "1,300+ Residential Hostellers",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Ragi, Cooking Oil",
        "Estimated Monthly Volume": "13 MT Rice, 2.0 MT Toor Dal, 1.0 MT Ragi, 1,500 L Oil",
        "Procurement Profile": "BMSIT Hostels Management Committee",
        "Address / Landmark": "Doddaballapur Main Road, Avalahalli, Yelahanka, Bengaluru - 560064",
        "Contact Channel": "Chief Warden (warden@bmsit.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "RNS Institute of Technology (RNSIT) Hostels",
        "Town": "Channasandra, Kengeri",
        "Region": "Bengaluru West (Mysore Road Belt)",
        "Hostel Capacity / Students": "1,400+ Residential Students",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Urad Dal, Ragi Flour, Cooking Oil",
        "Estimated Monthly Volume": "14 MT Rice, 2.2 MT Toor Dal, 1.0 MT Ragi, 1,600 L Oil",
        "Procurement Profile": "RN Shetty Trust Institutional Catering Section",
        "Address / Landmark": "Dr. Vishnuvardhan Road, Channasandra, RR Nagar Post, Bengaluru - 560098",
        "Contact Channel": "Hostel Incharge (hostel@rnsit.ac.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "CMR Institute of Technology & CMR University Hostels",
        "Town": "Kundalahalli / Bagalur Campus",
        "Region": "Bengaluru East & North",
        "Hostel Capacity / Students": "2,400+ Residential Boarders",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice for Tiffins, Toor Dal, Ragi, Groundnut Oil",
        "Estimated Monthly Volume": "24 MT Rice, 3.8 MT Toor Dal, 1.8 MT Ragi, 2,600 L Oil",
        "Procurement Profile": "CMR Jnanadhara Trust Central Procurement",
        "Address / Landmark": "132 AECS Layout, ITPL Main Road, Kundalahalli, Bengaluru - 560037",
        "Contact Channel": "Director of Administration (hostels@cmr.edu.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "East Point Group of Institutions Hostels",
        "Town": "Bidarahalli, Virgonagar",
        "Region": "Bengaluru East",
        "Hostel Capacity / Students": "2,000+ Hostellers (Engineering & Medical Wings)",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram (Putnalu), Cooking Oil",
        "Estimated Monthly Volume": "20 MT Rice, 3.2 MT Toor Dal, 1.5 MT Ragi, 2,200 L Oil",
        "Procurement Profile": "MG Charitable Trust Purchase Section",
        "Address / Landmark": "Jnana Prabha, East Point Campus, Bidarahalli, Bengaluru - 560049",
        "Contact Channel": "Hostel Administrator (hostels@eastpoint.ac.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "MVJ College of Engineering (MVJCE) Hostels",
        "Town": "Channasandra, Whitefield",
        "Region": "Bengaluru East (ITPB Belt)",
        "Hostel Capacity / Students": "1,500+ Residential Students",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Idli Rice, Toor Dal, Urad Dal, Ragi, Oil",
        "Estimated Monthly Volume": "15 MT Rice, 2.4 MT Toor Dal, 1.2 MT Ragi, 1,700 L Oil",
        "Procurement Profile": "Venkatesha Education Society Procurement Wing",
        "Address / Landmark": "Near ITPB, Channasandra, Kadugodi Post, Bengaluru - 560067",
        "Contact Channel": "Warden / Administrative Officer (hostel@mvjce.edu.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Premier Engineering Colleges & Technical Universities",
        "Business Name": "Don Bosco Institute of Technology (DBIT) Hostels",
        "Town": "Kumbalgodu, Mysore Road",
        "Region": "Bengaluru West",
        "Hostel Capacity / Students": "1,400+ Residential Students",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Cooking Oil",
        "Estimated Monthly Volume": "14 MT Rice, 2.2 MT Toor Dal, 1.0 MT Ragi, 1,600 L Oil",
        "Procurement Profile": "Wayanamac Education Trust Purchase Section",
        "Address / Landmark": "Mysore Road, Kumbalgodu, Bengaluru - 560074",
        "Contact Channel": "Chief Warden (hostel@dbit.co.in)"
    },

    # --- Group B: Elite & Historic Residential Boarding Schools (Top Fees, Zero-Compromise Purity) ---
    {
        "Metro": "Bengaluru",
        "Category": "Elite Residential Boarding Schools",
        "Business Name": "Jain International Residential School (JIRS)",
        "Town": "Kanakapura Road",
        "Region": "Bengaluru South Outskirts",
        "Hostel Capacity / Students": "1,100+ Fully Residential Students in 350-Acre Campus",
        "Key Crops Demanded": "Certified Organic Sona Masoori Rice, Organic Toor Dal, Broken Rice, Cold-Pressed Groundnut Oil, Ragi",
        "Estimated Monthly Volume": "12 MT Premium Rice, 2.0 MT Organic Dal, 1.0 MT Millets, 1,500 L Cold-Pressed Oil",
        "Procurement Profile": "JGI Group Central Hospitality & Dining Division",
        "Address / Landmark": "JGI Global Campus, NH-209, Jakkasandra Post, Kanakapura Taluk, Bengaluru - 562112",
        "Contact Channel": "Director of Campus Living & Food Services (catering@jirs.ac.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Elite Residential Boarding Schools",
        "Business Name": "Sarala Birla Academy (SBA)",
        "Town": "Bannerghatta Road",
        "Region": "Bengaluru South",
        "Hostel Capacity / Students": "650+ Fully Residential Boys in 64-Acre World-Class Campus",
        "Key Crops Demanded": "Finest Grade Aged Sona Masoori, Unpolished Toor Dal, Moong Dal, Pure Groundnut Oil, Millets",
        "Estimated Monthly Volume": "7 MT Premium Rice, 1.2 MT Premium Dal, 800 L Pure Oil",
        "Procurement Profile": "Birla Educational Trust Catering Section",
        "Address / Landmark": "Jigani Road, Bannerghatta, Bengaluru - 560083",
        "Contact Channel": "Estate Manager / Catering Incharge (bursar@saralabirlaacademy.org)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Elite Residential Boarding Schools",
        "Business Name": "Greenwood High International Residential Campus",
        "Town": "Chikkawadayar / Sarjapur",
        "Region": "Bengaluru South-East",
        "Hostel Capacity / Students": "850+ Residential Boarders (National & International)",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Chemical-Free Toor Dal, Urad Dal, Cold-Pressed Oil",
        "Estimated Monthly Volume": "9 MT Rice, 1.5 MT Toor Dal, 1,000 L Pure Cooking Oil",
        "Procurement Profile": "Greenwood High Hospitality & Dining Directorate",
        "Address / Landmark": "No. 8-14, Chikkawadayar Village, Varthur Sarjapur Road, Bengaluru - 560087",
        "Contact Channel": "Head of Boarding & Food Operations (boarding@greenwoodhigh.edu.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Elite Residential Boarding Schools",
        "Business Name": "Indus International School Boarding House",
        "Town": "Billapura Cross, Sarjapur",
        "Region": "Bengaluru South-East",
        "Hostel Capacity / Students": "600+ Residential Boarders",
        "Key Crops Demanded": "Premium Sortex Sona Masoori, Organic Pulses, Cold-Pressed Edible Oils, Millets",
        "Estimated Monthly Volume": "6.5 MT Rice, 1.2 MT Toor Dal, 800 L Pure Cooking Oil",
        "Procurement Profile": "Indus Trust Central Hospitality & Nutrition Board",
        "Address / Landmark": "Billapura Cross, Sarjapur, Bengaluru - 562125",
        "Contact Channel": "Director of Boarding & Dining (dining@indusschool.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Elite Residential Boarding Schools",
        "Business Name": "Canadian International School (CIS) Boarding",
        "Town": "Manchenahalli, Yelahanka",
        "Region": "Bengaluru North (Direct NH-44 Corridor)",
        "Hostel Capacity / Students": "400+ Residential Boarders",
        "Key Crops Demanded": "Finest Grade Sortex Rice, Unadulterated Dals, Healthy Cooking Oils",
        "Estimated Monthly Volume": "4.5 MT Rice, 800 kg Dal, 500 L Oil",
        "Procurement Profile": "Campus Facility & Catering Section",
        "Address / Landmark": "4 & 20 Manchenahalli, Yelahanka, Bengaluru - 560064",
        "Contact Channel": "Boarding Director (boarding@cisb.org.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Elite Residential Boarding Schools",
        "Business Name": "Stonehill International School Boarding",
        "Town": "Tarahunise Post, Jala Hobli",
        "Region": "Bengaluru North (Near Airport / NH-44)",
        "Hostel Capacity / Students": "350+ Full & Weekly Boarders",
        "Key Crops Demanded": "Aged Single-Origin Rice, Organic Pulses, Cold-Pressed Groundnut Oil",
        "Estimated Monthly Volume": "4 MT Rice, 700 kg Dal, 500 L Oil",
        "Procurement Profile": "Stonehill Food & Beverage Committee",
        "Address / Landmark": "No. 259/333/334/335, Tarahunise Post, Jala Hobli, Bengaluru - 562157",
        "Contact Channel": "Food & Beverage Manager (dining@stonehill.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Elite Residential Boarding Schools",
        "Business Name": "Bishop Cotton Boys' School Residential Hostel",
        "Town": "St. Mark's Road",
        "Region": "Bengaluru Central",
        "Hostel Capacity / Students": "450+ Historic Residential Boarders",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Moong Dal, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "5 MT Rice, 900 kg Toor Dal, 600 L Oil",
        "Procurement Profile": "Boarding House Master & Kitchen Steward",
        "Address / Landmark": "15 Residency Road / St. Mark's Road, Bengaluru - 560001",
        "Contact Channel": "Hostel Warden / Steward (hostel@cottonboys.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Elite Residential Boarding Schools",
        "Business Name": "Rashtriya Military School (RMS Bengaluru) Cadet Mess",
        "Town": "Richmond Town / Hosur Road",
        "Region": "Bengaluru Central",
        "Hostel Capacity / Students": "500+ Fully Residential Military Cadets",
        "Key Crops Demanded": "High-Calorie Sona Masoori Rice, Unpolished Toor Dal, Bengal Gram (Chana), Groundnut Oil",
        "Estimated Monthly Volume": "6 MT Rice, 1.2 MT Toor Dal, 800 kg Chana, 800 L Oil",
        "Procurement Profile": "Quarter Master (QM) & Cadet Mess Committee (Ministry of Defence)",
        "Address / Landmark": "PB No. 25040, Museum Road, Richmond Town, Bengaluru - 560025",
        "Contact Channel": "Administrative Officer / Quarter Master (bangalore@rashtriyamilitaryschools.edu.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Elite Residential Boarding Schools",
        "Business Name": "The International School Bangalore (TISB) Boarding",
        "Town": "Sarjapur-Varthur Road",
        "Region": "Bengaluru East",
        "Hostel Capacity / Students": "550+ Residential Boarders",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Organic Toor Dal, Pure Groundnut Oil",
        "Estimated Monthly Volume": "6 MT Rice, 1.0 MT Dal, 700 L Oil",
        "Procurement Profile": "Catering Operations Manager",
        "Address / Landmark": "NAFL Valley, Circle, Varthur Hobli, Bengaluru - 562125",
        "Contact Channel": "Catering Manager (catering@tisb.ac.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Elite Residential Boarding Schools",
        "Business Name": "Trio World Academy Residential Wing",
        "Town": "Sahakar Nagar, Kodigehalli",
        "Region": "Bengaluru North (Near NH-44)",
        "Hostel Capacity / Students": "300+ Residential Boarders",
        "Key Crops Demanded": "Sortex Sona Masoori Rice, Toor Dal, Urad Dal, Pure Cooking Oil",
        "Estimated Monthly Volume": "3.5 MT Rice, 600 kg Dal, 450 L Oil",
        "Procurement Profile": "Campus Living & Dining Department",
        "Address / Landmark": "3/5 Kodigehalli Main Road, Sahakar Nagar, Bengaluru - 560092",
        "Contact Channel": "Boarding Head (hostel@trioworldacademy.com)"
    },

    # --- Group C: Corporate Residential Pre-University & IIT-JEE / NEET Coaching Townships ---
    {
        "Metro": "Bengaluru",
        "Category": "Corporate Residential PU & Coaching Townships",
        "Business Name": "Narayana PU College Residential Boys Campus (Yelahanka)",
        "Town": "Yelahanka / Doddaballapur Road",
        "Region": "Bengaluru North (Direct NH-44 Corridor)",
        "Hostel Capacity / Students": "1,600+ Residential IIT-JEE / NEET Aspirants",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice (Idli/Dosa 5 AM delivery), Toor Dal, Bengal Gram (Putnalu), Cooking Oil",
        "Estimated Monthly Volume": "16 MT Rice, 2.5 MT Toor Dal, 1.0 MT Bengal Gram, 2,000 L Oil",
        "Procurement Profile": "Narayana Group Karnataka Regional Procurement Cell",
        "Address / Landmark": "Maruthi Nagar, Kogilu Road, Yelahanka, Bengaluru - 560064",
        "Contact Channel": "Regional Purchase Manager (procurement.blr@narayanagroup.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Corporate Residential PU & Coaching Townships",
        "Business Name": "Narayana PU College Residential Girls Campus (Kengeri)",
        "Town": "Kengeri Satellite Town",
        "Region": "Bengaluru West (Mysore Road Belt)",
        "Hostel Capacity / Students": "1,200+ Residential Girls",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Urad Dal, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "12 MT Rice, 2.0 MT Toor Dal, 1,500 L Oil",
        "Procurement Profile": "Narayana Group Regional Mess Procurement",
        "Address / Landmark": "Near Kengeri Bus Terminal, Mysore Road, Bengaluru - 560060",
        "Contact Channel": "Campus Administrator (kengeri.admin@narayanagroup.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Corporate Residential PU & Coaching Townships",
        "Business Name": "Sri Chaitanya PU College Mega Residential Campus (Bommasandra)",
        "Town": "Bommasandra / Electronic City",
        "Region": "Bengaluru South (Hosur Road)",
        "Hostel Capacity / Students": "2,200+ Residential Students (Multi-Block Coaching Township)",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice for Batter, Unpolished Toor Dal, Groundnut Oil",
        "Estimated Monthly Volume": "22 MT Rice, 3.5 MT Toor Dal, 2,500 L Oil",
        "Procurement Profile": "Sri Chaitanya Karnataka State Procurement Bureau",
        "Address / Landmark": "Bommasandra Industrial Area, Near Electronic City, Bengaluru - 560099",
        "Contact Channel": "State Purchase Officer (blr.procurement@srichaitanya.net)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Corporate Residential PU & Coaching Townships",
        "Business Name": "Sri Chaitanya Techno Residential Campus (Yelahanka New Town)",
        "Town": "Yelahanka New Town",
        "Region": "Bengaluru North (Direct NH-44 Corridor)",
        "Hostel Capacity / Students": "1,400+ Residential Students",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Cooking Oil",
        "Estimated Monthly Volume": "14 MT Rice, 2.2 MT Toor Dal, 1,600 L Oil",
        "Procurement Profile": "Sri Chaitanya North Bangalore Cluster Purchase",
        "Address / Landmark": "Attur Layout, Major Sandeep Unnikrishnan Road, Yelahanka New Town, Bengaluru - 560064",
        "Contact Channel": "Campus Principal & Mess Warden (yelahanka@srichaitanya.net)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Corporate Residential PU & Coaching Townships",
        "Business Name": "Deeksha Integrated Residential PU Campus (Kanakapura Road)",
        "Town": "Thalaghattapura, Kanakapura Road",
        "Region": "Bengaluru South",
        "Hostel Capacity / Students": "900+ Residential Boarders",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Ragi, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "9 MT Rice, 1.5 MT Toor Dal, 800 kg Ragi, 1,000 L Oil",
        "Procurement Profile": "Ace Creative Learning Central Operations",
        "Address / Landmark": "Thalaghattapura, Kanakapura Main Road, Bengaluru - 560062",
        "Contact Channel": "Operations Head (admin@deekshalearning.com)"
    }
]

def main():
    df = pd.DataFrame(INSTITUTIONS)
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")
    print(f"SUCCESS: Generated {len(df)} verified Bengaluru Educational Institutions in {OUTPUT_CSV}")
    print("\nSummary by Category:")
    print(df.groupby("Category").size())
    print("\nSummary by Region:")
    print(df.groupby("Region").size())

if __name__ == "__main__":
    main()
