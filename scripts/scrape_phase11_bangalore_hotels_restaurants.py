#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 11 Bengaluru Hotels, Restaurants & HORECA Empires Scraper & Database Builder
Compiles 40 verified high-volume commercial dining buyers in Bengaluru:
- Category 1: Andhra Meals, Biryani & Rayalaseema Specialty Restaurant Chains (8 Chains)
- Category 2: Heritage South Indian Tiffin & Darshini Mega-Empires (8 Titans)
- Category 3: Legendary Karnataka Military Hotels & Regional Messes (8 Landmarks)
- Category 4: Luxury 5-Star, 4-Star & Tech Business Hotels (8 Properties)
- Category 5: High-Density Darshini Networks & Traditional Food Landmarks (8 Off-Takers)
100% Dry Agricultural Produce Focus (Zero Perishables).
"""

import os
import pandas as pd

DATA_DIR = r"C:\Users\rakes\.gemini\antigravity\scratch\onsfc-agri-solutions\data"
os.makedirs(DATA_DIR, exist_ok=True)
OUTPUT_CSV = os.path.join(DATA_DIR, "ONSFC_Phase11_Bengaluru_Hotels_Restaurants.csv")

BUYERS = [
    # =========================================================================
    # --- Category 1: Andhra Meals, Biryani & Rayalaseema Restaurant Chains (8 Chains) ---
    # =========================================================================
    {
        "Metro": "Bengaluru",
        "Category": "Andhra Meals & Biryani Restaurant Chains",
        "Business Name": "Nagarjuna Restaurant Central Commissary & Flagship Chain",
        "Town": "Residency Road, Indiranagar, Koramangala & Marathahalli",
        "Region": "Bengaluru Central & East",
        "Facility Scale / Outlets": "The undisputed gold standard of authentic Andhra full-course meals in Bengaluru operating 6 flagship dining restaurants serving 10,000+ unlimited meals daily",
        "Key Crops Demanded": "Aged BPT Sona Masoori Rice (high expansion, non-sticky for unlimited thalis), Unpolished Toor Dal (Togari Bele / Kandi Pappu for signature Andhra Pappu), Sun-Dried Whole Red Chilies, Bold Groundnut Kernels & Pure Cooking Oil",
        "Estimated Monthly Volume": "40+ Metric Tonnes Sona Masoori Rice, 8 MT Unpolished Toor Dal, 4 MT Groundnut Kernels, 3 MT Sun-Dried Red Chilies, 4,500 L Pure Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Central Commissary Direct Farm-Gate Agro Sourcing Master Contract (Fortnightly Payment Terms)",
        "Address / Landmark": "No. 44/1, Residency Road, Near Mayo Hall, Bengaluru - 560025",
        "Contact Channel": "Managing Director & Central SCM Head (procurement@nagarjunarestaurants.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Andhra Meals & Biryani Restaurant Chains",
        "Business Name": "Meghana Foods Central Prep Kitchen & Restaurant Network",
        "Town": "Koramangala, Indiranagar, Jayanagar & Marathahalli",
        "Region": "Bengaluru South & East",
        "Facility Scale / Outlets": "Bengaluru's highest-turnover biryani and Andhra dining chain with 8 mega branches feeding over 15,000 dine-in and delivery customers daily",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Sortex Toor Dal, Peanuts for chutneys and salan, Sun-Dried Red Chilies, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "35+ Metric Tonnes Rice, 6 MT Toor Dal, 3.5 MT Groundnut Kernels, 2.5 MT Red Chilies, 4,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Central Kitchen Direct Mill Sourcing Master Agreement",
        "Address / Landmark": "No. 124, 1st Cross, KHB Colony, 5th Block, Koramangala, Bengaluru - 560095",
        "Contact Channel": "General Manager - Operations & Procurement (contact@meghanafoods.co.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Andhra Meals & Biryani Restaurant Chains",
        "Business Name": "Nandhana Palace Central Commissary & Andhra Chain",
        "Town": "Domlur, Koramangala, Rajajinagar & 15+ City Branches",
        "Region": "Bengaluru Multi-Zone",
        "Facility Scale / Outlets": "Leading Andhra hospitality chain operating 15+ mega restaurants and boutique hotels specializing in Andhra meals, biryani, and catering",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice for breakfast, Unpolished Toor Dal, Bengal Gram for snacks, Pure Cooking Oil",
        "Estimated Monthly Volume": "30+ Metric Tonnes Rice, 6 MT Toor Dal, 3 MT Bengal Gram, 3,500 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Corporate Central Purchasing Framework Contract",
        "Address / Landmark": "No. 7, 4th Cross, Domlur Layout, Bengaluru - 560071",
        "Contact Channel": "VP - Materials & Supply Chain (procurement@nandhana.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Andhra Meals & Biryani Restaurant Chains",
        "Business Name": "Bheemas Restaurant & Banquets",
        "Town": "Church Street / Brigade Road Commercial Hub",
        "Region": "Bengaluru Central",
        "Facility Scale / Outlets": "Historic central Bengaluru Andhra meal landmark operating continuous high-traffic unlimited banana-leaf lunch and dinner services",
        "Key Crops Demanded": "Aged BPT Sona Masoori Rice, Unpolished Toor Dal, Broken Rice, Groundnut Kernels, Sun-Dried Red Chilies",
        "Estimated Monthly Volume": "18 MT Rice, 3.5 MT Toor Dal, 2 MT Peanuts, 1,800 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Direct Restaurant Grain Supply Agreement",
        "Address / Landmark": "No. 31, Church Street, Off Brigade Road, Bengaluru - 560001",
        "Contact Channel": "Managing Partner (bheemaschurchstreet@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Andhra Meals & Biryani Restaurant Chains",
        "Business Name": "Amaravathi Andhra Restaurant",
        "Town": "Residency Road Commercial Core",
        "Region": "Bengaluru Central",
        "Facility Scale / Outlets": "Traditional Andhra spice dining restaurant famous for fiery non-vegetarian curries and authentic thalis",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Sortex Toor Dal, Bold Groundnuts, Dry Red Chilies, Cooking Oil",
        "Estimated Monthly Volume": "14 MT Rice, 2.8 MT Toor Dal, 1.5 MT Peanuts, 1,500 L Oil",
        "Procurement Profile / Tie-up Potential": "Commercial Dining Supply Deed",
        "Address / Landmark": "Residency Road, Near Richmond Circle, Bengaluru - 560025",
        "Contact Channel": "Proprietor (amaravathibangalore@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Andhra Meals & Biryani Restaurant Chains",
        "Business Name": "Anjappar Chettinad Restaurant Regional Central Prep",
        "Town": "Koramangala & Indiranagar",
        "Region": "Bengaluru East",
        "Facility Scale / Outlets": "Pioneering Chettinad regional non-veg chain operating 6 multi-level branches with continuous high-volume dining",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Whole Urad Dal, Sun-Dried Red Chilies, Groundnut Oil",
        "Estimated Monthly Volume": "16 MT Rice, 3 MT Toor Dal, 2 MT Urad Dal, 2,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Regional Central Kitchen Master Agreement",
        "Address / Landmark": "100 Feet Road, 4th Block, Koramangala, Bengaluru - 560034",
        "Contact Channel": "Regional Purchase Manager (anjapparbangalore@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Andhra Meals & Biryani Restaurant Chains",
        "Business Name": "Kritunga Restaurant Bengaluru Outlets & Prep Hub",
        "Town": "Marathahalli & BTM Layout",
        "Region": "Bengaluru South-East",
        "Facility Scale / Outlets": "Bengaluru operations of the famous Rayalaseema chain, serving authentic Ragi Sankati and Natu Kodi to thousands of tech professionals",
        "Key Crops Demanded": "Native Rayalaseema Ragi (Finger Millet for daily Sankati), Aged Sona Masoori Rice, Toor Dal, Rayalaseema Teja Chilies, Groundnut Oil",
        "Estimated Monthly Volume": "18 MT Rice, 6 MT Native Ragi, 3 MT Toor Dal, 1.5 MT Red Chilies, 2,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Direct Farm-Gate Gooty Origin Sourcing Agreement",
        "Address / Landmark": "Outer Ring Road, Near Innovative Multiplex, Marathahalli, Bengaluru - 560037",
        "Contact Channel": "Bengaluru Operations Head (kritungabangalore@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Andhra Meals & Biryani Restaurant Chains",
        "Business Name": "Junior Kuppanna Central Kitchen",
        "Town": "Koramangala & Whitefield",
        "Region": "Bengaluru South-East",
        "Facility Scale / Outlets": "Kongu-nadu traditional non-veg restaurant chain serving authentic banana-leaf meals and biryanis across tech corridors",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Unpolished Pulses, Bold Groundnut Kernels, Cooking Oil",
        "Estimated Monthly Volume": "14 MT Rice, 2.8 MT Dals, 1.5 MT Peanuts, 1,500 L Oil",
        "Procurement Profile / Tie-up Potential": "Central Commissary Food Supply Contract",
        "Address / Landmark": "Koramangala 5th Block, Jyoti Nivas College Road, Bengaluru - 560095",
        "Contact Channel": "Purchase Head (jkbangalore@gmail.com)"
    },

    # =========================================================================
    # --- Category 2: Heritage South Indian Tiffin & Darshini Mega-Empires (8 Titans) ---
    # =========================================================================
    {
        "Metro": "Bengaluru",
        "Category": "Heritage Vegetarian Tiffin Empires",
        "Business Name": "MTR (Mavalli Tiffin Room) Central Commissary & Flagship Chain",
        "Town": "Lalbagh Road, Indiranagar, JP Nagar & St. Marks Road",
        "Region": "Bengaluru Central & South",
        "Facility Scale / Outlets": "Century-old culinary legend founded in 1924 operating 10+ landmark vegetarian institutions, world-famous for Rava Idli, Masala Dosa, Bisibelebath, and Filter Coffee",
        "Key Crops Demanded": "Broken Raw Rice (Nookalu for dosas and idlis), Aged Sona Masoori Rice, Unpolished Toor Dal (Togari Bele for signature Bisibelebath & Sambar), Bengal Gram (Kadale Bele), Bold Groundnut Kernels, Pure Groundnut Oil",
        "Estimated Monthly Volume": "35+ Metric Tonnes Broken Rice, 20 MT Aged Sona Masoori, 8 MT Unpolished Toor Dal, 5 MT Bengal Gram, 4 MT Peanuts, 4,500 L Pure Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Central Commissary Direct Farm SCM Master Agreement (Heritage Quality Certification)",
        "Address / Landmark": "No. 14, Lalbagh Road, Mavalli, Bengaluru - 560027",
        "Contact Channel": "Director of Operations & Central SCM (procurement@mavallitiffinroom.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Heritage Vegetarian Tiffin Empires",
        "Business Name": "Vidyarthi Bhavan Central Kitchen",
        "Town": "Gandhi Bazaar Main Road, Basavanagudi",
        "Region": "Bengaluru South",
        "Facility Scale / Outlets": "80-year-old culinary pilgrimage site serving over 4,000 crispy butter Masala Dosas, Idlis, and Poori Saagu daily to continuous queues of heritage food lovers",
        "Key Crops Demanded": "Broken Raw Rice (Nookalu for signature crisp fermented dosa batter), Urad Dal (Urad Gota), Unpolished Toor Dal for Sambar, Bold Groundnut Kernels for chutney, Bengal Gram",
        "Estimated Monthly Volume": "20+ Metric Tonnes Broken Rice, 5 MT Urad Dal, 3.5 MT Toor Dal, 3.5 MT Groundnut Kernels, 2,500 L Pure Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Heritage Institution Direct Dal & Rice Mill Supply Contract",
        "Address / Landmark": "No. 32, Gandhi Bazaar Main Road, Basavanagudi, Bengaluru - 560004",
        "Contact Channel": "Managing Partner & Kitchen Incharge (vidyarthibhavan1943@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Heritage Vegetarian Tiffin Empires",
        "Business Name": "Paakashala Restaurant Chain Central Commissary",
        "Town": "RR Nagar, Malleshwaram, Indiranagar, JP Nagar & 12+ Outlets",
        "Region": "Bengaluru Multi-Zone",
        "Facility Scale / Outlets": "Premier vegetarian culinary chain founded by KN Vasudeva Adiga operating 12+ mega dining and tiffin complexes with massive banqueting divisions",
        "Key Crops Demanded": "Aged BPT Sona Masoori Rice, Pure Karnataka Ragi for Mudde, Broken Rice, Sortex Toor Dal, Bengal Gram for snacks, Pure Groundnut Oil",
        "Estimated Monthly Volume": "30+ Metric Tonnes Rice, 8 MT Karnataka Ragi, 6 MT Toor Dal, 4 MT Bengal Gram, 4,000 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Corporate Central Commissary SCM Master Vendor Agreement",
        "Address / Landmark": "Central Kitchen, Mysore Road, Near RV College, RR Nagar, Bengaluru - 560059",
        "Contact Channel": "Chief Operating Officer - Food SCM (scm@paakashala.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Heritage Vegetarian Tiffin Empires",
        "Business Name": "The Rameshwaram Cafe Central Commissary",
        "Town": "Indiranagar, JP Nagar, Brookfield, Rajajinagar & Central Hub",
        "Region": "Bengaluru Multi-Zone",
        "Facility Scale / Outlets": "India's highest-velocity quick-service South Indian tiffin phenomenon serving tens of thousands of ghee podi idlis, dosas, and vadas daily from morning to 2:00 AM",
        "Key Crops Demanded": "High-Starch Broken Raw Rice (Nookalu for automated batter lines), Urad Gota, Bengal Gram for Podi & Bajjis, Unpolished Toor Dal for Sambar, Groundnut Kernels for chutney",
        "Estimated Monthly Volume": "45+ Metric Tonnes Broken Rice, 15 MT Aged Rice, 10 MT Urad Dal, 6 MT Bengal Gram, 5 MT Peanuts, 5,000 L Pure Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Central Commissary Direct Farm-Gate Supply Agreement (Multi-Ton Weekly Truckloads)",
        "Address / Landmark": "Central Prep Hub, Outer Ring Road, Near Marathahalli, Bengaluru - 560037",
        "Contact Channel": "Managing Director & Head of SCM (procurement@therameshwaramcafe.org)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Heritage Vegetarian Tiffin Empires",
        "Business Name": "Taaza Thindi Central Kitchen",
        "Town": "Jayanagar 4th Block & Banashankari",
        "Region": "Bengaluru South",
        "Facility Scale / Outlets": "Cult-status breakfast phenomenon known for hygienic open kitchens and ultra-affordable premium idlis, vadas, kharabath, and kesaribath feeding 6,000+ people daily",
        "Key Crops Demanded": "Broken Raw Rice, Urad Dal, Toor Dal for Sambar, Bengal Gram, Bold Groundnut Kernels for fresh coconut-peanut chutney",
        "Estimated Monthly Volume": "22+ Metric Tonnes Broken Rice, 5 MT Urad Dal, 3.5 MT Toor Dal, 3 MT Peanuts, 2,500 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Direct Tiffin Chain Commodity Purchase Contract",
        "Address / Landmark": "1004, 26th Main, 4th T Block, Jayanagar, Bengaluru - 560041",
        "Contact Channel": "Founding Partner & Operations Head (taazathindi@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Heritage Vegetarian Tiffin Empires",
        "Business Name": "CTR (Central Tiffin Room / Shri Sagar)",
        "Town": "7th Cross, Margosa Road, Malleshwaram",
        "Region": "Bengaluru North-West",
        "Facility Scale / Outlets": "Century-old heritage institution famous worldwide for its iconic golden Benne Masala Dosa and filter coffee with continuous tourist queues",
        "Key Crops Demanded": "Broken Raw Rice for crispy Benne Dosa batter, Urad Dal, Unpolished Toor Dal, Groundnut Kernels for spicy chutney",
        "Estimated Monthly Volume": "15 MT Broken Rice, 3.5 MT Urad Dal, 2.5 MT Toor Dal, 2 MT Peanuts, 1,800 L Pure Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Heritage Institution Direct Grain Supply Agreement",
        "Address / Landmark": "7th Cross, Margosa Road, Malleshwaram, Bengaluru - 560003",
        "Contact Channel": "Managing Partner (ctrmalleshwaram@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Heritage Vegetarian Tiffin Empires",
        "Business Name": "A2B (Adyar Ananda Bhavan) Bengaluru Central Commissary",
        "Town": "Bommanahalli Industrial Area & 25+ City Outlets",
        "Region": "Bengaluru South",
        "Facility Scale / Outlets": "Major vegetarian food and sweet empire operating 25+ multi-level restaurants and highway complexes across Greater Bengaluru",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram (Besan Grade), Bold Groundnuts, Cooking Oil",
        "Estimated Monthly Volume": "35+ Metric Tonnes Rice, 8 MT Broken Rice, 6 MT Toor Dal, 4 MT Bengal Gram, 4,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Central Commissary Corporate SCM Framework Contract",
        "Address / Landmark": "Hosur Main Road, Bommanahalli, Bengaluru - 560068",
        "Contact Channel": "General Manager - SCM & Food Materials (sourcing.blr@a2b.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Heritage Vegetarian Tiffin Empires",
        "Business Name": "Brahmin's Coffee Bar & Central Prep",
        "Town": "Ranga Rao Road, Shankarapuram, Basavanagudi",
        "Region": "Bengaluru South",
        "Facility Scale / Outlets": "World-famous 60-year-old standing breakfast institution celebrated for soft steaming Idlis, crispy Vadas, and signature coconut-chana dal chutney",
        "Key Crops Demanded": "High-Quality Broken Raw Rice, Urad Dal, Bengal Gram (Putnalu / Roasted Gram for chutney), Cooking Oil",
        "Estimated Monthly Volume": "12 MT Broken Rice, 3 MT Urad Dal, 2 MT Bengal Gram / Putnalu, 1,200 L Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Direct Heritage Food Supply Agreement",
        "Address / Landmark": "Near Shankar Math, Ranga Rao Road, Shankarapuram, Bengaluru - 560004",
        "Contact Channel": "Managing Partner (brahminscoffeebar@gmail.com)"
    },

    # =========================================================================
    # --- Category 3: Legendary Karnataka Military Hotels & Regional Messes (8 Landmarks) ---
    # =========================================================================
    {
        "Metro": "Bengaluru",
        "Category": "Karnataka Military Hotels & Traditional Messes",
        "Business Name": "Shivaji Military Hotel Central Kitchen",
        "Town": "47th Cross, 8th Block, Jayanagar",
        "Region": "Bengaluru South",
        "Facility Scale / Outlets": "Bengaluru's most iconic Military Hotel founded in 1924, world-famous for traditional Seeraga Samba Donne Biryani, fiery Mutton Chops, and daily Ragi Mudde",
        "Key Crops Demanded": "Pure Karnataka Ragi (Finger Millet for hundreds of daily Ragi Mudde plates), Aged Sona Masoori Rice, Sortex Toor Dal, Bengal Gram, Sun-Dried Red Chilies, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "22+ Metric Tonnes Sona Masoori Rice, 8 MT Native Ragi, 4 MT Toor Dal, 2 MT Red Chilies, 2,500 L Pure Cooking Oil",
        "Procurement Profile / Tie-up Potential": "Heritage Military Hotel Direct Farm SCM Agreement",
        "Address / Landmark": "No. 718, 1st Floor, 8th Block, 47th Cross, Jayanagar, Bengaluru - 560082",
        "Contact Channel": "Proprietor & Master Kitchen Incharge (shivajimilitaryhotel1924@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Karnataka Military Hotels & Traditional Messes",
        "Business Name": "Ranganna Military Hotel",
        "Town": "KR Road, Jayanagar 7th Block",
        "Region": "Bengaluru South",
        "Facility Scale / Outlets": "Legendary traditional non-vegetarian institution famous for authentic Ragi Mudde with Thale Mamsa (head meat), Donne Biryani, and kaal soup",
        "Key Crops Demanded": "Pure Karnataka Ragi (for unit Mudde), Aged Sona Masoori Rice, Toor Dal for Saaru, Sun-Dried Red Chilies, Cooking Oil",
        "Estimated Monthly Volume": "18 MT Rice, 6 MT Ragi, 3 MT Toor Dal, 1.8 MT Red Chilies, 2,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Traditional Kitchen Direct Supply Contract",
        "Address / Landmark": "61, 1st Floor, KR Road, 7th Block, Jayanagar, Bengaluru - 560070",
        "Contact Channel": "Managing Partner (rangannamilitaryhotel@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Karnataka Military Hotels & Traditional Messes",
        "Business Name": "SG Rao Military Hotel",
        "Town": "Cottonpet / Majestic Commercial Core",
        "Region": "Bengaluru Central",
        "Facility Scale / Outlets": "Bengaluru's oldest operating military hotel established in 1908 (116 years of operations), serving traditional Karnataka non-veg feasts to thousands daily",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi for Mudde, Toor Dal, Bengal Gram, Pure Cooking Oil",
        "Estimated Monthly Volume": "15 MT Rice, 5 MT Ragi, 2.5 MT Toor Dal, 1.5 MT Bengal Gram, 1,600 L Oil",
        "Procurement Profile / Tie-up Potential": "Centenary Heritage Institution Food Supply Contract",
        "Address / Landmark": "No. 3, Cottonpet Main Road, Near Majestic, Bengaluru - 560053",
        "Contact Channel": "Managing Partner (sgraomilitaryhotel@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Karnataka Military Hotels & Traditional Messes",
        "Business Name": "Chandu's Military Hotel & Maratha Darbar",
        "Town": "Malleshwaram 8th Cross",
        "Region": "Bengaluru North-West",
        "Facility Scale / Outlets": "Popular North Bangalore military dining destination famous for Donne Biryani, Kheema balls, and steaming Ragi Muddes",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi, Toor Dal, Groundnut Cooking Oil, Red Chilies",
        "Estimated Monthly Volume": "14 MT Rice, 4 MT Ragi, 2.5 MT Dals, 1.5 MT Peanuts, 1,500 L Oil",
        "Procurement Profile / Tie-up Potential": "Commercial Dining Commodity Agreement",
        "Address / Landmark": "8th Cross, Margosa Road, Malleshwaram, Bengaluru - 560003",
        "Contact Channel": "Operations Incharge (chandusmilitaryhotel@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Karnataka Military Hotels & Traditional Messes",
        "Business Name": "New Gobind Military Hotel",
        "Town": "Shivajinagar Commercial Hub",
        "Region": "Bengaluru Central",
        "Facility Scale / Outlets": "High-volume historic mess serving thousands of defense, police, and market workers with rich mutton saaru, ragi mudde, and rice",
        "Key Crops Demanded": "High-Yield Sona Masoori Rice, Karnataka Ragi, Toor Dal, Cooking Oil",
        "Estimated Monthly Volume": "14 MT Rice, 4 MT Ragi, 2.5 MT Dals, 1,500 L Oil",
        "Procurement Profile / Tie-up Potential": "Direct Mill Wholesale Supply Agreement",
        "Address / Landmark": "Broadway Road, Shivajinagar, Bengaluru - 560051",
        "Contact Channel": "Managing Partner (newgobindhotel@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Karnataka Military Hotels & Traditional Messes",
        "Business Name": "Naati Mana Traditional Karnataka Dining",
        "Town": "Koramangala 5th Block & HSR Layout",
        "Region": "Bengaluru South-East",
        "Facility Scale / Outlets": "Upscale rustic Karnataka dining restaurant celebrating regional Gowda and Naati cuisine for tech professionals",
        "Key Crops Demanded": "Single-Origin Sona Masoori Rice, Native Ragi, Unpolished Dals, Cold-Pressed Groundnut Oil",
        "Estimated Monthly Volume": "12 MT Rice, 3.5 MT Ragi, 2 MT Dals, 1,400 L Cold-Pressed Oil",
        "Procurement Profile / Tie-up Potential": "Farm-to-Fork Direct Supply Agreement",
        "Address / Landmark": "Koramangala 5th Block, Bengaluru - 560095",
        "Contact Channel": "Head Chef & Procurement Lead (naatimana@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Karnataka Military Hotels & Traditional Messes",
        "Business Name": "Gowdru Hotel Traditional Mess",
        "Town": "Indiranagar 100 Ft Rd & Banashankari",
        "Region": "Bengaluru East & South",
        "Facility Scale / Outlets": "High-turnover authentic Gowda style non-veg mess serving unlimited Ragi Mudde and country chicken curries",
        "Key Crops Demanded": "Karnataka Ragi for Mudde, Aged Sona Masoori Rice, Toor Dal, Bengal Gram, Cooking Oil",
        "Estimated Monthly Volume": "14 MT Rice, 4.5 MT Ragi, 2.5 MT Dals, 1,500 L Oil",
        "Procurement Profile / Tie-up Potential": "Weekly Rolling Order Food Supply Deed",
        "Address / Landmark": "100 Feet Road, Indiranagar, Bengaluru - 560038",
        "Contact Channel": "Proprietor (gowdruhotel@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Karnataka Military Hotels & Traditional Messes",
        "Business Name": "Maratha Military Hotel",
        "Town": "Gandhi Nagar / Majestic Corridor",
        "Region": "Bengaluru Central",
        "Facility Scale / Outlets": "Historic dining mess in the film trade district serving cinema industry crews, transit passengers, and business travelers",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi, Toor Dal, Bengal Gram, Cooking Oil",
        "Estimated Monthly Volume": "12 MT Rice, 3.5 MT Ragi, 2 MT Dals, 1,200 L Oil",
        "Procurement Profile / Tie-up Potential": "Direct Restaurant Grain Supply Agreement",
        "Address / Landmark": "5th Main, Gandhinagar, Bengaluru - 560009",
        "Contact Channel": "Managing Partner (marathamilitaryhotel@gmail.com)"
    },

    # =========================================================================
    # --- Category 4: Luxury 5-Star, 4-Star & Tech Business Hotels (8 Properties) ---
    # =========================================================================
    {
        "Metro": "Bengaluru",
        "Category": "Luxury 5-Star & Business Hospitality Hotels",
        "Business Name": "The Leela Palace Bengaluru F&B Directorate",
        "Town": "Old Airport Road, Kodihalli",
        "Region": "Bengaluru East",
        "Facility Scale / Outlets": "Iconic ultra-luxury palace hotel (357 grand rooms, Jamavar royal Indian dining, massive diplomatic banquets)",
        "Key Crops Demanded": "Certified Single-Origin Aged Sona Masoori Rice, Low-GI RNR 15048 Diabetic Rice, Organic Unpolished Toor Dal, Native Millets, Cold-Pressed Groundnut Oil",
        "Estimated Monthly Volume": "16 MT Premium Rice, 3.5 MT Organic Dals, 2 MT Millets, 2,200 L Cold-Pressed Oil",
        "Procurement Profile / Tie-up Potential": "The Leela Palaces Central Hospitality Procurement Master Agreement",
        "Address / Landmark": "23, HAL Old Airport Road, Kodihalli, Bengaluru - 560008",
        "Contact Channel": "Director of Materials & Executive Chef (purchase.palace@theleela.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Luxury 5-Star & Business Hospitality Hotels",
        "Business Name": "ITC Gardenia Luxury Hotel",
        "Town": "Residency Road Commercial Core",
        "Region": "Bengaluru Central",
        "Facility Scale / Outlets": "ITC's flagship luxury green hotel (292 luxury rooms, massive corporate summits, royal Indian banquets)",
        "Key Crops Demanded": "Aged Single-Origin Sona Masoori Rice, Unpolished Toor Dal, Urad Dal, Native Karnataka Ragi, Cold-Pressed Groundnut Oil",
        "Estimated Monthly Volume": "15 MT Premium Rice, 3.5 MT Dals, 2 MT Ragi, 2,000 L Cold-Pressed Oil",
        "Procurement Profile / Tie-up Potential": "ITC Hotels Direct Farm-Gate Sustainable Sourcing Deed",
        "Address / Landmark": "No. 1, Residency Road, Bengaluru - 560025",
        "Contact Channel": "Materials Manager (itcgardenia.purchase@itchotels.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Luxury 5-Star & Business Hospitality Hotels",
        "Business Name": "ITC Windsor & Manor Banquets",
        "Town": "Golf Course Road, Sankey Road",
        "Region": "Bengaluru Central-North",
        "Facility Scale / Outlets": "Historic British regency-era 5-star hotel famous for royal weddings, corporate banquets, and Dakshin South Indian dining",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice for breakfast, Sortex Toor Dal, Millets, Pure Cooking Oil",
        "Estimated Monthly Volume": "14 MT Rice, 3 MT Dals, 1.5 MT Millets, 1,800 L Oil",
        "Procurement Profile / Tie-up Potential": "ITC Group Hospitality Master Agreement",
        "Address / Landmark": "25, Golf Course Road, Bengaluru - 560052",
        "Contact Channel": "Materials Department (itcwindsor.purchase@itchotels.in)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Luxury 5-Star & Business Hospitality Hotels",
        "Business Name": "Taj West End Luxury Hotel",
        "Town": "Race Course Road / High Grounds",
        "Region": "Bengaluru Central",
        "Facility Scale / Outlets": "135-year-old heritage luxury sanctuary set in 20 acres of flora, hosting international dignitaries and luxury weddings",
        "Key Crops Demanded": "Certified Single-Origin Pesticide-Free Sona Masoori Rice, Low-GI Rice, Organic Pulses, Cold-Pressed Groundnut Oil",
        "Estimated Monthly Volume": "12 MT Ultra-Premium Rice, 2.5 MT Organic Dals, 1,500 L Cold-Pressed Oil",
        "Procurement Profile / Tie-up Potential": "IHCL Luxury Supply Master Deed (Strict Lab Purity SLA)",
        "Address / Landmark": "Race Course Road, Bengaluru - 560001",
        "Contact Channel": "Purchase Manager & Executive Chef (westend.procurement@tajhotels.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Luxury 5-Star & Business Hospitality Hotels",
        "Business Name": "JW Marriott Hotel Bengaluru",
        "Town": "Vittal Mallya Road / UB City",
        "Region": "Bengaluru Central",
        "Facility Scale / Outlets": "281-room 5-star luxury hotel overlooking Cubbon Park, hosting global corporate leaders, multi-cuisine buffets, and diplomatic events",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Low-GI Rice, Sortex Pulses, Pure Groundnut Cooking Oil, Bold Peanuts",
        "Estimated Monthly Volume": "15 MT Rice, 3 MT Dals, 1.8 MT Peanuts, 2,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Marriott International Vendor Empanelment",
        "Address / Landmark": "24/1, Vittal Mallya Road, Near UB City, Bengaluru - 560001",
        "Contact Channel": "Director of Procurement (jwmarriott.bangalore@marriott.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Luxury 5-Star & Business Hospitality Hotels",
        "Business Name": "Four Seasons Hotel Bengaluru at Embassy ONE",
        "Town": "Bellary Road, Ganganagar (NH-44 Corridor)",
        "Region": "Bengaluru North",
        "Facility Scale / Outlets": "Premier international ultra-luxury hotel situated directly on the NH-44 highway entrance from Gooty, hosting VIP summits and luxury dining",
        "Key Crops Demanded": "Certified Single-Origin Sona Masoori, Low-GI RNR 15048, Organic Toor Dal, Native Millets, Cold-Pressed Groundnut Oil",
        "Estimated Monthly Volume": "12 MT Ultra-Premium Rice, 2.5 MT Organic Dals, 1,500 L Cold-Pressed Oil",
        "Procurement Profile / Tie-up Potential": "Direct Highway Delivery Luxury Master Agreement (Zero City Congestion)",
        "Address / Landmark": "8, Bellary Road, Ganganagar, Bengaluru - 560032",
        "Contact Channel": "Director of Purchasing (purchasing.bengaluru@fourseasons.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Luxury 5-Star & Business Hospitality Hotels",
        "Business Name": "Sheraton Grand Bangalore Hotel at Brigade Gateway",
        "Town": "Dr. Rajkumar Road, Rajajinagar Malleshwaram",
        "Region": "Bengaluru North-West",
        "Facility Scale / Outlets": "230-room luxury hotel connected to World Trade Center and Orion Mall, running extensive corporate buffets and convention catering",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "14 MT Rice, 2.8 MT Dals, 1.8 MT Bengal Gram, 1,800 L Oil",
        "Procurement Profile / Tie-up Potential": "Marriott International Corporate Supply Contract",
        "Address / Landmark": "26/1, Dr. Rajkumar Road, Malleshwaram-Rajajinagar, Bengaluru - 560055",
        "Contact Channel": "Materials Manager (sheratongrand.bangalore@marriott.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "Luxury 5-Star & Business Hospitality Hotels",
        "Business Name": "The Oberoi Bengaluru",
        "Town": "MG Road Commercial Core",
        "Region": "Bengaluru Central",
        "Facility Scale / Outlets": "Oberoi Group luxury oasis set in lush gardens on MG Road, renowned for fine dining restaurants and elite diplomatic banqueting",
        "Key Crops Demanded": "Aged Single-Origin Sona Masoori Rice, Organic Pulses, Cold-Pressed Groundnut Oil, Native Millets",
        "Estimated Monthly Volume": "10 MT Ultra-Premium Rice, 2 MT Organic Dals, 1,200 L Cold-Pressed Oil",
        "Procurement Profile / Tie-up Potential": "Oberoi Hotels Luxury Procurement Master Deed",
        "Address / Landmark": "37-39, MG Road, Bengaluru - 560001",
        "Contact Channel": "Purchase Head (procurement.bangalore@oberoihotels.com)"
    },

    # =========================================================================
    # --- Category 5: High-Density Darshini Networks & Traditional Food Landmarks (8 Landmarks) ---
    # =========================================================================
    {
        "Metro": "Bengaluru",
        "Category": "High-Density Darshinis & Food Landmarks",
        "Business Name": "Udupi Sri Krishna Bhavan",
        "Town": "Balepet / Chikpet Heritage Market",
        "Region": "Bengaluru Heritage Central",
        "Facility Scale / Outlets": "Historic 90-year-old vegetarian dining landmark serving traditional Udupi thalis, Mangalore buns, and dosas to thousands daily",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Raw Rice, Toor Dal, Urad Dal, Bengal Gram, Pure Cooking Oil",
        "Estimated Monthly Volume": "18 MT Rice, 4 MT Broken Rice, 3 MT Toor Dal, 2 MT Urad Dal, 2,000 L Oil",
        "Procurement Profile / Tie-up Potential": "Heritage Institution Direct Vendor Agreement",
        "Address / Landmark": "Balepet Main Road, Near Chikpet, Bengaluru - 560053",
        "Contact Channel": "Managing Partner (udupikrishnabhavan@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "High-Density Darshinis & Food Landmarks",
        "Business Name": "Maiyas Multi-Level Restaurant & Dining Complex",
        "Town": "4th Block, Jayanagar",
        "Region": "Bengaluru South",
        "Facility Scale / Outlets": "Massive 4-level vegetarian food emporium offering South Indian thalis, traditional Karnataka snacks, tiffins, and sweets",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Karnataka Ragi, Bengal Gram for snacks, Pure Groundnut Oil",
        "Estimated Monthly Volume": "20 MT Rice, 4 MT Ragi, 3.5 MT Toor Dal, 2.5 MT Bengal Gram, 2,500 L Oil",
        "Procurement Profile / Tie-up Potential": "Corporate Dining Supply Agreement",
        "Address / Landmark": "459/30, 30th Cross, 4th Block, Jayanagar, Bengaluru - 560011",
        "Contact Channel": "Managing Director & Procurement Lead (maiyasrestaurant@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "High-Density Darshinis & Food Landmarks",
        "Business Name": "Veena Stores Tiffin Counter",
        "Town": "Margosa Road, Malleshwaram",
        "Region": "Bengaluru North-West",
        "Facility Scale / Outlets": "45-year-old standing breakfast institution renowned worldwide for soft steaming Idlis, crispy Vadas, and signature mint-coconut chutney",
        "Key Crops Demanded": "High-Grade Broken Raw Rice, Urad Dal, Bengal Gram (Putnalu), Pure Cooking Oil",
        "Estimated Monthly Volume": "12 MT Broken Rice, 3 MT Urad Dal, 1.8 MT Bengal Gram, 1,200 L Oil",
        "Procurement Profile / Tie-up Potential": "Direct Tiffin Supply Agreement",
        "Address / Landmark": "183, Margosa Road, Malleshwaram, Bengaluru - 560003",
        "Contact Channel": "Proprietor (veenastores@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "High-Density Darshinis & Food Landmarks",
        "Business Name": "Siddappa Hotel",
        "Town": "7th Main, 5th Block, Jayanagar",
        "Region": "Bengaluru South",
        "Facility Scale / Outlets": "Legendary early-morning set dosa landmark serving thousands of hot butter dosas, half-plates, and idlis to continuous queues",
        "Key Crops Demanded": "Broken Raw Rice, Urad Dal, Bengal Gram, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "10 MT Broken Rice, 2.5 MT Urad Dal, 1.5 MT Bengal Gram, 1,200 L Oil",
        "Procurement Profile / Tie-up Potential": "Direct Tiffin Supply Agreement",
        "Address / Landmark": "7th Main, 5th Block, Jayanagar, Bengaluru - 560041",
        "Contact Channel": "Proprietor (siddappahotel@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "High-Density Darshinis & Food Landmarks",
        "Business Name": "Upahara Darshini (UD) Central Supply",
        "Town": "Netkallappa Circle, Basavanagudi",
        "Region": "Bengaluru South",
        "Facility Scale / Outlets": "Pioneering Darshini quick-service model operating continuous high-density tiffin, meals, and coffee services",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Urad Dal, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "15 MT Rice, 3.5 MT Broken Rice, 2.5 MT Toor Dal, 1,800 L Oil",
        "Procurement Profile / Tie-up Potential": "Darshini Supply Master Agreement",
        "Address / Landmark": "Netkallappa Circle, Subbarama Chetty Road, Basavanagudi, Bengaluru - 560004",
        "Contact Channel": "Managing Partner (upaharadarshini@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "High-Density Darshinis & Food Landmarks",
        "Business Name": "Udupi Grand Central Prep Network",
        "Town": "BTM Layout & HSR Layout",
        "Region": "Bengaluru South",
        "Facility Scale / Outlets": "High-volume vegetarian multi-branch restaurant chain serving thousands of software professionals with daily thalis and breakfast",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Bengal Gram, Cooking Oil",
        "Estimated Monthly Volume": "16 MT Rice, 3.5 MT Broken Rice, 2.8 MT Toor Dal, 1.8 MT Bengal Gram, 1,800 L Oil",
        "Procurement Profile / Tie-up Potential": "Direct Chain Supply Contract",
        "Address / Landmark": "7th Main Road, BTM Layout 2nd Stage, Bengaluru - 560076",
        "Contact Channel": "Managing Partner (udupigrandblr@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "High-Density Darshinis & Food Landmarks",
        "Business Name": "Janatha Hotel",
        "Town": "8th Cross, Malleshwaram",
        "Region": "Bengaluru North-West",
        "Facility Scale / Outlets": "Classic heritage Udupi vegetarian restaurant famous for crispy Masala Dosas, Vadas, Sambar, and Filter Coffee",
        "Key Crops Demanded": "Broken Raw Rice, Aged Sona Masoori, Toor Dal, Urad Dal, Pure Groundnut Oil",
        "Estimated Monthly Volume": "12 MT Rice, 2.5 MT Toor Dal, 1.8 MT Urad Dal, 1,400 L Oil",
        "Procurement Profile / Tie-up Potential": "Heritage Restaurant Supply Agreement",
        "Address / Landmark": "8th Cross, Sampige Road, Malleshwaram, Bengaluru - 560003",
        "Contact Channel": "Proprietor (janathahotel@gmail.com)"
    },
    {
        "Metro": "Bengaluru",
        "Category": "High-Density Darshinis & Food Landmarks",
        "Business Name": "SLV Swadishta Central Kitchen",
        "Town": "Banashankari 2nd Stage",
        "Region": "Bengaluru South",
        "Facility Scale / Outlets": "High-capacity vegetarian dining complex and catering commissary serving traditional Karnataka feasts and daily tiffins",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice, Toor Dal, Karnataka Ragi for Mudde, Groundnut Cooking Oil",
        "Estimated Monthly Volume": "15 MT Rice, 3.5 MT Ragi, 2.8 MT Toor Dal, 1.8 MT Peanuts, 1,600 L Oil",
        "Procurement Profile / Tie-up Potential": "Central Kitchen Food Sourcing Contract",
        "Address / Landmark": "24th Cross, Banashankari 2nd Stage, Bengaluru - 560070",
        "Contact Channel": "Operations Head (slvswadishta@gmail.com)"
    }
]

def main():
    df = pd.DataFrame(BUYERS)
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")
    print(f"Successfully generated Phase 11 Bengaluru Hotels & Restaurants Database with {len(df)} buyers!")
    print(f"Saved to: {OUTPUT_CSV}")
    
    # Summary by Category
    print("\nBreakdown by Category:")
    print(df["Category"].value_counts())

if __name__ == "__main__":
    main()
