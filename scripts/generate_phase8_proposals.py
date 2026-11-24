#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 8 (Hyderabad Film Production & Cine Catering) Proposal Generator & Sellbird Outbox Stager
Generates 3 benchmark commercial B2B outreach proposals:
1. Mythri Movie Makers Central Production Office (Jubilee Hills) - Production controller & unit catering direct dry staples supply
2. Ramoji Film City (RFC) Central Film Production Commissary & Outdoor Shooting Unit Kitchens (Abdullapurmet) - High-tonnage studio campus supply
3. Sri Satya Cine Caterers (Film Nagar) - Apex film unit catering master contractor
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
        "company_name": "Mythri Movie Makers Central Production Office",
        "recipient_title": "Executive Producer & Production Controller",
        "to_email": "production@mythrimoviemakers.com",
        "subject": "Direct Farm-Gate Aged Sona Masoori Rice & Sortexed Pulses for Mythri Movie Production Units",
        "crop_focus": "Aged Sona Masoori Rice (BPT 5204), Broken Rice for Breakfast Batters, Unpolished Toor Dal (Kandi Pappu), Bengal Gram (Besan Grade), Bold Groundnut Kernels, Pure Cooking Oil",
        "body": """Dear Executive Producer & Production Controller,

Namaskaram. In managing massive pan-India productions featuring hundreds of cast members, technicians, and crew across Hyderabad studios and outdoor locations, the quality, consistency, and cost of production catering directly influence daily shooting efficiency and crew morale.

ONSFC Agri Solutions operates a 1-acre pre-cleaning, pneumatic de-stoning, and grading hub at Gooty on the NH-44 corridor. We aggregate non-perishable paddy, pulses, and oilseeds directly from 5,000+ registered dryland farmers across 24 villages.

WHY SOURCING STAPLES THROUGH ONSFC EMPOWERS MYTHRI MOVIE MAKERS:
1. Certified 12-Month Aged Sona Masoori Rice (BPT 5204): Sourced directly from Pennar black-soil farms; cooks fluffy, non-sticky, and expands 2.8x in volume—ideal for large buffet chafing dishes and unit dining tents.
2. Machine De-Stoned & Optical Color Sorted: Guaranteed 99.9% purity. Zero mud pellets or stones, eliminating tedious kitchen sorting for your unit caterers.
3. Complete Unit Catering Staple Basket: We supply broken rice for morning breakfast batters (Idli/Dosa), unpolished Toor Dal for rich Sambar, Besan-grade Bengal Gram for 4:00 PM shooting floor snacks (Mirchi Bajji/Pakoda), and bold peanuts for morning chutney.
4. 15% to 20% Direct Cost Savings: Direct farm-gate sourcing bypasses middleman markups in Begum Bazaar, optimizing multi-crore production catering line items.
5. Direct 4.5-Hour Highway Delivery: Sacks arrive in Hyderabad by 4:30 AM via NH-44, delivered directly to your production store, studio floors, or outdoor unit base before the 5:30 AM call-sheet.
6. Corporate Project Accounting: Formal GST invoices, computerized weighbridge slips, and flexible payment terms tailored to production schedules.

We would be honoured to supply a trial 2-tonne consignment of our aged Sona Masoori rice, Toor Dal, and sorted Bengal Gram directly to your active set or central production store this week.

Sincerely,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Ramoji Film City (RFC) Central Film Production Commissary & Outdoor Shooting Unit Kitchens",
        "recipient_title": "Chief Procurement Officer - Food, Beverage & Film Unit Logistics",
        "to_email": "sourcing.rfc@ramojifilmcity.com",
        "subject": "Direct Farm-Gate Multi-Ton Rice, Pulses & Oil Supply for Ramoji Film City Central Commissary",
        "crop_focus": "Aged Sona Masoori Rice (BPT 5204), Broken Rice, Sortex Unpolished Toor Dal (Kandi Pappu), Bengal Gram (Besan Grade), Bold Groundnut Kernels, Refined & Cold-Pressed Groundnut Oil, Sun-Dried Red Chilies",
        "body": """Dear Chief Procurement Officer & F&B Directorate,

Namaskaram. As the world's largest integrated film city hosting 20 to 30 simultaneous feature film shootings, television productions, and thousands of resident hospitality guests, Ramoji Film City's daily food operations require unprecedented volume predictability, zero foreign matter, and competitive farm-gate procurement.

ONSFC Agri Solutions operates a 1-acre first-mile aggregation and pneumatic grading yard at Gooty on the NH-44 corridor, sourcing non-perishable staples directly from 5,000+ dryland farmers across 24 villages.

WHY SOURCING THROUGH ONSFC EMPOWERS RAMOJI FILM CITY:
1. High-Tonnage Dedicated Supply: Capacity to supply 80+ Metric Tonnes of aged Sona Masoori Rice, 20 MT of broken rice, and 25 MT of pulses monthly on scheduled multi-axle truckloads.
2. Dual-Pass Pneumatic De-Stoned & Sortex Graded: Guaranteed <0.01% impurities; safe for high-capacity automated steam kettles and continuous industrial cooking lines.
3. Direct Highway Route into RFC via Outer Ring Road: Located on NH-44, our dedicated carriers connect seamlessly to ORR Exit 11, docking at RFC central stores in 4.5 hours with zero city congestion.
4. Full Dry Crop Portfolio: Aged Sona Masoori, broken rice for breakfast preparations, unpolished Toor Dal, pure Bengal Gram for Besan, aflatoxin-tested groundnut kernels, and Rayalaseema sun-dried red chilies.
5. Strict Moisture Standard (<8.5%): Prevents weevil infestation and grain shrinkage during large-scale warehouse storage at your central commissary.
6. Institutional Master Vendor Agreement: Quarterly price indexing against official APMC benchmarks, backed by formal GST invoices and electronic weighbridge slips.

We would be pleased to arrange a trial 10-tonne testing consignment of our aged Sona Masoori rice and unpolished Toor Dal directly to your central commissary for quality evaluation.

Warm regards,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Sri Satya Cine Caterers (Satya Film Unit Catering Services)",
        "recipient_title": "Managing Partner & Chief Master Caterer",
        "to_email": "satyacinecatering@gmail.com",
        "subject": "Wholesale Farm-Gate Aged Sona Masoori Rice & Sortex Pulses for Sri Satya Cine Catering Services",
        "crop_focus": "Aged BPT Sona Masoori Rice, Broken Rice for Breakfast, Unpolished Toor Dal, Bengal Gram (Besan Grade), Bold Groundnut Kernels, Pure Groundnut Oil",
        "body": """Dear Managing Partner & Master Catering Team,

Namaskaram. Serving 1,500+ cast, crew, and technical staff daily on high-pressure Tollywood shooting sets demands ingredients that perform flawlessly under large-scale commercial cooking conditions. The success of a film unit caterer relies on white rice that stays separate and aromatic in chafing dishes, rich golden sambar, and crisp evening bajjis.

ONSFC Agri Solutions aggregates dry grains directly from 5,000+ farmers across Gooty Mandal (Rayalaseema), operating a dedicated pneumatic cleaning and grading facility on the NH-44 corridor.

WHY SRI SATYA CINE CATERERS BENEFITS FROM ONSFC DIRECT FARM-GATE SUPPLY:
1. Authentic 12-Month Aged Sona Masoori (BPT 5204): Plump, dry grains with exceptional water absorption that do not become soggy or mushy in commercial chafing trays during marathon shooting shifts.
2. Zero Foreign Matter Guarantee: Dual-pass pneumatic gravity separation removes 100% of mud pellets and stones, protecting your kitchen reputation and saving hours of manual labor.
3. Bold Groundnut Kernels for Daily Morning Chutney: Sorted uniform kernels, strictly <8.5% moisture, delivering rich, creamy, nutty Palli chutney for 1,000+ breakfast plates every morning.
4. Pure Besan-Grade Bengal Gram: Cleaned Senagalu calibrated for stone-milling into fragrant, golden Besan for shooting floor Mirchi Bajjis, Mysore Bondas, and Pakodas.
5. 12% to 15% Wholesale Savings vs Begum Bazaar Wholesalers: Direct farm-to-caterer pricing protects your profit margins on fixed per-plate production contracts.
6. Scheduled Direct Delivery: Fresh grain bags delivered directly to your Film Nagar base kitchen or mobile outdoor unit trucks by 4:30 AM.

We welcome you to inspect our grain arrivals at our Gooty hub, or we can dispatch a trial 1-tonne sample load of our aged rice and Toor Dal to your Film Nagar prep unit this week.

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
