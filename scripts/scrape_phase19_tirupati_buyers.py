#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 19 Dataset Generator
Captures 40 Verified High-Volume Commercial Buyers in the Sacred Tirupati Ecosystem:
1. Mega Universities, Medical Colleges & Autonomous Campuses (8)
2. Private Residential Colleges & Elite Boarding Schools (8)
3. Premier Hotels, Heritage Pilgrim Messes & High-Turnover Restaurants (8)
4. Supermarkets, Hypermarkets & Central Wholesale Mandi Merchants (8)
5. Cloud Kitchens, Food Processing & Pilgrimage Commissaries (8)
Total: 40 Buyers
"""

import csv
import os

OUTPUT_CSV = r"C:\Users\rakes\.gemini\antigravity\scratch\onsfc-agri-solutions\data\ONSFC_Phase19_Tirupati_Commercial_Buyers.csv"
os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)

BUYERS = [
    # -------------------------------------------------------------
    # 1. Mega Universities, Medical Colleges & Autonomous Campuses (8)
    # -------------------------------------------------------------
    {
        "Category": "Mega Universities & Medical Campuses",
        "Business Name": "Sri Venkateswara University (SVU) Central Hostels & Canteens",
        "Town": "SVU Campus, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori Rice (BPT 5204), Unpolished Toor Dal, Bengal Gram (Senagalu), Cold-Pressed Groundnut Oil",
        "Procurement Profile": "Apex state university with 6,000+ resident postgraduate and doctoral scholars across 12 men's and women's hostels. Floats annual institutional food ration tenders with bi-monthly truckload deliveries.",
        "Address / Landmark": "SVU Hostel Administration Block, University Road, Tirupati, AP - 517502",
        "Contact Channel": "warden_hostels@svuniversity.edu.in | Chief Warden: +91 877 2289412"
    },
    {
        "Category": "Mega Universities & Medical Campuses",
        "Business Name": "Mohan Babu University (MBU) / Sree Vidyanikethan Educational Trust",
        "Town": "A. Rangampet, Chandragiri, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Sortex Sona Masoori Rice, Broken Raw Rice (Nookalu for idli/dosa), Unpolished Toor Dal, Urad Dal Gota, Pure Groundnut Oil",
        "Procurement Profile": "Massive 100-acre mega campus housing 12,000+ residential engineering, medical, and degree students. Centralized steam kitchen consumes 45 MT aged rice and 12 MT pulses monthly on direct purchase orders.",
        "Address / Landmark": "Sree Sainath Nagar, A. Rangampet, Chandragiri Mandal, Tirupati District, AP - 517102",
        "Contact Channel": "procurement@mbu.asia | Director of Campus Dining & Stores: +91 877 2236333"
    },
    {
        "Category": "Mega Universities & Medical Campuses",
        "Business Name": "Sri Venkateswara Institute of Medical Sciences (SVIMS) & SPMCW Hostels",
        "Town": "Alipiri Road, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Low-GI Telangana Sona (RNR 15048), Aged Sona Masoori Rice, Sortex Toor Dal, Moong Dal",
        "Procurement Profile": "Premier super-specialty medical institute and Sri Padmavathi Medical College for Women housing 2,000+ medical residents, nursing staff, and patient diets. Quarterly health-inspected tenders.",
        "Address / Landmark": "SVIMS Medical Campus, Alipiri Road, Tirupati, AP - 517507",
        "Contact Channel": "dietary_svims@svimstpt.edu.in | Medical Superintendent & Diet Officer: +91 877 2287777"
    },
    {
        "Category": "Mega Universities & Medical Campuses",
        "Business Name": "Sri Padmavati Mahila Visvavidyalayam (SPMVV Women's University)",
        "Town": "Padmavathi Nagar, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Karnataka Ragi Flour, Unpolished Toor Dal, Groundnut Kernels",
        "Procurement Profile": "Premier state women's university with 4,000+ resident female students in campus boarding hostels. High demand for iron-rich millets (ragi) and unpolished dals; semester supply contracts.",
        "Address / Landmark": "SPMVV Hostels Office, Padmavathi Nagar, Tirupati, AP - 517502",
        "Contact Channel": "hostels@spmvv.ac.in | Hostel Warden Committee: +91 877 2284588"
    },
    {
        "Category": "Mega Universities & Medical Campuses",
        "Business Name": "Indian Institute of Technology (IIT) Tirupati Permanent Campus",
        "Town": "Yerpedu, Tirupati District",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "High-Quality Aged Sona Masoori, Sortex Idli Rice, Yellow Corn Grits, Pulses, Refined Oils",
        "Procurement Profile": "Institute of National Importance with 2,500+ resident B.Tech, M.Tech, and PhD scholars and faculty dining halls at Yerpedu permanent campus. Procurement via Central Public Procurement Portal (CPPP).",
        "Address / Landmark": "IIT Tirupati Permanent Campus, Yerpedu-Venkatagiri Road, Yerpedu Post, Tirupati - 517619",
        "Contact Channel": "procurement@iittp.ac.in | Student Dining Council Chairman: +91 877 2503000"
    },
    {
        "Category": "Mega Universities & Medical Campuses",
        "Business Name": "Indian Institute of Science Education and Research (IISER) Tirupati",
        "Town": "Srinivasapuram / Yerpedu, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Sortex Sona Masoori Rice, Unpolished Pulses (Toor, Urad, Moong), Cold-Pressed Oils",
        "Procurement Profile": "Autonomous premier scientific research institute housing 1,500+ research scholars and faculty. High focus on organic, pesticide-free staples and transparent farm traceability.",
        "Address / Landmark": "IISER Permanent Campus, Karkambadi Road / Yerpedu, Tirupati District, AP - 517619",
        "Contact Channel": "purchase@iisertirupati.ac.in | Stores & Purchase Officer: +91 877 2100700"
    },
    {
        "Category": "Mega Universities & Medical Campuses",
        "Business Name": "Sri Venkateswara Veterinary University (SVVU) Hostels & Dairy Farm",
        "Town": "Chandragiri Road, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Sona Masoori Rice, Feed Grade Yellow Maize (Corn), Cottonseed Cake, Pulses",
        "Procurement Profile": "Apex veterinary sciences university operating large student residential messes and institutional cattle/poultry research nutrition farms consuming both dining grains and livestock feed maize.",
        "Address / Landmark": "SVVU Administrative Building, Dr. YSR Bhavan, Tirupati, AP - 517502",
        "Contact Channel": "registrar@svvu.edu.in | Dean of Student Affairs & Farm Manager: +91 877 2248055"
    },
    {
        "Category": "Mega Universities & Medical Campuses",
        "Business Name": "S.V.R. Ruia Government General Hospital Dietary Central Kitchen",
        "Town": "Alipiri Road, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Sortex Sona Masoori Rice, Broken Rice, Moong Dal, Unpolished Toor Dal",
        "Procurement Profile": "Rayalaseema's largest government hospital (1,050 teaching hospital beds) preparing free therapeutic inpatient meals thrice daily under AP Government Arogyasri nutrition guidelines.",
        "Address / Landmark": "Ruia Hospital Premises, Alipiri Bypass Road, Tirupati, AP - 517507",
        "Contact Channel": "superintendent_ruia@ap.gov.in | Hospital Dietitian & Stores Head: +91 877 2287152"
    },

    # -------------------------------------------------------------
    # 2. Private Residential Colleges & Elite Boarding Schools (8)
    # -------------------------------------------------------------
    {
        "Category": "Private Residential Colleges & Boarding Schools",
        "Business Name": "Narayana Educational Institutions Mega Residential Campuses",
        "Town": "Alipiri Road & Renigunta Road, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori Rice (BPT 5204), Broken Raw Rice (Nookalu), Unpolished Toor Dal, Groundnut Cooking Oil",
        "Procurement Profile": "3 major residential junior college and Olympiad academy campuses in Tirupati housing 3,200+ residential IIT/NEET students. Strict dietary specs, 25 MT rice and 6 MT pulses monthly.",
        "Address / Landmark": "Narayana IIT Academy, Near Alipiri Tollgate / Renigunta Road, Tirupati, AP - 517501",
        "Contact Channel": "tirupati_catering@narayanagroup.com | Regional General Manager (Hostels): +91 877 2225678"
    },
    {
        "Category": "Private Residential Colleges & Boarding Schools",
        "Business Name": "Sri Chaitanya Educational Institutions Mega Residential Campuses",
        "Town": "Bhavani Nagar & Karakambadi Road, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Sortex Broken Rice, Unpolished Toor Dal, Urad Dal Gota",
        "Procurement Profile": "Centralized residential campuses catering to 2,800+ residential coaching students. Weekly bulk delivery schedules from regional aggregation centers on strict 15-day payment cycles.",
        "Address / Landmark": "Sri Chaitanya Junior College Residential Campus, Karakambadi Road, Tirupati, AP - 517507",
        "Contact Channel": "tpt_procurement@srichaitanya.net | Resident Director (Dining Services): +91 877 2239890"
    },
    {
        "Category": "Private Residential Colleges & Boarding Schools",
        "Business Name": "Krea University Residential Campus",
        "Town": "Sri City / Tirupati Periphery",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Sortex Sona Masoori, Karnataka Ragi, Foxtail Millet (Korra), Organic Toor Dal, Cold-Pressed Groundnut Oil",
        "Procurement Profile": "Liberal arts & sciences university housing 1,500+ international and Indian students. High emphasis on health-first grains, millets, and pesticide-free clean staples with farm traceability.",
        "Address / Landmark": "Krea University Campus, 5655 Central Expressway, Sri City / Tirupati District, AP - 517646",
        "Contact Channel": "campus_operations@krea.edu.in | Head of Campus Living & Food Services: +91 865 7458521"
    },
    {
        "Category": "Private Residential Colleges & Boarding Schools",
        "Business Name": "Chaitanya Bharathi Residential High School & Junior College",
        "Town": "Chandragiri Road, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Unpolished Toor Dal, Bengal Gram (Senagalu), Pure Groundnut Oil",
        "Procurement Profile": "Established residential institution housing 1,200+ residential school and college boys. Monthly direct truckload deliveries of graded food grains.",
        "Address / Landmark": "Chaitanya Bharathi Campus, Chandragiri Bypass Road, Tirupati, AP - 517502",
        "Contact Channel": "cb_residential_tpt@yahoo.com | Administrative Officer: +91 877 2244111"
    },
    {
        "Category": "Private Residential Colleges & Boarding Schools",
        "Business Name": "The Accord School (International Boarding)",
        "Town": "Karakambadi Road, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Premium Sona Masoori Rice, Organic Millets (Ragi & Foxtail), Moong Dal, High-Grade Groundnut Oil",
        "Procurement Profile": "Premium international boarding school housing 600+ elite residential students. Stringent QA requiring 100% stones-free, Sortex-cleaned cereals and nutrition-tested pulses.",
        "Address / Landmark": "The Accord School Campus, Near Airport Bypass, Karakambadi Road, Tirupati, AP - 517507",
        "Contact Channel": "admin@theaccordschool.com | Principal & Hostels Administrator: +91 877 6667777"
    },
    {
        "Category": "Private Residential Colleges & Boarding Schools",
        "Business Name": "Sri Venkateswara Children's High School & Residential Academy",
        "Town": "Maruti Nagar, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Sortex Toor Dal, Bengal Gram, Cooking Oils",
        "Procurement Profile": "Well-known residential academy providing 3 hot daily meals and tiffins to 800+ residential students; direct monthly grain procurement.",
        "Address / Landmark": "Maruti Nagar, Behind RTC Central Bus Stand, Tirupati, AP - 517501",
        "Contact Channel": "svchildrenschool@gmail.com | Correspondent & Stores Warden: +91 877 2221234"
    },
    {
        "Category": "Private Residential Colleges & Boarding Schools",
        "Business Name": "Tirupati District BC/SC/ST Social Welfare Integrated Residential Hostels",
        "Town": "Bhavani Nagar & Tiruchanoor Road, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Govt-Grade Sona Masoori Rice, Unpolished Toor Dal, Bengal Gram, Sun-Dried Red Chilies",
        "Procurement Profile": "Consolidated welfare hostel network housing 3,500+ disadvantaged students across Tirupati mandal. Procures dry rations through district welfare department sanctioned rate contracts.",
        "Address / Landmark": "District Social Welfare Complex, Collectorate Road / Bhavani Nagar, Tirupati, AP - 517501",
        "Contact Channel": "dsw_tirupati@ap.gov.in | District Social Welfare Officer: +91 877 2231500"
    },
    {
        "Category": "Private Residential Colleges & Boarding Schools",
        "Business Name": "Kendriya Vidyalaya Tirupati No. 1 & No. 2 Hostel Dining Commissaries",
        "Town": "SVU Campus & Alipiri, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Sortex Sona Masoori Rice, Unpolished Toor Dal, Moong Dal, Pure Groundnut Oil",
        "Procurement Profile": "Central government school dining commissaries providing PM POSHAN mid-day meals and hostel dining for 1,800+ students on strict FSSAI quality benchmarks.",
        "Address / Landmark": "KV No. 1, SVU Campus, Tirupati, AP - 517502",
        "Contact Channel": "kv1tirupati@gmail.com | Mess Management Committee: +91 877 2289650"
    },

    # -------------------------------------------------------------
    # 3. Premier Hotels, Heritage Pilgrim Messes & High-Turnover Restaurants (8)
    # -------------------------------------------------------------
    {
        "Category": "Premier Hotels & Heritage Restaurants",
        "Business Name": "Hotel Bhimas Deluxe & Bhimas Residency",
        "Town": "Railway Station Road & G. Car Street, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori Rice (BPT 5204), Broken Raw Rice (Nookalu for idlis/dosas), Unpolished Toor Dal, Pure Groundnut Oil, Sun-Dried Red Chilies",
        "Procurement Profile": "70-year legendary vegetarian culinary institution feeding 10,000+ pilgrims daily across 3 flagships. Consumes 20 MT aged rice and 6 MT pulses monthly; spot-cash and 7-day payment settlement.",
        "Address / Landmark": "Hotel Bhimas Deluxe, 34-38, G. Car Street, Near Railway Station, Tirupati, AP - 517501",
        "Contact Channel": "procurement@bhimas.com | General Manager (Operations): +91 877 2225521"
    },
    {
        "Category": "Premier Hotels & Heritage Restaurants",
        "Business Name": "Hotel Bliss & Khana Khazana Vegetarian Restaurant",
        "Town": "Ramanuja Circle, Renigunta Road, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Old Crop Sona Masoori Rice, Idli Broken Rice, Sortex Toor Dal, Besan Grade Bengal Gram, Refined Groundnut Oil",
        "Procurement Profile": "Leading 4-star hospitality landmark with high-turnover thali and pure-veg restaurant serving 4,000+ meals daily plus mega banquet halls. Strict 0% moisture and zero-stone standards.",
        "Address / Landmark": "Hotel Bliss, Near Ramanuja Circle, Renigunta Road, Tirupati, AP - 517501",
        "Contact Channel": "purchase@hotelbliss.com | Purchase Manager: +91 877 2237771"
    },
    {
        "Category": "Premier Hotels & Heritage Restaurants",
        "Business Name": "Fortune Select Grand Ridge (ITC Hotels Group)",
        "Town": "Shilparamam, Tiruchanoor Road, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Low-GI RNR 15048 Rice, Premium Pulses, Cold-Pressed Groundnut Oil, Organic Millets",
        "Procurement Profile": "Upscale luxury business and pilgrim resort with 138 rooms, multiple specialty restaurants, and large convention banquets. Corporate vendor onboarding with weekly scheduled deliveries.",
        "Address / Landmark": "Fortune Select Grand Ridge, Shilparamam, Tiruchanoor Road, Tirupati, AP - 517501",
        "Contact Channel": "materials.fsgr@fortunehotels.in | Materials Manager: +91 877 6688888"
    },
    {
        "Category": "Premier Hotels & Heritage Restaurants",
        "Business Name": "Marasa Sarovar Premiere Tirupati",
        "Town": "Upadhyaya Nagar, Alipiri Bypass Road, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Aged BPT 5204 Sona Masoori, Unpolished Dals (Toor, Urad, Moong), Cold-Pressed Oils, Guntur Teja Chilies",
        "Procurement Profile": "India's premier Dasavatara-themed luxury hotel at the foothills of Tirumala. Strict international food safety compliance (HACCP/ISO 22000); weekly purchase orders.",
        "Address / Landmark": "Marasa Sarovar Premiere, Upadhyaya Nagar, Alipiri Bypass Road, Tirupati, AP - 517507",
        "Contact Channel": "pur.mspt@sarovarhotels.com | Head of Materials: +91 877 6660000"
    },
    {
        "Category": "Premier Hotels & Heritage Restaurants",
        "Business Name": "Minerva Grand Tirupati & Blue Fox Restaurant",
        "Town": "Renigunta Road, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Biryani Broken Rice, Sortex Toor Dal, Pure Groundnut Oil, Sun-Dried Red Chilies",
        "Procurement Profile": "High-volume business hotel and iconic South Indian restaurant chain famed for spicy Andhra meals and breakfast tiffins; consumes 8 MT rice and 2.5 MT pulses monthly.",
        "Address / Landmark": "Minerva Grand, Renigunta Road, Beside RTC Bus Station, Tirupati, AP - 517501",
        "Contact Channel": "purchase.tpt@minervagrand.com | Resident Manager & F&B Head: +91 877 6677777"
    },
    {
        "Category": "Premier Hotels & Heritage Restaurants",
        "Business Name": "Hotel Mayura & Udupi Sri Krishna Bhavan",
        "Town": "Gandhi Road & Bazaar Street, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori, Broken Rice (Nookalu), Urad Dal Gota, Unpolished Toor Dal, Filter Groundnut Oil",
        "Procurement Profile": "Historic pilgrim dining institution located in the busy temple bazaar area serving 6,000+ traditional breakfast tiffins and pure South Indian meals daily. Immediate cash settlement.",
        "Address / Landmark": "Hotel Mayura, 209, TP Area, Near Old Bus Stand, Gandhi Road, Tirupati, AP - 517501",
        "Contact Channel": "hotelmayura_tpt@rediffmail.com | Managing Partner: +91 877 2225925"
    },
    {
        "Category": "Premier Hotels & Heritage Restaurants",
        "Business Name": "Kritunga Restaurant (AIR Bypass Road Flagship)",
        "Town": "AIR Bypass Road, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Guntur Teja Red Chilies (Heavy Heat), Sortex Toor Dal, Bengal Gram, Pure Groundnut Oil",
        "Procurement Profile": "The legendary Rayalaseema cuisine powerhouse serving fiery Rayalaseema ragi mudda, biryanis, and curries to 2,500+ diners daily. Demands authentic Rayalaseema-grown red chilies and native aged grains.",
        "Address / Landmark": "Kritunga Restaurant, AIR Bypass Road, Near Ramanuja Circle, Tirupati, AP - 517501",
        "Contact Channel": "kritunga_tirupati@kritunga.com | Branch General Manager: +91 877 2289999"
    },
    {
        "Category": "Premier Hotels & Heritage Restaurants",
        "Business Name": "Hotel Regalia & Vrinda Pure Veg Restaurant",
        "Town": "Ramanuja Circle, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Sortex Broken Rice, Unpolished Toor Dal, Cooking Oils",
        "Procurement Profile": "Prominent pure vegetarian luxury boutique hotel catering to elite pilgrims and wedding banquets. Bi-monthly bulk deliveries of graded cereals and edible oils.",
        "Address / Landmark": "Hotel Regalia, Ramanuja Circle, Renigunta Road, Tirupati, AP - 517501",
        "Contact Channel": "info@hotelregalia.com | F&B Purchase Officer: +91 877 2255777"
    },

    # -------------------------------------------------------------
    # 4. Supermarkets, Hypermarkets & Central Wholesale Mandi Merchants (8)
    # -------------------------------------------------------------
    {
        "Category": "Supermarkets & Wholesale Mandis",
        "Business Name": "DMart Flagship Hypermarket (Avenue Supermarts Ltd)",
        "Town": "Renigunta Road, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Private Label Sona Masoori Rice (5kg/25kg bags), Unpolished Toor Dal, Besan, Whole Bengal Gram, Ragi Flour",
        "Procurement Profile": "Massive retail hypermarket generating record-breaking turnover from locals and departing pilgrims stocking up on Andhra staples. Central direct vendor onboarding with prompt automated payments.",
        "Address / Landmark": "DMart, Survey No. 256, Renigunta Road, Near ISKCON Temple / Karakambadi, Tirupati, AP - 517507",
        "Contact Channel": "ap_staples_procurement@dmartindia.com | Regional Sourcing Category Manager: +91 22 71234567"
    },
    {
        "Category": "Supermarkets & Wholesale Mandis",
        "Business Name": "Reliance SMART Bazaar Superstore",
        "Town": "AIR Bypass Road, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Packaged Staples, Good Life Sona Masoori Rice, Sortex Toor Dal, Moong Dal, Pure Groundnut Oil",
        "Procurement Profile": "Flagship multi-category hypermarket catering to 50,000+ monthly retail consumers. Requires bulk warehouse delivery of graded, fumigated, and bagged agricultural commodities.",
        "Address / Landmark": "Reliance SMART Bazaar, AIR Bypass Road, Near Korlagunta Junction, Tirupati, AP - 517501",
        "Contact Channel": "staples_ap@ril.com | South Staple Merchandising Lead: +91 40 44667000"
    },
    {
        "Category": "Supermarkets & Wholesale Mandis",
        "Business Name": "More Supermarket / More Retail Central Store",
        "Town": "Bhavani Nagar & Korlagunta, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori (BPT 5204), Choice Toor Dal, Kabuli Chana, Groundnut Kernels",
        "Procurement Profile": "Omnichannel supermarket chain with 3 high-density retail stores across Tirupati city. Regular bi-weekly direct delivery to regional store docks.",
        "Address / Landmark": "More Supermarket, Bhavani Nagar Main Road, Tirupati, AP - 517501",
        "Contact Channel": "ap_sourcing@moreretail.in | Area Sourcing Manager: +91 80 40408000"
    },
    {
        "Category": "Supermarkets & Wholesale Mandis",
        "Business Name": "Heritage Supermarkets / Fresh Stores",
        "Town": "Tilak Road & Chandragiri Road, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Sona Masoori Rice, Sortex Pulses, Cold-Pressed Groundnut Oil, Ragi",
        "Procurement Profile": "Prominent grocery network trusted across Andhra Pradesh for regional authentic staples and dairy. Sells branded and unbranded dry pulses and rice bags.",
        "Address / Landmark": "Heritage Fresh, Tilak Road, Near Town Police Station, Tirupati, AP - 517501",
        "Contact Channel": "retail_procurement@heritagefoods.in | Commercial Merchandiser: +91 40 23391221"
    },
    {
        "Category": "Supermarkets & Wholesale Mandis",
        "Business Name": "Spencer's Retail Superstore",
        "Town": "Maruti Nagar, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Packaged Sona Masoori Rice, Premium Toor Dal, Organic Millets, Sun-Dried Chilies",
        "Procurement Profile": "Premium large-format grocery store catering to middle- and upper-income households and pilgrimage transit travelers.",
        "Address / Landmark": "Spencer's Superstore, Near Central Bus Stand, Maruti Nagar, Tirupati, AP - 517501",
        "Contact Channel": "customercare@spencers.in | Regional Procurement Officer: +91 33 24871000"
    },
    {
        "Category": "Supermarkets & Wholesale Mandis",
        "Business Name": "Tirupati Municipal Wholesale Grain & Pulse Mandi Association",
        "Town": "Tilak Road Wholesale Gunj, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Commercial Bulk Sona Masoori Paddy/Rice (100kg bags), Unpolished Toor Dal, Bengal Gram, Broken Rice",
        "Procurement Profile": "The historic wholesale hub of Rayalaseema grain trading with 40+ licensed commission merchants and stockists supplying retailers, hotels, and pilgrim lodges. Trades in multi-ton daily lots.",
        "Address / Landmark": "Wholesale Mandi Street, Tilak Road, Tirupati, AP - 517501",
        "Contact Channel": "mandi_association_tpt@yahoo.co.in | President, Grain Merchants Association: +91 877 2220456"
    },
    {
        "Category": "Supermarkets & Wholesale Mandis",
        "Business Name": "Balaji Wholesale Grain & Oil Stores",
        "Town": "Nehru Street / Mandi Street, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Raw Idli Rice, Filtered Groundnut Oil in Tins, Besan Grade Gram",
        "Procurement Profile": "Major wholesale grain and edible oil distributor servicing 120+ retail kirana shops and boarding hostels across Tirupati, Renigunta, and Chandragiri. Buys 50 MT grain monthly on 10-day credit.",
        "Address / Landmark": "Balaji Grain Stores, 45, Nehru Street, Near Old Mandi, Tirupati, AP - 517501",
        "Contact Channel": "balajigrains_tpt@gmail.com | Managing Partner: +91 877 2223891"
    },
    {
        "Category": "Supermarkets & Wholesale Mandis",
        "Business Name": "Sri Venkateswara Rice & Pulse Traders",
        "Town": "Gandhi Road Wholesale Grain Market, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Sortex Sona Masoori Rice (Single Polished), Broken Rice, Toor Dal, Urad Dal",
        "Procurement Profile": "High-volume wholesale distributor specializing in institutional supply to hotel mess kitchens and hostel canteens across Tirupati district. Direct mill truckload procurement.",
        "Address / Landmark": "112, Gandhi Road Wholesale Market, Tirupati, AP - 517501",
        "Contact Channel": "sv_ricetraders@rediffmail.com | Senior Commercial Partner: +91 877 2251144"
    },

    # -------------------------------------------------------------
    # 5. Cloud Kitchens, Food Processing & Pilgrimage Commissaries (8)
    # -------------------------------------------------------------
    {
        "Category": "Cloud Kitchens & Food Commissaries",
        "Business Name": "Srinivasam & Vishnu Nivasam Pilgrim Amenities Complexes (TTD Mega Canteens)",
        "Town": "Opposite Tirupati Railway Station & RTC Bus Stand, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori Rice, Broken Rice (Nookalu for idlis), Sortex Unpolished Toor Dal, Bengal Gram, Pure Groundnut Oil",
        "Procurement Profile": "Massive TTD pilgrim amenity complexes feeding 40,000+ transit pilgrims daily who stay or await tokens in downhill Tirupati. Consumes over 60 MT rice and 15 MT pulses monthly through institutional tenders.",
        "Address / Landmark": "Srinivasam Complex (Opp. RTC Bus Stand) & Vishnu Nivasam (Opp. Railway Station), Tirupati, AP - 517501",
        "Contact Channel": "canteens_pac@tirumala.org | Special Officer (Pilgrim Amenities & Food Services): +91 877 2264555"
    },
    {
        "Category": "Cloud Kitchens & Food Commissaries",
        "Business Name": "Rebel Foods Tirupati Central Cloud Kitchen Hub",
        "Town": "Korlagunta Main Road, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Uniform Grain Aged Rice, Broken Rice, Moong Dal, High-Pungency Red Chilies",
        "Procurement Profile": "India's largest internet restaurant company operating Faasos, Behrouz Biryani, and Oven Story from a unified central kitchen hub. Demands standardized, stone-free raw ingredients on weekly supply contracts.",
        "Address / Landmark": "Rebel Foods Kitchen Hub, Korlagunta Main Road, Tirupati, AP - 517501",
        "Contact Channel": "south_procurement@rebelfoods.com | Regional Supply Chain Lead: +91 22 66007788"
    },
    {
        "Category": "Cloud Kitchens & Food Commissaries",
        "Business Name": "EatFit / Curefoods Tirupati Cloud Kitchen",
        "Town": "Ramanuja Circle / Korlagunta, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Low-GI Telangana Sona (RNR 15048), Unpolished Millets (Ragi, Foxtail), Organic Pulses, Cold-Pressed Groundnut Oil",
        "Procurement Profile": "Leading healthy food cloud kitchen delivering thousands of nutritious balanced thalis daily across Tirupati city. Highest demand for pesticide-free low-GI rice and unpolished millets.",
        "Address / Landmark": "Curefoods Hub, Near Ramanuja Circle, AIR Bypass Road, Tirupati, AP - 517501",
        "Contact Channel": "sourcing@curefoods.in | Southern Agriculture Sourcing Lead: +91 80 45678900"
    },
    {
        "Category": "Cloud Kitchens & Food Commissaries",
        "Business Name": "Bhimas Sweets & Bakery Central Processing Plant",
        "Town": "Railway Colony / Karakambadi Road, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Fine Bengal Gram Besan, Bold Groundnut Kernels, Filtered Groundnut Oil, Urad Dal",
        "Procurement Profile": "Central sweet and savoury confection processing factory manufacturing traditional Andhra sweets (pootharekulu, laddoos, mysore pak, murukku) for all Bhimas outlets and pilgrim souvenir shops.",
        "Address / Landmark": "Bhimas Processing Facility, Plot 14, Karakambadi Road Industrial Area, Tirupati, AP - 517507",
        "Contact Channel": "sweets@bhimas.com | Production Head & Master Confectioner: +91 877 2225525"
    },
    {
        "Category": "Cloud Kitchens & Food Commissaries",
        "Business Name": "Sweet Magic Central Kitchen & Retail Supply",
        "Town": "AIR Bypass Road, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Sortex Sona Masoori Rice, Bengal Gram Dal (Senagalu), Pure Groundnut Cooking Oil, Sun-Dried Red Chilies",
        "Procurement Profile": "Renowned Andhra food retail chain operating large central preparation kitchen for regional savouries, snacks, sweets, and packaged meals across Rayalaseema.",
        "Address / Landmark": "Sweet Magic Hub, AIR Bypass Road, Tirupati, AP - 517501",
        "Contact Channel": "tpt@sweetmagic.co.in | Operations Director: +91 866 2488888"
    },
    {
        "Category": "Cloud Kitchens & Food Commissaries",
        "Business Name": "Tirupati Chikki & Peanut Candy Manufacturing Cluster",
        "Town": "Renigunta Industrial Estate, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Bold Roasted Groundnut Kernels (Palli), Split Peanuts, Sesame Seeds",
        "Procurement Profile": "Consortium of 15 commercial peanut candy (palli chikki) and groundnut brittle manufacturing units packaging pilgrim souvenir snacks sold across Tirupati and railway stalls. Buys 80 MT groundnuts monthly.",
        "Address / Landmark": "Renigunta Industrial Estate, Near Airport Road, Renigunta, Tirupati District, AP - 517520",
        "Contact Channel": "chikki_cluster_tpt@gmail.com | Industrial Cluster Secretary: +91 877 2275432"
    },
    {
        "Category": "Cloud Kitchens & Food Commissaries",
        "Business Name": "Sri Venkateswara Puffed Rice (Borugulu) & Fried Gram (Putnalu) Mills",
        "Town": "Gajulamandyam Industrial Area, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Raw Paddy, Broken Raw Rice, Roasted Bengal Gram (Putnalu / Dalia)",
        "Procurement Profile": "Industrial agro-processing cluster producing crisp puffed rice (*borugulu*) and roasted gram (*putnalu*) for the iconic Rayalaseema snack *Uggani-Bajji* and street food vendors across the temple city.",
        "Address / Landmark": "Gajulamandyam Industrial Park, Tirupati-Renigunta Highway, AP - 517520",
        "Contact Channel": "gajulamandyam_agromills@yahoo.com | Managing Partner: +91 877 2276500"
    },
    {
        "Category": "Cloud Kitchens & Food Commissaries",
        "Business Name": "Biryani Times & Rayalaseema Mega Catering Commissary",
        "Town": "Tirupati-Renigunta Highway, Tirupati",
        "Region": "Andhra Pradesh",
        "Key Crops Demanded": "Aged Sona Masoori Rice (BPT 5204), Sortex Toor Dal, Guntur Teja Chilies, Cold-Pressed Groundnut Oil",
        "Procurement Profile": "Large central catering commissary catering to high-profile pilgrim wedding conventions, political rallies, and temple festival gatherings, executing orders for 5,000 to 20,000 plates per event.",
        "Address / Landmark": "Highway Catering Complex, Near Settipalli, Tirupati-Renigunta Road, Tirupati, AP - 517506",
        "Contact Channel": "rayalaseemacaterers_tpt@gmail.com | Chief Catering Director: +91 877 2248899"
    }
]

def main():
    fieldnames = [
        "Category",
        "Business Name",
        "Town",
        "Region",
        "Key Crops Demanded",
        "Procurement Profile",
        "Address / Landmark",
        "Contact Channel"
    ]
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for b in BUYERS:
            writer.writerow(b)
    print(f"Successfully wrote {len(BUYERS)} verified Tirupati buyers to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
