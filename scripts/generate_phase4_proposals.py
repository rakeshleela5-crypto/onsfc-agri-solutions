#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 4 (Bengaluru Contractual Buyers) Proposal Generator & Sellbird Outbox Stager
Generates 3 benchmark institutional B2B outreach proposals:
1. Narayana Health City Central Dietary Kitchen (Healthcare in-patient clinical supply)
2. Rebel Foods Central Production Facility (Cloud kitchen network supply)
3. iD Fresh Food (India) Mega Manufacturing Plant (RTC batter wet-grinding grain supply)
"""

import os
import sqlite3
import uuid
import datetime

SELLBIRD_DB = r"C:\Users\rakes\.gemini\antigravity\scratch\sellbird\data\sellbird.db"
PROPOSALS_DIR = r"C:\Users\rakes\.gemini\antigravity\scratch\onsfc-agri-solutions\proposals"
os.makedirs(PROPOSALS_DIR, exist_ok=True)

CONTRACT_PROPOSALS = [
    {
        "company_name": "Narayana Health City Central Dietary Kitchen",
        "recipient_title": "Head of Dietetics & Clinical Nutrition / General Manager SCM",
        "to_email": "dietetics@narayanahealth.org",
        "subject": "Direct Farm-Gate Diabetic Sugar-Free Rice (RNR 15048) & Unpolished Dals for Narayana Health City In-Patient Kitchens",
        "crop_focus": "Diabetic Sugar-Free Rice (RNR 15048), Aged Sona Masoori Rice, Unpolished Moong & Toor Dal, Karnataka Ragi, Cold-Pressed Groundnut Oil",
        "body": """Dear Head of Clinical Nutrition & SCM Directorate,

Namaskara. With the divine blessings of Lord Shiva, we present this institutional healthcare supply presentation from ONSFC Agri Solutions Private Limited.

Providing clinical, therapeutic, and post-operative dietary meals to 2,000+ in-patients daily across Narayana Health City (including Mazumdar Shaw Medical Centre and Narayana Institute of Cardiac Sciences) requires ingredients that meet strict pharmacological and metabolic purity standards. High glycemic index rice, chemically polished pulses, or pesticide residues directly counteract medical therapy.

ONSFC aggregates non-perishable dry staples directly from 5,000+ dryland farmers across 24 villages of Gooty Mandal (Rayalaseema), operating a dedicated 1-acre pre-cleaning, pneumatic de-stoning, and certified grading hub along the NH-44 corridor.

OUR CLINICAL DIETARY SPECIFICATIONS FOR NARAYANA HEALTH CITY:
1. Certified Low-GI Sugar-Free Rice (RNR 15048): Low glycemic index (GI < 55) table rice, clinically optimal for diabetic, bariatric, and cardiac in-patient diets.
2. Naturally Aged Sona Masoori (BPT 5204 Old Crop): Aged >12 months, light, non-sticky, easily digestible for post-surgical recuperation.
3. 100% Unpolished Therapeutic Dals (Moong & Toor): High natural bioavailability protein, zero synthetic coloring, zero mineral wax, and zero chemical polishing agents.
4. Cold-Filtered Groundnut Cooking Oil: Heart-healthy cooking oil directly pressed from selected bold groundnut pods; zero trans-fat, zero palm oil blending.
5. Absolute Foreign Matter Purity (<0.01%): Dual pneumatic air-density de-stoners and rare-earth magnetic separation guarantee zero stones or grit.
6. Direct Overnight Transit via NH-44: 290 km direct highway transit (4.5 hrs). Dispatched from Gooty at 11:00 PM, arriving at your Bommasandra loading docks by 4:30 AM before morning meal preparation.

We propose establishing an Annual Rate Contract (ARC) or Vendor Empanelment agreement, and we invite your clinical nutrition committee to test a complimentary 25 kg evaluation consignment of our RNR 15048 Diabetic Rice and Unpolished Toor Dal.

Respectfully yours,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Expressway Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Rebel Foods Central Production Facility (Behrouz & Faasos)",
        "recipient_title": "Head of Global SCM & Commodity Sourcing",
        "to_email": "procurement@rebelfoods.com",
        "subject": "Direct Farm-Gate Aged Sona Masoori Rice & Whole Sun-Dried Red Chilies for Rebel Foods Central Commissary",
        "crop_focus": "Aged Sona Masoori Rice (BPT 5204), Biryani Raw Rice, Sun-Dried Red Chilies, Toor Dal, Pure Groundnut Oil",
        "body": """Dear Head of Commodity Sourcing & Supply Chain,

Scaling operations across 40+ cloud kitchen pods in Bengaluru serving Behrouz Biryani, Faasos, and LunchBox requires uncompromising batch consistency. A fluctuation in rice elongation or chili capsaicin potency disrupts standardized kitchen combi-oven recipes and inflates food costs.

ONSFC Agri Solutions operates a 1-acre first-mile aggregation yard at Gooty on the NH-44 expressway corridor, directly linking 5,000+ dryland farmers to enterprise food brands.

WHY REBEL FOODS SOURCING THROUGH ONSFC DELIVERS UNFAIR ADVANTAGES:
1. Certified Aged Sona Masoori Rice (BPT 5204): Minimum 12-month natural aging guarantee, delivering superior volumetric grain expansion and non-sticky separation essential for authentic dum biryanis.
2. Single-Origin Sun-Dried Red Chilies: Pure Rayalaseema sun-dried red chilies providing intense natural color and pungent flavor without artificial food coloring additives.
3. Machine De-Stoned & Sortex Graded: Zero foreign matter, certified moisture strictly below 8.5% in sealed tamper-evident 50kg bags.
4. 15% to 20% Direct Cost Arbitrage vs Local Wholesale APMC Mandis: Sourcing at the village farm-gate eliminates 3 layers of intermediate commission agents.
5. High-Turnover Logistics: Direct night-haul dispatches up NH-44 straight to your Kudlu Gate / Electronic City central commissary loading bays by 4:30 AM.
6. Corporate Master Service Agreement (MSA): Scheduled weekly deliveries with Net-30 payment credit cycles and formal GST documentation.

We welcome your quality assurance team to audit our Gooty processing hub or request a trial 1-tonne pilot consignment to your Bengaluru commissary.

Best regards,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "iD Fresh Food (India) Pvt Ltd Mega Manufacturing Plant",
        "recipient_title": "Chief Procurement Officer / VP Supply Chain",
        "to_email": "procurement@idfreshfood.com",
        "subject": "Bulk Farm-Gate High-Starch Broken Rice & Sortexed Urad Dal for iD Fresh Hosakote Mega Plant",
        "crop_focus": "High-Starch Broken Rice (Idli/Dosa Grade), Unpolished Urad Dal (Minapappu), Organic Grains",
        "body": """Dear Chief Procurement Officer & VP of Supply Chain,

Manufacturing 100,000+ kg of fresh, preservative-free Idli and Dosa batter daily at your flagship Hosakote mega-factory demands raw commodities of extraordinary starch integrity and dependable multi-truckload volume.

ONSFC Agri Solutions Private Limited operates a 1-acre first-mile aggregation and pneumatic grading yard at Gooty on the NH-44 expressway corridor. We aggregate non-perishable paddy, broken rice, and pulses directly from 5,000+ registered dryland farmers across 24 villages.

WHY SOURCING GRAINS FROM ONSFC ELEVATES ID FRESH FOOD MANUFACTURING:
1. High-Starch Sortex Broken Rice (Nookalu): Specially screened and graded for wet-grinding lines; guarantees optimal starch release for 100% natural, active batter fermentation without baking soda or chemical boosters.
2. Unpolished Farm-Gate Urad Dal (Black Gram / Minapappu): High mucilage content and natural protein density, delivering signature batter aeration, softness, and rise.
3. Multi-Axle Industrial Capacity: Capability to deliver 50 to 100 Metric Tonnes per weekly schedule on 10-wheel and multi-axle freight carriers directly to your Hosakote unloading hoppers.
4. Strict Moisture Assurance (<8.5%): Protects against bacterial spoilage and starch degradation in your grain silo storage.
5. Guaranteed 8-12% Cost Savings vs Mandi Wholesalers: Sourced directly at the farm-gate with digital weighbridge certificates.
6. Long-Term Master Supply Agreement: Flexible institutional billing, formal GST invoicing, and fixed quarterly price collars.

We would be delighted to dispatch a trial 10-tonne testing consignment of our Sortex Broken Rice and unpolished Urad Dal directly to your Hosakote plant for laboratory and grinding tests.

Sincerely,
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
    
    for item in CONTRACT_PROPOSALS:
        comp_name = item["company_name"]
        subject = item["subject"]
        body = item["body"]
        to_email = item["to_email"]
        
        # Save as Markdown artifact file
        slug = "".join(c for c in comp_name[:15] if c.isalnum()).lower()
        md_path = os.path.join(PROPOSALS_DIR, f"proposal_{slug}.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# B2B Contractual Proposal: {comp_name}\n\n**Subject:** {subject}\n\n**To:** {to_email}\n\n---\n\n{body}\n")
            
        print(f"Generated Phase 4 Proposal document: {md_path}")
        
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
            """, (outbox_id, "camp_onsfc_phase4_contracts", prospect_id, to_email, subject, body, "pending_review", now, now, now))
            staged_count += 1
            
    conn.commit()
    conn.close()
    print(f"\nSUCCESS: Staged {staged_count} Phase 4 benchmark proposals into Sellbird outbox!")

if __name__ == "__main__":
    main()
