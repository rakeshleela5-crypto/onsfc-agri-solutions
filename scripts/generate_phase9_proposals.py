#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 9 (Bengaluru Film Production & Cine Catering) Proposal Generator & Sellbird Outbox Stager
Generates 3 benchmark commercial B2B outreach proposals:
1. Hombale Films Central Production Headquarters (Basavanagudi) - Pan-India blockbuster slate dry staples supply
2. Kanteerava Studios Central Production Canteen & Studio Floors (Nandini Layout) - Historic apex studio campus supply
3. Sri Manjunatha Cine Catering Services (Gandhinagar / Rajajinagar) - Sandalwood's #1 film unit catering master contractor
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
        "company_name": "Hombale Films Central Production Headquarters",
        "recipient_title": "Executive Producer & Head of Production",
        "to_email": "production@hombalefilms.com",
        "subject": "Direct Farm-Gate Aged Sona Masoori Rice, Karnataka Ragi & Pulses for Hombale Films Production Units",
        "crop_focus": "Aged Sona Masoori Rice (BPT 5204), Pure Karnataka Ragi (for Ragi Mudde), Broken Rice for breakfast, Unpolished Toor Dal (Togari Bele), Bengal Gram (Besan Grade), Bold Groundnut Kernels, Pure Cooking Oil",
        "body": """Dear Executive Producer & Head of Production,

Namaskara. As India's premier powerhouse producing monumental pan-India cinematic spectacles (KGF, Kantara, Salaar, Bagheera) running multiple 1,000+ crew shooting units simultaneously across Karnataka, the consistency, nutritional quality, and cost-efficiency of film unit catering directly underpin daily shooting productivity.

ONSFC Agri Solutions operates a 1-acre pre-cleaning, pneumatic de-stoning, and grading hub at Gooty on the NH-44 expressway corridor. We aggregate non-perishable paddy, pulses, millets, and oilseeds directly from 5,000+ registered dryland farmers across 24 villages.

WHY SOURCING STAPLES THROUGH ONSFC EMPOWERS HOMBALE FILMS:
1. Authentic 12-Month Aged Sona Masoori Rice (BPT 5204): Plump grains with exceptional water absorption (2.8x expansion) that cook fluffy and remain non-sticky in commercial buffet chafing trays throughout marathon shooting shifts.
2. Pure Certified Karnataka Ragi (Finger Millet / ರಾಗಿ): Cleaned, machine-destoned, high-protein native Ragi specially graded for preparing authentic Ragi Mudde (ರಾಗಿ ಮುದ್ದೆ)—the staple power-lunch on every Kannada film set.
3. Complete Unit Catering Basket: We supply broken raw rice for morning Akki Rotti, Idli, and Dosa batters; unpolished Toor Dal for rich Mysore Sambar; pure Besan-grade Bengal Gram for 4:00 PM shooting floor snacks (Bajjis/Bondas); and bold groundnuts for daily morning chutney.
4. 15% to 20% Direct Cost Savings vs City Middlemen: Direct farm-gate procurement eliminates multi-layered commission agents at APMC Yeshwanthpur, directly protecting multi-crore production catering budgets.
5. Direct 4.5-Hour Highway Delivery: Sacks depart Gooty via NH-44 and arrive in Bengaluru by 4:00 AM, delivered directly to your production store, studio floors, or outdoor unit bases before the 5:30 AM call-sheet.
6. Transparent Production Accounting: Computerized weighbridge slips, formal GST invoices, and flexible payment terms tailored to production schedules.

We would be honoured to supply a trial 3-tonne consignment of our aged Sona Masoori rice, native Ragi, and unpolished Toor Dal directly to your active set or central production commissary this week.

Sincerely,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Kanteerava Studios Central Production Canteen & Studio Floors",
        "recipient_title": "Managing Director & Studio Facilities Manager",
        "to_email": "canteen.kanteerava@gmail.com",
        "subject": "Direct Farm-Gate Multi-Ton Rice, Ragi & Pulses Supply for Kanteerava Studios Central Production Canteen",
        "crop_focus": "Aged Sona Masoori Rice (BPT 5204), Pure Karnataka Ragi, Broken Rice for Idli/Dosa, Sortex Toor Dal (Togari Bele), Bengal Gram (Besan Grade), Bold Groundnut Kernels, Pure Groundnut Cooking Oil",
        "body": """Dear Managing Director & Studio Facilities Directorate,

Namaskara. As the historic 20-acre nerve center of the Kannada Film Industry hosting multiple simultaneous feature film shootings and feeding 2,000+ artists, technicians, and crew daily, Kanteerava Studios' central catering operations require guaranteed grain purity, volume predictability, and competitive wholesale pricing.

ONSFC Agri Solutions operates a dedicated 1-acre first-mile aggregation and pneumatic grading yard at Gooty on the NH-44 corridor, sourcing non-perishable staples directly from 5,000+ dryland farmers across 24 villages.

WHY SOURCING THROUGH ONSFC EMPOWERS KANTEERAVA STUDIOS:
1. High-Tonnage Dedicated Supply: Capacity to supply 40+ Metric Tonnes of aged Sona Masoori Rice, 15 MT of pure Karnataka Ragi, and 12 MT of pulses monthly on scheduled multi-axle truckloads.
2. Machine De-Stoned & Optical Color Sorted: Guaranteed <0.01% impurities; completely safe for high-capacity automated steam kettles and continuous commercial cooking lines.
3. Direct Highway Gateway via NH-44: Located on NH-44, our dedicated trucks reach Nandini Layout directly via the Outer Ring Road in 4.5 hours, docking at studio gates by 4:00 AM with zero city congestion.
4. Complete Karnataka Culinary Staples: Aged Sona Masoori, high-grade native Ragi for daily Ragi Mudde, unpolished Toor Dal for rich Sambar and Saaru, Besan for shooting floor tea-break snacks, and aflatoxin-tested groundnut kernels for morning Shenga chutney.
5. Strict Moisture Standard (<8.5%): Protects against insect infestation and grain shrinkage during warehouse storage at your studio commissary.
6. Institutional Master Vendor Agreement: Quarterly price indexing against official APMC benchmarks, backed by formal GST invoices and electronic weighbridge slips.

We would be pleased to arrange a trial 5-tonne testing consignment of our aged Sona Masoori rice, pure Ragi, and unpolished Toor Dal directly to your central canteen for quality evaluation.

Warm regards,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Sri Manjunatha Cine Catering Services",
        "recipient_title": "Managing Partner & Chief Master Caterer",
        "to_email": "srimanjunathacatering@gmail.com",
        "subject": "Wholesale Farm-Gate Aged Sona Masoori Rice, Ragi & Sortex Pulses for Sri Manjunatha Cine Catering",
        "crop_focus": "Aged BPT Sona Masoori Rice, Pure Karnataka Ragi (daily Ragi Mudde), Broken Rice for Akki Rotti/Idli/Dosa, Sortex Toor Dal, Bengal Gram (Besan Grade), Bold Groundnut Kernels, Pure Cooking Oil",
        "body": """Dear Managing Partner & Master Catering Team,

Namaskara. Feeding 1,200+ cast, crew, and technical personnel daily on fast-paced Sandalwood shooting sets demands ingredients that perform flawlessly under large-scale commercial cooking conditions. The reputation of a master film caterer hinges on non-sticky white rice in chafing trays, authentic smooth Ragi Mudde, rich aromatic Sambar, and crisp evening tea-break snacks.

ONSFC Agri Solutions aggregates dry grains directly from 5,000+ farmers across Gooty Mandal (Rayalaseema), operating a dedicated pneumatic cleaning and grading facility on the NH-44 corridor.

WHY SRI MANJUNATHA CINE CATERING BENEFITS FROM ONSFC DIRECT FARM-GATE SUPPLY:
1. Authentic 12-Month Aged Sona Masoori (BPT 5204): Plump, dry grains with exceptional water absorption that do not turn mushy or soggy in commercial chafing trays during long outdoor shooting shifts.
2. Pure Cleaned Karnataka Ragi: Destoned and sorted native Ragi, delivering consistent texture and rich nutty flavor for preparing hundreds of Ragi Muddes daily.
3. Zero Foreign Matter Guarantee: Dual-pass pneumatic gravity separation removes 100% of stones and mud pellets, protecting your culinary reputation and saving hours of manual labor for your cooks.
4. Bold Groundnut Kernels for Morning Shenga Chutney: Sorted uniform kernels, strictly <8.5% moisture, delivering rich, nutty chutney for morning Akki Rotti, Idli, and Dosa plates.
5. Pure Besan-Grade Bengal Gram: Cleaned Kadale Bele calibrated for stone-milling into fragrant, golden Besan for shooting floor Bajjis, Bondas, and Pakodas at 4:00 PM.
6. 12% to 15% Wholesale Savings vs Yeshwanthpur APMC Traders: Direct farm-to-caterer pricing protects your profit margins on fixed per-plate production contracts.

We welcome you to inspect our grain arrivals at our Gooty hub, or we can dispatch a trial 1-tonne sample load of our aged rice, Ragi, and Toor Dal to your Gandhinagar base kitchen or mobile unit trucks this week.

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
            VALUES (?, 'Production', 'Director', ?, ?, ?, 'active', ?, ?)
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
