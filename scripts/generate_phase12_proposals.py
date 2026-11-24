#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 12/13 (Agricultural EXIM & Merchant Exporters) Proposal Generator & Outbox Stager
Generates 3 benchmark commercial B2B outreach proposals:
1. ITC Agri Business Division (ABD) - Export Procurement Directorate (Guntur / Hyderabad)
2. Olam Agri India Private Limited - South SCM Desk (Bengaluru / Kakinada)
3. Pattabhi Agro Foods Private Limited (Star Export House) (Kakinada Port SEZ)
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
        "company_name": "ITC Agri Business Division (ABD) - Export Directorate",
        "recipient_title": "Executive Vice President & Head of Global Agricultural SCM",
        "to_email": "procurement.abd@itc.in",
        "subject": "Direct Farm-Gate Non-Basmati Rice, Red Chilies & Maize Origination for ITC Export Contracts",
        "crop_focus": "Certified 12-Month Aged Sona Masoori Rice (BPT 5204), Low-GI RNR 15048, Sun-Dried Whole Red Chilies (Teja & 334 Grades), Food-Grade Yellow Maize, Raw Cotton Bales",
        "body": """Dear Executive Vice President & Global SCM Leadership,

Namaskaram. As India's foremost agricultural export and processing conglomerate shipping hundreds of thousands of tonnes of identity-preserved agri-commodities across 60+ countries, ITC Agri Business Division (ABD) sets the benchmark for international food safety, sustainable sourcing, and farmer empowerment.

ONSFC Agri Solutions operates a dedicated 1-acre first-mile aggregation, pneumatic de-stoning, and optical color sorting hub at Gooty (Anantapuramu District)—the primary gateway connecting the Rayalaseema agricultural basin to the NH-44 expressway and port corridors. We aggregate directly from 5,000+ registered dryland farmers across 24 villages.

WHY SOURCING FROM ONSFC EMPOWERS ITC'S GLOBAL EXPORT SHIPMENTS:
1. Complete First-Mile Traceability: 100% origin-verified produce sourced from registered dryland farmers, supporting ITC's sustainable sourcing and ESG audit mandates.
2. Certified Single-Origin Sona Masoori (BPT 5204 & Low-GI RNR 15048): Laboratory verified <12.5% moisture,Sortex Grade-1 with <0.01% foreign matter, ready for containerized retail pack exports to the Middle East, UK, and North America.
3. Export-Quality Sun-Dried Red Chilies: Clean solar-bed dried Teja and 334 whole red chili pods (<10% moisture), free from banned chemical residues and high in natural capsaicin and ASTA color values for your Edlapadu Spice Park processing lines.
4. Food-Grade Yellow Maize & HPS Peanuts: Machine-cleaned, aflatoxin-controlled yellow corn and bold groundnut kernels for global food ingredient contracts.
5. Strategic Multimodal Freight Connectivity: Located on NH-44 and the Gooty-Guntakal rail freight corridor, offering rapid dispatch to Krishnapatnam Port (340 km), Chennai Port (380 km), Kakinada Port, and ICD Sanathnagar/Whitefield.
6. Significant Origin Cost Savings: Direct farm-gate aggregation bypasses multi-tier mandi cess and broker markups, delivering ₹1,800 to ₹2,500/MT procurement margin improvements.

We invite your South India commodity origination and quality inspection teams to inspect our Gooty hub, or we can dispatch a trial 10-tonne testing consignment of our Sortex Sona Masoori rice and sun-dried red chilies directly to your Guntur or Hyderabad export depot this week.

Sincerely,
Commercial EXIM Origination Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Olam Agri India Private Limited - South SCM Desk",
        "recipient_title": "Vice President & Head of Grain / Oilseeds Origination (South Asia)",
        "to_email": "grainprocurement.south@olamagri.com",
        "subject": "Direct Farm-Gate Non-Basmati Rice & HPS Groundnut Container Stuffing Supply for Olam Agri",
        "crop_focus": "Non-Basmati Parboiled & Raw Sona Masoori Rice, Broken Raw Rice (100% Sortex), Hand Picked Selected (HPS) Bold Groundnut Kernels, Raw Cotton Lint Bales",
        "body": """Dear Vice President & Regional Origination Directorate,

Namaskaram. Operating across 60+ countries with market leadership in non-basmati rice, edible oilseeds, and cotton trading, Olam Agri's high-velocity export programs through Kakinada and Chennai ports require uncompromising container readiness, tight moisture control, and reliable origin aggregation.

ONSFC Agri Solutions operates a 1-acre pre-cleaning, pneumatic grading, and moisture-controlled warehouse hub at Gooty on the NH-44 corridor, sourcing directly from 5,000+ dryland farmers across 24 villages.

WHY OLAM AGRI'S EXPORT TRADE PROFITS FROM ONSFC ORIGINATION:
1. Port-Ready Container Quality: All grains pass through dual-pass pneumatic de-stoners and Sortex optical color sorters, ensuring <0.01% impurities and <12.5% moisture for sea voyage stability.
2. High-Volume Broken Raw Rice (*Nookalu*): Cleaned, uniform broken raw rice with high starch density, ideal for your bulk container shipments to Southeast Asian food manufacturing importers.
3. HPS Groundnut Kernels (Bold & Java): Machine-graded, uniform count-per-ounce, strictly <8.5% moisture, solar-dried to eliminate aflatoxin risks for international confectionery and oilseed buyers.
4. Rayalaseema Long-Staple Cotton Bales: Farm-gathered Kapas ginned under standard moisture controls, delivering uniform 170 kg export lint bales.
5. Rapid Port Laycan Fulfillment: Direct overnight rail/road dispatch to Krishnapatnam Port, Chennai Port, and Kakinada Port container freight stations.
6. Institutional Vendor Compliance: Formal GST documentation, APEDA export quality certificates, E-Way bills, and prompt digital weighbridge receipts.

We welcome Olam's technical auditors to inspect our Gooty aggregation facilities, or we can stage a trial 2 x 20-ft container consignment (50 MT) of Sortex Sona Masoori rice and HPS groundnuts to your designated port CFS this week.

With respectful regards,
Commercial EXIM Origination Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Pattabhi Agro Foods Private Limited (Star Export House)",
        "recipient_title": "Managing Director & Chief Operating Officer (EXIM)",
        "to_email": "exports@pattabhiagro.com",
        "subject": "Direct Farm-Gate Certified Sona Masoori & Broken Rice Supply for Pattabhi Port Vessel Loading",
        "crop_focus": "Certified 12-Month Aged Sona Masoori Rice (BPT 5204), Parboiled Rice, Broken Raw Rice (100% Sortex for Export)",
        "body": """Dear Managing Director & Export Operations Directorate,

Namaskaram. As an APEDA 5-Star Export House and one of India's preeminent non-basmati rice exporters shipping over 300,000 MT annually through Kakinada Deep Water Port, Pattabhi Agro Foods commands global respect for scale, milling sophistication, and prompt vessel turnaround.

ONSFC Agri Solutions operates a dedicated 1-acre first-mile aggregation and pneumatic de-stoning hub at Gooty (Anantapuramu District), situated directly on the NH-44 highway and railway junction corridor, aggregating directly from 5,000+ dryland farmers across 24 villages.

WHY SOURCING FROM ONSFC EMPOWERS PATTABHI AGRO FOODS:
1. Certified Aged BPT 5204 Sona Masoori: Naturally aged 12 months, harvested from the fertile Pennar black-soil belt; laboratory tested <12.5% moisture with superior cooking elongation, highly prized in the Gulf and European ethnic markets.
2. Sortex Broken Raw Rice (*Nookalu*): Optical-sorted, 100% stone-free broken rice with high amylose starch, ideal for your high-tonnage Southeast Asian container export programs.
3. Dedicated Volume Allocation: Capacity to originate and dispatch 500 to 1,500 Metric Tonnes monthly on pre-scheduled rakes or multi-axle truck convoys directly to your Kakinada port warehousing complex.
4. Zero Stone & Dirt Rejection: Pneumatic gravity separators remove 100% of soil particles, protecting your automated port bagging lines from foreign matter stoppages.
5. Origin Price Arbitrage: Sourcing directly from Gooty mandal farmers saves ₹1,500 to ₹2,000 per MT compared to procuring through intermediate coastal brokers.
6. Seamless Export Documentation: Batch moisture analysis, digital weigh slips, full GST compliance, and E-Way bills for effortless export tax drawback processing.

We would be honored to stage a trial 50-tonne (2-truckload) consignment of our Sortex Sona Masoori rice directly to your Kakinada port reception bays this week.

Warm regards,
Commercial EXIM Origination Desk
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
        md_filename = f"ONSFC_Phase12_Proposal_{safe_name}.md"
        md_filepath = os.path.join(PROPOSALS_DIR, md_filename)
        
        with open(md_filepath, "w", encoding="utf-8") as f:
            f.write(f"# Commercial EXIM Proposal: {comp_name}\n")
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
        print(f"Staged EXIM Proposal for: {comp_name} -> {md_filename}")

    conn.commit()
    conn.close()
    print(f"\nSUCCESS: Generated and approved {staged_count} Phase 12/13 commercial EXIM proposals in Sellbird Outbox!")

if __name__ == "__main__":
    main()
