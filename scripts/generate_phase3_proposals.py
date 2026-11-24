#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 3 (Bengaluru Educational Institutions) Proposal Generator & Sellbird Outbox Stager
Generates 3 benchmark institutional B2B outreach proposals:
1. PES University Central Hospitality & Food Services (RR & EC Campuses - 7,000+ Hostellers)
2. Jain International Residential School (JIRS - Kanakapura Road - 1,100+ Boarders)
3. REVA University Mega Campus Hostels (Yelahanka / NH-44 - 5,200+ Hostellers)
"""

import os
import sqlite3
import uuid
import datetime

SELLBIRD_DB = r"C:\Users\rakes\.gemini\antigravity\scratch\sellbird\data\sellbird.db"
PROPOSALS_DIR = r"C:\Users\rakes\.gemini\antigravity\scratch\onsfc-agri-solutions\proposals"
os.makedirs(PROPOSALS_DIR, exist_ok=True)

INSTITUTIONAL_PROPOSALS = [
    {
        "company_name": "PES University - Ring Road Campus Hostels",
        "recipient_title": "Director of Hospitality & Food Services / Chief Warden",
        "to_email": "hostel@pes.edu",
        "subject": "5:00 AM Farm-Direct Sona Masoori Rice & Unpolished Toor Dal Dispatches for PES University Hostels",
        "crop_focus": "Aged Sona Masoori Rice (BPT 5204), Broken Idli Rice, Unpolished Toor Dal, Karnataka Ragi, Pure Cooking Oil",
        "body": """Dear Director of Hospitality & Central Mess Committee,

Namaskara. With the divine blessings of Lord Shiva, we present this institutional supply presentation from ONSFC Agri Solutions Private Limited.

Catering 4 meals daily to 7,000+ resident engineering and management students across PES University's Ring Road and Electronic City campuses is a massive operational feat. Student academic energy demands easily digestible, non-sticky rice, unadulterated protein-rich dals, and zero stones or foreign matter in morning tiffins.

ONSFC Agri Solutions operates a 1-acre first-mile aggregation yard and certified pre-cleaning facility at Gooty on the NH-44 corridor, directly linking 5,000+ dryland farmers across 24 villages to institutional buyers.

WHY SOURCING DRY STAPLES VIA ONSFC EMPOWERS PES UNIVERSITY MESSES:
1. Guaranteed 5:00 AM Delivery: Our direct night-haul departs Gooty at 11:00 PM via NH-44, arriving at your campus loading bay by 4:30 AM before morning chef shifts.
2. 100% Machine De-Stoned & Sortex Graded: Zero stones, zero mud pebbles, and pneumatic air-suction cleaning guarantee zero student foreign-body complaints.
3. Natural Old Crop Sona Masoori (BPT 5204): Aged over 12 months for maximum volumetric yield per kilogram, ensuring lower cost per meal served.
4. Karnataka Ragi & Unpolished Dals: Pure farm-grade Finger Millet for authentic Ragi Mudde and chemical-free Toor Dal (*Kandi Pappu*) with high protein retention.
5. 15% to 20% Direct Cost Savings vs Local APMC Yeshwanthpur Traders: Eliminating commission agents and mandi surcharges.
6. Flexible Institutional Credit: Net-30 billing backed by GST invoices and certified weighbridge slips.

We would be delighted to courier a complimentary 25 kg testing sack of our aged Sona Masoori Rice and Toor Dal for your culinary team to inspect and cook.

Warm regards,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Expressway Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Jain International Residential School (JIRS)",
        "recipient_title": "Director of Campus Living & Food Services",
        "to_email": "catering@jirs.ac.in",
        "subject": "Certified Stone-Free Single-Origin Grains & Cold-Pressed Groundnut Oil for JIRS Residential Students",
        "crop_focus": "Certified Sortex Sona Masoori Rice, Organic Toor Dal, Broken Rice, Cold-Pressed Groundnut Oil, Ragi",
        "body": """Dear Director of Campus Living & Dining Services,

Namaskara. At Jain International Residential School (JIRS), providing world-class holistic nutrition to 1,100+ residential students across your 350-acre Kanakapura campus requires ingredients of pristine purity and uncompromising safety.

ONSFC Agri Solutions Private Limited directly aggregates non-perishable food grains from 5,000+ dryland farmers in Gooty Mandal, processing them through a dedicated 1-acre grading and pneumatic cleaning hub along the NH-44 corridor.

OUR COMMITMENT TO JIRS RESIDENTIAL NUTRITION:
1. Absolute Purity & Zero Adulteration: Machine-cleaned with dual pneumatic de-stoners, rare-earth magnetic separators, and Sortex optical cameras. Guaranteed <0.01% impurities.
2. Nutrient-Dense Unpolished Pulses: Pure farm-gate Toor Dal and Moong Dal, free from artificial coloring, wax, or chemical polish.
3. Wood-Filtered / Cold-Pressed Groundnut Oil: Aromatic cooking oil pressed directly from selected bold groundnut pods harvested in Rayalaseema.
4. Certified Moisture (<8.5%): Protects against aflatoxin and storage insects in your campus dry stores.
5. Single-Origin Traceability: Every 50kg bag is tagged with the harvest village in Gooty Mandal.
6. Direct Overnight Transit: Dispatched via NH-44 and NICE Road directly to your Kanakapura campus loading docks.

We welcome your dining committee to test a sample consignment (no commercial obligation) to evaluate cooking aroma, fluffiness, and grain purity.

Respectfully yours,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "REVA University Mega Campus Hostels",
        "recipient_title": "Director of Student Affairs & Hostels",
        "to_email": "hostels@reva.edu.in",
        "subject": "Direct Highway Food Grain Supply (Rice, Dal, Ragi & Oil) for REVA University Yelahanka Campus",
        "crop_focus": "Aged Sona Masoori Rice, Broken Idli Rice, Unpolished Toor Dal, Ragi (Finger Millet), Groundnut Oil",
        "body": """Dear Director of Student Affairs & Hostels,

Namaskara. REVA University's sprawling 5,200+ hosteller community at Yelahanka is strategically situated right along the NH-44 expressway corridor—the exact direct transit artery connecting Gooty to North Bengaluru.

ONSFC Agri Solutions Private Limited operates a 1-acre first-mile aggregation yard at Gooty on NH-44. Because REVA University is located right at the northern entrance of Bengaluru on NH-44, our dedicated grain transport trucks reach your campus gates in just 4 hours direct highway drive without encountering any Bengaluru city traffic.

WHY SOURCING GRAINS FROM ONSFC EMPOWERS REVA HOSTELS:
1. Prime NH-44 Direct Route: Zero city delays. Loaded at 11:00 PM in Gooty, arriving at your Yelahanka hostel stores by 3:30 AM before kitchen morning preparation starts.
2. Volume Capacity: Supplying 50+ Metric Tonnes of Sona Masoori Rice, 8 MT of Toor Dal, and 3.5 MT of Karnataka Ragi monthly in scheduled weekly drops.
3. Strict Moisture Control (<8.5%): Grain arrives in tamper-evident 50kg HDPE bags, preventing moisture spoiling and pest infestation.
4. Guaranteed 15% Savings: Eliminates intermediate mandi brokers and secondary transport fees.
5. Full GST & Legal Metrology Compliance: Electronic weighbridge receipts accompanied by formal tax invoices and 30-day payment terms.

We invite your purchase department to request a 25 kg testing consignment of our Sortex Sona Masoori Rice and unpolished Toor Dal.

Sincerely,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub, AP (NH-44 Corridor)
Contact: procurement@onsfcagri.com"""
    }
]

def main():
    conn = sqlite3.connect(SELLBIRD_DB)
    cursor = conn.cursor()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    staged_count = 0
    
    for item in INSTITUTIONAL_PROPOSALS:
        comp_name = item["company_name"]
        subject = item["subject"]
        body = item["body"]
        to_email = item["to_email"]
        
        # Save as Markdown artifact file
        slug = "".join(c for c in comp_name[:15] if c.isalnum()).lower()
        md_path = os.path.join(PROPOSALS_DIR, f"proposal_{slug}.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# B2B Institutional Proposal: {comp_name}\n\n**Subject:** {subject}\n\n**To:** {to_email}\n\n---\n\n{body}\n")
            
        print(f"Generated Phase 3 Proposal document: {md_path}")
        
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
            """, (outbox_id, "camp_onsfc_phase3_institutions", prospect_id, to_email, subject, body, "pending_review", now, now, now))
            staged_count += 1
            
    conn.commit()
    conn.close()
    print(f"\nSUCCESS: Staged {staged_count} Phase 3 benchmark proposals into Sellbird outbox!")

if __name__ == "__main__":
    main()
