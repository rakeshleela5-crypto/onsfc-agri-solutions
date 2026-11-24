#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 6 (Bengaluru Supermarkets & Food Manufacturing) Proposal Generator & Sellbird Outbox Stager
Generates 3 benchmark commercial B2B outreach proposals:
1. More Retail Central Distribution Centre (Nelamangala) - Modern Trade FMCG staples & private-label supply
2. Kanti Sweets Central Mega Manufacturing Factory (Yeshwanthpur) - Pure Besan-grade Bengal Gram & sorted bold groundnut supply
3. Namdhari's Fresh & Simpli Namdhari's Central Procurement Hub (Bidadi) - Clean-label, single-origin low-GI rice, organic dals & cold-pressed oil
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
        "company_name": "More Retail Central Distribution Centre (More Supermarket & Hypermarket)",
        "recipient_title": "Category Head - Staples & Agri Commodities",
        "to_email": "sourcing.staples@moreretail.in",
        "subject": "Direct Farm-Gate Sona Masoori Rice & Sortexed Pulses Supply for More Retail Karnataka Central DC",
        "crop_focus": "Aged Sona Masoori Rice (BPT 5204), Low-GI RNR 15048 Rice, Unpolished Toor Dal, Urad Dal, Karnataka Ragi, Groundnut Kernels",
        "body": """Dear Category Head - Staples & Agri Commodities,

Namaskara. Sourcing high-velocity agricultural staples for 100+ More Supermarkets across Karnataka demands guaranteed volume predictability, low transit shrinkage, and competitive farm-gate pricing that improves retail category margins.

ONSFC Agri Solutions operates a 1-acre first-mile aggregation yard and certified pre-cleaning facility at Gooty on the NH-44 expressway corridor. We aggregate non-perishable paddy, pulses, and oilseeds directly from 5,000+ registered dryland farmers across 24 villages.

WHY SOURCING STAPLES THROUGH ONSFC EMPOWERS MORE RETAIL:
1. Certified Machine De-Stoned & Sortex Graded: Guaranteed <0.01% impurities with pneumatic air-density cleaning and optical color sorting.
2. Ready for Private-Label Packaging: Sona Masoori Rice (BPT 5204) and unpolished Toor Dal pre-cleaned and packed in 5kg, 10kg, and 25kg tamper-evident branded sacks.
3. 12% to 15% Cost Savings vs APMC Yeshwanthpur Mandi Brokers: Direct farm-gate intake bypasses intermediate commission agents and mandi cess.
4. Direct Highway Night-Hauls: Located on NH-44, our dedicated freight carriers reach your Nelamangala Mother DC in 4.5 hours overnight, docking at 4:30 AM before morning warehouse sorting shifts.
5. Strict Moisture Standard (<8.5%): Protects against insect infestation and weight loss during regional warehouse storage.
6. Corporate Annual Rate Contract (ARC): Transparent quarterly price indexing against mandi benchmarks, backed by GST invoices and digital weighbridge slips.

We would be delighted to dispatch a trial 10-tonne testing consignment of our Sortex Sona Masoori Rice and unpolished Toor Dal directly to your Nelamangala DC for quality and packaging evaluation.

Sincerely,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Expressway Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Kanti Sweets Central Mega Manufacturing Factory",
        "recipient_title": "Managing Director / Raw Materials Procurement Desk",
        "to_email": "info@kantisweets.com",
        "subject": "Pure Besan-Grade Bengal Gram & Bold Groundnut Kernels Supply for Kanti Sweets Yeshwanthpur Plant",
        "crop_focus": "Bengal Gram (Senagalu / Chana for Besan), Sorted Bold Groundnut Kernels (Peanuts), Raw White Rice Flour Grains, Urad Dal",
        "body": """Dear Managing Director & Central Procurement Directorate,

Namaskara. Producing traditional royal sweets and savories across Kanti Sweets' 90+ retail boutiques requires raw ingredients of extraordinary purity. The golden hue, aroma, and melt-in-mouth texture of signature Mysore Pak, Boondi Laddus, and savories depend fundamentally on the protein density and starch purity of the Bengal Gram milled for Besan.

ONSFC Agri Solutions aggregates dry pulses and oilseeds directly from 5,000+ dryland farmers across Gooty Mandal (Rayalaseema), operating a dedicated 1-acre grading and pneumatic cleaning hub along the NH-44 corridor.

WHY KANTI SWEETS BENEFITS FROM ONSFC DIRECT FARM-GATE SOURCING:
1. Pure Sortex Bengal Gram (Senagalu / Chana): Bold, sound kernels specially calibrated for in-house fresh Besan milling; delivers superior golden color and rich nutty aroma without blending or adulteration.
2. Uniform Bold Groundnut Kernels (Peanuts / Palli): Cleaned, destoned, calibrated to uniform count-per-ounce, strictly <8.5% moisture for peanut chikki, roasted spiced peanuts, and mixture lines.
3. High-Turnover Volume Reliability: Capacity to supply 50+ Metric Tonnes of Bengal Gram and 25+ MT of Groundnuts monthly on scheduled weekly dispatches.
4. Zero Foreign Matter Guarantee: Pneumatic de-stoning ensures zero mud pellets or stones enter your manufacturing mills.
5. Direct 4.5-Hour Transit to Yeshwanthpur: Direct night-haul via NH-44 reaches your Industrial Suburb plant by 4:30 AM before morning production shifts.
6. Multi-Year Sourcing Master Agreement: Flexible Net-30 payment credit backed by formal GST invoices and electronic weighbridge certificates.

We welcome your production and quality teams to inspect our incoming grain arrivals at our Gooty hub, or we can dispatch a trial 2-tonne consignment of sorted Bengal Gram and bold groundnuts to your Yeshwanthpur plant this week.

Warm regards,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Namdhari's Fresh & Simpli Namdhari's Central Procurement Hub",
        "recipient_title": "Chief Procurement Officer - Grains & Organics",
        "to_email": "procurement@namdharifresh.com",
        "subject": "Single-Origin Farm-Gate Sona Masoori & Organic Pulses for Simpli Namdhari's Retail Network",
        "crop_focus": "Single-Origin Sona Masoori Rice, Low-GI Diabetic Rice (RNR 15048), Organic Toor Dal, Foxtail Millet, Cold-Pressed Groundnut Oil",
        "body": """Dear Chief Procurement Officer & SCM Team,

Namaskara. Simpli Namdhari's pioneering leadership in providing single-origin, clean-label, and chemical-free food to affluent Bangalore households aligns perfectly with ONSFC Agri Solutions' first-mile farmer procurement model.

ONSFC aggregates non-perishable food grains directly from 5,000+ dryland farmers across 24 villages of Gooty Mandal. We operate a certified 1-acre pre-cleaning, pneumatic de-stoning, and grading hub along the NH-44 corridor.

OUR CLEAN-LABEL PROMISE FOR SIMPLI NAMDHARI'S STORES:
1. Single-Origin Farm-Gate Traceability: Every 25kg bag is traceable directly to registered dryland farmer clusters in Gooty Mandal.
2. Certified Low-GI Sugar-Free Rice (RNR 15048): Diabetic-friendly table rice with low glycemic index (GI < 55), perfectly suited for your health-conscious retail clientele.
3. 100% Unpolished Chemical-Free Pulses: High-protein Toor Dal and Moong Dal, completely free from artificial dyes, paraffin wax, or chemical polishing.
4. Cold-Pressed Pure Groundnut Oil: Wood-pressed aromatic oil extracted from selected bold peanut harvests; zero trans-fats, zero blending.
5. Purity Guarantee (<0.01% Impurities): Machine pneumatic de-stoning ensures zero customer complaints regarding stones or grit.
6. Direct Overnight Logistics: 290 km direct highway transit via NH-44 straight to your Bidadi Central Hub by 4:30 AM.

We would be honored to courier a complimentary testing hamper of our single-origin RNR 15048 Rice, unpolished Toor Dal, and cold-pressed oil for your quality assurance panel.

Respectfully yours,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Expressway Corridor), AP
Contact: procurement@onsfcagri.com"""
    }
]

def main():
    conn = sqlite3.connect(SELLBIRD_DB)
    cursor = conn.cursor()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    staged_count = 0
    
    for item in COMMERCIAL_PROPOSALS:
        comp_name = item["company_name"]
        subject = item["subject"]
        body = item["body"]
        to_email = item["to_email"]
        
        # Save as Markdown artifact file
        slug = "".join(c for c in comp_name[:15] if c.isalnum()).lower()
        md_path = os.path.join(PROPOSALS_DIR, f"proposal_{slug}.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# B2B Commercial Proposal: {comp_name}\n\n**Subject:** {subject}\n\n**To:** {to_email}\n\n---\n\n{body}\n")
            
        print(f"Generated Phase 6 Proposal document: {md_path}")
        
        # Match prospect in Sellbird SQLite DB
        cursor.execute("SELECT id FROM prospects WHERE company LIKE ?", (f"%{comp_name[:20]}%",))
        pros_row = cursor.fetchone()
        prospect_id = pros_row[0] if pros_row else f"pros_{uuid.uuid4().hex[:12]}"
        
        # Check if already staged in outbox
        cursor.execute("SELECT id FROM outbox WHERE to_email = ? AND subject = ?", (to_email, subject))
        existing_outbox = cursor.fetchone()
        
        if not existing_outbox:
            outbox_id = f"out_{uuid.uuid4().hex[:12]}"
            cursor.execute("""
            INSERT INTO outbox (id, campaign_id, prospect_id, to_email, subject, body, status, send_at, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (outbox_id, "camp_onsfc_phase6_bengaluru", prospect_id, to_email, subject, body, "pending_review", now, now, now))
            staged_count += 1
            
    conn.commit()
    conn.close()
    print(f"\nSUCCESS: Staged {staged_count} Phase 6 benchmark proposals into Sellbird outbox!")

if __name__ == "__main__":
    main()
