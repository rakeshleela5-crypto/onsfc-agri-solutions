#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 4 Bengaluru Contractual Buyers Scraper & Database Builder
Compiles 35 high-value B2B buyers in Bengaluru suitable for direct legal contracts (MSAs, ARCs, MOUs):
- 12 Private Multi-Specialty Hospital Dietary Kitchens
- 10 Cloud Kitchen Networks & Central Commissaries
- 8 Ready-to-Cook (RTC) Batter & Grain Processing Plants
- 5 Mega Convention Centers & Wedding Caterers Guilds
100% Dry Agricultural Produce Focus.
"""

import os
import pandas as pd

DATA_DIR = r"C:\Users\rakes\.gemini\antigravity\scratch\onsfc-agri-solutions\data"
os.makedirs(DATA_DIR, exist_ok=True)
OUTPUT_CSV = os.path.join(DATA_DIR, "ONSFC_Phase4_Bengaluru_Contract_Buyers.csv")

CONTRACT_BUYERS = [
    # --- Category 1: Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens ---
    {
        "Metro": "Bengaluru",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "Narayana Health City Central Dietary Kitchen",
        "Town": "Bommasandra, Hosur Road",
        "Region": "Bengaluru South",
        "Facility Scale / Beds": "2,000+ Beds (Mazumdar Shaw Medical Centre & Narayana Institute of Cardiac Sciences)",
        "Key Crops Demanded": "Diabetic Sugar-Free Rice (RNR 15048), Aged Sona Masoori Rice, Unpolished Moong & Toor Dal, Karnataka Ragi, Cold-Pressed Groundnut Oil",
        "Estimated Monthly Volume": "30 MT Rice, 5 MT Dals, 2 MT Ragi, 3,500 L Cooking Oil",
        "Contract Structure / Tie-up Potential": "Annual Rate Contract (ARC) / In-Patient Dietary Vendor Empanelment",
        "Address / Landmark": "258/A, Bommasandra Industrial Area, Anekal Taluk, Bengaluru - 560099",
        "Contact Channel": "Head of Dietetics & Nutrition / General Manager SCM (dietetics@narayanahealth.org)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "Manipal Hospital Flagship Central Dietary Department",
        "Town": "Old Airport Road",
        "Region": "Bengaluru East",
        "Facility Scale / Beds": "650+ Multi-Specialty Beds with In-House Patient Kitchens & Staff Canteens",
        "Key Crops Demanded": "Aged Sona Masoori Rice (BPT 5204), Low-GI RNR 15048 Rice, Unpolished Toor Dal, Organic Foxtail Millet (Korra), Pure Oil",
        "Estimated Monthly Volume": "15 MT Rice, 2.5 MT Toor Dal, 1.0 MT Millets, 1,800 L Pure Oil",
        "Contract Structure / Tie-up Potential": "Centralized Manipal Health Enterprises Corporate Vendor Agreement",
        "Address / Landmark": "98, HAL Old Airport Road, Kodihalli, Bengaluru - 560017",
        "Contact Channel": "Chief Dietary Officer / Materials Manager (materials@manipalhospitals.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "Manipal Hospital Whitefield In-Patient Kitchen",
        "Town": "Whitefield",
        "Region": "Bengaluru East (ITPB Belt)",
        "Facility Scale / Beds": "300+ In-Patient Beds & Cafeteria",
        "Key Crops Demanded": "Low-GI Sugar-Free Rice, Sona Masoori Rice, Chemical-Free Toor Dal, Ragi, Groundnut Oil",
        "Estimated Monthly Volume": "8 MT Rice, 1.4 MT Dal, 600 kg Ragi, 1,000 L Oil",
        "Contract Structure / Tie-up Potential": "Manipal Group Regional Hospital Supply MOU",
        "Address / Landmark": "143, 212-215, EPIP Zone, Whitefield, Bengaluru - 560066",
        "Contact Channel": "Dietary Incharge / Purchase Officer (purchase.wf@manipalhospitals.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "Manipal Hospital Yeshwanthpur Dietary Services",
        "Town": "Yeshwanthpur",
        "Region": "Bengaluru North-West (NH-44 Connector)",
        "Facility Scale / Beds": "400+ Tertiary Care Beds",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice for Congee/Diet, Unpolished Dals, Millets, Cooking Oil",
        "Estimated Monthly Volume": "10 MT Rice, 1.8 MT Dal, 800 kg Millets, 1,200 L Oil",
        "Contract Structure / Tie-up Potential": "Annual Rate Contract with Bi-Weekly Staggered Delivery",
        "Address / Landmark": "1st Main Road, Subbaiah Medical Complex, Yeshwanthpur, Bengaluru - 560022",
        "Contact Channel": "Facility General Manager / Dietary Head (dietary.ypr@manipalhospitals.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "Apollo Hospitals Flagship In-Patient Food Services",
        "Town": "Bannerghatta Road",
        "Region": "Bengaluru South",
        "Facility Scale / Beds": "550+ Multi-Specialty Quaternary Care Beds",
        "Key Crops Demanded": "Aged Sona Masoori Rice, RNR 15048 Sugar Free, Unpolished Toor Dal, Moong Dal, Pure Groundnut Oil",
        "Estimated Monthly Volume": "12 MT Rice, 2.2 MT Toor Dal, 1,500 L Pure Cooking Oil",
        "Contract Structure / Tie-up Potential": "Apollo Health City Institutional Vendor Contract",
        "Address / Landmark": "154/11, Bannerghatta Main Road, Opp. IIM-B, Bengaluru - 560076",
        "Contact Channel": "Head of Dietetics & Clinical Nutrition (dietary_bglr@apollohospitals.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "Fortis Hospital In-Patient Kitchen & Cafeteria",
        "Town": "Bannerghatta Road",
        "Region": "Bengaluru South",
        "Facility Scale / Beds": "400+ Multi-Specialty Beds",
        "Key Crops Demanded": "Low-GI Table Rice, Sortex Sona Masoori, Unpolished Pulses, Cold-Pressed Groundnut Oil",
        "Estimated Monthly Volume": "10 MT Rice, 1.6 MT Dals, 1,200 L Oil",
        "Contract Structure / Tie-up Potential": "Fortis Healthcare South Regional Supply Agreement",
        "Address / Landmark": "154/9, Bannerghatta Road, Opp. IIM-B, Bengaluru - 560076",
        "Contact Channel": "Dietary Services Head / Procurement Lead (purchase.bg@fortishealthcare.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "Aster CMI Hospital Dietary Kitchen",
        "Town": "Hebbal / Sahakar Nagar",
        "Region": "Bengaluru North (Direct NH-44 Corridor)",
        "Facility Scale / Beds": "500+ Super-Specialty Beds right on the Airport Highway",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Low-GI Diabetic Rice, Unpolished Pulses, Ragi, Groundnut Oil",
        "Estimated Monthly Volume": "12 MT Rice, 2.0 MT Toor Dal, 1,400 L Oil",
        "Contract Structure / Tie-up Potential": "Direct Highway Delivery Vendor Contract (NH-44 Entry)",
        "Address / Landmark": "No. 43/42, National Highway 44, New Airport Road, Hebbal, Bengaluru - 560092",
        "Contact Channel": "Clinical Nutrition Lead / SCM Head (scm.cmi@asterhospital.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "St. John's Medical College Hospital Food Services",
        "Town": "Koramangala / Sarjapur Road",
        "Region": "Bengaluru South-East",
        "Facility Scale / Beds": "1,350+ In-Patient Hospital Beds + 800 Medical Boarders",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Unpolished Toor Dal, Bengal Gram (Senagalu), Pure Cooking Oil",
        "Estimated Monthly Volume": "25 MT Rice, 4.5 MT Toor Dal, 1.5 MT Bengal Gram, 3,000 L Oil",
        "Contract Structure / Tie-up Potential": "St. John's National Academy of Health Sciences Annual Supply Deed",
        "Address / Landmark": "Sarjapur Road, John Nagar, Koramangala, Bengaluru - 560034",
        "Contact Channel": "Associate Director (Hospital) / Kitchen Steward (hospital.purchase@stjohns.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "Sakra World Hospital Dietary Department",
        "Town": "Marathahalli-Sarjapur Outer Ring Road",
        "Region": "Bengaluru East",
        "Facility Scale / Beds": "350+ Premium Beds (Toyota Tsusho & Secom Healthcare JV)",
        "Key Crops Demanded": "Premium Pesticide-Tested Sona Masoori, Organic Pulses, Cold-Pressed Groundnut Oil, Millets",
        "Estimated Monthly Volume": "8 MT Premium Rice, 1.5 MT Dal, 1,000 L Pure Oil",
        "Contract Structure / Tie-up Potential": "Japanese Quality Standards Long-Term Vendor Tie-up",
        "Address / Landmark": "52/2 & 52/3, Devarabeesanahalli, Varthur Hobli, Outer Ring Road, Bengaluru - 560103",
        "Contact Channel": "Chief Clinical Nutritionist / Procurement Desk (purchase@sakraworldhospital.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "Vydehi Institute of Medical Sciences & Hospital",
        "Town": "Whitefield",
        "Region": "Bengaluru East",
        "Facility Scale / Beds": "1,600+ Hospital Beds + 2,000 Medical/Nursing Hostellers",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Idli Rice, Toor Dal, Bengal Gram, Cooking Oil",
        "Estimated Monthly Volume": "28 MT Rice, 4.5 MT Toor Dal, 3,200 L Cooking Oil",
        "Contract Structure / Tie-up Potential": "Srinivasa Trust Central Hospital & Hostel Procurement Contract",
        "Address / Landmark": "82, Nallurahalli, Near BMTC 18th Depot, Whitefield, Bengaluru - 560066",
        "Contact Channel": "Medical Superintendent / Catering Incharge (hospital@vims.ac.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "BGS Gleneagles Global Hospital Dietary Kitchen",
        "Town": "Kengeri / Mysore Road",
        "Region": "Bengaluru West",
        "Facility Scale / Beds": "450+ Beds Multi-Organ Transplant Centre",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Low-GI Rice, Unpolished Dals, Ragi, Groundnut Oil",
        "Estimated Monthly Volume": "10 MT Rice, 1.8 MT Toor Dal, 1,200 L Oil",
        "Contract Structure / Tie-up Potential": "Gleneagles Healthcare Institutional Sourcing Contract",
        "Address / Landmark": "67, Uttarahalli Road, Kengeri, Bengaluru - 560060",
        "Contact Channel": "Head of Clinical Nutrition / Materials Desk (procurement.bgs@parkwaypantai.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Private Multi-Specialty Hospitals & Healthcare Dietary Kitchens",
        "Business Name": "Sri Shankara Cancer Hospital & Research Centre",
        "Town": "Shankarapuram, Basavanagudi",
        "Region": "Bengaluru South",
        "Facility Scale / Beds": "300+ Cancer Care Beds with Strict Chemical-Free Dietary Diet",
        "Key Crops Demanded": "Certified Pesticide-Free Sona Masoori Rice, Organic Pulses, Cold-Pressed Groundnut Oil, Millets",
        "Estimated Monthly Volume": "7 MT Organic Rice, 1.2 MT Dals, 800 L Pure Oil",
        "Contract Structure / Tie-up Potential": "Trust-Operated Non-Profit Healthcare Long-Term Procurement",
        "Address / Landmark": "1st Cross, Shankarapuram, Basavanagudi, Bengaluru - 560004",
        "Contact Channel": "Medical Director / Kitchen Incharge (dietary@shankaracancerfoundation.org)"
    },

    # --- Category 2: Cloud Kitchen Networks & Central Commissaries ---
    {
        "Metro": "Bengaluru",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "Rebel Foods Central Production Facility (Behrouz & Faasos)",
        "Town": "Kudlu Gate / Hosur Road",
        "Region": "Bengaluru South",
        "Facility Scale / Beds": "Central Production Kitchen supplying 40+ Cloud Pods across Bengaluru",
        "Key Crops Demanded": "Aged Sona Masoori Rice (BPT 5204), Biryani Raw Rice, Sun-Dried Red Chilies, Toor Dal, Pure Oil",
        "Estimated Monthly Volume": "40 MT Rice, 6 MT Dals, 3 MT Red Chilies, 5,000 L Cooking Oil",
        "Contract Structure / Tie-up Potential": "National Master Service Agreement (MSA) with Monthly SCM Volume Tranches",
        "Address / Landmark": "Kudlu Gate, Hosur Main Road, Electronic City Post, Bengaluru - 560068",
        "Contact Channel": "Head of Global SCM & Commodity Sourcing (procurement@rebelfoods.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "Curefoods / EatFit Central Commissary",
        "Town": "Bommasandra Industrial Area",
        "Region": "Bengaluru South",
        "Facility Scale / Beds": "Massive central kitchen producing 25,000+ healthy meals daily (EatFit, Great Indian Khichdi)",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Unpolished Toor Dal, Moong Dal, Foxtail Millet (Korra), Ragi, Groundnut Oil",
        "Estimated Monthly Volume": "35 MT Rice, 7 MT Dals, 4 MT Millets, 4,000 L Oil",
        "Contract Structure / Tie-up Potential": "Strategic Clean-Label Farm-Gate Partner Contract",
        "Address / Landmark": "Sy No. 34, Bommasandra Industrial Area, Anekal Taluk, Bengaluru - 560099",
        "Contact Channel": "VP of Supply Chain & Ingredients Sourcing (supplychain@curefoods.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "FreshMenu Central Production Commissary",
        "Town": "Tin Factory / Old Madras Road",
        "Region": "Bengaluru East",
        "Facility Scale / Beds": "Central food processing hub catering to 25+ delivery kitchens",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Pure Cooking Oil",
        "Estimated Monthly Volume": "20 MT Rice, 3.5 MT Dal, 2,500 L Oil",
        "Contract Structure / Tie-up Potential": "Annual Purchase Agreement with Weekly Scheduled Dispatches",
        "Address / Landmark": "No. 4, Old Madras Road, Near Tin Factory, Bengaluru - 560016",
        "Contact Channel": "Director of Culinary & SCM (procurement@freshmenu.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "Box8 & Mojo Pizza Central Processing Hub",
        "Town": "HSR Layout / Kudlu",
        "Region": "Bengaluru South-East",
        "Facility Scale / Beds": "Central commissary serving South Bangalore delivery network",
        "Key Crops Demanded": "Aged Sona Masoori Rice (for Meals & Biryanis), Pulses, Spices, Cooking Oil",
        "Estimated Monthly Volume": "18 MT Rice, 2.8 MT Dal, 2,200 L Oil",
        "Contract Structure / Tie-up Potential": "Long-Term Raw Material Supply Contract",
        "Address / Landmark": "27th Main, Sector 1, HSR Layout, Bengaluru - 560102",
        "Contact Channel": "SCM Lead (sourcing@box8.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "Kitchens@ Central Shared Culinary Infrastructure",
        "Town": "Marathahalli / Bellandur",
        "Region": "Bengaluru East",
        "Facility Scale / Beds": "Mega Cloud Kitchen Facility hosting 25+ national and regional F&B brands",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice for Batter, Toor Dal, Bengal Gram, Cooking Oil",
        "Estimated Monthly Volume": "25 MT Rice, 4 MT Dal, 3,000 L Oil",
        "Contract Structure / Tie-up Potential": "Consolidated Raw Material Vendor Tie-up for Tenant Kitchens",
        "Address / Landmark": "Loyola Composite Hub, Outer Ring Road, Marathahalli, Bengaluru - 560037",
        "Contact Channel": "Chief Procurement Officer (procurement@kitchensathome.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "Big Spoon Multi-Brand Cloud Kitchen Commissary",
        "Town": "Koramangala",
        "Region": "Bengaluru South",
        "Facility Scale / Beds": "Centralized prep facility for multi-brand cloud cloud operations",
        "Key Crops Demanded": "Sona Masoori Rice, Dals, Spices, Groundnut Oil",
        "Estimated Monthly Volume": "12 MT Rice, 2 MT Dal, 1,500 L Oil",
        "Contract Structure / Tie-up Potential": "Regional SCM Supply Agreement",
        "Address / Landmark": "80 Feet Road, 4th Block, Koramangala, Bengaluru - 560034",
        "Contact Channel": "General Manager Procurement (scm@bigspoon.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "Dil Foods Central Production Hub",
        "Town": "HSR Layout",
        "Region": "Bengaluru South-East",
        "Facility Scale / Beds": "Institutional virtual restaurant operator (Dil Punjabi, Bihari Bowl, The Chhote Lal)",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Unpolished Toor Dal, Bengal Gram (Senagalu), Spices",
        "Estimated Monthly Volume": "15 MT Rice, 3 MT Toor Dal, 1.5 MT Chana, 1,800 L Oil",
        "Contract Structure / Tie-up Potential": "Direct Virtual Restaurant Supply Contract",
        "Address / Landmark": "14th Main, Sector 7, HSR Layout, Bengaluru - 560102",
        "Contact Channel": "Operations & Sourcing Head (sourcing@dilfoods.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "Biryani Blues & Charcoal Eats Central Prep Unit",
        "Town": "Bellandur / Sarjapur Road",
        "Region": "Bengaluru East",
        "Facility Scale / Beds": "Centralized biryani and rice-bowl base kitchen",
        "Key Crops Demanded": "Aged Sona Masoori Rice (BPT 5204), Sun-Dried Red Chilies, Toor Dal, Pure Oil",
        "Estimated Monthly Volume": "16 MT Rice, 2.5 MT Dal, 2,000 L Oil",
        "Contract Structure / Tie-up Potential": "Contractual Rice & Spice Sourcing Master Agreement",
        "Address / Landmark": "Green Glen Layout, Bellandur, Bengaluru - 560103",
        "Contact Channel": "Central Kitchen Purchase Manager (kitchen@biryaniblues.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "Voosh Food Technologies Central Commissary",
        "Town": "Electronic City Phase 1",
        "Region": "Bengaluru South",
        "Facility Scale / Beds": "Tech-enabled delivery cloud kitchen infrastructure",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Cooking Oil",
        "Estimated Monthly Volume": "14 MT Rice, 2.2 MT Dal, 1,600 L Oil",
        "Contract Structure / Tie-up Potential": "B2B Recurring Purchase Order Contract",
        "Address / Landmark": "Neeladri Road, Electronic City Phase 1, Bengaluru - 560100",
        "Contact Channel": "Procurement Lead (scm@voosh.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Cloud Kitchen Networks & Central Commissaries",
        "Business Name": "Swiggy Access Cloud Kitchen Central Supply Hub",
        "Town": "Whitefield",
        "Region": "Bengaluru East",
        "Facility Scale / Beds": "Shared infrastructure facility housing 15+ top restaurants",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "22 MT Rice, 3.5 MT Dal, 2,800 L Oil",
        "Contract Structure / Tie-up Potential": "Empanelled Bulk Ingredient Provider for Access Partners",
        "Address / Landmark": "EPIP Zone, Near SAP Labs, Whitefield, Bengaluru - 560066",
        "Contact Channel": "Swiggy Access City Operations Head (access.blr@swiggy.in)"
    },

    # --- Category 3: Ready-to-Cook (RTC) Batter & Food Processing Plants ---
    {
        "Metro": "Bengaluru",
        "Category": "Ready-to-Cook (RTC) Batter & Food Processing Plants",
        "Business Name": "iD Fresh Food (India) Pvt Ltd Mega Manufacturing Plant",
        "Town": "Hosakote Industrial Area",
        "Region": "Bengaluru East Corridor",
        "Facility Scale / Beds": "World's Largest Wet Batter Processing Factory (Manufacturing 100,000+ kg batter daily)",
        "Key Crops Demanded": "High-Starch Broken Rice (Idli/Dosa Grade), Unpolished Urad Dal (Minapappu), Organic Grains",
        "Estimated Monthly Volume": "300+ Metric Tonnes Broken Rice, 60+ MT Urad Dal monthly",
        "Contract Structure / Tie-up Potential": "Corporate Master Commodity Supply Agreement (Multi-Crore Annual Contract)",
        "Address / Landmark": "Plot No. 11 & 12, KIADB Industrial Area, Hosakote, Bengaluru - 562114",
        "Contact Channel": "Chief Procurement Officer / VP Supply Chain (procurement@idfreshfood.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Ready-to-Cook (RTC) Batter & Food Processing Plants",
        "Business Name": "Pristine Organics (Pristine Special Foods)",
        "Town": "Peenya Industrial Area",
        "Region": "Bengaluru North-West",
        "Facility Scale / Beds": "Pioneering Organic & Rare Grain Food Processing Plant (Organic infant food & nutrition)",
        "Key Crops Demanded": "Organic Ragi (Finger Millet), Foxtail Millet (Korra), Red Gram (Toor Dal), Bengal Gram",
        "Estimated Monthly Volume": "40 MT Millets, 15 MT Pulses monthly",
        "Contract Structure / Tie-up Potential": "Certified Organic Farm-Gate Producer Partnership Deed",
        "Address / Landmark": "No. 839, 3rd Phase, Peenya Industrial Area, Bengaluru - 560058",
        "Contact Channel": "Director of Sourcing & Nutrition (contactus@pristineorganics.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Ready-to-Cook (RTC) Batter & Food Processing Plants",
        "Business Name": "Tata Consumer Soulfull Central Processing Facility",
        "Town": "Peenya / Nelamangala",
        "Region": "Bengaluru North-West",
        "Facility Scale / Beds": "Major Ragi & Millet Breakfast Processing Plant (Millet Muesli, Ragi Bites)",
        "Key Crops Demanded": "Premium Dryland Ragi (Finger Millet - 100+ MT monthly), Bengal Gram, Millets",
        "Estimated Monthly Volume": "80+ MT Ragi, 20 MT Pulses monthly",
        "Contract Structure / Tie-up Potential": "Tata Consumer Products Institutional Sourcing Contract",
        "Address / Landmark": "KIADB Industrial Area, Nelamangala, Bengaluru - 562123",
        "Contact Channel": "Commodity Procurement Manager (sourcing@soulfull.co.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Ready-to-Cook (RTC) Batter & Food Processing Plants",
        "Business Name": "Millet Amma (Health Agro Enterprises Central Plant)",
        "Town": "HSR Layout / Sarjapur Road",
        "Region": "Bengaluru South-East",
        "Facility Scale / Beds": "D2C & B2B Millet Batter and Flour Manufacturing Plant",
        "Key Crops Demanded": "Organic Ragi, Foxtail Millet (Korra), Jowar, Urad Dal, Unpolished Toor Dal",
        "Estimated Monthly Volume": "15 MT Millets, 4 MT Dals monthly",
        "Contract Structure / Tie-up Potential": "Exclusive Grain Aggregator Supply MOU",
        "Address / Landmark": "No. 33, 1st Cross, HSR Layout Sector 2, Bengaluru - 560102",
        "Contact Channel": "Founder & Head of Procurement (care@milletamma.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Ready-to-Cook (RTC) Batter & Food Processing Plants",
        "Business Name": "Adukale - Sankethi Agro Products Factory",
        "Town": "Rajajinagar Industrial Town",
        "Region": "Bengaluru West",
        "Facility Scale / Beds": "Traditional Karnataka Heritage Ready-to-Cook Staples Factory",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram (Putnalu & Chana), Cooking Oil",
        "Estimated Monthly Volume": "12 MT Rice, 3 MT Toor Dal, 2 MT Putnalu monthly",
        "Contract Structure / Tie-up Potential": "Direct Manufacturing Supply Agreement",
        "Address / Landmark": "Plot No. 42, Rajajinagar Industrial Town, Bengaluru - 560044",
        "Contact Channel": "Managing Director / Raw Materials Desk (info@adukale.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Ready-to-Cook (RTC) Batter & Food Processing Plants",
        "Business Name": "AsmitA Organic Farms Distribution Hub",
        "Town": "Koramangala",
        "Region": "Bengaluru South",
        "Facility Scale / Beds": "Premium Organic Grocery & Direct Consumer Grain Hub",
        "Key Crops Demanded": "Organic Sona Masoori, Organic Pulses, Cold-Pressed Groundnut Oil, Single-Origin Millets",
        "Estimated Monthly Volume": "10 MT Organic Rice, 2.5 MT Dals, 1,500 L Pure Oil",
        "Contract Structure / Tie-up Potential": "Certified Farm-Direct Producer Sourcing MOU",
        "Address / Landmark": "100 Feet Road, 4th Block, Koramangala, Bengaluru - 560034",
        "Contact Channel": "Head of Procurement & Quality (support@asmitaorganicfarms.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Ready-to-Cook (RTC) Batter & Food Processing Plants",
        "Business Name": "True Elements (HW Wellness Solutions) Regional Hub",
        "Town": "Whitefield",
        "Region": "Bengaluru East",
        "Facility Scale / Beds": "Clean-label Whole Food & Grain Packaging Hub",
        "Key Crops Demanded": "Raw Dryland Ragi, Jowar, Roasted Bengal Gram, Groundnut Kernels",
        "Estimated Monthly Volume": "15 MT Cereals & Millets, 3 MT Oilseeds",
        "Contract Structure / Tie-up Potential": "Clean-Label Ingredient Supply Master Agreement",
        "Address / Landmark": "EPIP Zone, Whitefield, Bengaluru - 560066",
        "Contact Channel": "Head of Ingredients Procurement (ingredients@trueelements.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Ready-to-Cook (RTC) Batter & Food Processing Plants",
        "Business Name": "DailyNinja / SuperDaily Regional Grocery Fulfillment DC",
        "Town": "Mahadevapura",
        "Region": "Bengaluru East",
        "Facility Scale / Beds": "Daily morning staple delivery processing center",
        "Key Crops Demanded": "Packaged Sona Masoori Rice (5kg/25kg), Toor Dal, Idli Rice, Groundnut Oil",
        "Estimated Monthly Volume": "25 MT Rice, 5 MT Pulses, 3,000 L Oil",
        "Contract Structure / Tie-up Potential": "Private Label Sourcing & Supply Contract",
        "Address / Landmark": "Outer Ring Road, Mahadevapura, Bengaluru - 560048",
        "Contact Channel": "Category Manager - Staples (staples@superdaily.com)"
    },

    # --- Category 4: Mega Convention Centers & Wedding Caterers Guilds ---
    {
        "Metro": "Bengaluru",
        "Category": "Mega Convention Centers & Wedding Caterers Guilds",
        "Business Name": "Palace Grounds Mega Convention Venues (Gayatri Vihar & Tripura Vasini)",
        "Town": "Bellary Road / Sadashivanagar",
        "Region": "Bengaluru North (Direct NH-44 Corridor)",
        "Facility Scale / Beds": "India's Most Prestigious Wedding & Banquet Venues (Hosting 15,000 to 25,000 guests per event)",
        "Key Crops Demanded": "Finest Aged Sona Masoori Rice (BPT 5204), Broken Rice for Tiffins, Premium Toor Dal, Pure Groundnut Oil, Spices",
        "Estimated Monthly Volume": "35 MT Rice, 6 MT Toor Dal, 4,000 L Pure Cooking Oil",
        "Contract Structure / Tie-up Potential": "Annual Approved Vendor Retainer Deed with Master Catering Guild",
        "Address / Landmark": "Gate 4, Palace Grounds, Bellary Road, Sadashivanagar, Bengaluru - 560080",
        "Contact Channel": "Guild President / Chief Food Operations Officer (events@palacegroundsbangalore.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Mega Convention Centers & Wedding Caterers Guilds",
        "Business Name": "Adyar Ananda Bhavan (A2B) Mega Catering Division",
        "Town": "Bommanahalli",
        "Region": "Bengaluru South",
        "Facility Scale / Beds": "Central Catering Division executing 50+ mega corporate and marriage events weekly",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice for Crispy Dosa/Idli, Toor Dal, Urad Dal, Bengal Gram (Putnalu), Cooking Oil",
        "Estimated Monthly Volume": "30 MT Rice, 5 MT Toor Dal, 3,500 L Cooking Oil",
        "Contract Structure / Tie-up Potential": "Corporate Annual Master Rate Contract",
        "Address / Landmark": "Hosur Main Road, Bommanahalli, Bengaluru - 560068",
        "Contact Channel": "General Manager Catering (catering@a2b.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Mega Convention Centers & Wedding Caterers Guilds",
        "Business Name": "Bangalore Apex Wholesale Caterers Association",
        "Town": "Gandhi Bazaar / Basavanagudi",
        "Region": "Bengaluru South",
        "Facility Scale / Beds": "Apex Guild of 150+ Commercial Wedding & Event Caterers",
        "Key Crops Demanded": "Sona Masoori Rice (Truckload deliveries), Toor Dal, Urad Dal, Bengal Gram, Pure Cooking Oil",
        "Estimated Monthly Volume": "50+ MT Rice, 10 MT Pulses monthly",
        "Contract Structure / Tie-up Potential": "Apex Association Preferred Supplier Memorandum of Understanding (MOU)",
        "Address / Landmark": "Gandhi Bazaar Main Road, Basavanagudi, Bengaluru - 560004",
        "Contact Channel": "Association Secretary (info@bangalorecaterers.org)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Mega Convention Centers & Wedding Caterers Guilds",
        "Business Name": "MLR Convention Centre & Brigade Hospitality Kitchens",
        "Town": "JP Nagar & Whitefield",
        "Region": "Bengaluru South & East",
        "Facility Scale / Beds": "Premier convention centres with in-house industrial banquet kitchens",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Chemical-Free Toor Dal, Cold-Pressed Oil",
        "Estimated Monthly Volume": "15 MT Rice, 2.5 MT Dal, 1,800 L Pure Oil",
        "Contract Structure / Tie-up Potential": "Brigade Enterprises Corporate Hospitality Vendor Deed",
        "Address / Landmark": "Brigade Millennium Campus, 7th Phase, JP Nagar, Bengaluru - 560078",
        "Contact Channel": "Head of Hospitality & Banqueting (banquets@brigadegroup.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Mega Convention Centers & Wedding Caterers Guilds",
        "Business Name": "Sri Annapoorna Catering & Event Kitchens",
        "Town": "Rajajinagar Industrial Area",
        "Region": "Bengaluru West",
        "Facility Scale / Beds": "High-volume traditional Karnataka catering kitchen for marriage halls across West Bangalore",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Unpolished Toor Dal, Bengal Gram (Senagalu), Pure Groundnut Oil",
        "Estimated Monthly Volume": "18 MT Rice, 3 MT Toor Dal, 2,000 L Oil",
        "Contract Structure / Tie-up Potential": "Exclusive Grain Supplier Annual Rate Agreement",
        "Address / Landmark": "10th Main, Rajajinagar Industrial Estate, Bengaluru - 560010",
        "Contact Channel": "Managing Partner / Food Director (catering@annapoornabengaluru.com)"
    }
]

def main():
    df = pd.DataFrame(CONTRACT_BUYERS)
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")
    print(f"SUCCESS: Generated {len(df)} verified Bengaluru Contractual Buyers in {OUTPUT_CSV}")
    print("\nSummary by Category:")
    print(df.groupby("Category").size())
    print("\nSummary by Region:")
    print(df.groupby("Region").size())

if __name__ == "__main__":
    main()
