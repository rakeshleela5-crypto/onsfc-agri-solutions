#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Kurnool High-Ticket Commercial Expansion Buyer Database Compiler
A dedicated, separate section analyzing high-ticket B2B buyers in Kurnool (50-92 km North via NH-44).
"""

import os
import csv

OUTPUT_DIR = r"C:\Users\rakes\.gemini\antigravity\scratch\onsfc-agri-solutions\data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "ONSFC_Kurnool_High_Ticket_Buyers.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

KURNOOL_HIGH_TICKET_BUYERS = [
    # =========================================================================
    # 1. MEGA PILGRIMAGE ANNADHANAM TRUSTS
    # =========================================================================
    {
        "Category": "Mega Pilgrimage Annadhanam Trusts",
        "Business Name": "Sri Raghavendra Swamy Mutt Central Annadhanam Trust (Mantralayam)",
        "Town": "Kurnool District",
        "Region": "Mantralayam (Via Yemmiganur/Kurnool)",
        "Key Crops Demanded": "Rice (Sona Masoori 1,000+ kg daily), Toor Dal (150 kg daily), Pure Groundnut Oil, Jaggery, Mustard/Cumin/Chilies",
        "Procurement Profile": "Famous sacred shrine serving free 'Tirtha Prasada' to 4,000 to 5,000 devotees daily (10,000+ on weekends/festivals). High-ticket direct supplier opportunity.",
        "Address / Landmark": "Sri Raghavendra Swamy Matha, Mantralayam - 518345",
        "Contact Channel": "Administrative Officer (AO) / Central Annadhanam Bhandaram Incharge"
    },

    # =========================================================================
    # 2. PREMIER UNIVERSITIES & RESIDENTIAL INSTITUTES OF NATIONAL IMPORTANCE
    # =========================================================================
    {
        "Category": "Universities & Premier National Institutes",
        "Business Name": "IIITDM Kurnool (Indian Institute of Information Technology, Design & Manufacturing)",
        "Town": "Kurnool",
        "Region": "Jagannathagattu / Dinnedevarapadu",
        "Key Crops Demanded": "Rice (Sona Masoori 350 kg daily), Toor Dal, Bengal Gram, Pure Cooking Oil",
        "Procurement Profile": "Central Government Institute of National Importance; 151-acre campus housing 1,200+ residential students across Kalam Hall, SRK, and Kalpana Chawla Hall of Residence.",
        "Address / Landmark": "Jagannathagattu, Dinnedevarapadu, Kurnool - 518007",
        "Contact Channel": "Registrar / Chief Warden / Student Mess Council"
    },
    {
        "Category": "Universities & Premier National Institutes",
        "Business Name": "G. Pulla Reddy Engineering College (GPREC) Autonomous Hostels",
        "Town": "Kurnool",
        "Region": "G. Pulla Reddy Nagar, Nandyal Road",
        "Key Crops Demanded": "Rice (Sona Masoori 500 kg daily), Toor Dal (60 kg daily), Groundnut Oil, Millets",
        "Procurement Profile": "Legendary premier institution housing 1,870 residential hostellers (670 boys in campus blocks + 1,200 girls at G. Narayanamma Balikala Vasathi Gruham) with 3 full meals daily.",
        "Address / Landmark": "GPREC Campus, Nandyal Road, Kurnool - 518007",
        "Contact Channel": "Hostel Warden / General Secretary & Mess Committee"
    },
    {
        "Category": "Universities & Premier National Institutes",
        "Business Name": "Silver Jubilee Government College (Autonomous) Residential Hostels",
        "Town": "Kurnool",
        "Region": "B-Camp, Kurnool",
        "Key Crops Demanded": "Rice (Sona Masoori 300 kg daily), Toor Dal, Bengal Gram, Cooking Oil",
        "Procurement Profile": "Historic 100% fully residential premier government college established by PV Narasimha Rao housing 800+ meritorious boarders managed by student mess observers.",
        "Address / Landmark": "B-Camp, Kurnool - 518002",
        "Contact Channel": "Principal & Student Mess Observer Committee"
    },
    {
        "Category": "Universities & Premier National Institutes",
        "Business Name": "Kurnool Medical College (KMC) & Resident Hostels",
        "Town": "Kurnool",
        "Region": "Budhawara Peta / Hospital Road",
        "Key Crops Demanded": "Rice (Sona Masoori 400 kg daily), Toor Dal, Bengal Gram, Groundnut Cooking Oil",
        "Procurement Profile": "One of the oldest medical colleges in South India housing 1,500+ undergraduate MBBS students, intern doctors, and PG residents in on-campus hostels.",
        "Address / Landmark": "Near GGH, Budhawara Peta, Kurnool - 518002",
        "Contact Channel": "Vice-Principal & Resident Doctors Mess Committee"
    },
    {
        "Category": "Universities & Premier National Institutes",
        "Business Name": "Rayalaseema University (RU Campus & Hostels)",
        "Town": "Kurnool",
        "Region": "Pasupula / Nandyal Road",
        "Key Crops Demanded": "Rice (350 kg daily), Toor Dal, Groundnut Oil, Spices",
        "Procurement Profile": "State university campus with Tungabhadra Boys Hostel and on-campus Women's Hostel housing 700+ university boarders.",
        "Address / Landmark": "Pasupula Village, Nandyal Road, Kurnool - 518007",
        "Contact Channel": "Registrar / Hostel Executive Warden"
    },
    {
        "Category": "Universities & Premier National Institutes",
        "Business Name": "Dr. K.V. Subba Reddy Group of Institutions (Engineering & Pharmacy)",
        "Town": "Kurnool",
        "Region": "Opp. Dupadu Railway Station, NH-44",
        "Key Crops Demanded": "Rice (300 kg daily), Toor Dal, Bengal Gram, Groundnut Oil",
        "Procurement Profile": "Large highway campus on NH-44 with 1,000+ residential hostellers and daily dining halls.",
        "Address / Landmark": "Opp. Dupadu RS, NH-44, Kurnool - 518218",
        "Contact Channel": "Administrative Officer / Campus Mess Contractor"
    },
    {
        "Category": "Universities & Premier National Institutes",
        "Business Name": "G. Pullaiah College of Engineering and Technology (GPCET)",
        "Town": "Kurnool",
        "Region": "Nandikotkur Road",
        "Key Crops Demanded": "Rice, Toor Dal, Edible Oil, Spices",
        "Procurement Profile": "Reputed engineering college with separate on-campus hostels boarding 800+ students.",
        "Address / Landmark": "Near Venkayapalle, Nandikotkur Road, Kurnool - 518452",
        "Contact Channel": "Hostel Supervisor / Administrative Office"
    },
    {
        "Category": "Universities & Premier National Institutes",
        "Business Name": "Brindavan Institute of Technology and Science (BITS Kurnool)",
        "Town": "Kurnool",
        "Region": "NH-44, Peddatekur",
        "Key Crops Demanded": "Rice (200 kg daily), Toor Dal, Groundnut Oil",
        "Procurement Profile": "Campus directly located on the NH-44 Gooty-Kurnool highway housing 600+ boarders.",
        "Address / Landmark": "NH-44, Peddatekur, Kurnool - 518218",
        "Contact Channel": "Campus Director / Hostel Mess Manager"
    },

    # =========================================================================
    # 3. PRIVATE CORPORATE RESIDENTIAL MEGA-CAMPUSES (NARAYANA & SRI CHAITANYA)
    # =========================================================================
    {
        "Category": "Private Corporate Residential Mega-Campuses",
        "Business Name": "Narayana IIT-JEE Mega Residential Boys Campus (Nannur Toll Plaza)",
        "Town": "Kurnool",
        "Region": "Nannur / Orvakal NH-40 Corridor",
        "Key Crops Demanded": "Rice (Sona Masoori 500 kg daily), Toor Dal (60 kg daily), Groundnut Oil",
        "Procurement Profile": "High-density residential coaching township housing 1,500+ intermediate IIT-JEE/NEET aspirants with strict 4-meal daily catering.",
        "Address / Landmark": "Near Nannur Toll Plaza, Kurnool - 518002",
        "Contact Channel": "Zonal Purchase Manager / Campus DGM"
    },
    {
        "Category": "Private Corporate Residential Mega-Campuses",
        "Business Name": "Narayana Residential Girls Campus (Orvakal / Gayatri Estates)",
        "Town": "Kurnool",
        "Region": "Gayatri Estates & Orvakal",
        "Key Crops Demanded": "Rice (350 kg daily), Toor Dal, Bengal Gram, Cooking Oil",
        "Procurement Profile": "Dedicated girls residential coaching academy with 1,000+ hostellers.",
        "Address / Landmark": "Gayatri Estates / Orvakal Campus, Kurnool - 518002",
        "Contact Channel": "Campus Incharge / Food & Nutrition Supervisor"
    },
    {
        "Category": "Private Corporate Residential Mega-Campuses",
        "Business Name": "Sri Chaitanya Boys Residential IIT Academy (B. Tandrapadu)",
        "Town": "Kurnool",
        "Region": "B. Tandrapadu",
        "Key Crops Demanded": "Rice (Sona Masoori 450 kg daily), Toor Dal, Groundnut Oil",
        "Procurement Profile": "Flagship residential boys campus boarding 1,200+ students on rigid exam diets.",
        "Address / Landmark": "B. Tandrapadu, Kurnool - 518002",
        "Contact Channel": "Kurnool Regional Dean / Mess Contractor"
    },
    {
        "Category": "Private Corporate Residential Mega-Campuses",
        "Business Name": "Sri Chaitanya Girls Residential Academy (Dinnedevarapadu)",
        "Town": "Kurnool",
        "Region": "Dinnedevarapadu",
        "Key Crops Demanded": "Rice (350 kg daily), Toor Dal, Bengal Gram, Edible Oil",
        "Procurement Profile": "Residential girls campus boarding 1,000+ students.",
        "Address / Landmark": "Dinnedevarapadu, Kurnool - 518002",
        "Contact Channel": "Campus Administrator"
    },
    {
        "Category": "Private Corporate Residential Mega-Campuses",
        "Business Name": "Keshava Reddy Residential Educational Complex",
        "Town": "Kurnool",
        "Region": "NH-44 Bypass / Alur Road",
        "Key Crops Demanded": "Rice, Toor Dal, Edible Oil, Chana",
        "Procurement Profile": "Historic residential schooling network boarding 700+ students.",
        "Address / Landmark": "NH-44 Bypass, Kurnool - 518003",
        "Contact Channel": "Principal & Procurement Head"
    },

    # =========================================================================
    # 4. STATE DEFENSE, POLICE FORCES & CORRECTIONAL MESSES
    # =========================================================================
    {
        "Category": "State Armed Police & Defense Messes",
        "Business Name": "2nd Battalion APSP (Andhra Pradesh Special Police) Central Mess",
        "Town": "Kurnool",
        "Region": "APSP Battalion Complex, Kurnool",
        "Key Crops Demanded": "Rice (Sona Masoori 600 kg daily), Toor Dal (75 kg daily), Groundnut Oil, Spices",
        "Procurement Profile": "Major state armed police battalion headquarters and training base housing 1,200+ jawans and personnel with 3 daily dining mess sessions.",
        "Address / Landmark": "2nd Battalion APSP Grounds, Kurnool - 518003",
        "Contact Channel": "Commandant / Quarter Master & Battalion Mess Secretary"
    },
    {
        "Category": "State Armed Police & Defense Messes",
        "Business Name": "Kurnool District Jail & Correctional Ration Store",
        "Town": "Kurnool",
        "Region": "Near Collectorate / Old Town",
        "Key Crops Demanded": "Rice (Coarse/Sona Masoori 350 kg daily), Toor Dal, Bengal Gram, Cooking Oil",
        "Procurement Profile": "Government correctional institution catering to inmates under statutory prison ration schedules.",
        "Address / Landmark": "Near District Court Complex, Kurnool - 518001",
        "Contact Channel": "Jail Superintendent / Ration Store Keeper"
    },

    # =========================================================================
    # 5. HOSPITALS & IN-PATIENT DIETARY KITCHENS
    # =========================================================================
    {
        "Category": "Hospitals & Dietary Canteens",
        "Business Name": "Government General Hospital (GGH Kurnool) Dietary Kitchen",
        "Town": "Kurnool",
        "Region": "Hospital Road / Budhawara Peta",
        "Key Crops Demanded": "Rice (500 kg daily), Toor Dal (60 kg daily), Ragi, Broken Rice, Cooking Oil",
        "Procurement Profile": "Massive 1,500-bed apex government teaching hospital serving three daily meals to inpatients, plus huge medical staff canteen.",
        "Address / Landmark": "GGH Complex, Kurnool - 518002",
        "Contact Channel": "Hospital Superintendent / Dietary Department Contractor"
    },
    {
        "Category": "Hospitals & Dietary Canteens",
        "Business Name": "KIMS Hospitals Kurnool (Central Canteen & Dietary Kitchen)",
        "Town": "Kurnool",
        "Region": "Joharapuram Road / New Building",
        "Key Crops Demanded": "Sona Masoori Rice, Toor Dal, Unadulterated Groundnut Oil, Millets",
        "Procurement Profile": "350-bed premier corporate hospital with 24/7 cafeteria on Ground Floor and dedicated in-patient dietary food service.",
        "Address / Landmark": "Joharapuram Road, Kurnool - 518002",
        "Contact Channel": "Facility General Manager / Dietary Incharge"
    },
    {
        "Category": "Hospitals & Dietary Canteens",
        "Business Name": "Medicover Hospitals Kurnool Cafeteria & In-Patient Service",
        "Town": "Kurnool",
        "Region": "Sampath Nagar",
        "Key Crops Demanded": "Rice, Toor Dal, Bengal Gram, Pure Cooking Oil",
        "Procurement Profile": "250-bed multi-super-specialty corporate hospital with centralized dining facility.",
        "Address / Landmark": "Sampath Nagar, Kurnool - 518003",
        "Contact Channel": "Hospital Admin & F&B Manager"
    },

    # =========================================================================
    # 6. EDIBLE OIL REFINERIES, SOLVENT EXTRACTION & COTTON GINNING GIANTS
    # =========================================================================
    {
        "Category": "Edible Oil, Solvent Extraction & Cotton Giants",
        "Business Name": "Damodara Oil Mill (Edible Oil Processors)",
        "Town": "Kurnool",
        "Region": "Kallur Road (Near Apco Bhavan)",
        "Key Crops Demanded": "Groundnut Pods & Kernels (100+ MT monthly)",
        "Procurement Profile": "Historic and premier groundnut crushing and oil processing plant in the Kallur corridor.",
        "Address / Landmark": "Kallur Road, Kurnool - 518003",
        "Contact Channel": "Managing Director / Raw Seed Purchase Desk"
    },
    {
        "Category": "Edible Oil, Solvent Extraction & Cotton Giants",
        "Business Name": "Sri Laxmi Venkateswara Oil Mill",
        "Town": "Kurnool",
        "Region": "Kallur Industrial Estate",
        "Key Crops Demanded": "Groundnut Kernels, Cotton Seeds, Sunflower Seeds",
        "Procurement Profile": "Heavy-duty expeller mill in Kallur Industrial Estate processing oilseeds into bulk oil and oil cake.",
        "Address / Landmark": "Plot 27, Shed 1, Kallur Industrial Estate, Kurnool - 518003",
        "Contact Channel": "Factory Proprietor"
    },
    {
        "Category": "Edible Oil, Solvent Extraction & Cotton Giants",
        "Business Name": "Sri Guru Raghavendra Oil Mill",
        "Town": "Kurnool",
        "Region": "Bellary Road / Hanuman Kanta",
        "Key Crops Demanded": "Groundnut Pods, Cotton Seed, Kapas",
        "Procurement Profile": "Major processor on Bellary Road consuming steady farm-gate arrivals.",
        "Address / Landmark": "Near Hanuman Kanta, Bellary Road, Kurnool - 518001",
        "Contact Channel": "Plant Incharge"
    },
    {
        "Category": "Edible Oil, Solvent Extraction & Cotton Giants",
        "Business Name": "Sree Shiva Ginning and Pressing Factory",
        "Town": "Kurnool",
        "Region": "Kallur / Kurnool Outer",
        "Key Crops Demanded": "Raw Cotton (Kapas - 200+ quintals weekly during peak harvest)",
        "Procurement Profile": "Industrial cotton ginning and pressing mill separating raw Kapas into lint bales and cottonseed for oil mills.",
        "Address / Landmark": "Industrial Area, Kallur, Kurnool - 518003",
        "Contact Channel": "Managing Partner"
    },
    {
        "Category": "Edible Oil, Solvent Extraction & Cotton Giants",
        "Business Name": "Sree Bhavani Ginning & Pressing Factory",
        "Town": "Kurnool",
        "Region": "Nandyal Highway Corridor",
        "Key Crops Demanded": "Kapas (Raw Seed Cotton)",
        "Procurement Profile": "Modern ginning plant with automated bale presses and seed storage godowns.",
        "Address / Landmark": "Nandyal Road, Kurnool - 518004",
        "Contact Channel": "Procurement General Manager"
    },

    # =========================================================================
    # 7. PUFFED RICE (BORUGULU) & FRIED GRAM (PUTNALU) MEGA-BHATTIS
    # =========================================================================
    {
        "Category": "Puffed Rice & Fried Gram Mega-Bhattis",
        "Business Name": "SLN Borugula Batti & Puffed Rice Works",
        "Town": "Kurnool",
        "Region": "Nandyal Check Post / Kallur Belt",
        "Key Crops Demanded": "Paddy / Specialized Rice (1,000+ bags monthly)",
        "Procurement Profile": "Kurnool is world-famous for Borugulu. This industrial unit operates continuous roasting kilns supplying wholesale puffed rice across South India.",
        "Address / Landmark": "Near Nandyal Check Post, Kurnool - 518002",
        "Contact Channel": "Factory Proprietor"
    },
    {
        "Category": "Puffed Rice & Fried Gram Mega-Bhattis",
        "Business Name": "Kurnool Central Fried Gram (Putnalu) Dal Mills",
        "Town": "Kurnool",
        "Region": "Kallur Industrial Area",
        "Key Crops Demanded": "Bengal Gram (Chana / Senagalu - 200+ MT monthly)",
        "Procurement Profile": "Massive chickpea roastery splitting and roasting Bengal gram into premium Putnala Pappu for the Rayalaseema Uggani and snack export ecosystem.",
        "Address / Landmark": "Kallur Industrial Estate, Kurnool - 518003",
        "Contact Channel": "Bulk Purchase Desk"
    },

    # =========================================================================
    # 8. SUPERMARKETS & HYPERMARKETS IN KURNOOL
    # =========================================================================
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "DMart Flagship Hypermarket (Kalluru / Bellary Chowrasta)",
        "Town": "Kurnool",
        "Region": "Bellary Chowrasta, Kalluru",
        "Key Crops Demanded": "Rice (Packaged 10kg/25kg), Toor Dal, Groundnut Kernels, Millets, Cooking Oil",
        "Procurement Profile": "Avenue Supermarts flagship store with massive retail FMCG footfall; high turnover in dry food grains.",
        "Address / Landmark": "Near Bellary Chowrasta, SBI Nirmal Nagar, Kalluru, Kurnool - 518001",
        "Contact Channel": "Regional FMCG Purchase Manager / Store Manager"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "Reliance SMART Bazaar Flagship (C-Camp)",
        "Town": "Kurnool",
        "Region": "C-Camp / Station Road",
        "Key Crops Demanded": "Sona Masoori Rice, Toor Dal, Groundnut, Spices",
        "Procurement Profile": "Reliance Retail regional flagship supercenter with private label packaging demands.",
        "Address / Landmark": "C-Camp Main Road, Kurnool - 518002",
        "Contact Channel": "Staples Category Manager"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "More Supermarket (Gayatri Estate)",
        "Town": "Kurnool",
        "Region": "Gayatri Estate",
        "Key Crops Demanded": "Rice, Pulses, Palli, Millets",
        "Procurement Profile": "Premium neighborhood grocery supermarket chain with strong local demand.",
        "Address / Landmark": "Gayatri Estate, Kurnool - 518002",
        "Contact Channel": "Store Manager"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "Vishal Mega Mart (Bellary Road)",
        "Town": "Kurnool",
        "Region": "Bellary Road / Old Bus Stand",
        "Key Crops Demanded": "Rice, Pulses, Edible Oil",
        "Procurement Profile": "Value retail superstore selling high volumes of dry food staples in 10kg and 25kg bags.",
        "Address / Landmark": "Bellary Road, Kurnool - 518001",
        "Contact Channel": "Store General Manager"
    },
    {
        "Category": "Supermarkets & Hypermarkets",
        "Business Name": "Spencers Supermarket (C-Camp)",
        "Town": "Kurnool",
        "Region": "C-Camp",
        "Key Crops Demanded": "Rice (BPT 5204, RNR), Organic Dals, Millets",
        "Procurement Profile": "Reputed chain catering to middle and upper-middle class residential colonies.",
        "Address / Landmark": "Near Rythu Bazaar, C-Camp, Kurnool - 518002",
        "Contact Channel": "Branch Manager"
    },

    # =========================================================================
    # 9. APMC MANDI & WHOLESALE GRAIN MERCHANTS GUILD
    # =========================================================================
    {
        "Category": "Wholesale Mandi & Grain Merchants",
        "Business Name": "Kurnool APMC Market Yard & Grain Merchants Association",
        "Town": "Kurnool",
        "Region": "C-Camp / Bellary Road",
        "Key Crops Demanded": "Rice (All varieties), Kapas (Cotton), Bengal Gram, Groundnut, Maize",
        "Procurement Profile": "One of the highest-turnover agricultural commodity market yards in Andhra Pradesh; 100+ registered commission merchants and wholesale godowns buying full truckloads on spot cash.",
        "Address / Landmark": "Agriculture Market Yard, Bellary Road, Kurnool - 518003",
        "Contact Channel": "Secretary, APMC Kurnool / President, Grain Merchants Association"
    },

    # =========================================================================
    # 10. MEGA CONVENTION HALLS & CATERERS GUILD
    # =========================================================================
    {
        "Category": "Convention Halls & Catering Guilds",
        "Business Name": "Mourya Inn & Convention Centre",
        "Town": "Kurnool",
        "Region": "Bhagya Nagar",
        "Key Crops Demanded": "Premium Sona Masoori Rice, Toor Dal, Pure Groundnut Oil, Spices",
        "Procurement Profile": "Premier hospitality venue hosting massive weddings and conferences consuming quintals of rice and oil every weekend.",
        "Address / Landmark": "Bhagya Nagar, Kurnool - 518001",
        "Contact Channel": "General Manager / F&B Director"
    },
    {
        "Category": "Convention Halls & Catering Guilds",
        "Business Name": "Kurnool District Master Caterers & Kalyana Mandapams Guild",
        "Town": "Kurnool",
        "Region": "Old Town & C-Camp",
        "Key Crops Demanded": "Rice (BPT 5204), Toor Dal, Bengal Gram, Cooking Oil",
        "Procurement Profile": "Apex association of wedding caterers contracting bulk farm-direct staple supplies for 50+ marriage halls across Kurnool district.",
        "Address / Landmark": "C-Camp, Kurnool - 518002",
        "Contact Channel": "Association Secretary"
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
        for row in KURNOOL_HIGH_TICKET_BUYERS:
            writer.writerow(row)
            
    print(f"Successfully compiled {len(KURNOOL_HIGH_TICKET_BUYERS)} high-ticket Kurnool buyers into:")
    print(OUTPUT_FILE)

if __name__ == "__main__":
    main()
