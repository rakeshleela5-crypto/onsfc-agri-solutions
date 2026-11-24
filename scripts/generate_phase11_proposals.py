#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 11 (Bengaluru Hotels & Restaurants) Proposal Generator & Sellbird Outbox Stager
Generates 3 benchmark commercial B2B outreach proposals:
1. Nagarjuna Restaurant Central Commissary & Flagship Chain (Residency Road) - Bengaluru's #1 Andhra meals empire
2. MTR (Mavalli Tiffin Room) Central Commissary & Heritage Chain (Lalbagh Road) - The legendary centenary vegetarian titan
3. Shivaji Military Hotel Central Kitchen (Jayanagar) - The century-old Donne Biryani & Ragi Mudde landmark (est. 1924)
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
        "company_name": "Nagarjuna Restaurant Central Commissary & Flagship Chain",
        "recipient_title": "Founder & Managing Director / Central SCM Directorate",
        "to_email": "procurement@nagarjunarestaurants.com",
        "subject": "Direct Farm-Gate Aged Sona Masoori, Unpolished Toor Dal & Rayalaseema Chilies for Nagarjuna",
        "crop_focus": "Certified 12-Month Aged Sona Masoori Rice (BPT 5204), Unpolished Sortex Toor Dal (Togari Bele), Sun-Dried Red Chilies (Rayalaseema Teja Grade), Bold Groundnut Kernels",
        "body": """Dear Managing Director & Central SCM Directorate,

Namaskara. For nearly four decades across Bengaluru, the name 'Nagarjuna' has been synonymous with the gold standard of authentic Andhra banana-leaf dining. The sheer daily volume of your signature unlimited thalis, Guntur chicken, spicy biryanis, and aromatic Pappu-Neyyi commands unmatched grain consistency, high cooking expansion, and pure single-origin ingredients.

ONSFC Agri Solutions operates a dedicated 1-acre first-mile aggregation, pneumatic de-stoning, and grading hub at Gooty (Anantapuramu District)—the direct historic gateway connecting Rayalaseema to Bengaluru along the NH-44 expressway. We source directly from 5,000+ dryland farmers across 24 villages.

WHY SOURCING THROUGH ONSFC EMPOWERS NAGARJUNA RESTAURANTS:
1. Certified 12-Month Aged Sona Masoori Rice (BPT 5204): Sourced from Pennar riverbed black-soil farms; laboratory verified <13% moisture, cooking to exceptional grain elongation and non-sticky fluffiness—vital for high-turnover unlimited thali service across all 6 branches.
2. Pure Unpolished Sortex Toor Dal (*Togari Bele*): 100% natural, zero mineral oil or artificial yellow polish; delivers thick, creamy consistency and rich aroma for your daily signature Andhra Pappu and Sambar cauldrons.
3. Fiery Sun-Dried Red Chilies (Rayalaseema Teja & 334 Varieties): Pure whole red chili pods directly sun-dried on farm beds, delivering the intense heat, vibrant red color, and smoky punch that define Nagarjuna's iconic curries and spice blends.
4. Bold Groundnut Kernels (*Shenga / Palli*): Machine-cleaned, uniform bold grade for your daily breakfast chutneys, tadkas, and spiced podis.
5. 12% to 15% Cost Savings vs. Local Wholesale: Direct farm-gate procurement eliminates intermediate broker commissions at Yeshwanthpur APMC and Begum Bazaar.
6. Direct 4-Hour Overnight Transit: Trucks leave our Gooty hub at 11:00 PM via the signal-free NH-44 corridor, docking at your Central Commissary by 3:30 AM before morning kitchen shifts commence.

We would be honored to supply a trial 4-tonne consignment of our aged Sona Masoori rice, Toor Dal, and sun-dried red chilies directly to your central commissary this week.

Sincerely,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "MTR (Mavalli Tiffin Room) Central Commissary & Heritage Chain",
        "recipient_title": "Chief Executive Officer & Head of Quality / SCM",
        "to_email": "procurement@mavallitiffinroom.com",
        "subject": "Direct Farm-Gate Cleaned Broken Rice, Sortex Toor Dal & Bold Peanuts for MTR Central Commissary",
        "crop_focus": "Pneumatically Cleaned Broken Raw Rice (Nookalu for Rava/Rice Idlis & Dosas), Unpolished Toor Dal (Togari Bele for Bisibelebath & Sambar), Bold Groundnut Kernels, Bengal Gram",
        "body": """Dear Chief Executive Officer & Culinary Operations Leadership,

Namaskara. Celebrating over a century of timeless culinary excellence since 1924, Mavalli Tiffin Room (MTR) represents the quintessential heritage of Bengaluru's pure vegetarian gastronomy. From your iconic Rava Idlis and crispy Masala Dosas to your legendary Bisibelebath and piping hot Sambar, MTR's century-old brand equity rests entirely on impeccable ingredient purity and zero batch variance.

ONSFC Agri Solutions operates a 1-acre pre-cleaning, pneumatic de-stoning, and optical color sorting facility at Gooty on the NH-44 corridor.

WHY MTR COMMISSARY OPERATES WITH GREATER QUALITY & PURITY THROUGH ONSFC:
1. Machine-Destoned Broken Raw Rice (*Nookalu*): Dual-pass pneumatic gravity separators remove 100% of mud pellets and stones, protecting your heavy commercial grinders and ensuring fluffy fermentation for your daily idli and dosa batters.
2. Unpolished Sortex Toor Dal (*Togari Bele*): Pure single-origin pulses without mineral oil coating or artificial color additives; delivers the authentic, wholesome nutty aroma and deep golden hue indispensable for MTR's signature Bisibelebath and Sambar recipes.
3. Bold Groundnut Kernels (*Shenga*): Hand-sorted, single-variety bold peanuts with strictly <8.5% moisture; rich in natural oils, perfect for fresh daily breakfast chutneys and savory mixtures.
4. Native Millets (Ragi & Jowar): Chemical-free, nutrient-rich finger millet for MTR's specialized millet tiffin and health menus.
5. Absolute Supply Chain Assurance: Dedicated 35+ Metric Tonnes monthly allocation with full lot traceability from 24 villages in Gooty Mandal.
6. Seamless Overnight Delivery: Direct 290 km straight-line transit along NH-44 directly into Central Bengaluru by 4:00 AM.

We welcome your quality assurance and executive culinary teams to inspect sample consignments, or we can deliver a trial 3-tonne load to your Lalbagh Road central commissary this week.

With utmost respect,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Shivaji Military Hotel Central Kitchen & Flagship",
        "recipient_title": "Managing Proprietor & Kitchen Master",
        "to_email": "procurement@shivajimilitaryhotel.com",
        "subject": "Direct Farm-Gate Native Ragi, Aged Sona Masoori & Fiery Red Chilies for Shivaji Military Hotel",
        "crop_focus": "Native Karnataka Ragi (Finger Millet for daily Ragi Mudde), Aged Sona Masoori Rice (for Donne Biryani & Meals), Unpolished Toor Dal, Sun-Dried Red Chilies, Bold Groundnut Kernels",
        "body": """Dear Managing Proprietor & Master Chefs,

Namaskara. Since 1924, Shivaji Military Hotel in Jayanagar has stood as the undisputed pioneer and crown jewel of Karnataka's military hotel culture. Serving thousands of devoted patrons daily with your iconic Donne Biryani, steaming hot Ragi Mudde (*ರಾಗಿ ಮುದ್ದೆ*), spicy mutton saaru, and fiery dry fries, your culinary tradition requires raw ingredients of uncompromised rustic character.

ONSFC Agri Solutions operates a direct farmer-aggregation and pneumatic cleaning hub at Gooty on the NH-44 corridor, working with 5,000+ registered dryland farmers.

WHY SHIVAJI MILITARY HOTEL PROFITS FROM ONSFC DIRECT FARM SUPPLY:
1. Machine-Cleaned Native Ragi (*ರಾగులు / Ragi*): Stone-free, mud-free, finely sorted native finger millet specially calibrated for making soft, lump-free, aromatic daily Ragi Mudde that keeps your patrons coming back.
2. Premium Aged Sona Masoori Rice: Naturally seasoned for 12 months; high starch resilience, ensuring every grain in your daily biryani degs and steamed meals cooks distinct, firm, and fully separated.
3. Authentic Sun-Dried Red Chilies: Fiery whole red chilies with intense heat, rich red oil dispersion, and smoky aroma—the secret soul behind authentic military hotel mutton saaru and chili chicken.
4. Sortex-Graded Toor Dal & Bengal Gram: Completely free from foreign seeds and stones, ready for immediate morning boiling and grinding.
5. Farm-Direct Cost Advantage: Direct procurement from Gooty eliminates local market middlemen, saving 12% on your high-tonnage monthly dry grocery expenditure.
6. Direct 4-Hour Truck Delivery: Dispatched straight from Gooty to your Jayanagar prep unit by 4:00 AM before early morning butchery and kitchen fires are lit.

We invite you to test a 2-tonne trial consignment of our native Ragi, aged rice, and sun-dried chilies at your main kitchen this week.

Warm regards,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    }
]

def main():
    conn = sqlite3.connect(SELLBIRD_DB)
    cursor = conn.cursor()

    # Ensure proposals table exists
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
        
        # Check company_id
        cursor.execute("SELECT id FROM companies WHERE name = ?", (comp_name,))
        comp_row = cursor.fetchone()
        company_id = comp_row[0] if comp_row else f"comp_{uuid.uuid4().hex[:12]}"
        
        # Check prospect_id
        cursor.execute("SELECT id FROM prospects WHERE company = ?", (comp_name,))
        pros_row = cursor.fetchone()
        prospect_id = pros_row[0] if pros_row else f"pros_{uuid.uuid4().hex[:12]}"

        # Save markdown file
        safe_name = "".join(c for c in comp_name if c.isalnum() or c in (" ", "_", "-")).strip().replace(" ", "_")
        md_filename = f"ONSFC_Phase11_Proposal_{safe_name}.md"
        md_filepath = os.path.join(PROPOSALS_DIR, md_filename)
        
        with open(md_filepath, "w", encoding="utf-8") as f:
            f.write(f"# Commercial Proposal: {comp_name}\n")
            f.write(f"**Recipient**: {p['recipient_title']}\n")
            f.write(f"**Target Crops**: {p['crop_focus']}\n")
            f.write(f"**Email Subject**: {p['subject']}\n")
            f.write(f"**Date**: {now}\n\n---\n\n")
            f.write(p["body"])
        
        # Insert/Update in Sellbird DB with status='approved'
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
        print(f"Staged Proposal for: {comp_name} -> {md_filename}")

    conn.commit()
    conn.close()
    print(f"\nSUCCESS: Generated and approved {staged_count} Phase 11 commercial proposals in Sellbird Outbox!")

if __name__ == "__main__":
    main()
