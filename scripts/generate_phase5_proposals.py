#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 5 (Hyderabad Contractual Buyers) Proposal Generator & Sellbird Outbox Stager
Generates 3 benchmark institutional B2B outreach proposals:
1. AIG Hospitals (Asian Institute of Gastroenterology) Central Dietary Dept (Clinical GI and metabolic nutrition)
2. BITS Pilani - Hyderabad Campus Central Mess Directorate (Premier technical university 3,500+ hosteller supply)
3. Priya Foods Central Manufacturing Plant (Ushodaya Enterprises / Ramoji Group) (Industrial spices & food processing contract)
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
        "company_name": "AIG Hospitals (Asian Institute of Gastroenterology) Central Dietary Dept",
        "recipient_title": "Chief Clinical Nutritionist / GM Procurement",
        "to_email": "dietary@aighospitals.com",
        "subject": "Clinical-Grade Single-Origin Telangana Sona (RNR 15048) & Unpolished Dals for AIG Hospitals In-Patient Kitchens",
        "crop_focus": "Telangana Sona Low-GI Sugar-Free Rice (RNR 15048), Aged Sona Masoori Rice, Unpolished Moong & Toor Dal, Foxtail Millet, Cold-Pressed Groundnut Oil",
        "body": """Dear Chief of Clinical Nutrition & SCM Directorate,

Namaskaram. With the divine blessings of Lord Shiva, we submit this institutional healthcare supply presentation from ONSFC Agri Solutions Private Limited.

As India's foremost apex institution in gastroenterology, hepatology, and metabolic health, AIG Hospitals operates under clinical dietary mandates where carbohydrate complexity, GI indices, and chemical purity directly impact patient gut microbiome and therapeutic recovery. Serving 800+ in-patients requires grains with zero pesticide residue, low glycemic response, and absolute stone-free purity.

ONSFC directly aggregates non-perishable dry staples from 5,000+ dryland farmers across 24 villages of Gooty Mandal along the NH-44 corridor, operating a certified 1-acre pre-cleaning, pneumatic de-stoning, and grading hub.

OUR CLINICAL DIETARY SPECIFICATIONS FOR AIG HOSPITALS:
1. Authentic Telangana Sona Low-GI Rice (RNR 15048): Clinically proven low glycemic index (GI < 55) table rice, tested for slow-release starch, optimal for diabetic, bariatric, and gastroenterology in-patient diets.
2. 100% Unpolished Therapeutic Dals (Moong & Toor): High natural bioavailability protein, zero synthetic coloring, zero mineral wax, and zero chemical polishing agents.
3. Cold-Filtered Groundnut Cooking Oil: Heart-healthy cooking oil pressed directly from selected bold groundnut pods; zero trans-fat, zero palm oil blending.
4. Absolute Foreign Matter Purity (<0.01%): Dual pneumatic air-density de-stoners and magnetic separators guarantee zero stones or grit.
5. Direct Overnight Transit via NH-44: 300 km direct highway transit (4.5 hrs). Dispatched from Gooty at 11:00 PM, arriving at your Gachibowli loading docks by 4:30 AM before morning meal preparation.

We propose establishing an Annual Rate Contract (ARC) or Vendor Empanelment agreement, and we invite your clinical nutrition committee to test a complimentary 25 kg evaluation consignment of our RNR 15048 Telangana Sona and Unpolished Moong Dal.

Respectfully yours,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Expressway Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "BITS Pilani - Hyderabad Campus Central Mess Directorate",
        "recipient_title": "Dean of Student Welfare / Mess Council Warden",
        "to_email": "warden@hyderabad.bits-pilani.ac.in",
        "subject": "5:00 AM Farm-Direct Sona Masoori Rice & Machine De-Stoned Dals for BITS Pilani Hyderabad Hostels",
        "crop_focus": "Aged Sona Masoori Rice (BPT 5204), Broken Rice for Tiffins, Unpolished Toor Dal, Urad Dal, Bengal Gram, Pure Cooking Oil",
        "body": """Dear Dean of Student Welfare & Central Mess Council,

Namaskaram. Sourcing dry staples for 3,500+ residential engineering and research scholars across BITS Pilani's Hyderabad campus demands guaranteed volume consistency, high volumetric cooking yield, and complete elimination of foreign matter complaints.

ONSFC Agri Solutions operates a 1-acre first-mile aggregation yard and certified pre-cleaning facility at Gooty on the NH-44 corridor, directly linking 5,000+ dryland farmers across 24 villages to institutional buyers.

WHY SOURCING GRAINS THROUGH ONSFC EMPOWERS BITS PILANI MESSES:
1. Guaranteed 5:00 AM Delivery: Our direct night-haul departs Gooty at 11:00 PM via NH-44 and Hyderabad ORR, arriving at your Jawahar Nagar campus loading bay by 4:30 AM before morning chef shifts.
2. 100% Machine De-Stoned & Sortex Graded: Zero stones, zero mud pebbles, and pneumatic air-suction cleaning guarantee zero student foreign-body complaints.
3. Natural Old Crop Sona Masoori (BPT 5204): Aged over 12 months for maximum volumetric yield per kilogram, ensuring lower cost per meal served.
4. Chemical-Free Dals & Tiffin Broken Rice: Pure farm-grade Toor Dal (*Kandi Pappu*) and high-starch broken rice for fluffy idlis and crisp dosas.
5. 15% to 20% Direct Cost Savings vs Local Mandi Wholesalers: Sourced straight from the farm-gate with digital weighbridge certificates.
6. Flexible Institutional Credit: Net-30 billing backed by GST invoices and formal university vendor empanelment.

We would be delighted to courier a complimentary 25 kg testing sack of our aged Sona Masoori Rice and Toor Dal for your culinary team to inspect and cook.

Warm regards,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Expressway Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Priya Foods Central Manufacturing Plant (Ushodaya Enterprises / Ramoji Group)",
        "recipient_title": "Head of Raw Material Procurement & Agricultural Sourcing",
        "to_email": "sourcing@priyafoods.com",
        "subject": "Bulk Farm-Gate Sun-Dried Red Chilies & Unpolished Pulses Supply for Priya Foods Ramoji Film City Plant",
        "crop_focus": "Sun-Dried Whole Red Chilies, Unpolished Toor Dal, Bengal Gram, Groundnut Oil, Rice",
        "body": """Dear Head of Raw Material Procurement & Agricultural Sourcing,

Producing India's most beloved traditional pickles, spice mixes, and ready-to-eat foods at your flagship Ramoji Film City mega-factory requires agricultural commodities of exceptional color density, natural pungency, and guaranteed farm-gate traceability.

ONSFC Agri Solutions aggregates dry agricultural produce directly from 5,000+ registered dryland farmers across 24 villages of Gooty Mandal and the surrounding Rayalaseema chili-growing belt. We operate a dedicated 1-acre aggregation and grading facility right on the NH-44 expressway corridor.

WHY ONSFC DELIVERS UNFAIR ADVANTAGES FOR PRIYA FOODS INDUSTRIAL SOURCING:
1. Single-Origin Sun-Dried Whole Red Chilies: Harvested directly from Rayalaseema black-soil farms, offering intense natural red color (high ASTA value) and pungent capsaicin bite, completely free from chemical dusting or artificial coloring.
2. Large Multi-Truckload Capacity: Ability to supply 50 to 100 Metric Tonnes per monthly schedule on multi-axle freight carriers directly to your Ramoji Film City unloading godowns.
3. Strict Moisture Control (<8.5%): Prevents aflatoxin and fungal spoilage in bulk storage godowns.
4. High-Purity Unpolished Pulses: Farm-gate Toor Dal and Bengal Gram (*Senagalu*) graded for wet and dry food processing.
5. Direct Highway Linkage: Located right on NH-44, our trucks reach your Hayathnagar plant in 4 hours direct transit.
6. Corporate Master Procurement Contract: Structured quarterly price hedging, digital weighbridge tare slips, and 100% GST compliance.

We would be honored to dispatch a trial 5-tonne testing consignment of our selected whole red chilies and unpolished Toor Dal directly to your plant for laboratory quality and spice extraction testing.

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
            
        print(f"Generated Phase 5 Proposal document: {md_path}")
        
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
            """, (outbox_id, "camp_onsfc_phase5_hyderabad", prospect_id, to_email, subject, body, "pending_review", now, now, now))
            staged_count += 1
            
    conn.commit()
    conn.close()
    print(f"\nSUCCESS: Staged {staged_count} Phase 5 benchmark proposals into Sellbird outbox!")

if __name__ == "__main__":
    main()
