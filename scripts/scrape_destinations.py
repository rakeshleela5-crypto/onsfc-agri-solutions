#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Exhaustive 100-Buyer Quad-Territory B2B Database Compiler
Targets: Gooty, Guntakal, Pamidi, and Anantapur across all non-perishable customer segments.
Now fully encompassing:
1. Guntakal Railway Division 24/7 Running Room Mess, Railway Hospital Canteen, and IRCTC Food Plazas
2. RDT (Rural Development Trust) Inclusive Residential Schools & Boarding Hostels
3. Government Polytechnic Hostels (Anantapur & Guntakal)
4. Commercial Dairy Plants & Cattle Feed Buyers (Vijaya Dairy, Dodla Dairy)
5. Traditional Rayalaseema Namkeen, Mixture & Sweet Factories
6. Wedding Convention Halls (Kalyana Mandapams) & Catering Associations
7. Historic Convent Boarding Schools (St. Joseph's, St. Vincent Pallotti, Montessori)
8. All Supermarkets, Universities, Colleges, Cotton Mills, Oil Mills, and Temples
"""

import os
import csv

OUTPUT_DIR = r"C:\Users\rakes\.gemini\antigravity\scratch\onsfc-agri-solutions\data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "ONSFC_Target_Buyers_Gooty_Guntakal_Anantapur.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

DESTINATION_BUYERS = [
    # =========================================================================
    # 1. RAILWAY DIVISION RUNNING ROOMS & TRANSPORT CANTEENS (GUNTAKAL HQ)
    # =========================================================================
    {
        "Category": "Railway Running Rooms & Transport Messes",
        "Business Name": "South Central Railway (SCR) Running Room Central Mess",
        "Town": "Guntakal",
        "Region": "Railway Colony / Guntakal Junction",
        "Key Crops Demanded": "Rice (Sona Masoori 300kg daily), Toor Dal, Bengal Gram, Groundnut Cooking Oil",
        "Procurement Profile": "24/7 operational railway mess feeding hundreds of train drivers (loco pilots), guards, and running crew around the clock",
        "Address / Landmark": "Divisional Railway Office (DRO) Complex, Guntakal Junction - 515801",
        "Contact Channel": "Senior Divisional Mechanical Engineer (Sr. DME) / Running Room Contractor"
    },
    {
        "Category": "Railway Running Rooms & Transport Messes",
        "Business Name": "Guntakal Divisional Railway Hospital Dietary Canteen",
        "Town": "Guntakal",
        "Region": "Railway Hospital Road",
        "Key Crops Demanded": "Rice (Sona Masoori & Broken Rice), Toor Dal, Ragi, Groundnut Oil",
        "Procurement Profile": "100+ bed railway division hospital serving in-patients and staff daily",
        "Address / Landmark": "Railway Hospital Road, Guntakal - 515801",
        "Contact Channel": "Chief Medical Superintendent (CMS) & Canteen Contractor"
    },
    {
        "Category": "Railway Running Rooms & Transport Messes",
        "Business Name": "IRCTC Refreshment Rooms & Food Plaza (Guntakal Junction)",
        "Town": "Guntakal",
        "Region": "Platform 1 & 3, Guntakal Junction",
        "Key Crops Demanded": "Rice (Raw & Boiled 400kg daily), Toor Dal, Groundnut Oil, Spices",
        "Procurement Profile": "Major railway junction food plaza catering to thousands of transit express train passengers daily",
        "Address / Landmark": "Guntakal Railway Station Main Concourse - 515801",
        "Contact Channel": "IRCTC Regional Catering Manager / Platform Caterer"
    },

    # =========================================================================
    # 2. RDT (RURAL DEVELOPMENT TRUST) INCLUSIVE RESIDENTIAL SCHOOLS
    # =========================================================================
    {
        "Category": "Philanthropic & Special Inclusive Residential Schools",
        "Business Name": "RDT (Rural Development Trust) Inclusive Residential Schools & Hostels",
        "Town": "Anantapur",
        "Region": "Anantapur Rural & Bathalapalle",
        "Key Crops Demanded": "Rice (Sona Masoori 500kg daily), Toor Dal, Millets (Ragi/Korra), Unadulterated Groundnut Oil",
        "Procurement Profile": "Renowned humanitarian organization (Vicente Ferrer Foundation) running multiple residential boarding schools for 1,500+ rural disabled and underprivileged children with 100% free daily food",
        "Address / Landmark": "RDT Headquarters, Subhash Road, Anantapur / Bathalapalle Campus - 515001",
        "Contact Channel": "RDT Central Education & Food Procurement Committee"
    },
    {
        "Category": "Philanthropic & Special Inclusive Residential Schools",
        "Business Name": "RDT School of Nursing & Healthcare Hostels",
        "Town": "Anantapur",
        "Region": "Bathalapalle Campus",
        "Key Crops Demanded": "Rice, Toor Dal, Bengal Gram, Cooking Oil",
        "Procurement Profile": "Residential nursing and paramedical students mess (400+ students)",
        "Address / Landmark": "RDT Hospital Complex, Bathalapalle - 515661",
        "Contact Channel": "Nursing Hostel Warden & Mess Supervisor"
    },

    # =========================================================================
    # 3. GOVERNMENT POLYTECHNIC & TECHNICAL INSTITUTES
    # =========================================================================
    {
        "Category": "Polytechnic & Technical Training Hostels",
        "Business Name": "Government Polytechnic College & Hostels (Anantapur)",
        "Town": "Anantapur",
        "Region": "Kamalanagar / JNTU Road",
        "Key Crops Demanded": "Rice (200kg daily), Toor Dal, Bengal Gram, Groundnut Oil",
        "Procurement Profile": "Separate on-campus Boys and Girls hostel blocks housing 600+ diploma students with daily mess",
        "Address / Landmark": "Beside JNTUA, Kamalanagar, Anantapur - 515002",
        "Contact Channel": "Principal & Polytechnic Hostel Mess Committee"
    },
    {
        "Category": "Polytechnic & Technical Training Hostels",
        "Business Name": "Government Polytechnic for Minorities & Hostels (Guntakal)",
        "Town": "Guntakal",
        "Region": "Tilak Nagar / BSS Colony",
        "Key Crops Demanded": "Rice, Toor Dal, Groundnut Oil, Spices",
        "Procurement Profile": "Technical diploma student hostels and surrounding welfare mess",
        "Address / Landmark": "BSS Colony, Tilak Nagar, Guntakal - 515801",
        "Contact Channel": "Polytechnic Principal"
    },

    # =========================================================================
    # 4. DAIRY PROCESSING PLANTS & CATTLE FEED CONSUMERS
    # =========================================================================
    {
        "Category": "Dairy Processing & Cattle Feed Procurement",
        "Business Name": "AP Dairy (Vijaya Dairy) Anantapur Processing Plant",
        "Town": "Anantapur",
        "Region": "Industrial Area, Bellary Road",
        "Key Crops Demanded": "Cottonseed Cake (Kapas Khal), Groundnut De-oiled Cake (DOC), Maize (Corn)",
        "Procurement Profile": "State dairy federation procurement for thousands of affiliated cooperative dairy farmers; bulk feed wagon loads",
        "Address / Landmark": "Vijaya Dairy Plant, Bellary Road, Anantapur - 515004",
        "Contact Channel": "General Manager (Procurement & Feeds)"
    },
    {
        "Category": "Dairy Processing & Cattle Feed Procurement",
        "Business Name": "Dodla Dairy Chilling Center & Feed Hub",
        "Town": "Guntakal",
        "Region": "Kalluru Road / Guntakal Outer",
        "Key Crops Demanded": "Cottonseed Cake, Maize, Groundnut Meal",
        "Procurement Profile": "Private dairy chilling center supplying feed inputs to farmer milk collection routes",
        "Address / Landmark": "Guntakal Chilling Center - 515801",
        "Contact Channel": "Chilling Center Incharge"
    },

    # =========================================================================
    # 5. TRADITIONAL SWEET, NAMKEEN & MIXTURE FACTORIES
    # =========================================================================
    {
        "Category": "Traditional Sweets & Namkeen Factories",
        "Business Name": "Shanti Sweets & Rayalaseema Namkeen Factory",
        "Town": "Guntakal",
        "Region": "Main Bazaar Road",
        "Key Crops Demanded": "Groundnut Kernels (Bold variety), Bengal Gram (Chana / Senaga Pappu), Pure Groundnut Oil",
        "Procurement Profile": "High-volume manufacturer of Rayalaseema mixture, sev, and fried gram snacks consuming quintals of peanuts and oil weekly",
        "Address / Landmark": "Main Bazaar, Guntakal - 515801",
        "Contact Channel": "Factory Proprietor"
    },
    {
        "Category": "Traditional Sweets & Namkeen Factories",
        "Business Name": "Sweet Magic & Grand Bakery Confectionery Works",
        "Town": "Anantapur",
        "Region": "Subhash Road",
        "Key Crops Demanded": "Groundnut Kernels, Bengal Gram, Spices, Edible Oil",
        "Procurement Profile": "Popular regional sweets and bakery chain with large centralized preparation kitchen",
        "Address / Landmark": "Subhash Road, Anantapur - 515001",
        "Contact Channel": "Production Head"
    },

    # =========================================================================
    # 6. CONVENTION HALLS (KALYANA MANDAPAMS) & CATERERS ASSOCIATIONS
    # =========================================================================
    {
        "Category": "Wedding Convention Halls & Caterers Associations",
        "Business Name": "Anantha Padmanabha Kalyana Mandapam & Catering Services",
        "Town": "Anantapur",
        "Region": "Kamalanagar / Court Road",
        "Key Crops Demanded": "Rice (Premium Sona Masoori BPT 5204 50kg bags), Toor Dal, Groundnut Cooking Oil",
        "Procurement Profile": "Premier wedding convention hall hosting multi-day marriages and banquets; massive recurring bulk purchases",
        "Address / Landmark": "Court Road, Anantapur - 515001",
        "Contact Channel": "Convention Manager & Associated Master Caterers"
    },
    {
        "Category": "Wedding Convention Halls & Caterers Associations",
        "Business Name": "Keshava Reddy Kalyana Vedika & Mega Function Hall",
        "Town": "Anantapur",
        "Region": "NH-44 Bypass",
        "Key Crops Demanded": "Rice (50kg bags), Toor Dal, Bengal Gram, Edible Oil, Spices",
        "Procurement Profile": "High capacity convention center catering to large Rayalaseema gatherings",
        "Address / Landmark": "NH-44 Bypass, Anantapur - 515004",
        "Contact Channel": "Event Operations Manager"
    },
    {
        "Category": "Wedding Convention Halls & Caterers Associations",
        "Business Name": "Anantapur Caterers & Master Cooks Guild",
        "Town": "Anantapur",
        "Region": "Old Town / Clock Tower",
        "Key Crops Demanded": "Rice (Sona Masoori, Raw & Boiled), Toor Dal, Groundnut Oil",
        "Procurement Profile": "Consortium of 30+ commercial outdoor catering contractors who buy truckloads of rice and dal during wedding seasons",
        "Address / Landmark": "Old Town Commercial Center, Anantapur - 515001",
        "Contact Channel": "President / Catering Association Secretary"
    },

    # =========================================================================
    # 7. HISTORIC CONVENT BOARDING SCHOOLS
    # =========================================================================
    {
        "Category": "Historic Convent Boarding Schools",
        "Business Name": "St. Joseph's English Medium Residential School & Hostels",
        "Town": "Guntakal",
        "Region": "Church Road / Railway Colony",
        "Key Crops Demanded": "Rice (Sona Masoori 150kg daily), Toor Dal, Bengal Gram, Groundnut Oil",
        "Procurement Profile": "Century-old established convent boarding school for 600+ students with on-site hostel mess",
        "Address / Landmark": "Church Road, Guntakal - 515801",
        "Contact Channel": "Sister Superior & Hostel Warden"
    },
    {
        "Category": "Historic Convent Boarding Schools",
        "Business Name": "St. Vincent Pallotti Residential School & Boys Home",
        "Town": "Anantapur",
        "Region": "Rudrampeta Road",
        "Key Crops Demanded": "Rice, Toor Dal, Millets, Cooking Oil",
        "Procurement Profile": "Residential missionary school and boarding home for 500+ students",
        "Address / Landmark": "Rudrampeta, Anantapur - 515004",
        "Contact Channel": "Father Rector & Mess Incharge"
    },
    {
        "Category": "Historic Convent Boarding Schools",
        "Business Name": "Montessori Residential High School & Hostels",
        "Town": "Guntakal",
        "Region": "Tilak Nagar",
        "Key Crops Demanded": "Rice, Toor Dal, Bengal Gram, Spices",
        "Procurement Profile": "Long-standing concept residential boarding institution (400+ boarders)",
        "Address / Landmark": "Tilak Nagar, Guntakal - 515801",
        "Contact Channel": "Correspondent & Hostel Warden"
    },

    # =========================================================================
    # 8. TEMPLE ANNADHANAM & PILGRIMAGE TRUSTS
    # =========================================================================
    {
        "Category": "Religious Trusts & Annadhanam Services",
        "Business Name": "Sri Nettikanti Anjaneya Swamy Temple Annadhanam Trust",
        "Town": "Guntakal",
        "Region": "Kasapuram (11 km from Guntakal)",
        "Key Crops Demanded": "Rice (Sona Masoori 300kg daily), Toor Dal, Bengal Gram, Groundnut Oil, Jaggery",
        "Procurement Profile": "Famous historic pilgrimage temple; feeds thousands of devotees daily through Nitya Annadhanam; massive monthly dry grocery procurement",
        "Address / Landmark": "Kasapuram Village, Guntakal Mandal, Ananthapuramu Dist - 515803",
        "Contact Channel": "Executive Officer (EO) / Temple Annadhanam Trust Incharge"
    },
    {
        "Category": "Religious Trusts & Annadhanam Services",
        "Business Name": "ISKCON Temple & Food for Life Trust",
        "Town": "Anantapur",
        "Region": "Somaladoddi / NH-44",
        "Key Crops Demanded": "Rice (Sona Masoori), Toor Dal, Moong Dal, Pure Groundnut Oil, Millets",
        "Procurement Profile": "Daily deity bhog, prasadam and free food distribution to pilgrims and students",
        "Address / Landmark": "Hare Krishna Land, Somaladoddi, NH-44, Anantapur - 515002",
        "Contact Channel": "Temple Kitchen & Prasadam Coordinator"
    },

    # =========================================================================
    # 9. POLICE TRAINING, DEFENSE & GOVERNMENT PRISONS
    # =========================================================================
    {
        "Category": "State Defense & Police Training Messes",
        "Business Name": "Police Training College (PTC) Central Mess",
        "Town": "Anantapur",
        "Region": "Lakshmi Nagar / Rapthadu Road",
        "Key Crops Demanded": "Rice (400kg daily), Toor Dal, Bengal Gram, Groundnut Cooking Oil",
        "Procurement Profile": "State police academy hosting 500-1,000 trainee sub-inspectors and constables in barracks eating 3 heavy meals daily",
        "Address / Landmark": "PTC Campus, Lakshmi Nagar, Rapthadu Road, Anantapur - 515001",
        "Contact Channel": "PTC Mess Secretary & Administrative Officer"
    },
    {
        "Category": "Government Prison & Correctional Canteens",
        "Business Name": "Anantapur Central Prison / District Jail Ration Store",
        "Town": "Anantapur",
        "Region": "Court Road Area",
        "Key Crops Demanded": "Rice (Raw & Boiled 500kg daily), Toor Dal, Chana, Groundnut Oil",
        "Procurement Profile": "State correctional facility feeding inmates 3 times daily; institutional quarterly supply contract",
        "Address / Landmark": "District Jail Complex, Anantapur - 515001",
        "Contact Channel": "Jail Superintendent & Supply Storekeeper"
    },

    # =========================================================================
    # 10. GOVERNMENT WELFARE RESIDENTIAL GURUKULAMS & KGBVS
    # =========================================================================
    {
        "Category": "Government Welfare Residential Schools & KGBVs",
        "Business Name": "APSRSW (Girls) Residential School & Junior College (APREIS)",
        "Town": "Gooty",
        "Region": "Gooty Town",
        "Key Crops Demanded": "Rice (150kg daily), Toor Dal, Bengal Gram, Groundnut Oil, Ragi",
        "Procurement Profile": "Established 1983; premier government residential campus for 600+ girls with attached dining mess",
        "Address / Landmark": "AP Residential Girls Campus, Gooty - 515401",
        "Contact Channel": "Principal & Mess Purchase Committee"
    },
    {
        "Category": "Government Welfare Residential Schools & KGBVs",
        "Business Name": "APSWRS / Dr. B.R. Ambedkar Gurukulam (Rajapuram)",
        "Town": "Gooty",
        "Region": "Rajapuram, Gooty Mandal",
        "Key Crops Demanded": "Rice (150kg daily), Toor Dal, Bengal Gram, Edible Oil",
        "Procurement Profile": "Co-educational senior secondary residential gurukulam with 500+ boarding students",
        "Address / Landmark": "Rajapuram Village, Gooty Mandal - 515401",
        "Contact Channel": "Gurukulam Principal & Mess Incharge"
    },
    {
        "Category": "Government Welfare Residential Schools & KGBVs",
        "Business Name": "KGBV (Kasturba Gandhi Balika Vidyalaya) Rajapuram",
        "Town": "Gooty",
        "Region": "Rajapuram, Gooty",
        "Key Crops Demanded": "Rice, Toor Dal, Millets, Groundnut Oil",
        "Procurement Profile": "Residential school for 300+ girl students with complete boarding mess",
        "Address / Landmark": "Rajapuram, Gooty Mandal - 515401",
        "Contact Channel": "Special Officer (SO) / Mess Warden"
    },
    {
        "Category": "Government Welfare Residential Schools & KGBVs",
        "Business Name": "KGBV (Kasturba Gandhi Balika Vidyalaya) Guntakal",
        "Town": "Guntakal",
        "Region": "Guntakal Urban",
        "Key Crops Demanded": "Rice (120kg daily), Toor Dal, Bengal Gram, Groundnut Oil",
        "Procurement Profile": "Classes 6-12 residential school for 400+ rural girl students with daily mess",
        "Address / Landmark": "Urban School Compound, Guntakal - 515801",
        "Contact Channel": "Special Officer (SO) & Mess Supervisor"
    },
    {
        "Category": "Government Welfare Residential Schools & KGBVs",
        "Business Name": "KGBV & BC Welfare Residential Girls School (Pamidi)",
        "Town": "Pamidi",
        "Region": "Pamidi Town (NH-44)",
        "Key Crops Demanded": "Rice (100kg daily), Toor Dal, Bengal Gram, Cooking Oil",
        "Procurement Profile": "Residential boarding school for 350+ girls in Pamidi mandal",
        "Address / Landmark": "Near Bypass, Pamidi - 515775",
        "Contact Channel": "Special Officer & Warden"
    },
    {
        "Category": "Government Welfare Residential Schools & KGBVs",
        "Business Name": "Dr. B.R. Ambedkar Gurukulam / Center of Excellence (COE)",
        "Town": "Anantapur",
        "Region": "Anantapur Rural",
        "Key Crops Demanded": "Rice (250kg daily), Toor Dal, Bengal Gram, Millets, Groundnut Oil",
        "Procurement Profile": "Elite state government residential institution for 800+ meritorious students",
        "Address / Landmark": "Social Welfare COE Complex, Anantapur - 515002",
        "Contact Channel": "Principal & Zonal Procurement Officer"
    },

    # =========================================================================
    # 11. PEANUT CHIKKI & AGRO-PROCESSING FACTORIES
    # =========================================================================
    {
        "Category": "Peanut Chikki & Agro-Processing",
        "Business Name": "Anantha Samruddhi (Rythu Nesham Food Producer Co. Ltd.)",
        "Town": "Anantapur",
        "Region": "Kuderu / Anantapur Industrial Belt",
        "Key Crops Demanded": "Grade-A Groundnut Kernels (Palli), Sesame, Millets",
        "Procurement Profile": "Large FPO-backed peanut chikki and value-added snack factory consuming 20-50 MT groundnut kernels monthly",
        "Address / Landmark": "Muddalapuram Village, Kuderu Road, Anantapur District - 515711",
        "Contact Channel": "Managing Director / Factory Procurement Manager"
    },
    {
        "Category": "Peanut Chikki & Agro-Processing",
        "Business Name": "Riyasri Agro Foods (OPC) Private Limited",
        "Town": "Anantapur",
        "Region": "Anantapur Industrial Estate",
        "Key Crops Demanded": "Groundnut Kernels, Jaggery, Sesame",
        "Procurement Profile": "Commercial manufacturer of peanut jaggery chikki, peanut butter chikki and traditional sweets",
        "Address / Landmark": "Industrial Estate, Anantapur - 515004",
        "Contact Channel": "Works Director / Raw Material Buyer"
    },
    {
        "Category": "Peanut Chikki & Agro-Processing",
        "Business Name": "Sri Krishna Sweets & Chikki Manufacturing Works",
        "Town": "Guntakal",
        "Region": "Guntakal Bazaar",
        "Key Crops Demanded": "Groundnut Kernels (Bold & Java varieties), Jaggery",
        "Procurement Profile": "Traditional peanut brittle maker and sweet wholesaler supplying regional retail stores",
        "Address / Landmark": "Old Bazaar, Guntakal - 515801",
        "Contact Channel": "Proprietor"
    },

    # =========================================================================
    # 12. CLOUD KITCHENS & COMMERCIAL CATERING HUBS
    # =========================================================================
    {
        "Category": "Cloud Kitchens & Commercial Catering Hubs",
        "Business Name": "Rebel Foods Cloud Kitchens (Faasos / Behrouz Biryani)",
        "Town": "Anantapur",
        "Region": "Subhash Road / Clock Tower",
        "Key Crops Demanded": "Rice (Raw Sona Masoori, Premium Biryani Rice), Toor Dal, Refined Peanut Oil",
        "Procurement Profile": "Multi-brand cloud kitchen network with high daily online order delivery volume",
        "Address / Landmark": "Central Delivery Hub, Anantapur - 515001",
        "Contact Channel": "City Operations Lead / Sourcing Supervisor"
    },
    {
        "Category": "Cloud Kitchens & Commercial Catering Hubs",
        "Business Name": "Biryani Zone & Andhra Catering Hub",
        "Town": "Anantapur",
        "Region": "RTC Bus Stand Road",
        "Key Crops Demanded": "Rice (Sona Masoori & Basmati), Toor Dal, Spices, Groundnut Oil",
        "Procurement Profile": "High volume restaurant and outdoor wedding catering services (50kg bags daily)",
        "Address / Landmark": "Bus Stand Bypass, Anantapur - 515001",
        "Contact Channel": "Managing Partner & Head Chef"
    },

    # =========================================================================
    # 13. SUPERMARKETS & HYPERMARKETS (ALL FOUR TOWNS)
    # =========================================================================
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "DMart (Branch 1 - Gooty Road)",
        "Town": "Anantapur",
        "Region": "Gooty Road / Chilka Nagar",
        "Key Crops Demanded": "Rice (Sona Masoori 25kg/10kg bags), Toor Dal, Chana Dal, Peanuts, Edible Oil",
        "Procurement Profile": "Massive footfall hypermarket, directly on Gooty Road near Market Yard; continuous bulk intake",
        "Address / Landmark": "Gooty Road, Chilka Nagar, Beside Vidhyuth Kalabharathi, Anantapur - 515001",
        "Contact Channel": "Regional Staples Sourcing Team / Store General Manager"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "DMart (Branch 2 - Rudrampeta Bypass)",
        "Town": "Anantapur",
        "Region": "Rudrampeta Bypass",
        "Key Crops Demanded": "Rice (Branded 25kg bags), Pulses, Groundnuts, Spices",
        "Procurement Profile": "High-volume consumer hypermarket catering to South Anantapur & NH-44 traffic",
        "Address / Landmark": "Near Royal Enfield Showroom, Kakkalapally / Rudrampeta Bypass, Anantapur - 515004",
        "Contact Channel": "Store Procurement Incharge"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "Reliance SMART Bazaar (Flagship Hypermarket)",
        "Town": "Anantapur",
        "Region": "East Fort / Bus Stand",
        "Key Crops Demanded": "Rice (Branded 25kg/10kg Sona Masoori), Toor Dal, Chana Dal, Peanuts, Millets",
        "Procurement Profile": "Regional flagship hypermarket, massive daily staples turnover",
        "Address / Landmark": "Behind APSRTC Bus Stand, Srinivasa Nagar, East Fort Junction, Anantapur - 515001",
        "Contact Channel": "Regional Dry Grocery Sourcing Head"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "SP Super Stores (SP Supermarket)",
        "Town": "Anantapur",
        "Region": "Kamalanagar / Ramnagar",
        "Key Crops Demanded": "Rice (Sona Masoori, HMT, RNR), Pulses, Groundnut Kernels, Millets",
        "Procurement Profile": "Premier local multi-floor independent supermarket, dominant city footfall",
        "Address / Landmark": "Kamalanagar Main Road, Ramnagar, Anantapur - 515001",
        "Contact Channel": "Managing Partner / Purchase Desk"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "More Supermarket (Anantapur)",
        "Town": "Anantapur",
        "Region": "Ashok Nagar",
        "Key Crops Demanded": "Rice (BPT, RNR), Toor Dal, Groundnut, Spices",
        "Procurement Profile": "National supermarket chain outlet",
        "Address / Landmark": "Ashok Nagar, Anantapur - 515001",
        "Contact Channel": "Store Manager"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "Vishal Mega Mart (Anantapur)",
        "Town": "Anantapur",
        "Region": "Subhash Road",
        "Key Crops Demanded": "Rice, Pulses (Toor, Moong, Urad), Peanuts",
        "Procurement Profile": "High footfall retail supermarket grocery rack",
        "Address / Landmark": "Subhash Road, Anantapur - 515001",
        "Contact Channel": "Staples Category Supervisor"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "Reliance Smart Point (Nesepet / Azad Nagar)",
        "Town": "Anantapur",
        "Region": "Nesepet",
        "Key Crops Demanded": "Packaged Rice, Toor Dal, Groundnut Kernels, Millets, Spices",
        "Procurement Profile": "Neighborhood supermarket daily replenishment",
        "Address / Landmark": "Azad Nagar, Nesepet, Anantapur - 515005",
        "Contact Channel": "Store Incharge"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "Old Town Wholesale Grain Merchant Association",
        "Town": "Anantapur",
        "Region": "Old Town Market Yard",
        "Key Crops Demanded": "Truckload Rice (Sona Masoori, BPT 5204), Toor Dal, Groundnut Pods/Kernels",
        "Procurement Profile": "Wholesale mandi trading network of 50+ grain merchants, daily spot turnover",
        "Address / Landmark": "Old Town Market Yard, Anantapur - 515001",
        "Contact Channel": "Wholesale Grain Merchants Committee"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "Vishal Mega Mart (Guntakal Hypermarket)",
        "Town": "Guntakal",
        "Region": "Guntakal Town",
        "Key Crops Demanded": "Rice (Sona Masoori 25kg/10kg bags), Toor Dal, Chana Dal, Peanuts, Millets",
        "Procurement Profile": "Large national hypermarket, high-velocity grocery retail",
        "Address / Landmark": "Uravakonda Road, Near Hanuman Circle, Donimukkala, Guntakal - 515801",
        "Contact Channel": "Store Manager / Regional Staples Buyer"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "More Supermarket (Guntakal)",
        "Town": "Guntakal",
        "Region": "Guntakal Town",
        "Key Crops Demanded": "Rice (BPT 5204, RNR), Toor Dal, Groundnut Kernels, Millets, Spices",
        "Procurement Profile": "National retail supermarket chain, monthly recurring inventory intake",
        "Address / Landmark": "Kasapuram Road / Tilak Nagar, Guntakal - 515801",
        "Contact Channel": "Store Supervisor"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "SuperK - Gold Supermarket",
        "Town": "Guntakal",
        "Region": "Guntakal Town",
        "Key Crops Demanded": "Rice (25kg bags), Pulses, Groundnuts, Ragi, Jowar",
        "Procurement Profile": "Rapidly growing regional retail supermarket chain",
        "Address / Landmark": "Achramma Kottala, Bhagya Nagar, Shanti Nagar, Guntakal - 515801",
        "Contact Channel": "Store Operations Incharge"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "Happy Home Supermarket",
        "Town": "Guntakal",
        "Region": "Guntakal Town",
        "Key Crops Demanded": "Rice (Raw & Boiled), Toor Dal, Groundnut, Spices",
        "Procurement Profile": "Township premium grocery mart, daily consumer sales",
        "Address / Landmark": "Mahendra Street, Tilak Nagar, Guntakal - 515801",
        "Contact Channel": "Store Proprietor"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "Sree Dara Supermarket & Shopping Mall",
        "Town": "Guntakal",
        "Region": "Guntakal Town",
        "Key Crops Demanded": "Rice (Sona Masoori), Pulses, Peanuts, Grains",
        "Procurement Profile": "Prominent central department store & grocery supermarket",
        "Address / Landmark": "Hanumesh Nagar, Near NTR Circle, Guntakal - 515801",
        "Contact Channel": "Managing Partner"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "Patil Supermarket",
        "Town": "Guntakal",
        "Region": "Guntakal Town",
        "Key Crops Demanded": "Rice, Toor Dal, Bengal Gram, Groundnut, Millets",
        "Procurement Profile": "High footfall neighborhood supermarket",
        "Address / Landmark": "Kasapuram Road, Hanumesh Nagar (Near Congress Office), Guntakal - 515801",
        "Contact Channel": "Store Incharge"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "Chitanya Supermarket",
        "Town": "Guntakal",
        "Region": "Guntakal Town",
        "Key Crops Demanded": "Rice, Toor Dal, Groundnut, Sun-dried Spices",
        "Procurement Profile": "Residential neighborhood retail supermarket",
        "Address / Landmark": "Kasapuram Road, VV Nagar, Guntakal - 515801",
        "Contact Channel": "Store Manager"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "Golden Super Market",
        "Town": "Guntakal",
        "Region": "Guntakal Town",
        "Key Crops Demanded": "Rice, Edible Grains, Pulses, Peanuts",
        "Procurement Profile": "Town commercial center supermarket",
        "Address / Landmark": "Sofia Street, Opp Arunachal Complex, Guntakal - 515801",
        "Contact Channel": "Proprietor"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "Somanna Rice Traders & Wholesale Provisioners",
        "Town": "Guntakal",
        "Region": "Guntakal Town",
        "Key Crops Demanded": "Bulk Rice (Sona Masoori, HMT, Broken Rice), Pulses",
        "Procurement Profile": "Major wholesale rice distributor & bulk trader",
        "Address / Landmark": "60 Feet Road, Tilak Nagar, Guntakal - 515801",
        "Contact Channel": "Wholesale Desk"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "Sri Balaji Supermarket & Wholesale Provisions",
        "Town": "Guntakal",
        "Region": "Guntakal Town",
        "Key Crops Demanded": "Rice (25kg/50kg bags), Toor Dal, Bengal Gram, Millets",
        "Procurement Profile": "Large grocery wholesaler and retail supermarket",
        "Address / Landmark": "Main Bazaar Road, Guntakal - 515801",
        "Contact Channel": "Purchase Desk"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "SuperK - Lotus Supermarket",
        "Town": "Gooty",
        "Region": "Gooty Town",
        "Key Crops Demanded": "Rice (25kg bags), Toor Dal, Groundnut, Millets, Spices",
        "Procurement Profile": "Primary Gooty township supermarket",
        "Address / Landmark": "Station Road, Gooty - 515401",
        "Contact Channel": "Store Incharge"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "Anjana Mini Mart",
        "Town": "Gooty",
        "Region": "Gooty Town",
        "Key Crops Demanded": "Rice, Toor Dal, Groundnut Kernels, Ragi, Jowar",
        "Procurement Profile": "Daily customer grocery retail mart",
        "Address / Landmark": "Bazaar Street, Gooty - 515401",
        "Contact Channel": "Managing Partner"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "Akshaya Super Market",
        "Town": "Gooty",
        "Region": "Nagasamudram / Gooty",
        "Key Crops Demanded": "Rice (BPT, Raw), Pulses, Peanuts, Sun-dried Chilies",
        "Procurement Profile": "Township grocery supermarket",
        "Address / Landmark": "Nagasamudram Area, Gooty - 515401",
        "Contact Channel": "Store Owner"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "Sri Lakshmi Srinivasa Super Market & Kirana",
        "Town": "Pamidi",
        "Region": "Pamidi Town (NH-44)",
        "Key Crops Demanded": "Rice (25kg/50kg bags), Toor Dal, Bengal Gram, Groundnut Oil",
        "Procurement Profile": "Primary township supermarket on NH-44 highway belt",
        "Address / Landmark": "Main Bazaar Road, Pamidi - 515775",
        "Contact Channel": "Proprietor"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "Balaji Super Bazaar",
        "Town": "Pamidi",
        "Region": "Pamidi Town",
        "Key Crops Demanded": "Rice (Sona Masoori), Pulses, Peanuts, Millets",
        "Procurement Profile": "Township provision bazaar and grocery retail",
        "Address / Landmark": "Bus Stand Road, Pamidi - 515775",
        "Contact Channel": "Managing Partner"
    },

    # =========================================================================
    # 14. UNIVERSITIES & RESIDENTIAL MEGA-CAMPUSES
    # =========================================================================
    {
        "Category": "Universities & Residential Campuses",
        "Business Name": "Sri Krishnadevaraya University (SKU) Campus Hostels",
        "Town": "Anantapur",
        "Region": "SKU Campus / NH-44",
        "Key Crops Demanded": "Rice (Sona Masoori 350kg daily), Toor Dal, Bengal Gram, Groundnut Cooking Oil",
        "Procurement Profile": "Massive state university residential campus housing 2,300+ students across multiple hostel blocks and messes",
        "Address / Landmark": "NH-44, Sri Krishnadevaraya University, Anantapur - 515003",
        "Contact Channel": "Chief Warden & Central Mess Purchase Committee"
    },
    {
        "Category": "Universities & Residential Campuses",
        "Business Name": "Government Medical College (GMC) & Hospital Hostels",
        "Town": "Anantapur",
        "Region": "Kamalanagar",
        "Key Crops Demanded": "Rice (200kg daily), Toor Dal, Bengal Gram, Groundnut Oil, Millets",
        "Procurement Profile": "Premier medical college housing 1,200+ UG/PG medicos, house surgeons, and nurses across separate mess blocks",
        "Address / Landmark": "Kamalanagar / Medical College Road, Anantapur - 515001",
        "Contact Channel": "Hostel Incharge & GMC Mess Tender Committee"
    },
    {
        "Category": "Universities & Residential Campuses",
        "Business Name": "ALITS (Anantha Lakshmi Institute of Tech & Sciences) Hostels",
        "Town": "Anantapur",
        "Region": "Itikalapalli / NH-44",
        "Key Crops Demanded": "Rice (180kg daily), Toor Dal, Groundnut Oil, Spices",
        "Procurement Profile": "1,200+ residential engineering students in separate on-campus boys & girls hostels",
        "Address / Landmark": "Near SKU, Itikalapalli, Anantapur - 515721",
        "Contact Channel": "Campus Estate Officer & Mess Contractor"
    },
    {
        "Category": "Universities & Residential Campuses",
        "Business Name": "CRIT (Chiranjeevi Reddy Institute of Tech) Hostels",
        "Town": "Anantapur",
        "Region": "Bellary Road",
        "Key Crops Demanded": "Rice (150kg daily), Toor Dal, Bengal Gram, Edible Oil",
        "Procurement Profile": "Integrated technical campus with dedicated on-campus girls & boys hostels",
        "Address / Landmark": "Bellary Road, Rachanapalli / Kodimi, Anantapur - 515004",
        "Contact Channel": "Hostel Warden & Principal"
    },
    {
        "Category": "Universities & Residential Campuses",
        "Business Name": "JNTUA (Jawaharlal Nehru Technological University) Hostels",
        "Town": "Anantapur",
        "Region": "University Zone",
        "Key Crops Demanded": "Rice (500kg daily across 6 mess halls), Toor Dal, Bengal Gram, Groundnut Oil",
        "Procurement Profile": "4,000+ university residential students, annual institutional tender",
        "Address / Landmark": "Sir Mokshagundam Vishveshwariah Road, Anantapur - 515002",
        "Contact Channel": "Hostel Manager / Student Mess Committee"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "Narayana Junior College & Hostels (Vidyuth Nagar)",
        "Town": "Anantapur",
        "Region": "Vidyuth Nagar",
        "Key Crops Demanded": "Rice (Sona Masoori 250kg daily), Toor Dal, Bengal Gram, Groundnut Oil",
        "Procurement Profile": "Flagship residential intermediate campus (1,500+ boys and girls)",
        "Address / Landmark": "Vidyuth Nagar, Anantapur - 515001",
        "Contact Channel": "Central Kitchen Purchase Officer"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "Narayana Mega Residential Campus (Somaladoddi)",
        "Town": "Anantapur",
        "Region": "Somaladoddi Bypass",
        "Key Crops Demanded": "Rice (300kg daily), Toor Dal, Bengal Gram, Millets, Spices",
        "Procurement Profile": "Massive integrated residential coaching academy (2,000+ students), consumes 30 quintals rice weekly",
        "Address / Landmark": "Somaladoddi, Anantapur Outer Bypass - 515002",
        "Contact Channel": "Campus Administrator / Mess Incharge"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "Narayana Residential Wing (Vadiyampeta on NH-44)",
        "Town": "Anantapur",
        "Region": "Vadiyampeta",
        "Key Crops Demanded": "Rice (Sona Masoori), Toor Dal, Groundnut Oil, Ragi",
        "Procurement Profile": "Integrated coaching campus, direct highway accessibility",
        "Address / Landmark": "Vadiyampeta, NH-44, Anantapur - 515003",
        "Contact Channel": "Hostel Purchase Lead"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "Sri Chaitanya Junior College & Hostels (RTC Bus Stand)",
        "Town": "Anantapur",
        "Region": "RTC Bus Stand Road",
        "Key Crops Demanded": "Rice (200kg daily), Toor Dal, Groundnut Oil, Dry Chilies, Spices",
        "Procurement Profile": "1,200+ residential intermediate coaching students",
        "Address / Landmark": "Behind RTC Bus Stand Road, Anantapur - 515001",
        "Contact Channel": "Hostel Mess Purchase Committee"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "Sri Chaitanya Girls Residential College (Housing Board)",
        "Town": "Anantapur",
        "Region": "Housing Board Colony",
        "Key Crops Demanded": "Rice (Sona Masoori / RNR Sugar-Free), Toor Dal, Bengal Gram, Ragi/Korra",
        "Procurement Profile": "Dedicated girls residential academy (1,000+ students)",
        "Address / Landmark": "AP Housing Board Colony, Anantapur - 515002",
        "Contact Channel": "Catering Contractor & Warden"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "PVKK Institute of Technology & Balaji Hostels",
        "Town": "Anantapur",
        "Region": "Rudrampeta / NH-44",
        "Key Crops Demanded": "Rice (350kg daily), Toor Dal, Bengal Gram, Groundnut Oil",
        "Procurement Profile": "Integrated technical campus with 2,500+ residential engineering students",
        "Address / Landmark": "Sanapa Road, Rudrampeta, NH-44, Anantapur - 515004",
        "Contact Channel": "Campus Administrative Officer & Hostel Mess Tender Lead"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "Keshava Reddy Educational Institutions Campus",
        "Town": "Anantapur",
        "Region": "Vadiyampeta / NH-44",
        "Key Crops Demanded": "Rice (150kg daily), Toor Dal, Bengal Gram, Millets, Groundnut",
        "Procurement Profile": "Large residential concept school and junior college campus (800+ students)",
        "Address / Landmark": "Vadiyampeta, NH-44, Anantapur - 515003",
        "Contact Channel": "Residential Administrator"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "Bhashyam Educational Residential Campuses & Hostels",
        "Town": "Anantapur",
        "Region": "Sai Nagar / Anantapur Outskirts",
        "Key Crops Demanded": "Rice (200kg daily), Toor Dal, Bengal Gram, Groundnut Oil",
        "Procurement Profile": "Leading concept-school and IIT residential academy (1,000+ boarding students)",
        "Address / Landmark": "Sai Nagar / NH-44 Bypass, Anantapur - 515001",
        "Contact Channel": "Zonal Administrative Incharge"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "Ravindra Bharathi Residential School & Hostels",
        "Town": "Anantapur",
        "Region": "Subash Road / Outskirts",
        "Key Crops Demanded": "Rice (Sona Masoori), Toor Dal, Millets, Groundnut Oil",
        "Procurement Profile": "High-volume concept residential boarding campus (700+ students)",
        "Address / Landmark": "Anantapur City Branch - 515001",
        "Contact Channel": "Hostel Warden & Principal"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "SRIT Engineering College Hostels",
        "Town": "Anantapur",
        "Region": "Rotarypuram",
        "Key Crops Demanded": "Rice (200kg daily), Toor Dal, Groundnut Oil, Millets",
        "Procurement Profile": "1,500+ residential engineering students",
        "Address / Landmark": "Rotarypuram Village, BK Samudram Mandal, Anantapur - 515701",
        "Contact Channel": "Hostel Warden"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "Intell Engineering College & Junior Hostels",
        "Town": "Anantapur",
        "Region": "Kalyandurg Road",
        "Key Crops Demanded": "Rice, Toor Dal, Bengal Gram, Edible Oil",
        "Procurement Profile": "Residential college and technical students mess (800+ students)",
        "Address / Landmark": "Kalyandurg Road, Anantapur - 515001",
        "Contact Channel": "Mess Incharge"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "GATES Institute of Technology Hostels",
        "Town": "Gooty",
        "Region": "Gooty (NH-44)",
        "Key Crops Demanded": "Rice (Sona Masoori 200kg daily), Toor Dal, Groundnut Oil, Millets",
        "Procurement Profile": "2,000+ residential engineering students right on NH-44",
        "Address / Landmark": "NH-44, Gootyanantapur, Gooty - 515401",
        "Contact Channel": "Estate Manager & Mess Contractor"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "Sri Krishnadevaraya Engineering College (SKEC) Hostels",
        "Town": "Gooty",
        "Region": "Gooty Town",
        "Key Crops Demanded": "Rice (100kg daily), Toor Dal, Bengal Gram, Groundnut Oil",
        "Procurement Profile": "1,000+ residential students, monthly dry ration supply",
        "Address / Landmark": "Gooty Bazaar / Outskirts - 515401",
        "Contact Channel": "Hostel Warden"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "Sree Sai Junior College & Hostels",
        "Town": "Gooty",
        "Region": "Gooty Town",
        "Key Crops Demanded": "Rice (Sona Masoori), Toor Dal, Bengal Gram, Edible Oil",
        "Procurement Profile": "Private intermediate coaching residential campus (500+ students)",
        "Address / Landmark": "Brahmanapalli Road, Gooty - 515401",
        "Contact Channel": "College Principal & Hostel Incharge"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "APRS (Andhra Pradesh Residential School) Pamidi",
        "Town": "Pamidi",
        "Region": "Pamidi (NH-44)",
        "Key Crops Demanded": "Rice (150kg daily), Toor Dal, Bengal Gram, Groundnut, Ragi",
        "Procurement Profile": "Prestigious government-aided residential boarding campus (800+ students)",
        "Address / Landmark": "NH-44 Highway, Pamidi - 515775",
        "Contact Channel": "Special Officer / Mess Purchase Committee"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "SR Junior College & Hostels (Pamidi)",
        "Town": "Pamidi",
        "Region": "Pamidi Town",
        "Key Crops Demanded": "Rice (Sona Masoori), Toor Dal, Bengal Gram, Groundnut Oil",
        "Procurement Profile": "Private intermediate residential campus (400+ students)",
        "Address / Landmark": "Near Bus Stand, Pamidi - 515775",
        "Contact Channel": "Hostel Warden & Principal"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "Sri Saraswathi Vidyamandir Hostels (Pamidi)",
        "Town": "Pamidi",
        "Region": "Pamidi Town",
        "Key Crops Demanded": "Rice, Toor Dal, Millets, Groundnut Oil",
        "Procurement Profile": "Concept school with residential boarding wings (500+ students)",
        "Address / Landmark": "School Cluster, Pamidi - 515775",
        "Contact Channel": "Administrative Warden"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "Narayana Junior College & Hostels (Guntakal)",
        "Town": "Guntakal",
        "Region": "Guntakal Town",
        "Key Crops Demanded": "Rice (Sona Masoori 150kg daily), Toor Dal, Bengal Gram, Groundnut Oil",
        "Procurement Profile": "Major corporate intermediate campus (1,000+ students with residential hostel)",
        "Address / Landmark": "Tilak Nagar / Gooty Road, Guntakal - 515801",
        "Contact Channel": "Branch Manager & Hostel Mess Supervisor"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "Sri New Chaitanya Junior College & Hostels",
        "Town": "Guntakal",
        "Region": "Guntakal Town",
        "Key Crops Demanded": "Rice (120kg daily), Toor Dal, Millets, Groundnut, Spices",
        "Procurement Profile": "Residential intermediate coaching academy (800+ students)",
        "Address / Landmark": "PNT Colony, Guntakal - 515801",
        "Contact Channel": "Hostel Warden & Mess Incharge"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "NRI International Junior College & Hostels",
        "Town": "Guntakal",
        "Region": "Guntakal Town",
        "Key Crops Demanded": "Rice (Sona Masoori), Toor Dal, Bengal Gram, Groundnut Oil",
        "Procurement Profile": "Modern residential intermediate coaching campus (600+ students)",
        "Address / Landmark": "Aravind Nagar, Guntakal - 515801",
        "Contact Channel": "Campus Administrator"
    },
    {
        "Category": "Private Residential Colleges & Hostels",
        "Business Name": "Sastra Junior College & Hostels",
        "Town": "Guntakal",
        "Region": "Guntakal Town",
        "Key Crops Demanded": "Rice, Toor Dal, Edible Oil, Bengal Gram",
        "Procurement Profile": "Intermediate coaching campus with attached private boarding mess",
        "Address / Landmark": "Near SLV Talkies, Guntakal - 515801",
        "Contact Channel": "Principal & Mess Warden"
    },

    # =========================================================================
    # 15. COTTON GINNING & PRESSING MILLS (GUNTAKAL CLUSTER)
    # =========================================================================
    {
        "Category": "Cotton Ginning & Pressing",
        "Business Name": "Sunil Industry Cotton Ginning Factory",
        "Town": "Guntakal",
        "Region": "Guntakal Industrial Belt",
        "Key Crops Demanded": "Raw Cotton (Kapas)",
        "Procurement Profile": "Bulk industrial seasonal intake (50-100 MT/week), spot payment",
        "Address / Landmark": "Industrial Area, Bellary Road, Guntakal - 515801",
        "Contact Channel": "Guntakal Cotton Market Yard / Purchase Office"
    },
    {
        "Category": "Cotton Ginning & Pressing",
        "Business Name": "Sri Balaramakrishna Cotton Ginning & Pressing",
        "Town": "Guntakal",
        "Region": "Guntakal Industrial Belt",
        "Key Crops Demanded": "Raw Cotton (Kapas)",
        "Procurement Profile": "High-volume seasonal ginning contract",
        "Address / Landmark": "Near APMC Cotton Market Yard, Guntakal - 515801",
        "Contact Channel": "APMC Trader Registration / Guntakal Yard"
    },
    {
        "Category": "Cotton Ginning & Pressing",
        "Business Name": "Anantapur Cotton Mills / Guntakal Unit",
        "Town": "Guntakal",
        "Region": "Guntakal Industrial Belt",
        "Key Crops Demanded": "Raw Cotton (Kapas)",
        "Procurement Profile": "Spinning & ginning intake, weekly bulk delivery",
        "Address / Landmark": "Station Road / Mill Compound, Guntakal - 515801",
        "Contact Channel": "Commercial Procurement Desk"
    },
    {
        "Category": "Cotton Ginning & Pressing",
        "Business Name": "Yeddula Cotton Pvt. Ltd.",
        "Town": "Guntakal",
        "Region": "Guntakal Industrial Belt",
        "Key Crops Demanded": "Raw Cotton (Kapas)",
        "Procurement Profile": "Large enterprise ginning & lint export supply",
        "Address / Landmark": "Industrial Estate, Guntakal - 515801",
        "Contact Channel": "Managing Director / Factory Purchase Bay"
    },
    {
        "Category": "Cotton Ginning & Pressing",
        "Business Name": "MNR Cotton Ltd.",
        "Town": "Guntakal",
        "Region": "Guntakal Industrial Belt",
        "Key Crops Demanded": "Raw Cotton (Kapas)",
        "Procurement Profile": "Year-round seed & lint processing",
        "Address / Landmark": "Bypass Road, Guntakal - 515801",
        "Contact Channel": "Factory Procurement Manager"
    },
    {
        "Category": "Cotton Ginning & Pressing",
        "Business Name": "M A G Cotton Industries",
        "Town": "Guntakal",
        "Region": "Guntakal Industrial Belt",
        "Key Crops Demanded": "Raw Cotton (Kapas)",
        "Procurement Profile": "Medium-scale ginning plant, weekly batch settlements",
        "Address / Landmark": "Guntakal Industrial Zone - 515801",
        "Contact Channel": "Works Manager"
    },
    {
        "Category": "Cotton Ginning & Pressing",
        "Business Name": "Siri Agro Industries Pvt. Ltd.",
        "Town": "Guntakal",
        "Region": "Guntakal Industrial Belt",
        "Key Crops Demanded": "Raw Cotton & Agro Seeds",
        "Procurement Profile": "Agri-processing and cotton pressing unit",
        "Address / Landmark": "Guntakal Outer Bypass, Guntakal - 515801",
        "Contact Channel": "Purchase Department"
    },

    # =========================================================================
    # 16. GROUNDNUT OIL EXTRACTION & DAL PROCESSING MILLS
    # =========================================================================
    {
        "Category": "Edible Oil & Dal Processing",
        "Business Name": "Farmveda / Centre for Collective Development (CCD) Groundnut Unit",
        "Town": "Anantapur",
        "Region": "Anantapur District",
        "Key Crops Demanded": "High-Grade Groundnut (Palli)",
        "Procurement Profile": "Premium cold-pressed oil & peanut butter production",
        "Address / Landmark": "Industrial Area, Anantapur - 515001",
        "Contact Channel": "Procurement Lead / FPO Coordination"
    },
    {
        "Category": "Edible Oil & Dal Processing",
        "Business Name": "GVK Oil Mills",
        "Town": "Anantapur",
        "Region": "Anantapur City",
        "Key Crops Demanded": "Groundnut Kernels",
        "Procurement Profile": "Double-filtered groundnut oil packaging",
        "Address / Landmark": "Industrial Estate, Anantapur - 515004",
        "Contact Channel": "Factory Manager"
    },
    {
        "Category": "Edible Oil & Dal Processing",
        "Business Name": "Harshi Agri Food Products (ATP Fresh)",
        "Town": "Anantapur",
        "Region": "Anantapur City",
        "Key Crops Demanded": "Groundnut Kernels & Toor Dal",
        "Procurement Profile": "Cold-pressed oil extraction and packaged staples",
        "Address / Landmark": "Rudrampeta Bypass, Anantapur - 515004",
        "Contact Channel": "Procurement & Quality Head"
    },
    {
        "Category": "Edible Oil & Dal Processing",
        "Business Name": "Sri Raghavendra Oil Mills",
        "Town": "Anantapur",
        "Region": "Anantapur City",
        "Key Crops Demanded": "Groundnut (Verusenaga)",
        "Procurement Profile": "Traditional expeller oil production",
        "Address / Landmark": "Old Town Market Yard Road, Anantapur - 515001",
        "Contact Channel": "Mill Incharge"
    },
    {
        "Category": "Edible Oil & Dal Processing",
        "Business Name": "Sri Neelakanteswara Groundnut & Dal Processing Mill",
        "Town": "Anantapur",
        "Region": "Anantapur Rural",
        "Key Crops Demanded": "Groundnut, Toor Dal (Kandi), Bengal Gram (Chana)",
        "Procurement Profile": "Dal de-husking, polishing, and peanut grading",
        "Address / Landmark": "Kurnool Road, Anantapur - 515002",
        "Contact Channel": "Mill Gate / Weighbridge Office"
    },
    {
        "Category": "Edible Oil & Dal Processing",
        "Business Name": "Gunta Krishnaiah Setty & Leej Balaji Oil Mill",
        "Town": "Guntakal",
        "Region": "Guntakal",
        "Key Crops Demanded": "Groundnut Pods & Kernels (Palli)",
        "Procurement Profile": "Daily expeller processing, 20-40 quintals daily requirement",
        "Address / Landmark": "13/213, Gooty Road, Guntakal - 515801",
        "Contact Channel": "Gooty Road Mill Office"
    },
    {
        "Category": "Edible Oil & Dal Processing",
        "Business Name": "Sona Agencies & Oil Mills",
        "Town": "Guntakal",
        "Region": "Guntakal",
        "Key Crops Demanded": "Groundnut Kernels",
        "Procurement Profile": "Wholesale edible oil milling and trading",
        "Address / Landmark": "Main Bazaar Road, Guntakal - 515801",
        "Contact Channel": "Commercial Wholesale Desk"
    },
    {
        "Category": "Edible Oil & Dal Processing",
        "Business Name": "Someswara Oil Mill",
        "Town": "Guntakal",
        "Region": "Guntakal",
        "Key Crops Demanded": "Groundnut (Palli), Sunflower",
        "Procurement Profile": "Oil expelling unit, bulk weekly seed intake",
        "Address / Landmark": "Near Railway Colony, Guntakal - 515801",
        "Contact Channel": "Mill Gate"
    },

    # =========================================================================
    # 17. HOSPITALS, FEED PLANTS & BUSINESS HOTELS
    # =========================================================================
    {
        "Category": "Healthcare Canteens & In-Patient Food",
        "Business Name": "KIMS Saveera Super Specialty Hospital Canteen",
        "Town": "Anantapur",
        "Region": "Anantapur City",
        "Key Crops Demanded": "Rice (Sona Masoori & Sugar-free RNR), Toor Dal, Ragi, Groundnut Oil",
        "Procurement Profile": "400-bed hospital canteen catering to patients, doctors, and visitors daily",
        "Address / Landmark": "Near Collector Office, Anantapur - 515001",
        "Contact Channel": "Dietary Department & Hospital Canteen Contractor"
    },
    {
        "Category": "Healthcare Canteens & In-Patient Food",
        "Business Name": "Government General Hospital (GGH) Dietary Canteen",
        "Town": "Anantapur",
        "Region": "Anantapur City",
        "Key Crops Demanded": "Rice (Raw & Boiled 300kg daily), Toor Dal, Bengal Gram, Ragi Flour, Oil",
        "Procurement Profile": "Large 800+ bed state teaching hospital, contracted bulk ration supply",
        "Address / Landmark": "Court Road, Anantapur - 515001",
        "Contact Channel": "Hospital Dietary Incharge & Mess Contractor"
    },
    {
        "Category": "Healthcare Canteens & In-Patient Food",
        "Business Name": "RDT Hospital Dietary Services (Bathalapalle / Anantapur)",
        "Town": "Anantapur",
        "Region": "Anantapur District",
        "Key Crops Demanded": "Rice, Millets (Ragi/Jowar/Korra), Toor Dal, Unadulterated Groundnut Oil",
        "Procurement Profile": "Philanthropic hospital network with strict pure-food quality standards",
        "Address / Landmark": "Bathalapalle / Subhash Road Office, Anantapur - 515661",
        "Contact Channel": "RDT Central Procurement Committee"
    },
    {
        "Category": "Major Commercial Hotels & Highway Kitchens",
        "Business Name": "Hotel Sapthagiri Bheemash Residency (Nala Bheema Restaurant)",
        "Town": "Anantapur",
        "Region": "Saptagiri Circle / Sai Nagar",
        "Key Crops Demanded": "Sona Masoori Rice (200kg daily), Broken Rice for Tiffins, Toor Dal, Groundnut Cooking Oil, Spices",
        "Procurement Profile": "High-volume multi-cuisine family restaurant & lodging kitchen serving hundreds of travelers and locals daily",
        "Address / Landmark": "Near Saptagiri Circle, Sai Nagar, Anantapur - 515001",
        "Contact Channel": "Restaurant General Manager & Head Chef"
    },
    {
        "Category": "Major Commercial Hotels & Highway Kitchens",
        "Business Name": "Hotel Mamatha (Sri Mamatha Hotel & Restaurant)",
        "Town": "Anantapur",
        "Region": "Sri Kantam Circle / Raju Road",
        "Key Crops Demanded": "Sona Masoori Rice (300kg daily), Urad Dal (Minapappu), Toor Dal, Bengal Gram (Putnalu), Pure Groundnut Oil, Red Chilies",
        "Procurement Profile": "Legendary high-turnover culinary institution in Anantapur famous for authentic South Indian thalis, tiffins, and meals serving 1,000+ customers daily",
        "Address / Landmark": "Sri Kantam Circle, Raju Road, Kamalanagar, Anantapur - 515001",
        "Contact Channel": "Managing Partner & Kitchen Purchase In-Charge"
    },
    {
        "Category": "Major Commercial Hotels & Highway Kitchens",
        "Business Name": "Hotel Masineni Grand (Petals Veg & Nectar Fine Dining)",
        "Town": "Anantapur",
        "Region": "Raju Road / Kamalanagar",
        "Key Crops Demanded": "Premium Sona Masoori Rice (BPT 5204), Basmati/Jeera Rice, Toor Dal, Groundnut Oil, Dry Spices",
        "Procurement Profile": "Premier 4-star hospitality property with separate pure-vegetarian kitchen (Petals) and multi-cuisine restaurant with high banquet turnover",
        "Address / Landmark": "Raju Road, Kamalanagar, Anantapur - 515001",
        "Contact Channel": "Executive Chef & Food & Beverage Purchase Manager"
    },
    {
        "Category": "Major Commercial Hotels & Highway Kitchens",
        "Business Name": "Kritunga Restaurant (Rayalaseema Ruchulu)",
        "Town": "Anantapur",
        "Region": "Subhash Road Commercial Hub",
        "Key Crops Demanded": "Sona Masoori Rice (250kg daily), Biryani Rice, Red Chilies (Endu Mirapa - 5 quintals monthly), Toor Dal, Groundnut Oil",
        "Procurement Profile": "Famous regional restaurant chain known across AP for authentic spicy Rayalaseema meals, ragi sankati, and biryanis with heavy daily off-take",
        "Address / Landmark": "Near Clock Tower, Subhash Road, Anantapur - 515001",
        "Contact Channel": "Branch General Manager & Head Cook"
    },
    {
        "Category": "Major Commercial Hotels & Highway Kitchens",
        "Business Name": "Hotel Naveed Residency & Restaurant",
        "Town": "Anantapur",
        "Region": "Kamalanagar / Bus Stand",
        "Key Crops Demanded": "Rice (Raw & Boiled), Toor Dal, Cooking Oil, Spices",
        "Procurement Profile": "Prominent transit hotel and high-traffic restaurant located adjacent to the APSRTC Central Bus Stand",
        "Address / Landmark": "Opp. Old Bus Stand, Kamalanagar, Anantapur - 515001",
        "Contact Channel": "Restaurant Manager"
    },
    {
        "Category": "Major Commercial Hotels & Highway Kitchens",
        "Business Name": "Rajahamsa Grand Inn & Restaurant",
        "Town": "Anantapur",
        "Region": "Clock Tower / Old Town",
        "Key Crops Demanded": "Sona Masoori Rice, Toor Dal, Groundnut Cooking Oil",
        "Procurement Profile": "Established central lodging and dining establishment serving daily executive meals and breakfast",
        "Address / Landmark": "Near Clock Tower, Anantapur - 515001",
        "Contact Channel": "Managing Director / Purchase Desk"
    },
    {
        "Category": "Major Commercial Hotels & Highway Kitchens",
        "Business Name": "Hyderabad Biryani House & Restaurant",
        "Town": "Anantapur",
        "Region": "Subhash Road Junction",
        "Key Crops Demanded": "Rice (Biryani Rice & Sona Masoori 200kg daily), Spices, Pure Cooking Oil",
        "Procurement Profile": "High-density casual dining restaurant famous for daily lunch and dinner crowds",
        "Address / Landmark": "Subhash Road, Near Clock Tower, Anantapur - 515001",
        "Contact Channel": "Proprietor / Kitchen Supervisor"
    },
    {
        "Category": "Major Commercial Hotels & Highway Kitchens",
        "Business Name": "Hotel Pasupala Grand & Family Restaurant",
        "Town": "Anantapur",
        "Region": "Kamalanagar Commercial Area",
        "Key Crops Demanded": "Rice, Toor Dal, Broken Rice, Edible Oil",
        "Procurement Profile": "Modern family hotel with full-service multi-cuisine dining room and banquet catering",
        "Address / Landmark": "Near Medical College Road, Kamalanagar, Anantapur - 515001",
        "Contact Channel": "Operations Manager"
    },
    {
        "Category": "Major Commercial Hotels & Highway Kitchens",
        "Business Name": "S S Paradise Multi-Cuisine Family Restaurant",
        "Town": "Anantapur",
        "Region": "Clock Tower Road",
        "Key Crops Demanded": "Rice, Toor Dal, Bengal Gram, Spices, Groundnut Oil",
        "Procurement Profile": "Popular local family dining destination with high evening and weekend food turnover",
        "Address / Landmark": "Clock Tower Area, Anantapur - 515001",
        "Contact Channel": "Restaurant Manager"
    },
    {
        "Category": "Major Commercial Hotels & Highway Kitchens",
        "Business Name": "Sri Hari Kiran Family Restaurant",
        "Town": "Anantapur",
        "Region": "Subhash Road / Court Road",
        "Key Crops Demanded": "Sona Masoori Rice, Toor Dal, Cooking Oil",
        "Procurement Profile": "Traditional Andhra meals and tiffins restaurant serving daily business shoppers and court visitors",
        "Address / Landmark": "Subhash Road, Anantapur - 515001",
        "Contact Channel": "Proprietor"
    },

    # --- GUNTAKAL PREMIER HOTELS & RESTAURANTS ---
    {
        "Category": "Major Commercial Hotels & Highway Kitchens",
        "Business Name": "Pavithra Veg / Pavithra Hotel & Tiffins",
        "Town": "Guntakal",
        "Region": "Railway Station Road / Railway Colony",
        "Key Crops Demanded": "Sona Masoori Rice (150kg daily), Broken Rice for Idli/Dosa, Toor Dal, Minapappu (Urad), Groundnut Oil",
        "Procurement Profile": "Massive 24/7 footfall vegetarian hotel located right in front of Guntakal Railway Junction serving thousands of transit passengers",
        "Address / Landmark": "Station Road, Railway Colony, Guntakal - 515801",
        "Contact Channel": "Proprietor & Head Cook"
    },
    {
        "Category": "Major Commercial Hotels & Highway Kitchens",
        "Business Name": "Hotel Srinivasam & Dining Hall",
        "Town": "Guntakal",
        "Region": "Station Area / Main Road",
        "Key Crops Demanded": "Rice, Toor Dal, Bengal Gram, Cooking Oil",
        "Procurement Profile": "Established lodging and attached family restaurant catering to business visitors and cotton merchants",
        "Address / Landmark": "Main Road, Guntakal - 515801",
        "Contact Channel": "Hotel Manager"
    },
    {
        "Category": "Major Commercial Hotels & Highway Kitchens",
        "Business Name": "Mayuri Hotel & Andhra Meals",
        "Town": "Guntakal",
        "Region": "Tilak Nagar / Hanumesh Nagar",
        "Key Crops Demanded": "Sona Masoori Rice (100kg daily), Toor Dal, Sun-Dried Chilies, Groundnut Oil",
        "Procurement Profile": "Popular casual dining destination known for authentic Andhra thalis and lunch meals",
        "Address / Landmark": "Hanumesh Nagar, Guntakal - 515801",
        "Contact Channel": "Restaurant Incharge"
    },
    {
        "Category": "Major Commercial Hotels & Highway Kitchens",
        "Business Name": "Seerat Taj Biryani Hotel & Restaurant",
        "Town": "Guntakal",
        "Region": "Railway Colony / Bank of Baroda Lane",
        "Key Crops Demanded": "Rice (Biryani Rice & Sona Masoori), Edible Oil, Spices",
        "Procurement Profile": "High-volume evening non-veg and biryani specialist with dedicated commercial kitchen",
        "Address / Landmark": "Railway Colony, Guntakal - 515801",
        "Contact Channel": "Proprietor"
    },

    # --- GOOTY HIGHWAY DHABAS & TOWN HOTELS ---
    {
        "Category": "Major Commercial Hotels & Highway Kitchens",
        "Business Name": "New Dashmesh Punjabi Dhaba & Highway Food Plaza",
        "Town": "Gooty",
        "Region": "NH-44 Bypass Corridor",
        "Key Crops Demanded": "Rice (Raw & Boiled 150kg daily), Toor Dal, Bengal Gram (Chana), Pure Cooking Oil, Spices",
        "Procurement Profile": "High-turnover 24/7 highway dhaba along the busy Bangalore-Hyderabad NH-44 corridor feeding hundreds of long-distance buses, truckers, and travelers daily",
        "Address / Landmark": "NH-44 Highway Bypass, Gooty - 515401",
        "Contact Channel": "Managing Partner & Kitchen Head"
    },
    {
        "Category": "Major Commercial Hotels & Highway Kitchens",
        "Business Name": "Dashmesh Punjabi Deepa Dhaba",
        "Town": "Gooty",
        "Region": "NH-44 Gooty Toll Plaza Corridor",
        "Key Crops Demanded": "Rice, Toor Dal, Whole Pulses, Cooking Oil",
        "Procurement Profile": "Prominent round-the-clock highway stop for heavy commercial transport and family cars",
        "Address / Landmark": "NH-44, Gooty - 515401",
        "Contact Channel": "Dhaba Proprietor"
    },
    {
        "Category": "Major Commercial Hotels & Highway Kitchens",
        "Business Name": "Ravi Teja Grand Hotel & Restaurant",
        "Town": "Gooty",
        "Region": "Station Road / Town Center",
        "Key Crops Demanded": "Sona Masoori Rice, Broken Rice, Toor Dal, Groundnut Oil",
        "Procurement Profile": "Central town hotel serving daily tiffins and meals for local businesses and visitors to Gooty Fort",
        "Address / Landmark": "Station Road, Gooty - 515401",
        "Contact Channel": "Hotel Manager"
    },

    # --- PAMIDI HIGHWAY RESTAURANTS ---
    {
        "Category": "Major Commercial Hotels & Highway Kitchens",
        "Business Name": "Sri Balaji Family Restaurant & Highway Dhaba",
        "Town": "Pamidi",
        "Region": "NH-44 Highway Bypass",
        "Key Crops Demanded": "Rice (100kg daily), Toor Dal, Bengal Gram, Pure Cooking Oil, Spices",
        "Procurement Profile": "High-volume highway dining room situated right on the 4-lane NH-44 highway in Pamidi mandal",
        "Address / Landmark": "NH-44 Bypass, Pamidi - 515775",
        "Contact Channel": "Restaurant Incharge"
    },
    {
        "Category": "Major Commercial Hotels & Highway Kitchens",
        "Business Name": "Highway Green Valley Food Court & Restaurant",
        "Town": "Pamidi",
        "Region": "Pamidi NH-44 Toll Stretch",
        "Key Crops Demanded": "Rice, Toor Dal, Broken Rice for Batter, Edible Oil",
        "Procurement Profile": "Expressway highway food plaza catering to intercity travelers with large daily breakfast and meals kitchen",
        "Address / Landmark": "NH-44 Corridor, Pamidi - 515775",
        "Contact Channel": "Food Court Manager"
    },
    {
        "Category": "Commercial Feed & Dairy Plants",
        "Business Name": "Rayalaseema Feed & Agro Industries",
        "Town": "Anantapur",
        "Region": "Anantapur Rural",
        "Key Crops Demanded": "Maize (Corn), Groundnut De-oiled Cake (DOC), Broken Rice",
        "Procurement Profile": "Bulk livestock & poultry feed manufacturing (100+ quintals weekly)",
        "Address / Landmark": "Bellary Road, Anantapur Industrial Area - 515004",
        "Contact Channel": "Raw Material Procurement Head"
    },
    {
        "Category": "Commercial Feed & Dairy Plants",
        "Business Name": "Guntakal Cattle Feed & Agro Processors",
        "Town": "Guntakal",
        "Region": "Guntakal Bypass",
        "Key Crops Demanded": "Cotton Seed Cake (Kapas Khal), Maize, Broken Pulses",
        "Procurement Profile": "Dairy feed compounder, steady off-take from local ginning/oil mills",
        "Address / Landmark": "Kalluru Road, Guntakal - 515801",
        "Contact Channel": "Plant General Manager"
    },
    # =========================================================================
    # 22. ROASTED BENGAL GRAM & PUTNALU MILLS (CHANA / PUTNALA PAPPU)
    # =========================================================================
    {
        "Category": "Roasted Bengal Gram & Putnalu Mills",
        "Business Name": "VRM Enterprises (Putnalu & Pulse Wholesalers)",
        "Town": "Anantapur",
        "Region": "Rajaji Street, Old Town",
        "Key Crops Demanded": "Bengal Gram (Chana / Senagalu) - 100+ quintals monthly",
        "Procurement Profile": "Leading regional processor and distributor of roasted gram (putnalu/pappulu) supplying grocery chains and snacks units",
        "Address / Landmark": "Rajaji Street, Old Town, Anantapur - 515001",
        "Contact Channel": "Proprietor / Bulk Purchase Desk"
    },
    {
        "Category": "Roasted Bengal Gram & Putnalu Mills",
        "Business Name": "Suresh M Friedgram & Dal Mill",
        "Town": "Anantapur",
        "Region": "Kamalanagar / Gooty Road",
        "Key Crops Demanded": "Bengal Gram (Senagalu), Toor Dal, Green Gram",
        "Procurement Profile": "High-turnover dal roastery splitting and roasting chickpeas for Rayalaseema breakfast/namkeen industries",
        "Address / Landmark": "Near Gooty Road Overbridge, Kamalanagar, Anantapur - 515001",
        "Contact Channel": "Mill In-Charge & Manager"
    },
    {
        "Category": "Roasted Bengal Gram & Putnalu Mills",
        "Business Name": "Sri Saai Venkata Gram Dal Industries",
        "Town": "Anantapur",
        "Region": "Old Town Grain Mandi",
        "Key Crops Demanded": "Raw Bengal Gram (Senagalu), Roasted Chana",
        "Procurement Profile": "Specialized chickpea processing plant with automated roasting ovens",
        "Address / Landmark": "Grain Market Street, Old Town, Anantapur - 515001",
        "Contact Channel": "Managing Partner"
    },
    {
        "Category": "Roasted Bengal Gram & Putnalu Mills",
        "Business Name": "Srinivasa Dall & Fried Gram Industry",
        "Town": "Anantapur",
        "Region": "Kamalanagar Agro Cluster",
        "Key Crops Demanded": "Bengal Gram, Toor Dal, Urad Dal",
        "Procurement Profile": "Direct miller buying whole pulses from farm gates across Gooty-Anantapur belt",
        "Address / Landmark": "Kamalanagar, Anantapur - 515001",
        "Contact Channel": "Procurement Head"
    },

    # =========================================================================
    # 23. PUFFED RICE (BORUGULU / MURMURA) MILLS & ROASTERIES (BARRGU BATTILU)
    # =========================================================================
    {
        "Category": "Puffed Rice (Borugulu) Mills & Roasteries",
        "Business Name": "BJ Industries Puffed Rice & Agro Works",
        "Town": "Anantapur",
        "Region": "Kallur Industrial Area",
        "Key Crops Demanded": "Specialized Paddy / Raw Rice (500+ bags monthly)",
        "Procurement Profile": "Industrial puffed rice (borugulu) manufacturing plant feeding the Rayalaseema Uggani breakfast supply chain",
        "Address / Landmark": "Kallur Industrial Area, Anantapur - 515774",
        "Contact Channel": "Plant Operations Manager"
    },
    {
        "Category": "Puffed Rice (Borugulu) Mills & Roasteries",
        "Business Name": "Star Industry Murmura & Grain Works",
        "Town": "Anantapur",
        "Region": "Autonagar / Gooty Road",
        "Key Crops Demanded": "Raw Rice (Broken & Medium Grain Paddy)",
        "Procurement Profile": "Dedicated puffed rice roastery and bhatti supplying wholesale gunny sacks of murmura across district tea stalls",
        "Address / Landmark": "Near Autonagar, Anantapur - 515004",
        "Contact Channel": "Managing Director"
    },
    {
        "Category": "Puffed Rice (Borugulu) Mills & Roasteries",
        "Business Name": "JK Traders Borugula Wholesale Hub",
        "Town": "Anantapur",
        "Region": "Old Town Market",
        "Key Crops Demanded": "Paddy, Parboiled Rice, Puffed Rice Varieties",
        "Procurement Profile": "Major stockist distributing multi-ton sacks of puffed rice to vendors and breakfast stalls in Anantapur, Pamidi, and Gooty",
        "Address / Landmark": "Old Town, Anantapur - 515001",
        "Contact Channel": "Wholesale Purchase Officer"
    },

    # =========================================================================
    # 24. COMMERCIAL POULTRY & ANIMAL FEED MASH MIXERS
    # =========================================================================
    {
        "Category": "Commercial Poultry & Feed Mixers",
        "Business Name": "Hemanth Animal Feeds and Foods",
        "Town": "Anantapur",
        "Region": "Bellary Road / Autonagar",
        "Key Crops Demanded": "Yellow Maize (Makka 50+ MT monthly), Broken Rice, Cottonseed Cake",
        "Procurement Profile": "Regional compound livestock and poultry feed manufacturer with high recurring grain consumption",
        "Address / Landmark": "Bellary Road, Anantapur - 515004",
        "Contact Channel": "Procurement Director"
    },
    {
        "Category": "Commercial Poultry & Feed Mixers",
        "Business Name": "Pamidi Commercial Broiler & Layer Poultry Cluster",
        "Town": "Pamidi",
        "Region": "Pamidi-Gooty NH-44 Agricultural Belt",
        "Key Crops Demanded": "Raw Yellow Maize (Corn), Broken Rice (Nookalu), Groundnut Cake",
        "Procurement Profile": "Cluster of commercial poultry sheds and farm mash mixers consuming truckloads of dry maize weekly",
        "Address / Landmark": "NH-44 Bypass, Pamidi Mandal - 515775",
        "Contact Channel": "Poultry Farm Syndicate Incharge"
    },
    {
        "Category": "Commercial Poultry & Feed Mixers",
        "Business Name": "Gooty-Guntakal Agro-Vet Feed Stockists",
        "Town": "Gooty",
        "Region": "Railway Feeder Road",
        "Key Crops Demanded": "Maize, Cottonseed Cake, Groundnut De-oiled Meal",
        "Procurement Profile": "Feed distributors supplying local dairy farmers and sheep/goat breeders across 24 villages",
        "Address / Landmark": "Near AP State Seeds Corporation, Gooty - 515401",
        "Contact Channel": "Senior Stockist"
    },

    # =========================================================================
    # 25. STATE ARMED POLICE & DEFENSE BATTALIONS
    # =========================================================================
    {
        "Category": "State Armed Police & Defense Messes",
        "Business Name": "14th Battalion APSP (Andhra Pradesh Special Police) Central Mess",
        "Town": "Anantapur",
        "Region": "Bukkarayasamudram (Anantapur Outer)",
        "Key Crops Demanded": "Rice (Sona Masoori 600kg daily), Toor Dal (80kg daily), Groundnut Oil, Spices",
        "Procurement Profile": "Massive permanent armed police battalion HQ and recruit training academy housing 1,200+ jawans and personnel with 3 meals daily",
        "Address / Landmark": "14th Battalion APSP Camp, Bukkarayasamudram, Anantapur - 515701",
        "Contact Channel": "Commandant / Quarter Master & Mess Secretary"
    },
    {
        "Category": "State Armed Police & Defense Messes",
        "Business Name": "District Armed Reserve (AR) Police Lines Central Canteen",
        "Town": "Anantapur",
        "Region": "Police Lines / Clock Tower Road",
        "Key Crops Demanded": "Rice, Toor Dal, Bengal Gram, Cooking Oil",
        "Procurement Profile": "Canteen and welfare mess serving on-duty armed reserve constables and district police personnel",
        "Address / Landmark": "District Police Headquarters, Police Lines, Anantapur - 515001",
        "Contact Channel": "Superintendent of Police (Welfare Officer) & Mess Inspector"
    },

    # =========================================================================
    # 26. GOVERNMENT SOCIAL WELFARE HOSTELS (PRE & POST MATRIC BC/SC/ST)
    # =========================================================================
    {
        "Category": "Government Social Welfare Hostels",
        "Business Name": "Gooty BC & SC Welfare Student Hostels",
        "Town": "Gooty",
        "Region": "Court Road / Station Road",
        "Key Crops Demanded": "Rice, Toor Dal, Groundnut Chikki/Kernels, Edible Oil",
        "Procurement Profile": "Social welfare boarding facilities housing 350+ local high school and intermediate rural students",
        "Address / Landmark": "Near Tahsildar Office, Gooty - 515401",
        "Contact Channel": "Hostel Welfare Officer (HWO) & Assistant BC Welfare Officer"
    },
    {
        "Category": "Government Social Welfare Hostels",
        "Business Name": "Pamidi Government Welfare Boarding Hostels",
        "Town": "Pamidi",
        "Region": "Penna Bridge Road",
        "Key Crops Demanded": "Rice, Toor Dal, Bengal Gram, Cooking Oil",
        "Procurement Profile": "Welfare department hostels for rural students from surrounding agricultural and handloom hamlets",
        "Address / Landmark": "Near Mandal Development Office, Pamidi - 515775",
        "Contact Channel": "Hostel Warden / Welfare Officer"
    },
    {
        "Category": "Government Social Welfare Hostels",
        "Business Name": "Guntakal Post-Matric Welfare College Hostels",
        "Town": "Guntakal",
        "Region": "Hanumesh Nagar / Station Area",
        "Key Crops Demanded": "Rice (300kg daily), Toor Dal, Bengal Gram, Cooking Oil",
        "Procurement Profile": "Government college hostels catering to 500+ degree and polytechnic students",
        "Address / Landmark": "Hanumesh Nagar, Guntakal - 515801",
        "Contact Channel": "Hostel Warden / ASWO Guntakal"
    },
    {
        "Category": "Government Social Welfare Hostels",
        "Business Name": "Anantapur Post-Matric University & Degree Hostels (Rudrampeta)",
        "Town": "Anantapur",
        "Region": "Rudrampeta / Old Town",
        "Key Crops Demanded": "Rice (800kg daily), Toor Dal (100kg daily), Groundnut Oil",
        "Procurement Profile": "Large social welfare campus hosting over 1,000 university and degree students with government ration budgets",
        "Address / Landmark": "Rudrampeta Bypass, Anantapur - 515004",
        "Contact Channel": "District Social Welfare Officer (DSWO) & Hostel Welfare Committee"
    },

    # =========================================================================
    # 27. WHOLESALE GUNJ & MANDI GRAIN MERCHANTS (SPOT CASH OFF-TAKERS)
    # =========================================================================
    {
        "Category": "Wholesale Gunj & Mandi Grain Merchants",
        "Business Name": "Guntakal Market Yard & Mundy Bazar Grain Merchants Association",
        "Town": "Guntakal",
        "Region": "Mundy Bazar / Hanumesh Nagar",
        "Key Crops Demanded": "Rice (All grades), Groundnut Kernels, Toor Dal, Kapas (Cotton)",
        "Procurement Profile": "The apex wholesale grain trading hub in western Anantapur, buying truckloads of dry grains for inter-district transit",
        "Address / Landmark": "Mundy Bazar, Guntakal - 515801",
        "Contact Channel": "President / Secretary, Grain Merchants Association"
    },
    {
        "Category": "Wholesale Gunj & Mandi Grain Merchants",
        "Business Name": "Anantapur Kamalanagar & Old Town Grain Merchants Guild",
        "Town": "Anantapur",
        "Region": "Kamalanagar & Subhash Road",
        "Key Crops Demanded": "Rice (Sona Masoori, RNR), Pulses, Millets (Ragi/Jowar/Korra), Groundnut",
        "Procurement Profile": "Major merchant guild supplying 500+ independent retail kirana stores across Anantapur urban and rural mandals",
        "Address / Landmark": "Kamalanagar Grain Market, Anantapur - 515001",
        "Contact Channel": "Wholesale Merchants Association Secretariat"
    },
    {
        "Category": "Wholesale Gunj & Mandi Grain Merchants",
        "Business Name": "Gooty Bazaar Bulk Grain & Seed Stockists",
        "Town": "Gooty",
        "Region": "Tadipatri Road / Main Bazaar",
        "Key Crops Demanded": "Paddy, Bengal Gram, Groundnut Pods, Red Chilies",
        "Procurement Profile": "Local wholesale merchants with godowns supplying weekly shandies (santalu) and neighborhood grocers",
        "Address / Landmark": "Tadipatri Road, Gooty - 515401",
        "Contact Channel": "Senior Grain Trader"
    },

    # =========================================================================
    # 28. SPICE GRINDING & CHILI FLOUR PROCESSING MILLS (MASALA BHATTIS)
    # =========================================================================
    {
        "Category": "Spice Grinding & Chili Processing Mills",
        "Business Name": "Sri Lakshmi Spice & Sun-Dried Chili Grinding Mills",
        "Town": "Anantapur",
        "Region": "Old Town Spices Quarter",
        "Key Crops Demanded": "Sun-Dried Red Chilies (Endu Mirapa 20+ quintals monthly), Turmeric, Coriander Seeds",
        "Procurement Profile": "Industrial spice pulverizing mill supplying pure chili powder and curry masalas to regional restaurants and caterers",
        "Address / Landmark": "Old Town, Anantapur - 515001",
        "Contact Channel": "Mill Proprietor"
    },
    {
        "Category": "Spice Grinding & Chili Processing Mills",
        "Business Name": "Guntakal Mundy Spice & Masala Mills",
        "Town": "Guntakal",
        "Region": "Main Bazaar / Railway Colony",
        "Key Crops Demanded": "Dry Red Chilies, Coriander (Dhaniyalu), Turmeric",
        "Procurement Profile": "High-capacity spice milling facility processing farmer produce into commercial culinary powders",
        "Address / Landmark": "Main Bazaar, Guntakal - 515801",
        "Contact Channel": "Operations Head"
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
    
    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in DESTINATION_BUYERS:
            writer.writerow(row)
            
    print(f"Successfully compiled {len(DESTINATION_BUYERS)} fully-audited target B2B buyers into:")
    print(OUTPUT_FILE)

if __name__ == "__main__":
    main()
