#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 14 (Sovereign, Divine & Heavy Industrial Mega-Off-Takers) Proposal Generator & Outbox Stager
Generates 3 benchmark commercial B2B outreach proposals:
1. Tirumala Tirupati Devasthanams (TTD) - Srivari Annaprasadam & Laddu Besan Directorate (Tirupati)
2. Srisailam Sri Bhramaramba Mallikarjuna Swamy Devasthanam (Lord Shiva Jyotirlinga) - Nitya Annadhanam Trust
3. JSW Steel Vijayanagar Works Central Canteen & Vidyanagar Township Cooperative (Toranagallu, Bellary)
"""

import os
import sqlite3
import uuid
import datetime

SELLBIRD_DB = r"C:\Users\rakes\.gemini\antigravity\scratch\sellbird\data\sellbird.db"
PROPOSALS_DIR = r"C:\Users\rakes\.gemini\antigravity\scratch\onsfc-agri-solutions\proposals"
os.makedirs(PROPOSALS_DIR, exist_ok=True)

COMMERCIAL_PROPOSALS = [
    {
        "company_name": "Tirumala Tirupati Devasthanams (TTD) - Srivari Annaprasadam & Laddu Production Hub",
        "recipient_title": "Executive Officer (EO) / General Manager (Procurement) & DyEO (Annaprasadam)",
        "to_email": "procurement@tirumala.org",
        "subject": "Direct Farm-Gate Pure Bengal Gram (Besan), Aged Sona Masoori & Sortex Dals for Srivari Annaprasadam & Laddus",
        "crop_focus": "Pure A-Grade Bengal Gram (Senagalu for super-fine Laddu Besan), Certified 12-Month Aged Sona Masoori Rice (BPT 5204), Unpolished Sortex Toor Dal, Pure Groundnut Oil",
        "body": """Om Namo Venkateshaya.
Respected Executive Officer & General Manager (Procurement) Directorate,

With profound devotion and humility, ONSFC Agri Solutions Private Limited offers this expression of interest to supply pure, single-origin agricultural commodities directly from 5,000+ dryland farmers of Gooty Mandal (Anantapuramu District) to Tirumala Tirupati Devasthanams.

As the sacred custodian of the world's most revered pilgrimage center feeding 100,000+ devotees daily at the Tarigonda Vengamamba Annaprasadam Complex and preparing hundreds of thousands of world-famous sacred Tirupati Laddus daily, TTD commands the highest standards of purity, zero adulteration, and unbroken supply security.

WHY ONSFC DIRECT FARM-GATE SUPPLY EMPOWERS TTD:
1. Pure Bengal Gram for Sacred Laddu Besan: Hand-sorted, machine-cleaned, chemical-free Bengal Gram (*Senagalu*) cultivated in the black soils of Rayalaseema, ideal for milling into the fragrant, golden Besan flour indispensable for Srivari Laddus.
2. Certified 12-Month Aged BPT 5204 Sona Masoori: Naturally seasoned rice sourced from Pennar riverbed farms; moisture <12.5%, cooking to immense fluffiness and high volume, feeding thousands of devotees per cauldron without stickiness.
3. Machine De-Stoned & Optical Color Sorted: Dual-pass pneumatic gravity separators remove 100% of stones and dirt pellets, eliminating manual cleaning and protecting TTD's automated steam cooking cauldrons.
4. Pure Unpolished Toor Dal (*Kandi Pappu*): Zero mineral oil, zero synthetic color additives; produces rich, wholesome, highly nutritious Sambar for daily Annaprasadam.
5. Direct Geographic Proximity (280 km via NH-716/NH-44): Scheduled truck convoys can deliver 50 to 100 Metric Tonnes within 6 hours from our Gooty hub directly to TTD Central Stores in Tirupati.
6. Absolute AP e-Procurement Compliance: Registered farmer-producer aggregation enterprise with full batch lab testing certificates, digital weighment slips, and statutory GST e-invoices.

We humbly request the opportunity to submit formal tender quotations and stage a trial 20-tonne consignment of our Sortex Sona Masoori rice and Bengal gram directly to TTD Central Stores this month.

Humbly submitted at the sacred feet of Lord Venkateswara,
Commercial & Institutional Supply Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Srisailam Sri Bhramaramba Mallikarjuna Swamy Devasthanam (Lord Shiva Jyotirlinga)",
        "recipient_title": "Executive Officer (EO) & In-Charge (Nitya Annadhanam Trust)",
        "to_email": "eo@srisailamtemple.com",
        "subject": "Direct Farm-Gate Certified Sona Masoori Rice & Sortex Dals for Srisailam Nitya Annadhanam Trust",
        "crop_focus": "Certified 12-Month Aged Sona Masoori Rice (BPT 5204), Sortex Unpolished Toor Dal, Roasted Bengal Gram (Putnalu), Native Millets (Ragi/Jowar), Pure Groundnut Cooking Oil",
        "body": """Om Namah Shivaya.
Respected Executive Officer & Sacred Nitya Annadhanam Directorate,

With deepest reverence to Lord Mallikarjuna Swamy and Goddess Bhramaramba Devi, ONSFC Agri Solutions Private Limited—an agricultural enterprise founded with the divine blessings of Lord Shiva to uplift 5,000+ dryland farming families across Gooty Mandal—presents our direct farm-gate supply partnership.

Located only 220 km from our Gooty hub in the neighboring Nandyal district, the sacred Jyotirlinga of Srisailam feeds tens of thousands of visiting pilgrims daily through the revered Nitya Annadhanam Scheme. Serving holy Annaprasadam to Shiva devotees requires staples of absolute purity, pristine cleanliness, and deep agricultural integrity.

WHY ONSFC DIRECT FARM-GATE SUPPLY EMPOWERS SRISAILAM ANNADHANAM:
1. Sacred Alignment & Agricultural Purity: Produced by devoted dryland farmers from the historic Gateway of Rayalaseema (Gooty), processed with sacred intention.
2. Machine De-Stoned & Sortex Graded: Guaranteed <0.01% impurities; completely stone-free and mud-free, ensuring every devotee receives pure, safe, delicious prasadam.
3. Certified Aged Sona Masoori Rice: Naturally seasoned for 12 months; high water absorption, cooking to separate, fragrant, digestible grains for mass Annadhanam.
4. Pure Unpolished Sortex Toor Dal: 100% natural golden split pulses without artificial yellow polish, delivering thick, aromatic Sambar and Pappu.
5. Native Millets (Ragi & Jowar): Nutrient-rich, traditional dryland grains for special fasting and health offerings.
6. Direct 4-Hour Truck Delivery: Scheduled weekly drops directly to the Srisailam Devasthanam Annadhanam storerooms atop the temple hill.

We humbly seek your blessings to empanel ONSFC on the temple's official supplier registry and dispatch a trial 10-tonne consignment of our aged Sona Masoori rice and Toor Dal directly to Srisailam this week.

Hara Hara Mahadeva Shambho Shankara!
Institutional Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "JSW Steel Vijayanagar Works Central Canteen & Vidyanagar Township Cooperative",
        "recipient_title": "Head of Administration & Township Services / Central Canteen Committee",
        "to_email": "procurement.canteen@jsw.in",
        "subject": "Direct Farm-Gate Aged Sona Masoori Rice, Sortex Pulses & Cooking Oil for JSW 35,000+ Workforce Canteens",
        "crop_focus": "Certified 12-Month Aged Sona Masoori Rice, Broken Rice (for Idli/Dosa breakfasts), Sortex Toor Dal, Bengal Gram, Pure Groundnut Cooking Oil",
        "body": """Dear Head of Administration & Township Services / Central Canteen Directorate,

Operating India's largest single-location steel plant with 35,000+ employees and residents living across Vidyanagar township, JSW Steel Vijayanagar Works runs one of the most massive 24/7 industrial feeding and consumer cooperative operations in the nation. Ensuring high-calorie, nutritious, stone-free meals for thousands of shift workers while controlling monthly catering overheads is a strategic priority.

ONSFC Agri Solutions operates a dedicated 1-acre first-mile aggregation, pneumatic cleaning, and grading hub at Gooty (Anantapuramu District)—located only 90 km from Toranagallu via the Guntakal-Bellary highway corridor! We aggregate directly from 5,000+ dryland farmers across 24 villages.

WHY SOURCING FROM ONSFC DIRECTLY ADVANTAGES JSW STEEL CANTEENS:
1. Neighboring Agro-Hub Advantage (Only 90 km Away): Trucks leave Gooty and arrive at Toranagallu within 90 minutes, eliminating long-haul freight costs and guaranteeing rapid replenishment.
2. Massive Industrial Volume Capacity: Dedicated capacity to supply 60 to 100 Metric Tonnes monthly of aged Sona Masoori rice and 20 MT of pulses on scheduled weekly dispatches.
3. 100% Stone-Free Pneumatic Grading: Dual-pass pneumatic gravity separators remove all mud and stones, protecting your commercial kitchen equipment and ensuring high worker dining satisfaction.
4. Broken Rice for Daily Shift Breakfasts: Sortex broken raw rice (*Nookalu*) with high starch yield, producing fluffy idlis and crisp dosas for morning shift counters.
5. 12% to 15% Cost Savings vs. Bellary Wholesale: Direct farm-gate procurement eliminates intermediate mandi brokers, lowering per-meal catering costs across your plant canteens.
6. Corporate Vendor Compliance: Formal GST e-invoices, E-Way bills, batch lab analysis certificates, and Net-30 institutional billing terms.

We invite your Township Administration and Canteen Committee to inspect our Gooty aggregation yard, or we can dispatch a trial 15-tonne consignment of our aged Sona Masoori rice and Toor Dal directly to your Toranagallu central stores this week.

Sincerely,
Commercial Industrial Origination Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    }
]

def main():
    conn = sqlite3.connect(SELLBIRD_DB)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS proposals (
        id TEXT PRIMARY KEY,
        prospect_id TEXT,
        company_id TEXT,
        subject TEXT,
        body TEXT,
        status TEXT DEFAULT 'draft',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    staged_count = 0

    for p in COMMERCIAL_PROPOSALS:
        comp_name = p["company_name"]
        
        cursor.execute("SELECT id FROM companies WHERE name = ?", (comp_name,))
        comp_row = cursor.fetchone()
        company_id = comp_row[0] if comp_row else f"comp_{uuid.uuid4().hex[:12]}"
        
        cursor.execute("SELECT id FROM prospects WHERE company = ?", (comp_name,))
        pros_row = cursor.fetchone()
        prospect_id = pros_row[0] if pros_row else f"pros_{uuid.uuid4().hex[:12]}"

        safe_name = "".join(c for c in comp_name if c.isalnum() or c in (" ", "_", "-")).strip().replace(" ", "_")
        md_filename = f"ONSFC_Phase14_Proposal_{safe_name}.md"
        md_filepath = os.path.join(PROPOSALS_DIR, md_filename)
        
        with open(md_filepath, "w", encoding="utf-8") as f:
            f.write(f"# Commercial Proposal: {comp_name}\n")
            f.write(f"**Recipient**: {p['recipient_title']}\n")
            f.write(f"**Target Commodities**: {p['crop_focus']}\n")
            f.write(f"**Email Subject**: {p['subject']}\n")
            f.write(f"**Date**: {now}\n\n---\n\n")
            f.write(p["body"])
        
        cursor.execute("SELECT id FROM proposals WHERE subject = ?", (p["subject"],))
        existing_prop = cursor.fetchone()
        
        if existing_prop:
            cursor.execute("""
            UPDATE proposals 
            SET body = ?, status = 'approved', updated_at = ?
            WHERE id = ?
            """, (p["body"], now, existing_prop[0]))
        else:
            prop_id = f"prop_{uuid.uuid4().hex[:12]}"
            cursor.execute("""
            INSERT INTO proposals (id, prospect_id, company_id, subject, body, status, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, 'approved', ?, ?)
            """, (prop_id, prospect_id, company_id, p["subject"], p["body"], now, now))
            
        staged_count += 1
        print(f"Staged Phase 14 Proposal for: {comp_name} -> {md_filename}")

    conn.commit()
    conn.close()
    print(f"\nSUCCESS: Generated and approved {staged_count} Phase 14 commercial proposals in Sellbird Outbox!")

if __name__ == "__main__":
    main()
