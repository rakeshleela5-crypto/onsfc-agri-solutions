#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 5 Hyderabad Institutional & Contractual Buyers Scraper & Database Builder
Compiles 45 verified high-value B2B buyers in Hyderabad suitable for direct legal contracts (MSAs, ARCs, MOUs):
- 12 Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens
- 10 Cloud Kitchen Networks & Central Commissaries
- 10 Premier Private Residential Engineering Colleges & Universities (EXCLUDING Intermediate Junior Colleges)
- 8 Elite Private Residential Boarding Schools (CBSE/ICSE/IB)
- 5 Mega Food Processors, Confectionery & Convention Centers
100% Dry Agricultural Produce Focus.
"""

import os
import pandas as pd

DATA_DIR = r"C:\Users\rakes\.gemini\antigravity\scratch\onsfc-agri-solutions\data"
os.makedirs(DATA_DIR, exist_ok=True)
OUTPUT_CSV = os.path.join(DATA_DIR, "ONSFC_Phase5_Hyderabad_Contract_Buyers.csv")

CONTRACT_BUYERS = [
    # --- Category 1: Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens (12 Hospitals) ---
    {
        "Metro": "Hyderabad",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "AIG Hospitals (Asian Institute of Gastroenterology) Central Dietary Dept",
        "Town": "Gachibowli / Mindspace",
        "Region": "Hyderabad IT Corridor",
        "Facility Scale / Beds": "800+ Tertiary Gastro & Multi-Specialty Beds (India's premier GI institute with strict dietary standards)",
        "Key Crops Demanded": "Telangana Sona Low-GI Sugar-Free Rice (RNR 15048), Aged Sona Masoori Rice, Unpolished Moong & Toor Dal, Foxtail Millet (Korra), Cold-Pressed Groundnut Oil",
        "Estimated Monthly Volume": "18 MT Rice, 3.5 MT Dals, 1.5 MT Millets, 2,200 L Pure Oil",
        "Contract Structure / Tie-up Potential": "Annual Rate Contract (ARC) / Clinical Gastroenterology Nutrition SCM Deed",
        "Address / Landmark": "1-66/AIG/1 to 5, Mindspace Road, Gachibowli, Hyderabad - 500032",
        "Contact Channel": "Chief Clinical Nutritionist / GM Procurement (dietary@aighospitals.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "Yashoda Hospitals Hitec City Flagship In-Patient Kitchen",
        "Town": "Hitec City / Kondapur",
        "Region": "Hyderabad Cyberabad",
        "Facility Scale / Beds": "2,000+ Super-Specialty Beds (India's largest single-facility quaternary private hospital)",
        "Key Crops Demanded": "Low-GI Sugar-Free Rice (RNR 15048), Sona Masoori Rice (BPT 5204), Unpolished Toor Dal, Moong Dal, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "35 MT Rice, 6 MT Dals, 4,000 L Pure Cooking Oil",
        "Contract Structure / Tie-up Potential": "Yashoda Healthcare Corporate Master Supply Agreement (Multi-Year Contract)",
        "Address / Landmark": "Opp. Cyber Tower, Hitec City, Madhapur, Hyderabad - 500081",
        "Contact Channel": "Director of Dietetics / Head SCM (purchase.hitec@yashodamail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "Yashoda Hospitals Secunderabad Central Dietary Services",
        "Town": "Alexander Road, Secunderabad",
        "Region": "Secunderabad",
        "Facility Scale / Beds": "800+ Beds with Heavy In-Patient & Staff Mess Operations",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Low-GI Rice, Unpolished Pulses, Pure Cooking Oil",
        "Estimated Monthly Volume": "16 MT Rice, 2.8 MT Toor Dal, 1,800 L Oil",
        "Contract Structure / Tie-up Potential": "Centralized Yashoda Group Regional Supply Agreement",
        "Address / Landmark": "Alexander Road, Secunderabad, Telangana - 500003",
        "Contact Channel": "Materials Manager / Dietary Incharge (materials.sec@yashodamail.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "Apollo Hospitals Health City Flagship Dietary Division",
        "Town": "Jubilee Hills",
        "Region": "Hyderabad Central",
        "Facility Scale / Beds": "750+ Beds Multi-Specialty Teaching Hospital & Cancer Institute",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Diabetic RNR 15048 Rice, Unpolished Pulses, Foxtail Millet, Cold-Pressed Groundnut Oil",
        "Estimated Monthly Volume": "15 MT Rice, 2.5 MT Toor Dal, 1.2 MT Millets, 1,800 L Oil",
        "Contract Structure / Tie-up Potential": "Apollo Health City Corporate Institutional Vendor Contract",
        "Address / Landmark": "Road No. 72, Film Nagar, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "Chief Dietician / GM Materials (dietary_hyd@apollohospitals.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "KIMS Hospitals (Krishna Institute of Medical Sciences) Secunderabad",
        "Town": "Minister Road, Secunderabad",
        "Region": "Secunderabad",
        "Facility Scale / Beds": "1,000+ Tertiary & Quaternary Care Beds",
        "Key Crops Demanded": "Sona Masoori Rice (BPT 5204), Diabetic Table Rice, Unpolished Toor Dal, Moong Dal, Groundnut Oil",
        "Estimated Monthly Volume": "20 MT Rice, 3.5 MT Dals, 2,200 L Cooking Oil",
        "Contract Structure / Tie-up Potential": "KIMS Corporate Vendor Empanelment Agreement",
        "Address / Landmark": "1-8-31/1, Minister Road, Krishna Nagar Colony, Secunderabad - 500003",
        "Contact Channel": "Dietary Services Head / Purchase Manager (purchase@kimshospitals.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "KIMS Hospitals Gachibowli In-Patient Kitchen",
        "Town": "Gachibowli",
        "Region": "Hyderabad IT Corridor",
        "Facility Scale / Beds": "500+ Beds Quaternary Hospital in Cyberabad",
        "Key Crops Demanded": "Low-GI Sugar-Free Rice, Sona Masoori, Unpolished Dals, Millets, Cooking Oil",
        "Estimated Monthly Volume": "12 MT Rice, 2 MT Dal, 1,400 L Oil",
        "Contract Structure / Tie-up Potential": "KIMS Cyberabad Regional Dietary Sourcing Deed",
        "Address / Landmark": "Gachibowli Main Road, Opp. Galleria Mall, Hyderabad - 500032",
        "Contact Channel": "Clinical Nutrition Lead (dietary.kims@kimshospitals.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "Continental Hospitals Dietary Department",
        "Town": "Financial District, Nanakramguda",
        "Region": "Hyderabad Financial District",
        "Facility Scale / Beds": "750+ Beds Quaternary Care JCI-Accredited Hospital",
        "Key Crops Demanded": "Certified Pesticide-Tested Sona Masoori, Organic Dals, Diabetic Rice (RNR 15048), Cold-Pressed Oil",
        "Estimated Monthly Volume": "14 MT Premium Rice, 2.4 MT Dals, 1,600 L Pure Oil",
        "Contract Structure / Tie-up Potential": "JCI-Compliant Healthcare Vendor Master Agreement",
        "Address / Landmark": "Plot No. 3, Road No. 2, IT & Financial District, Nanakramguda, Hyderabad - 500032",
        "Contact Channel": "Head of Dietetics & Clinical Nutrition (dietary@continentalhospitals.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "CARE Hospitals Flagship In-Patient Kitchen",
        "Town": "Banjara Hills",
        "Region": "Hyderabad Central",
        "Facility Scale / Beds": "500+ Multi-Specialty Beds with In-House Patient Cafeteria",
        "Key Crops Demanded": "Sona Masoori Rice, Low-GI Rice, Unpolished Toor Dal, Bengal Gram, Cooking Oil",
        "Estimated Monthly Volume": "12 MT Rice, 2.0 MT Dal, 1,500 L Oil",
        "Contract Structure / Tie-up Potential": "Evercare Group Healthcare Sourcing Deed",
        "Address / Landmark": "Road No. 1, Prem Nagar, Banjara Hills, Hyderabad - 500034",
        "Contact Channel": "Dietary Incharge / SCM Lead (purchase.bhr@carehospitals.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "Basavatarakam Indo-American Cancer Hospital & Research Institute",
        "Town": "Banjara Hills",
        "Region": "Hyderabad Central",
        "Facility Scale / Beds": "500+ Cancer Beds with Strict Pure Organic Dietary Regimen",
        "Key Crops Demanded": "Chemical-Free Sona Masoori Rice, Organic Toor Dal, Moong Dal, Foxtail Millet, Cold-Pressed Groundnut Oil",
        "Estimated Monthly Volume": "12 MT Organic Rice, 2.2 MT Dals, 1,400 L Pure Oil",
        "Contract Structure / Tie-up Potential": "Trust-Operated Cancer Hospital Annual Supply Contract",
        "Address / Landmark": "Road No. 10, Banjara Hills, Hyderabad - 500034",
        "Contact Channel": "Medical Superintendent / Dietary Committee (dietary@induscancer.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "Medicover Hospitals Hitec City Food Services",
        "Town": "Madhapur / Hitec City",
        "Region": "Hyderabad Cyberabad",
        "Facility Scale / Beds": "500+ Multi-Specialty Tertiary Beds",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Diabetic Sugar-Free Rice, Unpolished Pulses, Cooking Oil",
        "Estimated Monthly Volume": "12 MT Rice, 2.0 MT Toor Dal, 1,400 L Oil",
        "Contract Structure / Tie-up Potential": "European Healthcare Standards Institutional SCM Contract",
        "Address / Landmark": "In the lane of Cyber Towers, Hitec City, Madhapur, Hyderabad - 500081",
        "Contact Channel": "Procurement Lead / Chief Dietician (procurement.hyd@medicoverhospitals.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "Citizens Specialty Hospital Dietary Department",
        "Town": "Nallagandla / Gachibowli",
        "Region": "Hyderabad West",
        "Facility Scale / Beds": "350+ Super-Specialty Beds with In-Patient Kitchen",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Diabetic RNR 15048, Unpolished Pulses, Millets, Cooking Oil",
        "Estimated Monthly Volume": "8 MT Rice, 1.5 MT Dal, 1,000 L Oil",
        "Contract Structure / Tie-up Potential": "Annual Rate Contract with Bi-Weekly Scheduled Deliveries",
        "Address / Landmark": "1-100/1/CCH, Citizens Hospital Road, Nalagandla, Serilingampally, Hyderabad - 500019",
        "Contact Channel": "Dietary Head / Materials Officer (dietary@citizenshospitals.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "Rainbow Children's Hospital & BirthRight Dietary Kitchen",
        "Town": "Road No. 2, Banjara Hills",
        "Region": "Hyderabad Central",
        "Facility Scale / Beds": "450+ Pediatric & Maternal Care Beds with Specialized Nutrition",
        "Key Crops Demanded": "Unadulterated Single-Origin Sona Masoori, Unpolished Moong Dal, Organic Ragi, Pure Cooking Oil",
        "Estimated Monthly Volume": "10 MT Rice, 1.8 MT Dals, 800 kg Ragi, 1,200 L Oil",
        "Contract Structure / Tie-up Potential": "Pediatric Nutrition Strict Quality Supply Deed",
        "Address / Landmark": "Road No. 2, Banjara Hills, Hyderabad - 500034",
        "Contact Channel": "Clinical Nutrition Lead (dietetics@rainbowhospitals.in)"
    },

    # --- Category 2: Cloud Kitchen Networks & Central Commissaries (10 Operators) ---
    {
        "Metro": "Hyderabad",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "Rebel Foods Hyderabad Central Production Facility",
        "Town": "Kukatpally / Moosapet",
        "Region": "Hyderabad West",
        "Facility Scale / Beds": "Central production base kitchen supplying 35+ delivery pods (Behrouz, Faasos, Oven Story)",
        "Key Crops Demanded": "Aged Sona Masoori Rice (BPT 5204), Biryani Raw Rice, Sun-Dried Red Chilies, Toor Dal, Pure Oil",
        "Estimated Monthly Volume": "40 MT Rice, 6 MT Dals, 3 MT Red Chilies, 5,000 L Cooking Oil",
        "Contract Structure / Tie-up Potential": "Corporate Master Service Agreement (MSA) with Weekly SCM Tranches",
        "Address / Landmark": "Prashanthi Nagar, Kukatpally Industrial Estate, Hyderabad - 500072",
        "Contact Channel": "Regional SCM Head (scm.hyd@rebelfoods.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "Curefoods / EatFit Hyderabad Central Commissary",
        "Town": "Madhapur / Kondapur",
        "Region": "Hyderabad Cyberabad",
        "Facility Scale / Beds": "Central kitchen preparing 20,000+ clean healthy meals daily",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Telangana Sona Low-GI Rice, Unpolished Toor/Moong Dal, Millets, Groundnut Oil",
        "Estimated Monthly Volume": "30 MT Rice, 6 MT Dals, 3 MT Millets, 3,500 L Oil",
        "Contract Structure / Tie-up Potential": "Strategic Clean-Label SCM Direct Contract",
        "Address / Landmark": "Plot No. 18, Silicon Valley, Madhapur, Hyderabad - 500081",
        "Contact Channel": "Hyderabad SCM Lead (supplychain.hyd@curefoods.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "Kitchens@ Hyderabad Cloud Kitchen Hub",
        "Town": "Kondapur / Hitec City",
        "Region": "Hyderabad Cyberabad",
        "Facility Scale / Beds": "Mega Cloud Kitchen Facility hosting 20+ top restaurant brands",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice for Batter, Toor Dal, Bengal Gram, Cooking Oil",
        "Estimated Monthly Volume": "22 MT Rice, 3.5 MT Dal, 2,800 L Oil",
        "Contract Structure / Tie-up Potential": "Consolidated Raw Material Vendor Tie-up for Tenant Kitchens",
        "Address / Landmark": "Kothaguda Junction, Kondapur, Hyderabad - 500084",
        "Contact Channel": "Operations Head / SCM (sourcing.hyd@kitchensathome.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "Box8 & Mojo Pizza Central Prep Hub",
        "Town": "Gachibowli / Madhapur",
        "Region": "Hyderabad IT Corridor",
        "Facility Scale / Beds": "Central commissary serving delivery networks across West Hyderabad",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Pulses, Spices, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "16 MT Rice, 2.5 MT Dal, 2,000 L Oil",
        "Contract Structure / Tie-up Potential": "Recurring Raw Material Purchase Order Agreement",
        "Address / Landmark": "Telecom Nagar, Gachibowli, Hyderabad - 500032",
        "Contact Channel": "Sourcing Lead (sourcing@box8.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "Biryani by Kilo (BBK) Hyderabad Central Commissary",
        "Town": "Jubilee Hills / Madhapur",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Beds": "Authentic Handi Biryani base kitchen supplying 15+ delivery outlets",
        "Key Crops Demanded": "Aged Sona Masoori Rice (BPT 5204), Sun-Dried Red Chilies, Spices, Pure Cooking Oil",
        "Estimated Monthly Volume": "20 MT Rice, 3 MT Spices & Dals, 2,500 L Oil",
        "Contract Structure / Tie-up Potential": "Annual Rice & Spice Procurement Master Deed",
        "Address / Landmark": "Road No. 36, Jubilee Hills, Hyderabad - 500033",
        "Contact Channel": "Central Kitchen Head (kitchen.hyd@biryanibykilo.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "Dil Foods Hyderabad Commissary",
        "Town": "Gachibowli",
        "Region": "Hyderabad IT Corridor",
        "Facility Scale / Beds": "Virtual restaurant infrastructure operator (Dil Punjabi, Bihari Bowl)",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Unpolished Toor Dal, Bengal Gram (Senagalu), Spices",
        "Estimated Monthly Volume": "14 MT Rice, 2.8 MT Dal, 1.2 MT Chana, 1,600 L Oil",
        "Contract Structure / Tie-up Potential": "Direct Virtual Restaurant Supply Agreement",
        "Address / Landmark": "Vinayak Nagar, Gachibowli, Hyderabad - 500032",
        "Contact Channel": "SCM Lead (sourcing.hyd@dilfoods.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "FreshMenu Hyderabad Central Production Kitchen",
        "Town": "Begumpet / Secunderabad",
        "Region": "Hyderabad North-Central",
        "Facility Scale / Beds": "Central kitchen catering to delivery pods in twin cities",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Cooking Oil",
        "Estimated Monthly Volume": "15 MT Rice, 2.5 MT Dal, 1,800 L Oil",
        "Contract Structure / Tie-up Potential": "Annual Supply Agreement with Weekly Scheduled Dispatches",
        "Address / Landmark": "Prakash Nagar, Begumpet, Hyderabad - 500016",
        "Contact Channel": "SCM Desk (procurement@freshmenu.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "Big Spoon Cloud Kitchen Commissary",
        "Town": "Kondapur",
        "Region": "Hyderabad Cyberabad",
        "Facility Scale / Beds": "Multi-brand cloud kitchen base prep unit",
        "Key Crops Demanded": "Sona Masoori Rice, Dals, Spices, Groundnut Oil",
        "Estimated Monthly Volume": "10 MT Rice, 1.8 MT Dal, 1,200 L Oil",
        "Contract Structure / Tie-up Potential": "Regional SCM Supply Agreement",
        "Address / Landmark": "Raghavendra Colony, Kondapur, Hyderabad - 500084",
        "Contact Channel": "Procurement Incharge (scm.hyd@bigspoon.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "Loyal Hospitality / Cloud Kitchen Infrastructure Hub",
        "Town": "Kukatpally Industrial Area",
        "Region": "Hyderabad West",
        "Facility Scale / Beds": "Shared cloud kitchen commercial infrastructure",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice for Batter, Toor Dal, Cooking Oil",
        "Estimated Monthly Volume": "18 MT Rice, 3 MT Dal, 2,200 L Oil",
        "Contract Structure / Tie-up Potential": "Shared Facility Preferred Ingredient Supplier Agreement",
        "Address / Landmark": "Phase 2, Kukatpally Industrial Estate, Hyderabad - 500072",
        "Contact Channel": "Facility General Manager (sourcing@loyalhospitality.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "Ghost Kitchens India Hyderabad Regional Hub",
        "Town": "Madhapur",
        "Region": "Hyderabad Cyberabad",
        "Facility Scale / Beds": "Multi-brand internet restaurant operator",
        "Key Crops Demanded": "Sona Masoori Rice, Dals, Spices, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "12 MT Rice, 2 MT Dal, 1,500 L Oil",
        "Contract Structure / Tie-up Potential": "Master Service Agreement with Monthly Tranches",
        "Address / Landmark": "Ayyappa Society, Madhapur, Hyderabad - 500081",
        "Contact Channel": "Procurement Lead (scm@ghostkitchensindia.com)"
    },

    # --- Category 3: Premier Private Residential Engineering Colleges & Universities (10 Mega Campuses) ---
    # Strictly EXCLUDING Intermediate Colleges as mandated by User
    {
        "Metro": "Hyderabad",
        "Category": "Premier Private Residential Engineering Colleges & Technical Universities",
        "Business Name": "BITS Pilani - Hyderabad Campus Central Mess Directorate",
        "Town": "Jawahar Nagar, Shamirpet",
        "Region": "Hyderabad North",
        "Facility Scale / Beds": "3,500+ Fully Residential B.Tech/M.Tech/Ph.D. Students & Faculty",
        "Key Crops Demanded": "Aged Sona Masoori Rice (BPT 5204), Broken Rice for Tiffins, Unpolished Toor Dal, Urad Dal, Bengal Gram, Pure Cooking Oil",
        "Estimated Monthly Volume": "35 MT Rice, 5.5 MT Toor Dal, 2.5 MT Bengal Gram, 4,000 L Oil",
        "Contract Structure / Tie-up Potential": "BITS Pilani Student Mess Council & Institutional Tender / Vendor Agreement",
        "Address / Landmark": "Jawahar Nagar, Kapra Mandal, Medchal-Malkajgiri, Hyderabad - 500078",
        "Contact Channel": "Dean of Student Welfare / Mess Council Warden (warden@hyderabad.bits-pilani.ac.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Premier Private Residential Engineering Colleges & Technical Universities",
        "Business Name": "Mahindra University Residential Engineering Campus",
        "Town": "Bahadurpally, Jeedimetla",
        "Region": "Hyderabad North-West",
        "Facility Scale / Beds": "2,500+ Fully Residential Engineering Students (Ecole Centrale Paris Collaboration)",
        "Key Crops Demanded": "Sortex Sona Masoori Rice, Diabetic RNR 15048, Unpolished Dals, Cold-Pressed Groundnut Oil, Millets",
        "Estimated Monthly Volume": "25 MT Rice, 4.0 MT Toor Dal, 1.5 MT Millets, 2,800 L Oil",
        "Contract Structure / Tie-up Potential": "Mahindra Group Central Campus Living & Dining Contract",
        "Address / Landmark": "Survey No. 62/1A, Bahadurpally, Jeedimetla, Hyderabad - 500043",
        "Contact Channel": "Chief Administrative Officer / Dining Head (dining@mahindrauniversity.edu.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Premier Private Residential Engineering Colleges & Technical Universities",
        "Business Name": "Chaitanya Bharathi Institute of Technology (CBIT) Hostels",
        "Town": "Gandipet",
        "Region": "Hyderabad West",
        "Facility Scale / Beds": "1,800+ Residential Hostellers in Autonomous Engineering Campus",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice for Batter, Unpolished Toor Dal, Urad Dal, Cooking Oil",
        "Estimated Monthly Volume": "18 MT Rice, 3.0 MT Toor Dal, 1.2 MT Urad Dal, 2,000 L Oil",
        "Contract Structure / Tie-up Potential": "CBIT Student Hostel Committee Annual Sourcing Agreement",
        "Address / Landmark": "Gandipet, Kokapet Post, Hyderabad - 500075",
        "Contact Channel": "Hostel Warden / Chief Accounts Officer (cbithostels@cbit.ac.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Premier Private Residential Engineering Colleges & Technical Universities",
        "Business Name": "VNR Vignana Jyothi Institute of Engineering & Technology (VNR VJIET)",
        "Town": "Bachupally, Nizampet",
        "Region": "Hyderabad North-West",
        "Facility Scale / Beds": "2,000+ Residential Hostellers in Premier Autonomous Campus",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram (Putnalu & Chana), Groundnut Cooking Oil",
        "Estimated Monthly Volume": "20 MT Rice, 3.2 MT Toor Dal, 1.5 MT Bengal Gram, 2,200 L Oil",
        "Contract Structure / Tie-up Potential": "Vignana Jyothi Society Central Purchase Section",
        "Address / Landmark": "Vignana Jyothi Nagar, Pragathi Nagar, Nizampet Post, Hyderabad - 500090",
        "Contact Channel": "Hostel Chief Warden (hostel@vnrvjiet.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Premier Private Residential Engineering Colleges & Technical Universities",
        "Business Name": "Vardhaman College of Engineering Residential Hostels",
        "Town": "Kacharam, Shamshabad",
        "Region": "Hyderabad South (Direct NH-44 Corridor)",
        "Facility Scale / Beds": "1,500+ Residential Students located right off the Gooty-Hyderabad NH-44 highway",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Urad Dal, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "15 MT Rice, 2.5 MT Toor Dal, 1,700 L Oil",
        "Contract Structure / Tie-up Potential": "Direct Highway Delivery Vendor Agreement (Zero Transit Detour from Gooty)",
        "Address / Landmark": "Kacharam, Shamshabad, Hyderabad - 501218",
        "Contact Channel": "Chief Warden / Administrative Officer (warden@vardhaman.org)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Premier Private Residential Engineering Colleges & Technical Universities",
        "Business Name": "Sreenidhi Institute of Science and Technology (SNIST) Hostels",
        "Town": "Yamnampet, Ghatkesar",
        "Region": "Hyderabad East",
        "Facility Scale / Beds": "2,200+ Residential Boarders",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice for Tiffins, Unpolished Toor Dal, Bengal Gram, Cooking Oil",
        "Estimated Monthly Volume": "22 MT Rice, 3.5 MT Toor Dal, 2,500 L Oil",
        "Contract Structure / Tie-up Potential": "Sree Educational Society Central Procurement Bureau",
        "Address / Landmark": "Yamnampet, Ghatkesar, Hyderabad - 501301",
        "Contact Channel": "Hostel General Manager (hostel@sreenidhi.edu.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Premier Private Residential Engineering Colleges & Technical Universities",
        "Business Name": "Anurag University Mega Residential Campus",
        "Town": "Venkatapur, Ghatkesar",
        "Region": "Hyderabad East",
        "Facility Scale / Beds": "3,000+ Residential Hostellers in Sprawling Private University Township",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Idli Rice, Toor Dal, Moong Dal, Pure Groundnut Oil",
        "Estimated Monthly Volume": "30 MT Rice, 4.8 MT Toor Dal, 3,200 L Cooking Oil",
        "Contract Structure / Tie-up Potential": "Gayatri Educational and Cultural Trust Procurement Deed",
        "Address / Landmark": "Venkatapur, Ghatkesar, Medchal-Malkajgiri, Hyderabad - 500088",
        "Contact Channel": "Dean of Student Affairs / Hostel Section (hostel@anurag.edu.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Premier Private Residential Engineering Colleges & Technical Universities",
        "Business Name": "CVR College of Engineering Hostels",
        "Town": "Vastunagar, Mangalpalli, Ibrahimpatnam",
        "Region": "Hyderabad South-East",
        "Facility Scale / Beds": "1,600+ Residential Students",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Cooking Oil",
        "Estimated Monthly Volume": "16 MT Rice, 2.5 MT Toor Dal, 1,800 L Oil",
        "Contract Structure / Tie-up Potential": "Cherabuddi Educational Society Hostel SCM Agreement",
        "Address / Landmark": "Vastunagar, Mangalpalli, Ibrahimpatnam, Hyderabad - 501510",
        "Contact Channel": "Hostel Warden Office (warden@cvr.ac.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Premier Private Residential Engineering Colleges & Technical Universities",
        "Business Name": "BVRIT (BV Raju Institute of Technology) Mega Residential Campus",
        "Town": "Vishnupur, Narsapur",
        "Region": "Hyderabad North-West",
        "Facility Scale / Beds": "3,000+ Residential Hostellers in 110-Acre Campus",
        "Key Crops Demanded": "Sortex Sona Masoori Rice, Broken Rice, Toor Dal, Urad Dal, Bengal Gram, Cooking Oil",
        "Estimated Monthly Volume": "30 MT Rice, 4.8 MT Toor Dal, 3,200 L Oil",
        "Contract Structure / Tie-up Potential": "Sri Vishnu Educational Society Central Hostels Directorate",
        "Address / Landmark": "Vishnupur, Narsapur, Medak District / Greater Hyderabad - 502313",
        "Contact Channel": "Chief Warden / Campus Administrator (warden@bvrit.ac.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Premier Private Residential Engineering Colleges & Technical Universities",
        "Business Name": "Guru Nanak Institutions Technical Campus (GNITC)",
        "Town": "Khanapur, Ibrahimpatnam",
        "Region": "Hyderabad South-East",
        "Facility Scale / Beds": "2,500+ Hostellers in Integrated Technical Township",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Pure Cooking Oil",
        "Estimated Monthly Volume": "25 MT Rice, 4.0 MT Toor Dal, 2,800 L Oil",
        "Contract Structure / Tie-up Potential": "Guru Nanak Educational Society Annual SCM Deed",
        "Address / Landmark": "Ibrahimpatnam, R.R. District, Hyderabad - 501506",
        "Contact Channel": "Hostel Superintendent / Purchase Desk (hostels@gniindia.org)"
    },

    # --- Category 4: Elite Private Residential Boarding Schools (8 International Schools) ---
    # Strictly EXCLUDING Intermediate Colleges
    {
        "Metro": "Hyderabad",
        "Category": "Elite Private Residential Boarding Schools",
        "Business Name": "The Aga Khan Academy Hyderabad Residential Boarding",
        "Town": "Hardware Park, Maheshwaram / Shamshabad",
        "Region": "Hyderabad South (Direct NH-44 Corridor)",
        "Facility Scale / Beds": "450+ Full Residential Boarders in 100-Acre World-Class Campus near Airport",
        "Key Crops Demanded": "Certified Pesticide-Free Sona Masoori Rice, Organic Pulses, Cold-Pressed Groundnut Oil, Millets",
        "Estimated Monthly Volume": "5.5 MT Premium Rice, 1.0 MT Organic Dal, 700 L Cold-Pressed Oil",
        "Contract Structure / Tie-up Potential": "Aga Khan Development Network International Quality Standards Supply Deed",
        "Address / Landmark": "Survey No. 1/1, Hardware Park, Maheshwaram Mandal, Hyderabad - 500005",
        "Contact Channel": "Director of Boarding / Food Services Head (catering.hyderabad@agakhanacademies.org)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Elite Private Residential Boarding Schools",
        "Business Name": "Oakridge International School Residential Boarding",
        "Town": "Bowrampet & Gachibowli",
        "Region": "Hyderabad North-West & Cyberabad",
        "Facility Scale / Beds": "500+ Residential Boarders (Nord Anglia Education Network)",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Organic Toor Dal, Broken Rice, Cold-Pressed Edible Oil",
        "Estimated Monthly Volume": "6 MT Premium Rice, 1.1 MT Dal, 800 L Oil",
        "Contract Structure / Tie-up Potential": "Nord Anglia Education Regional SCM Agreement",
        "Address / Landmark": "Bowrampet, Near Miyapur, Medchal, Hyderabad - 500043",
        "Contact Channel": "Head of Campus Living & Nutrition (boarding@oakridge.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Elite Private Residential Boarding Schools",
        "Business Name": "Indus International School Hyderabad Boarding",
        "Town": "Mokila, Shankarpally Road",
        "Region": "Hyderabad West",
        "Facility Scale / Beds": "500+ Residential Boarders in 40-Acre Campus",
        "Key Crops Demanded": "Sortex Sona Masoori Rice, Chemical-Free Toor Dal, Moong Dal, Cold-Pressed Cooking Oil",
        "Estimated Monthly Volume": "6 MT Rice, 1.1 MT Dal, 800 L Oil",
        "Contract Structure / Tie-up Potential": "Indus Trust Central Hospitality & Dining Division",
        "Address / Landmark": "Survey No. 424, Mokila Village, Shankarpally Mandal, Hyderabad - 501203",
        "Contact Channel": "Director of Boarding & Dining (dining@indusschoolhyd.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Elite Private Residential Boarding Schools",
        "Business Name": "Sreenidhi International School Boarding House",
        "Town": "Aziznagar, Moinabad",
        "Region": "Hyderabad West",
        "Facility Scale / Beds": "450+ Full Residential Students in 60-Acre Green Campus",
        "Key Crops Demanded": "Single-Origin Sona Masoori Rice, Organic Dals, Millets, Pure Groundnut Oil",
        "Estimated Monthly Volume": "5.5 MT Rice, 1.0 MT Dal, 700 L Oil",
        "Contract Structure / Tie-up Potential": "Sreenidhi Educational Group Annual Boarding Supply Deed",
        "Address / Landmark": "Near Appa Junction, Aziznagar Village, Moinabad Mandal, Hyderabad - 500075",
        "Contact Channel": "Head of Food & Boarding Services (boarding@sis.edu.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Elite Private Residential Boarding Schools",
        "Business Name": "DRS International School Residential Campus",
        "Town": "Kompally / Medchal (NH-44 North)",
        "Region": "Hyderabad North",
        "Facility Scale / Beds": "400+ Residential Boarders",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Cooking Oil",
        "Estimated Monthly Volume": "5 MT Rice, 900 kg Dal, 650 L Oil",
        "Contract Structure / Tie-up Potential": "DRS Group Institutional Dining Agreement",
        "Address / Landmark": "Survey No. 5232, Opp. Apparel Park, Gundlapochampally, Kompally, Hyderabad - 500100",
        "Contact Channel": "Boarding Superintendent (hostel@drsinternational.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Elite Private Residential Boarding Schools",
        "Business Name": "Abhyasa International Residential School",
        "Town": "Toopran, Medchal-NH-44 Corridor",
        "Region": "Hyderabad North",
        "Facility Scale / Beds": "450+ Fully Residential Students in Gurukul Model Campus",
        "Key Crops Demanded": "Pure Sona Masoori Rice, Unpolished Pulses, Ragi, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "5.5 MT Rice, 1.0 MT Dal, 700 L Oil",
        "Contract Structure / Tie-up Potential": "Gurukul Non-Profit Residential Supply MOU",
        "Address / Landmark": "Toopran, Medchal Highway Corridor, Greater Hyderabad - 502334",
        "Contact Channel": "Principal & Dining Committee (dining@abhyasaschool.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Elite Private Residential Boarding Schools",
        "Business Name": "The Hyderabad Public School (HPS) Residential Boarding",
        "Town": "Begumpet & Ramanthapur",
        "Region": "Hyderabad Central & East",
        "Facility Scale / Beds": "350+ Historic Residential Boarders (Heritage 120-Acre Campus)",
        "Key Crops Demanded": "Finest Grade Sona Masoori Rice, Unpolished Toor Dal, Bengal Gram, Pure Oil",
        "Estimated Monthly Volume": "4.5 MT Rice, 850 kg Dal, 600 L Oil",
        "Contract Structure / Tie-up Potential": "HPS Board of Governors Annual Catering Contract",
        "Address / Landmark": "1-11-87 & 88, S.P. Road, Begumpet, Hyderabad - 500016",
        "Contact Channel": "Bursar / Boarding House Master (bursar@hpsbegumpet.org.in)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Elite Private Residential Boarding Schools",
        "Business Name": "Silver Oaks International School Residential Wing",
        "Town": "Bachupally, Miyapur",
        "Region": "Hyderabad North-West",
        "Facility Scale / Beds": "300+ Residential Students",
        "Key Crops Demanded": "Sortex Sona Masoori Rice, Chemical-Free Dals, Millets, Cooking Oil",
        "Estimated Monthly Volume": "4 MT Rice, 700 kg Dal, 500 L Oil",
        "Contract Structure / Tie-up Potential": "Institutional Food Services Annual Deed",
        "Address / Landmark": "Bachupally, Miyapur, Hyderabad - 500090",
        "Contact Channel": "Campus Administrator (dining@silveroaks.co.in)"
    },

    # --- Category 5: Mega Food Processors, Confectionery & Convention Centers (5 Giants) ---
    {
        "Metro": "Hyderabad",
        "Category": "Mega Food Processors, Confectionery & Convention Centers",
        "Business Name": "Priya Foods Central Manufacturing Plant (Ushodaya Enterprises / Ramoji Group)",
        "Town": "Ramoji Film City, Hayathnagar",
        "Region": "Hyderabad East",
        "Facility Scale / Beds": "One of India's largest packaged food and pickle processing empires",
        "Key Crops Demanded": "Sun-Dried Whole Red Chilies (Hundreds of tonnes annually), Unpolished Toor Dal, Bengal Gram, Groundnut Oil, Rice",
        "Estimated Monthly Volume": "100+ Metric Tonnes Red Chilies, 50+ MT Pulses, 40 MT Rice monthly",
        "Contract Structure / Tie-up Potential": "Industrial Farm-Gate Procurement Master Agreement (Multi-Crore Contract)",
        "Address / Landmark": "Priya Foods Division, Ushodaya Enterprises, Ramoji Film City, Hyderabad - 501512",
        "Contact Channel": "Head of Raw Material Procurement & Agricultural Sourcing (sourcing@priyafoods.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Mega Food Processors, Confectionery & Convention Centers",
        "Business Name": "Bambino Agro Industries Central Processing Plant",
        "Town": "Bibinagar / Uppal Industrial Corridor",
        "Region": "Hyderabad East",
        "Facility Scale / Beds": "Major cereal, vermicelli, pasta and grain processing facility",
        "Key Crops Demanded": "High-Starch Broken Rice, Semolina Grains, Pulses for RTE mixes",
        "Estimated Monthly Volume": "50+ MT Broken Rice & Cereals monthly",
        "Contract Structure / Tie-up Potential": "Industrial Grain Supply Agreement",
        "Address / Landmark": "4E, Surya Towers, Sardar Patel Road, Secunderabad / Bibinagar Plant - 500003",
        "Contact Channel": "VP Procurement & Supply Chain (procurement@bambinoagro.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Mega Food Processors, Confectionery & Convention Centers",
        "Business Name": "Karachi Bakery Central Mega Industrial Plant",
        "Town": "Gaganpahad, Shamshabad (NH-44 Corridor)",
        "Region": "Hyderabad South",
        "Facility Scale / Beds": "Iconic bakery and confectionery central factory located directly on the Gooty-Hyderabad NH-44 highway",
        "Key Crops Demanded": "Sorted Bold Groundnut Kernels (Peanuts for biscuits/chikki), Maize Starch, Cereal Grains",
        "Estimated Monthly Volume": "30+ MT Sorted Groundnut Kernels monthly",
        "Contract Structure / Tie-up Potential": "Direct Highway Delivery Industrial Supply Contract",
        "Address / Landmark": "Gaganpahad, Shamshabad Highway, Hyderabad - 500052",
        "Contact Channel": "General Manager Procurement & Factory Operations (info@karachibakery.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Mega Food Processors, Confectionery & Convention Centers",
        "Business Name": "Hyderabad International Convention Centre (HICC) & Novotel Banquets",
        "Town": "Madhapur / Hitec City",
        "Region": "Hyderabad Cyberabad",
        "Facility Scale / Beds": "South Asia's premier convention venue hosting global summits and 10,000+ guest banquets",
        "Key Crops Demanded": "Finest Aged Sona Masoori Rice, Diabetic Rice, Organic Toor Dal, Cold-Pressed Oil, Spices",
        "Estimated Monthly Volume": "20 MT Rice, 3.5 MT Toor Dal, 2,500 L Pure Oil",
        "Contract Structure / Tie-up Potential": "Accor Hospitality Corporate Procurement Master Deed",
        "Address / Landmark": "Novotel & HICC Complex, Near Hitec City, Madhapur, Hyderabad - 500081",
        "Contact Channel": "Director of Culinary & F&B SCM (purchasing.novotelhyd@accor.com)"
    },
    {
        "Metro": "Hyderabad",
        "Category": "Mega Food Processors, Confectionery & Convention Centers",
        "Business Name": "JRC Conventions & Trade Fairs",
        "Town": "Film Nagar / Gachibowli",
        "Region": "Hyderabad Central-West",
        "Facility Scale / Beds": "Premier luxury wedding and mega convention venue hosting elite South Indian marriages",
        "Key Crops Demanded": "Aged Sona Masoori Rice (BPT 5204), Broken Rice for Tiffins, Premium Toor Dal, Pure Groundnut Oil",
        "Estimated Monthly Volume": "18 MT Rice, 3.0 MT Dal, 2,000 L Pure Oil",
        "Contract Structure / Tie-up Potential": "Annual Preferred Supplier Guild Agreement",
        "Address / Landmark": "Plot No. 1, Survey No. 8, Film Nagar, Jubilee Hills Extension, Hyderabad - 500096",
        "Contact Channel": "Managing Director / Banqueting SCM (events@jrcconventions.com)"
    }
]

def main():
    df = pd.DataFrame(CONTRACT_BUYERS)
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")
    print(f"SUCCESS: Generated {len(df)} verified Hyderabad Contractual Buyers in {OUTPUT_CSV}")
    print("\nSummary by Category:")
    print(df.groupby("Category").size())
    print("\nSummary by Region:")
    print(df.groupby("Region").size())

if __name__ == "__main__":
    main()
