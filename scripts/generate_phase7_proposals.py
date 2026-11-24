#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 7 (Hyderabad Supermarkets & Food Manufacturing) Proposal Generator & Sellbird Outbox Stager
Generates 3 benchmark commercial B2B outreach proposals:
1. Ratnadeep Supermarket Central Distribution Center (Medchal) - Modern trade FMCG staples & private-label supply
2. G. Pulla Reddy Sweets Central Manufacturing Factory (Somajiguda) - Pure Besan-grade Bengal Gram & sorted bold groundnut supply
3. Q-Mart Gourmet Supermarket Central Procurement Hub (Jubilee Hills) - Clean-label, single-origin low-GI rice, organic dals & cold-pressed oil
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
        "company_name": "Ratnadeep Supermarket Central Distribution Center (Ratnadeep Retail Pvt Ltd)",
        "recipient_title": "VP - Supply Chain & Category Head Staples",
        "to_email": "staples.sourcing@ratnadeep.com",
        "subject": "Direct Farm-Gate Sona Masoori Rice & Sortexed Pulses Supply for Ratnadeep Central DC Hyderabad",
        "crop_focus": "Aged BPT 5204 Sona Masoori Rice, Low-GI RNR 15048 Telangana Sona, Premium Unpolished Toor Dal (Kandi Pappu), Urad Dal, Bold Groundnut Kernels, Cold-Pressed Groundnut Oil",
        "body": """Dear VP - Supply Chain & Category Head Staples,

Namaskaram. As Hyderabad's premier supermarket retail titan serving hundreds of thousands of households across 140+ Ratnadeep stores, maintaining flawless grain consistency, zero foreign matter, and competitive procurement margins across dry agricultural staples is paramount.

ONSFC Agri Solutions operates a 1-acre pre-cleaning, pneumatic de-stoning, and grading hub strategically located at Gooty on the NH-44 expressway corridor. We aggregate non-perishable paddy, pulses, and oilseeds directly from 5,000+ registered dryland farmers across 24 villages.

WHY SOURCING STAPLES THROUGH ONSFC EMPOWERS RATNADEEP:
1. Machine De-Stoned & Sortex Graded: Optical color sorting delivers 99.9% purity, eliminating stones, black grains, and chaff before retail packaging.
2. Ready for Private-Label Sacks: Sona Masoori Rice (BPT 5204) and popular Low-GI Telangana Sona (RNR 15048) packaged in 5kg, 10kg, and 26kg tamper-proof branded poly-woven bags.
3. 12% to 15% Cost Savings vs Begum Bazaar Middlemen: Direct farm-gate procurement eliminates multi-layered broker commissions and mandi handling cess.
4. Direct NH-44 Highway Gateway: Located on NH-44, our dedicated freight trucks cover the 300 km corridor directly into your Medchal Central DC in just 4.5 hours, arriving at 4:30 AM before morning DC intake.
5. Strict Moisture Standard (<8.5%): Protects against insect infestation, fungal growth, and retail shrinkage during regional warehousing.
6. Corporate Annual Rate Contract (ARC): Transparent quarterly price indexing against official mandi benchmarks, backed by formal GST invoices and computerized weighbridge slips.

We would be delighted to dispatch a trial 10-tonne testing consignment of our Sortex Sona Masoori Rice and unpolished Kandi Pappu directly to your Medchal DC for quality evaluation.

Sincerely,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "G. Pulla Reddy Sweets Central Manufacturing Factory",
        "recipient_title": "Factory Operations & Sourcing Director",
        "to_email": "procurement@pullareddysweets.com",
        "subject": "Pure Besan-Grade Bengal Gram & Bold Groundnut Kernels Supply for G. Pulla Reddy Sweets Hyderabad",
        "crop_focus": "Premium Besan-Grade Bengal Gram (Senagalu / Chana), Bold Groundnut Kernels, Broken Raw Rice Flour Grains",
        "body": """Dear Factory Operations & Sourcing Director,

Namaskaram. For decades, G. Pulla Reddy Sweets has stood as the gold standard of pure ghee sweets and authentic Andhra savouries. The melt-in-mouth texture, aroma, and rich golden hue of your signature Mysore Pak, Motichoor Laddus, and festive mixtures rely completely on the protein density and starch purity of the Bengal Gram milled for Besan.

ONSFC Agri Solutions directly procures dry pulses and oilseeds from 5,000+ dryland farmers across Gooty Mandal (Rayalaseema), operating a state-of-the-art grading and pneumatic de-stoning hub along the NH-44 corridor.

WHY G. PULLA REDDY SWEETS BENEFITS FROM ONSFC DIRECT SOURCING:
1. Pure Sortex Bengal Gram (Senagalu / Chana): Bold, sound kernels specially calibrated for in-house stone-milling into Besan; delivers exceptional golden color and rich nutty aroma with zero chemical adulteration.
2. Uniform Bold Groundnut Kernels (Palli / Peanuts): Cleaned, destoned, calibrated to uniform count-per-ounce, strictly <8.5% moisture for royal mixtures, roasted salted nuts, and chikkis.
3. High-Turnover Volume Reliability: Dedicated capacity to supply 40+ Metric Tonnes of Besan-grade Bengal Gram and 15+ MT of Groundnuts monthly on scheduled weekly dispatches.
4. Zero Stone & Dirt Contamination: Dual-pass pneumatic gravity separators ensure zero mud pellets or stones enter your manufacturing pulverizers.
5. Direct 4.5-Hour Transit: Direct highway run via NH-44 directly into Hyderabad by 4:30 AM before morning manufacturing shifts.
6. Enterprise Quality Guarantee: Batch lab-tested purity certificates, formal GST invoices, and Net-30 credit terms for institutional operations.

We welcome your production and quality teams to inspect our incoming grain arrivals at our Gooty hub, or we can dispatch a trial 3-tonne consignment of sorted Bengal Gram and bold groundnuts to your factory this week.

Warm regards,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Q-Mart Gourmet Supermarket Central Procurement Hub (Q-Mart Retail Ltd)",
        "recipient_title": "Head of Gourmet Procurement & Farm Sourcing",
        "to_email": "purchase@qmart.co.in",
        "subject": "Single-Origin Farm-Gate Sona Masoori, Low-GI Rice & Cold-Pressed Oils for Q-Mart Gourmet Stores",
        "crop_focus": "Certified Single-Origin Sona Masoori Rice, Low-GI RNR 15048 Diabetic Rice, Organic Unpolished Toor Dal, Foxtail Millet (Korra), Wood-Pressed Groundnut Oil",
        "body": """Dear Head of Gourmet Procurement & Farm Sourcing,

Namaskaram. Q-Mart's reputation as Hyderabad's foremost luxury gourmet supermarket in Jubilee Hills and Gachibowli resonates with affluent families seeking authenticated, chemical-free, single-origin staples.

ONSFC Agri Solutions aggregates dryland non-perishable commodities directly from 5,000+ registered family farms in Gooty Mandal. We operate a dedicated pre-cleaning and pneumatic de-stoning facility on the NH-44 corridor.

WHY Q-MART GOURMET NETWORK BENEFITS FROM ONSFC DIRECT FARM-GATE SUPPLY:
1. Single-Origin Sona Masoori & Low-GI RNR 15048: Sourced directly from Pennar black-soil farmers; naturally aged for 12+ months to guarantee non-sticky, aromatic cooking performance.
2. Certified Low-GI Rice: Lab-verified Glycemic Index <55, highly sought after by health-conscious professionals across Jubilee Hills and HITEC City.
3. Unpolished Native Pulses (Kandi Pappu): Zero synthetic food polish or mineral oils, retaining full dietary fiber and natural golden pulse flavor.
4. Wood-Pressed Groundnut Oil: Crushed at ambient temperature from hand-selected Gooty peanuts, delivering uncompromised natural aroma and heart-healthy fats.
5. High Gross Retail Margins: Direct farm-gate sourcing yields 25% to 35% retail margins for Q-Mart while maintaining fair, unexploited pricing for Gooty farmers.
6. Traceability Guarantee: Each retail sack includes QR-coded harvest date, village origin, and lab purity certificates.

We would be honoured to provide sample tasting and packaging kits of our aged Sona Masoori, low-GI rice, and wood-pressed oils to your Jubilee Hills store management this week.

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
    
    # 1. Fetch Campaign ID (or use first active campaign)
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
        
        # Save markdown proposal in proposals dir
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
        
        # Find prospect in Sellbird
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
            
        # Check if already staged in outbox
        cursor.execute("SELECT id FROM outbox WHERE to_email = ? AND subject = ?", (to_email, subject))
        existing_outbox = cursor.fetchone()
        
        if not existing_outbox:
            outbox_id = f"out_{uuid.uuid4().hex[:12]}"
            cursor.execute("""
            INSERT INTO outbox (
                id, campaign_id, prospect_id, to_email, subject, body, status, send_at, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, 'pending', ?, ?, ?)
            """, (outbox_id, campaign_id, prospect_id, to_email, subject, body, now, now, now))
            staged_count += 1
            print(f"Staged in Sellbird Outbox: {to_email} ({subject[:45]}...)")
            
    conn.commit()
    conn.close()
    print(f"\nSUCCESS: Generated {len(COMMERCIAL_PROPOSALS)} proposals and staged {staged_count} new emails in Sellbird outbox!")

if __name__ == "__main__":
    main()
