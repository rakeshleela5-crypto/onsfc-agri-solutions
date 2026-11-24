#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 15 (Conventions, Prisons, Ethanol & SEZ Cities) Proposal Generator & Outbox Stager
Generates 3 benchmark commercial B2B outreach proposals:
1. Palace Grounds Central Wedding & Convention Enclaves (Bengaluru) - Royal Wedding & Banquet Catering
2. Parappana Agrahara Central Prison Central Stores (Bengaluru) - Karnataka State Prison Department Rations
3. SPY Agro Industries Limited - Grain Distillery & Bio-Ethanol Division (Nandyal - 80 km from Gooty!)
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
        "company_name": "Palace Grounds Central Wedding & Convention Enclaves (Gayatri Vihar & Tripuravasini)",
        "recipient_title": "Director of Banquets / Master Catering Operations Lead",
        "to_email": "events@palacegroundsbangalore.com",
        "subject": "Direct Farm-Gate Aged Sona Masoori, Sortex Toor Dal & Besan for Palace Grounds Royal Banquets",
        "crop_focus": "Certified 12-Month Aged Sona Masoori Rice (BPT 5204), Broken Raw Rice (Batter Grade), Sortex Toor Dal, Bengal Gram (Besan for Live Counters), Pure Groundnut Oil",
        "body": """Dear Director of Banquets & Master Catering Directorate,

Namaskara. As India's most prestigious royal destination wedding and mega-convention enclave, Palace Grounds hosts royal receptions, high-profile corporate galas, and national expos where feeding 5,000 to 10,000 guests in a single evening is routine. Flawless grain presentation, separate fluffy rice grains in giant cauldrons, and zero culinary variance are non-negotiable standards.

ONSFC Agri Solutions operates a dedicated 1-acre first-mile aggregation, pneumatic de-stoning, and optical color sorting hub at Gooty (Anantapuramu District)—directly along the NH-44 expressway corridor. We aggregate non-perishable staples directly from 5,000+ dryland farmers across 24 villages.

WHY SOURCING FROM ONSFC ELEVATES PALACE GROUNDS WEDDING BANQUETS:
1. Certified 12-Month Aged Sona Masoori Rice: Sourced from Pennar riverbed black-soil farms; laboratory tested <12.5% moisture with unmatched water absorption and elongation—ensuring massive, non-sticky volume for royal buffet dining.
2. Sortex Broken Raw Rice (*Nookalu*): Machine-destoned broken rice with high amylose starch for crispy breakfast dosas and soft idlis for morning muhurtham tiffins.
3. Pure Unpolished Toor Dal (*Togari Bele*): 100% natural, free from mineral oil or artificial color; delivers thick, aromatic Mysore Sambar and Rasam.
4. Bengal Gram (*Senagalu & Besan*): Finely graded pulses and freshly milled Besan for evening live snack counters (bajjis, pakodas, boondi).
5. Direct 4-Hour Overnight Express Transit: Dispatched from Gooty at 11:00 PM along NH-44, arriving directly at Palace Grounds receiving docks by 3:30 AM before early morning banquet cooking begins.
6. 15% Cost Savings vs. Wholesale Agents: Eliminates intermediary broker commissions across the Yeshwanthpur APMC market.

We would be honored to supply a trial 5-tonne consignment of our aged Sona Masoori rice and Sortex Toor Dal directly to your central banquet stores ahead of this upcoming wedding season.

Sincerely,
Commercial Events & Banquets Origination Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Parappana Agrahara Central Prison & Correctional Administration Central Stores",
        "recipient_title": "Chief Superintendent of Prisons & Central Stores Ration Committee",
        "to_email": "prison-central@karnataka.gov.in",
        "subject": "Direct Farm-Gate Certified Non-Basmati Rice, Sortex Pulses & Native Ragi for Central Prison Inmate Rations",
        "crop_focus": "Government Specification Non-Basmati Milled Rice, Sortex Toor Dal, Whole Bengal Gram (Senagalu), Native Karnataka Ragi, Edible Cooking Oil",
        "body": """Dear Chief Superintendent & Central Stores Ration Committee,

Managing India's largest central prison complex housing over 5,000 inmates requires strict adherence to statutory dietary guidelines, zero-contamination food security, and rigorous cost efficiency. Providing three wholesome, balanced meals daily across multiple kitchen blocks demands raw ingredients of verified purity and high nutritional yield.

ONSFC Agri Solutions operates a 1-acre pre-cleaning, pneumatic de-stoning, and grading facility at Gooty on the NH-44 expressway corridor, aggregating directly from 5,000+ dryland farmers across 24 villages.

WHY SOURCING FROM ONSFC EMPOWERS PRISON ADMINISTRATION:
1. Guaranteed 100% Stone-Free Purity: Dual-pass pneumatic gravity separators remove all mud pellets, stones, and foreign matter (<0.01% impurities), completely protecting mechanized steam kitchens from blockages and ensuring inmate meal safety.
2. Certified Native Karnataka Ragi (*Finger Millet*): Clean, stone-free native Ragi specially calibrated for making smooth, lump-free daily Ragi Mudde (*ರಾಗಿ ಮುದ್ದೆ*) for the mandatory prison diet.
3. High-Expansion Sona Masoori Rice: Naturally seasoned for 12 months; high starch resilience, ensuring high yield per bag without becoming mushy.
4. Sortex-Graded Unpolished Toor Dal & Bengal Gram: Completely free from weevils and dirt, ready for immediate morning boiling.
5. Direct 4-Hour Highway Delivery: Inbound trucks enter South Bengaluru via the NICE Road directly into Electronic City / Parappana Agrahara by 4:00 AM.
6. Full Government Tender Compliance: Batch lab test reports, formal GST e-invoices, digital weighbridge receipts, and compliance with Karnataka Transparency in Public Procurements (KTPP) norms.

We would welcome the opportunity to submit our credentials for upcoming state prison ration tenders and deliver a trial 10-tonne testing load of our Sortex Sona Masoori rice and native Ragi directly to your central ration depot this month.

With highest regards,
Institutional Government Supplies Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "SPY Agro Industries Limited - Grain-Based Distillery & Ethanol Plant",
        "recipient_title": "Commercial Vice President & Head of Grain Origination",
        "to_email": "rawmaterials@spyagro.com",
        "subject": "Direct Farm-Gate Broken Raw Rice & Yellow Maize Bulk Supply for SPY Agro Bio-Ethanol Distilleries",
        "crop_focus": "Broken Raw Rice (100% Nookalu / Industrial Starch Grade), Damaged Food Grains, Yellow Maize (Corn)",
        "body": """Dear Commercial Vice President & Head of Grain Origination,

As one of South India's preeminent grain-based distilleries and biofuel ethanol manufacturers located right in our neighboring Nandyal district (only 80 km from Gooty!), SPY Agro Industries plays a crucial role in India's National Biofuel Blending Programme. Operating continuous grain fermentation columns consuming hundreds of tonnes of starch-rich feedstock daily requires uninterrupted raw material flow and strict moisture control.

ONSFC Agri Solutions operates a dedicated 1-acre first-mile aggregation and pneumatic de-stoning yard at Gooty (Anantapuramu District), aggregating directly from 5,000+ dryland farmers across 24 villages.

WHY SOURCING FROM ONSFC ADVANTAGES SPY AGRO'S ETHANOL PRODUCTION:
1. Neighboring Plant Proximity (Only 80 km Away): Delivery trucks travel from Gooty to Nandyal within 90 minutes via NH-40/NH-67, ensuring rapid turnaround and minimal logistics freight.
2. High Starch Density Broken Rice (*Nookalu*): 100% broken raw rice with high amylose starch content, maximizing alcohol yield per metric tonne fermented.
3. Moisture Guaranteed (<13%): Solar-bed dried and laboratory verified, preventing clumping and fungal spoilage in storage hoppers.
4. Yellow Corn (Feed Maize): Mechanically graded, uniform coarse corn grain ready for immediate milling and slurry preparation.
5. Large-Scale Dispatch Capacity: Ability to supply 500 to 1,500 Metric Tonnes monthly in multi-axle tipper trailers directly to your plant intake bays on spot payment or Net-7 terms.
6. Local Economic Integration: Directly connects Rayalaseema dryland farmers with Rayalaseema's leading agro-energy manufacturing plant.

We invite your grain procurement team to inspect sample consignments, or we can dispatch an initial 50-tonne (2-truckload) testing consignment of our broken raw rice directly to your Nandyal distillery hoppers this week.

Sincerely,
Commercial Agro-Industrial Origination Desk
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
        md_filename = f"ONSFC_Phase15_Proposal_{safe_name}.md"
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
        print(f"Staged Phase 15 Proposal for: {comp_name} -> {md_filename}")

    conn.commit()
    conn.close()
    print(f"\nSUCCESS: Generated and approved {staged_count} Phase 15 commercial proposals in Sellbird Outbox!")

if __name__ == "__main__":
    main()
