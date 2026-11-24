#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 2 (Bengaluru & Hyderabad) Proposal Generator & Sellbird Outbox Stager
Generates 2 benchmark metro B2B outreach proposals:
1. The Rameshwaram Cafe Central Commissary (Bengaluru) - Premium Aged Sona Masoori & Idli Rice
2. Sneha Farms Mega Feed Mill & Grain Silos (Jadcherla / Hyderabad NH-44) - Yellow Maize & Broken Rice
"""

import os
import sqlite3
import uuid
import datetime

SELLBIRD_DB = r"C:\Users\rakes\.gemini\antigravity\scratch\sellbird\data\sellbird.db"
PROPOSALS_DIR = r"C:\Users\rakes\.gemini\antigravity\scratch\onsfc-agri-solutions\proposals"
os.makedirs(PROPOSALS_DIR, exist_ok=True)

METRO_PROPOSALS = [
    {
        "company_name": "The Rameshwaram Cafe Central Commissary",
        "recipient_title": "Chief Procurement Officer / Supply Chain Head",
        "to_email": "procurement@therameshwaramcafe.org",
        "subject": "Direct Farm-Gate Aged Sona Masoori & Pneumatically De-Stoned Idli Rice for Rameshwaram Cafe Kitchens",
        "crop_focus": "Aged Sona Masoori Rice (BPT 5204), Broken Idli Rice, Unpolished Toor Dal, Cold-Pressed Groundnut Oil",
        "body": """Dear Chief Procurement Officer & Culinary Operations Head,

Namaskara. With the divine blessings of Lord Shiva, we present this farm-direct supply proposal from ONSFC Agri Solutions Private Limited.

The extraordinary standard of The Rameshwaram Cafe's iconic crispy dosas, fluffy idlis, and ghee-laden pongal requires grains of absolute perfection—uncompromising starch consistency, natural aging, zero stones, and pristine freshness.

ONSFC aggregates dry agricultural staples directly from 5,000+ dryland farmers across 24 villages of Gooty Mandal (Rayalaseema), operating a certified 1-acre pre-cleaning, pneumatic de-stoning, and grading hub right on the NH-44 expressway corridor.

OUR DEDICATED SUPPLY COMMITMENTS FOR RAMESHWARAM CAFE:
1. 100% Aged Sona Masoori Rice (BPT 5204): Naturally aged over 12 months, delivering non-sticky, maximum volumetric cooking expansion.
2. Premium Broken Rice for Batter: High-starch, sortexed, zero stone/grit rice that ferments smoothly for signature melt-in-mouth idlis and golden dosas.
3. Unpolished Farm-Gate Toor Dal & Urad Dal: High protein density, free from chemical polishing agents or artificial luster.
4. Cold-Filtered Groundnut Oil: Aromatic cooking oil pressed directly from fresh Rayalaseema peanut harvests.
5. Direct Overnight NH-44 Transit: 290 km direct highway transit (4.5 hrs). Dispatched from Gooty at 11:00 PM, arriving at your Bengaluru central commissary by 4:30 AM before morning chef shifts.
6. 15-20% Savings vs APMC Yeshwanthpur Wholesalers: Sourced directly at the farm gate, passing massive cost savings without middleman commissions.

We would be honored to deliver a complimentary 25 kg sample bag of our aged Sona Masoori and Idli Rice directly to your Bengaluru central kitchen for your master chefs to evaluate batter consistency and texture.

With warm regards,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Expressway Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Sneha Farms Mega Feed Mill & Grain Silos (Jadcherla / Hyderabad)",
        "recipient_title": "General Manager (Raw Material Sourcing) / Feed Operations Head",
        "to_email": "procurement.feed@snehafarms.com",
        "subject": "Bulk Farm-Gate Yellow Maize (Corn) & Broken Rice Dispatches for Sneha Farms Jadcherla Silos",
        "crop_focus": "Yellow Maize (Makka), Broken Rice (Nookalu), Groundnut De-Oiled Meal",
        "body": """Dear General Manager (Raw Material Sourcing),

Managing raw material feed operations across Sneha Farms' massive 150,000 MT grain silos at Jadcherla demands guaranteed volume consistency, strict moisture thresholds, and competitive farm-gate pricing.

ONSFC Agri Solutions Private Limited operates a 1-acre first-mile aggregation yard at Gooty on the NH-44 expressway corridor. Located just 180 km south of your Jadcherla mega-facility, we directly link 5,000+ dryland grain and cereal farmers to large-scale agro-industrial off-takers.

WHY SOURCING GRAINS THROUGH ONSFC EMPOWERS SNEHA FARMS:
1. Certified Low Moisture (<8.5%): Critical for long-term silo storage. Our digital moisture grading prevents aflatoxin build-up and microbiological spoilage.
2. High-Capacity Truckload Dispatches: Multi-axle 25-tonne and 40-tonne truckloads dispatched directly up NH-44 straight to your Jadcherla hopper unloading bays within 3 hours.
3. 5-8% Direct Savings vs Hyderabad/Osmangunj Mandi Traders: Eliminates commission agents, mandi market fees, and secondary handling markups.
4. Unadulterated Broken Rice (Nookalu): Pure rice grits with high digestible energy for optimal poultry feed conversion ratios (FCR).
5. Calibrated Digital Weighbridge Receipts & Spot Settlements: Clear Legal Metrology certification with full GST billing.

We invite your technical inspection team to review our intake grain parameters at our Gooty yard, or we can dispatch a trial 20-tonne consignment of dried yellow maize directly to your Jadcherla plant this week.

Sincerely,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    }
]

def main():
    conn = sqlite3.connect(SELLBIRD_DB)
    cursor = conn.cursor()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    staged_count = 0
    
    for item in METRO_PROPOSALS:
        comp_name = item["company_name"]
        subject = item["subject"]
        body = item["body"]
        to_email = item["to_email"]
        
        # Save as Markdown artifact file
        slug = "".join(c for c in comp_name[:15] if c.isalnum()).lower()
        md_path = os.path.join(PROPOSALS_DIR, f"proposal_{slug}.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# B2B Proposal: {comp_name}\n\n**Subject:** {subject}\n\n**To:** {to_email}\n\n---\n\n{body}\n")
            
        print(f"Generated Phase 2 Proposal document: {md_path}")
        
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
            """, (outbox_id, "camp_onsfc_phase2_metros", prospect_id, to_email, subject, body, "pending_review", now, now, now))
            staged_count += 1
            
    conn.commit()
    conn.close()
    print(f"\nSUCCESS: Staged {staged_count} Phase 2 benchmark proposals into Sellbird outbox!")

if __name__ == "__main__":
    main()
