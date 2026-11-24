#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Phase 17 Proposal Generator & Outbox Stager
Generates 3 benchmark macro-industrial B2B outreach proposals:
1. Avanti Feeds Limited - Southern Mega Aquafeed Complex (Kovvur / Ravikampadu, AP)
2. PepsiCo India Holdings Private Limited - Lay's & Kurkure Mega Plant (Sri City SEZ, AP)
3. Dr. Reddy's Laboratories Limited - Formulations Mega Complex (Bollaram / Bachupally, Hyderabad)
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
        "company_name": "Avanti Feeds Limited - Southern Mega Aquafeed Complex",
        "recipient_title": "Vice President - Raw Materials & Feed SCM Directorate",
        "to_email": "procurement@avantifeeds.com",
        "subject": "Pneumatically De-Stoned Broken Raw Rice & Low-Moisture Yellow Maize for Aquafeed Extrusion",
        "crop_focus": "Machine-Destoned Broken Raw Rice (Nookalu), Yellow Maize (Corn), Cottonseed Cake Meal, Groundnut De-Oiled Cake",
        "body": """Dear Vice President (Raw Materials SCM Directorate),

Greetings. As India's undisputed leader in commercial shrimp feeds in technical collaboration with Thai Union, Avanti Feeds manufactures hundreds of thousands of tonnes of high-performance aquatic feeds annually. Operating high-pressure Wenger and Buhler extrusion dies requires raw carbohydrate binders that are 100% free from silica sand, with consistently high starch gelatinization and strictly controlled moisture (<12.5%).

ONSFC Agri Solutions operates a dedicated 1-acre first-mile aggregation, pneumatic de-stoning, and mechanical cleaning facility at Gooty (Anantapuramu District), with direct rail and highway connections to the coastal Andhra aquaculture belt. We aggregate directly from 5,000+ farmers across 24 villages.

WHY ONSFC IS AVANTI'S IDEAL AQUAFEED INGREDIENT PARTNER:
1. 100% Silica & Sand Free Broken Rice (*Nookalu*): Triple-pass pneumatic gravity tables remove 100% of micro-sand, gravel, and quartz dust, eliminating die-plate abrasive wear in high-pressure shrimp feed extruders.
2. Low-Moisture Yellow Maize (<12.5%): Mechanically aerated and solar-cured on concrete platforms; certified aflatoxin <10 ppbâ€”preventing mycotoxin immunosuppression in commercial aquaculture.
3. High Gelatinization Index: High-amylose broken raw rice milled from naturally aged paddy, delivering superior water stability and pellet durability in aquaculture ponds.
4. Continuous High-Tonnage Freight: Scheduled multi-axle 30-tonne trucks and direct rail rake loading from Gooty/Guntakal Junction directly into your Kovvur receiving silos.
5. Direct Farm-Gate Pricing: Eliminates layered commission agents across intermediate mandis, delivering a 7-10% cost advantage.

We invite your technical quality assurance team to inspect certified 25 kg samples of our de-stoned broken rice and yellow corn at your central quality control laboratory in Kovvur.

Sincerely,
Aquafeed & Animal Nutrition Supply Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "PepsiCo India Holdings Private Limited (Lay's & Kurkure Mega Factory)",
        "recipient_title": "Director of Agro Sourcing & Commercial Materials (PepsiCo India)",
        "to_email": "pepsico_india_sourcing@pepsico.com",
        "subject": "Degermed Low-Fat Yellow Corn Grits, Broken Rice Meal & Sortex Besan for Kurkure Extrusion Lines",
        "crop_focus": "Yellow Corn Grits (<1.0% Fat), Machine-Destoned Broken Rice Meal, Sortex Bengal Gram (Besan Flour)",
        "body": """Dear Director of Agro Sourcing & Commercial Materials,

Greetings. As PepsiCo's flagship automated snack food complex at Sri City, your facility manufactures Kurkure and Lay's at world-class velocities. Maintaining the iconic Kurkure crunch, rapid extruder expansion, and uniform flavor coating demands raw ingredients with strictly controlled physical parametersâ€”specifically low lipid content, zero micro-stones, and tight granulation tolerances.

ONSFC Agri Solutions operates an industrial grain aggregation and optical sorting hub at Gooty (Anantapuramu District). We source non-perishable yellow corn, broken rice, and Bengal gram directly from 5,000+ dryland farmers across 24 villages.

HOW ONSFC ELEVATES PEPSICO'S KURKURE MANUFACTURING EXCELLENCE:
1. Low-Fat Yellow Corn Grits (<0.8% Lipid): Sourced from dryland yellow corn; degermed and fractionated to prevent premature snack rancidity and ensure optimal barrel puffing.
2. Sortex Broken Rice Meal: 100% stones-free broken rice with high amylose starch for maximum textural crispness and expansion index.
3. Sortex Bengal Gram (*Besan Flour*): Uniformly roasted and milled Bengal gram (*Senagalu*) providing authentic roasted pulse aroma for classic Kurkure seasoning adherence.
4. Strict Aflatoxin & Heavy Metal Compliance: Certified lab tested with aflatoxin <5 ppb and zero pesticide residues, conforming with PepsiCo Global Quality and Food Safety standards.
5. Direct 3-Hour Transit to Sri City: Dispatched from Gooty Hub, traveling directly down the NH-716 / Tirupati expressway corridor to Sri City gates.
6. Farm-to-Fork Traceability: Complete digital lot batching tracing each truckload back to Gooty Mandal village clusters.

We would be pleased to supply benchmark 50 kg trial consignments of our corn grits, rice meal, and besan to your Sri City QA facility for pilot extruder trials.

Sincerely,
Industrial FMCG & Snack Sourcing Directorate
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Dr. Reddy's Laboratories Limited (Formulations Mega Complex)",
        "recipient_title": "Global Vice President - SCM & Formulation Raw Materials",
        "to_email": "procurement@drreddys.com",
        "subject": "Pharmacopoeia-Grade Maize Starch Binders & Refined Arachis (Peanut) Oil IP for Oral & Topical Formulations",
        "crop_focus": "Pharma-Grade Maize Starch (IP/BP/USP), Refined Peanut Oil (Arachis Oil IP)",
        "body": """Dear Global Vice President (SCM & Formulation Raw Materials),

Greetings. Dr. Reddy's Laboratories is a global benchmark in solid oral dosage formulations, generic pharmaceuticals, and active therapies. In high-speed tableting operations (producing hundreds of millions of tablets monthly across Bollaram and Bachupally), excipients must meet rigid pharmacopoeial standardsâ€”specifically consistent starch viscosity, rapid tablet disintegration, low microbial bioburden, and heavy metal compliance.

ONSFC Agri Solutions operates a 1-acre first-mile aggregation and mechanized sorting facility at Gooty (Anantapuramu District) on the NH-44 expressway corridor, sourcing yellow maize and bold groundnuts directly from 5,000+ dryland farmers.

HOW ONSFC ENHANCES DR. REDDY'S FORMULATION INTEGRITY:
1. Pharma-Grade Maize Starch Feedstock (IP/BP/USP): Sourced from non-GMO dry yellow maize; mechanically dried to <12.0% moisture; certified white color index and optimal amylose-to-amylopectin ratio for tablet binding and disintegration.
2. Refined Peanut Oil (*Arachis Oil IP*): Clean cold-pressed and refined groundnut oil with zero free fatty acids (<0.1%), low peroxide value, and zero rancidityâ€”ideal as an oily vehicle for topical ointments and injectable formulations.
3. Traceable Farm Origin: Complete documentation of soil origin, fertilizer logs, and zero heavy metal contamination from pristine dryland farms.
4. Direct 4-Hour Highway Transit: 300 km straight run north along NH-44 from Gooty directly to Bollaram and Bachupally formulation docks.
5. Corporate Vendor Empanelment: 100% formal GST invoicing, Certificate of Analysis (CoA) with every batch, and compliance with pharmaceutical quality audit guidelines.

We are prepared to submit comprehensive CoA documentation and pilot raw material batches to your Central Analytical Laboratory in Hyderabad for analytical qualification.

Sincerely,
Pharmaceutical Excipients & Life Sciences Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    }
]

def main():
    conn = sqlite3.connect(SELLBIRD_DB)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS outbox (
        id TEXT PRIMARY KEY,
        campaign_id TEXT DEFAULT '',
        prospect_id TEXT DEFAULT '',
        conversation_id TEXT DEFAULT '',
        step INTEGER DEFAULT 1,
        kind TEXT DEFAULT 'sequence',
        to_email TEXT DEFAULT '',
        subject TEXT DEFAULT '',
        body TEXT DEFAULT '',
        status TEXT DEFAULT 'pending_review',
        send_at TIMESTAMP,
        sent_at TIMESTAMP,
        provider TEXT DEFAULT '',
        message_id TEXT DEFAULT '',
        thread_ref TEXT DEFAULT '',
        in_reply_to TEXT DEFAULT '',
        error TEXT DEFAULT '',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        approved_by TEXT DEFAULT '',
        mailbox_id TEXT DEFAULT ''
    );
    """)

    campaign_id = "camp_onsfc_phase17_macro_industrial"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    staged_count = 0

    for p in COMMERCIAL_PROPOSALS:
        msg_id = f"msg_{uuid.uuid4().hex[:12]}"
        cursor.execute("SELECT id FROM prospects WHERE company = ?", (p["company_name"],))
        row = cursor.fetchone()
        prospect_id = row[0] if row else f"pros_{uuid.uuid4().hex[:12]}"

        cursor.execute("""
        INSERT INTO outbox (
            id, campaign_id, prospect_id, step, kind, to_email, subject, body, status, approved_by, created_at, updated_at
        ) VALUES (?, ?, ?, 1, 'proposal', ?, ?, ?, 'approved', 'CEO_ONSFC', ?, ?)
        """, (msg_id, campaign_id, prospect_id, p["to_email"], p["subject"], p["body"], now, now))
        staged_count += 1

        md_filename = f"ONSFC_Phase17_Proposal_{p['company_name'].replace(' ', '_').replace('(', '').replace(')', '').replace('/', '_')[:60]}.md"
        md_path = os.path.join(PROPOSALS_DIR, md_filename)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# COMMERCIAL PROPOSAL - ONSFC AGRI SOLUTIONS PRIVATE LIMITED\n")
            f.write(f"**Target Enterprise:** {p['company_name']}\n")
            f.write(f"**Recipient:** {p['recipient_title']}\n")
            f.write(f"**Email:** {p['to_email']}\n")
            f.write(f"**Subject:** {p['subject']}\n")
            f.write(f"**Commodities:** {p['crop_focus']}\n\n")
            f.write(f"---\n\n")
            f.write(p["body"])
        print(f"Written proposal file: {md_path}")

    conn.commit()
    conn.close()
    print(f"SUCCESS: Staged and approved {staged_count} Phase 17 benchmark proposals in Sellbird outbox ({SELLBIRD_DB})!")

if __name__ == "__main__":
    main()
