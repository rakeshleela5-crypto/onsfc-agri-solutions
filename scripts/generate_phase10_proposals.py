#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 10 (Hyderabad Hotels & Restaurants) Proposal Generator & Sellbird Outbox Stager
Generates 3 benchmark commercial B2B outreach proposals:
1. Kritunga Restaurant Central Commissary (Panjagutta) - The Palegars of Rayalaseema cuisine (Ragi Sankati & Sona Masoori)
2. Chutneys Central Commissary & Restaurant Chain (Banjara Hills) - Hyderabad's #1 vegetarian dining titan
3. Novotel Hyderabad Airport & Convention Center (Shamshabad, NH-44) - 5-star hotel directly on Gooty truck arrival corridor
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
        "company_name": "Kritunga Restaurant Central Commissary & Flagship Chain",
        "recipient_title": "Founder & Managing Director / Central SCM Head",
        "to_email": "procurement@kritunga.com",
        "subject": "Direct Rayalaseema Farm-Gate Ragi, Aged Sona Masoori & Dry Red Chilies for Kritunga Restaurants",
        "crop_focus": "Native Rayalaseema Ragi (Finger Millet for daily Ragi Sankati), Aged BPT Sona Masoori Rice, Sortex Toor Dal (Kandi Pappu), Sun-Dried Red Chilies (Rayalaseema Teja Grade), Bold Groundnut Kernels & Pure Cooking Oil",
        "body": """Dear Founder & Managing Director / Central SCM Directorate,

Namaskaram. As 'The Palegars of Rayalaseema Cuisine' operating 18+ high-volume restaurants across Hyderabad, Kritunga's legendary reputation is built upon the fiery, rustic, and authentic flavors of our native Rayalaseema soil. The heart of your menu—signature Ragi Sankati with Natu Kodi Pulusu, spicy Rayalaseema biryanis, and unlimited thalis—demands unadulterated, single-origin dry staples sourced directly from the heartland.

ONSFC Agri Solutions operates a 1-acre pre-cleaning, pneumatic de-stoning, and grading hub at Gooty (Anantapuramu District)—the exact historic gateway of Rayalaseema. We aggregate non-perishable paddy, native millets, pulses, and sun-dried chilies directly from 5,000+ registered dryland farmers across 24 villages.

WHY SOURCING THROUGH ONSFC EMPOWERS KRITUNGA RESTAURANTS:
1. Authentic Rayalaseema Ragi (*రాగులు*): Cleaned, machine-destoned, 100% stone-free native Ragi specially calibrated for smooth, aromatic, lump-free daily Ragi Sankati across all 18 branches.
2. Authentic 12-Month Aged Sona Masoori Rice (BPT 5204): Sourced from Pennar black-soil farms; cooks fluffy, high-volume, non-sticky—essential for high-tonnage unlimited thalis and biryani prep.
3. Fiery Sun-Dried Red Chilies (Rayalaseema Teja & 334 Varieties): Pure sun-dried whole red pods delivering authentic pungent aroma and vibrant natural red color for your signature curries and mirchi mixtures.
4. Bold Groundnut Kernels (*Palli*): Cleaned, uniform count-per-ounce, strictly <8.5% moisture for daily chutneys, curries, and tadkas.
5. 15% Direct Farm-to-Kitchen Cost Savings: Direct procurement eliminates broker markups at Begum Bazaar and intermediate mandis, protecting kitchen operating margins across your chain.
6. Direct 4.5-Hour Transit: Dispatches from Gooty cruise directly along NH-44, arriving at your Central Commissary by 4:00 AM before morning prep shifts.

We would be honoured to supply a trial 3-tonne consignment of our native Ragi, aged Sona Masoori rice, and sun-dried red chilies directly to your central kitchen this week.

Sincerely,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Chutneys Central Commissary & Restaurant Chain",
        "recipient_title": "Managing Director & Central Commissary SCM Lead",
        "to_email": "procurement@chutneys.in",
        "subject": "Direct Farm-Gate Broken Rice, Bold Peanuts & Sortex Pulses for Chutneys Hyderabad Commissary",
        "crop_focus": "Broken Raw Rice (Nookalu for Idlis/Dosas), Urad Dal (Minapappu), Unpolished Toor Dal (Kandi Pappu), Bold Groundnut Kernels (for signature 7 Chutneys), Bengal Gram for Bajjis",
        "body": """Dear Managing Director & Central Commissary SCM Team,

Namaskaram. For decades, Chutneys has stood as Hyderabad's undisputed pinnacle of vegetarian breakfast and fine dining. The legendary reputation of your steaming Guntur Idlis, Babai Hotel Idlis, MLA Dosas, and iconic 7 signature chutneys relies entirely upon the starch quality of broken rice and the fresh, nutty sweetness of the groundnuts crushed for your daily chutneys.

ONSFC Agri Solutions operates a dedicated 1-acre first-mile aggregation and pneumatic grading yard at Gooty on the NH-44 corridor, sourcing dry staples directly from 5,000+ dryland farmers across 24 villages.

WHY CHUTNEYS BENEFITS FROM ONSFC DIRECT FARM-GATE SUPPLY:
1. Pure Cleaned Broken Raw Rice (*Nookalu*): Machine-destoned, sortex-graded broken raw rice with optimal starch extraction, ensuring your breakfast Idlis steam ultra-fluffy and Dosas crisp to perfection without sticking.
2. Bold Groundnut Kernels (*Palli / Peanuts*): Uniform single-size bold kernels, strictly <8.5% moisture, delivering rich, creamy, nutty aroma for your signature daily Palli chutney.
3. Pure Unpolished Toor Dal (*Kandi Pappu*): Zero mineral oil or artificial yellow dyes; delivers authentic golden color, high protein density, and irresistible aroma for your morning Sambar cauldrons.
4. Zero Stone & Dirt Contamination: Dual-pass pneumatic gravity separators remove 100% of mud pellets and stones, eliminating tedious kitchen sorting.
5. High-Throughput Volume Reliability: Dedicated capacity to supply 30+ Metric Tonnes of broken rice, 15 MT of aged Sona Masoori, and 6 MT of groundnuts monthly on scheduled weekly dispatches.
6. Direct 4.5-Hour Transit: Deliveries reach your Banjara Hills central commissary by 4:00 AM before morning 5:00 AM tiffin grinding shifts begin.

We welcome your culinary and operations teams to inspect our grain arrivals, or we can dispatch a trial 2-tonne consignment of our broken rice, Toor Dal, and bold groundnuts to your central prep unit this week.

Warm regards,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Novotel Hyderabad Airport & Convention Center",
        "recipient_title": "Director of Materials & Executive Chef",
        "to_email": "h6107-mat@accor.com",
        "subject": "Direct Farm-Gate Certified Sona Masoori, Low-GI Rice & Organic Pulses for Novotel Hyderabad Airport",
        "crop_focus": "Certified Single-Origin Sona Masoori Rice, Low-GI RNR 15048 Telangana Sona, Organic Unpolished Toor Dal, Millets (Ragi/Jowar), Cold-Pressed Groundnut Oil",
        "body": """Dear Director of Materials & Executive Culinary Directorate,

Namaskaram. As a premier 5-star international airport property hosting multinational airline crews, global business summits, and luxury banquets, Novotel Hyderabad Airport's culinary operations require uncompromising food safety, grain traceability, and zero-shrinkage delivery.

ONSFC Agri Solutions operates a 1-acre pre-cleaning and pneumatic grading hub at Gooty directly along the NH-44 expressway corridor.

WHY NOVOTEL HYDERABAD AIRPORT EMPOWERS ITS KITCHENS THROUGH ONSFC:
1. Direct Highway Arrival (Zero In-City Transit): Located right on the NH-44 corridor at Shamshabad, our trucks dock at your receiving bay in 4.5 hours straight from our Gooty hub without encountering a single city traffic restriction.
2. Certified Single-Origin Sona Masoori & Low-GI RNR 15048: Sourced directly from Pennar black-soil farms; lab-verified Low-GI (<55) sugar-free rice, ideal for international and health-conscious guests.
3. Machine De-Stoned & Optical Color Sorted: Guaranteed <0.01% impurities; completely safe for your high-capacity commercial kitchens and luxury banqueting buffets.
4. Native Millets (Ragi & Jowar): Chemical-free, nutrient-dense millets for curated breakfast wellness corners and regional culinary showcases.
5. Ambient Cold-Pressed Groundnut Cooking Oil: Unrefined, cold-pressed from hand-sorted Gooty peanuts, offering rich natural aroma and zero trans fats.
6. Accor Institutional Vendor Compliance: Batch lab test certificates, E-Way bills, formal GST invoices, and structured Net-30 credit terms.

We would be delighted to provide a sample presentation kit and dispatch a trial 1-tonne testing load of our aged Sona Masoori rice and unpolished Toor Dal directly to your Shamshabad receiving dock this week.

With respectful regards,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    }
]

def main():
    conn = sqlite3.connect(SELLBIRD_DB)
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM campaigns LIMIT 1")
    camp_row = cursor.fetchone()
    campaign_id = camp_row[0] if camp_row else f"camp_{uuid.uuid4().hex[:12]}"
    
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    staged_count = 0
    
    for prop in COMMERCIAL_PROPOSALS:
        comp_name = prop["company_name"]
        to_email = prop["to_email"]
        subject = prop["subject"]
        body = prop["body"]
        
        # Save markdown proposal
        slug = "".join(c if c.isalnum() else "_" for c in comp_name[:35]).strip("_").lower()
        file_path = os.path.join(PROPOSALS_DIR, f"proposal_{slug}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# COMMERCIAL PROPOSAL: {comp_name}\n")
            f.write(f"**To:** {prop['recipient_title']} ({to_email})\n")
            f.write(f"**Subject:** {subject}\n")
            f.write(f"**Commodities:** {prop['crop_focus']}\n\n")
            f.write("---\n\n")
            f.write(body)
            
        print(f"Generated proposal file: {file_path}")
        
        # Check or insert prospect
        cursor.execute("SELECT id FROM prospects WHERE company = ?", (comp_name,))
        pros_row = cursor.fetchone()
        if pros_row:
            prospect_id = pros_row[0]
        else:
            prospect_id = f"pros_{uuid.uuid4().hex[:12]}"
            cursor.execute("""
            INSERT INTO prospects (id, first_name, last_name, email, company, title, status, created_at, updated_at)
            VALUES (?, 'Purchase', 'Director', ?, ?, ?, 'active', ?, ?)
            """, (prospect_id, to_email, comp_name, prop["recipient_title"], now, now))
            
        # Check or insert outbox
        cursor.execute("SELECT id FROM outbox WHERE to_email = ? AND subject = ?", (to_email, subject))
        existing_outbox = cursor.fetchone()
        
        if not existing_outbox:
            outbox_id = f"out_{uuid.uuid4().hex[:12]}"
            cursor.execute("""
            INSERT INTO outbox (
                id, campaign_id, prospect_id, to_email, subject, body, status, send_at, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, 'approved', ?, ?, ?)
            """, (outbox_id, campaign_id, prospect_id, to_email, subject, body, now, now, now))
            staged_count += 1
            print(f"Staged & Approved in Sellbird Outbox: {to_email} ({subject[:45]}...)")
            
    conn.commit()
    conn.close()
    print(f"\nSUCCESS: Generated {len(COMMERCIAL_PROPOSALS)} proposals and staged {staged_count} approved emails in Sellbird outbox!")

if __name__ == "__main__":
    main()
