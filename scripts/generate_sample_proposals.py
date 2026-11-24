#!/usr/bin/env python3
"""
ONSFC Agri Solutions - B2B Sample Proposal Generator & Sellbird Outbox Stager
Generates 4 benchmark tailored B2B outreach proposals across the 4 major crop flows:
1. Sacred Annadhanam (Mantralayam Matha) - Rice, Toor Dal, Groundnut Oil
2. Residential College Mess (Narayana Nannur / Somaladoddi) - Triple Staple Contract
3. Cotton Ginning Mill (Sunil Industry Guntakal) - Direct Kapas Farm-Gate Contract
4. Peanut Processing & Chikki (Anantha Samruddhi) - Graded Groundnut Kernel Contract
"""

import os
import sqlite3
import uuid
import datetime

SELLBIRD_DB = r"C:\Users\rakes\.gemini\antigravity\scratch\sellbird\data\sellbird.db"
PROPOSALS_DIR = r"C:\Users\rakes\.gemini\antigravity\scratch\onsfc-agri-solutions\proposals"
os.makedirs(PROPOSALS_DIR, exist_ok=True)

BENCHMARK_PROPOSALS = [
    {
        "company_name": "Sri Raghavendra Swamy Mutt Central Annadhanam Trust (Mantralayam)",
        "recipient_title": "Administrative Officer (AO) / Central Annadhanam Bhandaram Incharge",
        "to_email": "annadhanam@srsmutt.org",
        "subject": "Pure Farm-Direct Sona Masoori Rice & Toor Dal Supply for Mantralayam Nitya Annadhanam",
        "crop_focus": "Sona Masoori Rice (BPT 5204), Toor Dal, Pure Filtered Groundnut Oil",
        "body": """Respected Administrative Officer & Trustees,

Namaskaram. With the divine blessings of Lord Shiva and the sacred grace of Sri Guru Raghavendra Swamy, we submit this institutional supply presentation from ONSFC Agri Solutions Private Limited.

We deeply revere the holy service conducted at Mantralayam, where 4,000 to 5,000 visiting devotees receive sacred Tirtha Prasada every single day. Serving thousands of pilgrims requires grains of absolute purity, zero adulteration, and stone-free perfection.

ONSFC aggregates dry staples directly from 5,000+ dryland farmers across 24 villages of Gooty Mandal. We operate a dedicated 1-acre pre-cleaning, pneumatic de-stoning, and grading hub along the NH-44 corridor.

OUR COMMITTED SPECIFICATIONS FOR MANTRALAYAM ANNADHANAM:
1. Sona Masoori Rice (BPT 5204 Old Crop): Machine-cleaned, 100% sortexed, zero stones, moisture strictly below 8.5%.
2. Unpolished Toor Dal (Kandi Pappu): Pure farm-grade red gram dal, free from artificial colors or chemical polishing.
3. Cold-Filtered Groundnut Oil: Pure, aromatic cooking oil directly cold-pressed from Rayalaseema peanut harvests.
4. Tamper-Proof 50kg Bagging & Legal Metrology Calibrated Weights.

Because we aggregate directly at the farm gate, we eliminate all intermediate commission agent margins, supplying Mantralayam at 10% below local mandi wholesale rates with dedicated truckload dispatches.

We humbly request an opportunity to deliver a complimentary 25 kg sample bag of our Sona Masoori Rice and Toor Dal for inspection by your Temple Food Committee.

Respectfully yours,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Narayana IIT-JEE Mega Residential Boys Campus (Nannur Toll Plaza)",
        "recipient_title": "Zonal Purchase Manager / Campus DGM",
        "to_email": "procurement.kurnool@narayanagroup.com",
        "subject": "Reliable 5:00 AM Triple-Staple Delivery (Rice + Dal + Oil) for Narayana Nannur Campus Hostels",
        "crop_focus": "Sona Masoori Rice, Toor Dal, Groundnut Cooking Oil",
        "body": """Dear Zonal Purchase Manager,

Managing three daily meals for 1,500+ resident IIT-JEE aspirants at the Narayana Nannur residential township demands an uncompromising food supply chain. A delay in grain delivery or high-moisture rice disrupts student breakfast schedules and inflates kitchen operating expenses.

ONSFC Agri Solutions Private Limited operates a 1-acre first-mile dry aggregation godown at Gooty on the NH-44 expressway, directly supplying large educational campuses across the Rayalaseema corridor.

THE ONSFC TRIPLE-STAPLE GUARANTEE FOR NARAYANA HOSTELS:
1. Guaranteed 5:00 AM Delivery: Our dedicated logistics dispatch departs at 3:30 AM via NH-44, ensuring all sacks are stacked in your kitchen godown before cooking shifts begin.
2. Certified Moisture & Purity: Every batch of Sona Masoori Rice (BPT 5204) and Toor Dal is certified under 8.5% moisture with pneumatic de-stoning (zero stones/mud).
3. 10% Cost Reduction vs Mandi Contractors: By procuring directly from 5,000+ Gooty farmers, we pass 10% direct savings to Narayana without broker markups.
4. Flexible Institutional Billing: Net-15 / Net-30 payment cycles backed by formal GST invoices.

We propose a 1-week quality trial shipment (no long-term commitment) so your hostel catering head can verify our grain fluffiness, yield, and morning delivery punctuality.

Best regards,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Mandal (NH-44 Corridor), AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Sunil Industry Cotton Ginning & Pressing",
        "recipient_title": "Managing Partner / Factory Proprietor",
        "to_email": "sunilcotton.gtk@gmail.com",
        "subject": "Direct Farm-Gate Kapas (Raw Seed Cotton) Supply from 24 Gooty Villages",
        "crop_focus": "Kapas (Raw Cotton)",
        "body": """Dear Managing Partner,

As the peak cotton harvest commences, commission agent markups at the mandi yard and unpredictable moisture content compress ginning margins. 

ONSFC Agri Solutions Private Limited directly aggregates raw Kapas from 5,000+ registered farmers across all 24 revenue villages of Gooty Mandal. We supply ginning and pressing mills directly from our 1-acre yard located just 25 km from your Guntakal facility.

WHY SOURCING KAPAS VIA ONSFC BENEFITS SUNIL INDUSTRY:
1. Zero Brokerage & Mandi Surcharge: Sourced straight from village Rythu Bharosa Kendras (RBKs) and farm gates, saving 3-5% in middleman commissions.
2. Low Moisture & High Lint Recovery: We measure moisture on-site with calibrated digital probes to ensure minimal moisture loss and maximum lint turnout per quintal.
3. High-Turnover Volume: Capacity to deliver 20 to 50 Metric Tonnes per multi-axle truckload on scheduled morning dispatches.
4. Certified Digital Weighbridge Receipts: Every delivery is backed by Legal Metrology certified tare and gross weight slips.

We welcome you or your representative to inspect our incoming Kapas arrivals at our Gooty yard or invite a trial 10-tonne dispatch to your Guntakal pressing plant.

Sincerely,
Commercial Procurement Desk
ONSFC Agri Solutions Private Limited
Gooty Hub, Ananthapuramu District, AP
Contact: procurement@onsfcagri.com"""
    },
    {
        "company_name": "Anantha Samruddhi (Rythu Nesham Food Producer Co. Ltd. - RNFPCL)",
        "recipient_title": "Factory Managing Director & Purchase Head",
        "to_email": "procurement@ananthasamruddhi.com",
        "subject": "Machine-Cleaned Graded Groundnut Kernels for Anantha Samruddhi Chikki Processing",
        "crop_focus": "Groundnut Kernels (Bold & Java), Bengal Gram",
        "body": """Dear Factory Managing Director,

Anantha Samruddhi's reputation for premium peanut chikki and peanut butter depends on uniform seed size, zero aflatoxin risk, and rich natural oil content. 

ONSFC Agri Solutions Private Limited aggregates groundnut directly from dryland farmers across Gooty Mandal. In our 1-acre Gooty facility, harvested pods are decorticated, destoned, and sieved into standard seed-count grades (Bold and Java).

OUR PROCUREMENT ADVANTAGE FOR YOUR CHIKKI PLANT:
1. Uniform Seed Calibration: Graded by screen count, ensuring uniform roasting without burnt or under-roasted peanuts.
2. Strict Moisture Testing (<8.5%): Eliminates fungal/aflatoxin risk and maximizes shelf life.
3. Dependable Monthly Off-take: Ability to contract 20 to 50 Metric Tonnes of kernels monthly across Kharif and Rabi harvest seasons.
4. Competitive Factory-Gate Pricing: Direct aggregation delivers 8-10% cost advantage compared to open-market wholesale traders.

We would be glad to courier a 5 kg representative sample bag of our current sorted Bold Groundnut Kernels for your roasting test.

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
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    staged_count = 0
    
    for item in BENCHMARK_PROPOSALS:
        comp_name = item["company_name"]
        subject = item["subject"]
        body = item["body"]
        to_email = item["to_email"]
        
        # Save as Markdown artifact file
        slug = comp_name.split()[0].lower()
        md_path = os.path.join(PROPOSALS_DIR, f"proposal_{slug}.md")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# B2B Proposal: {comp_name}\n\n**Subject:** {subject}\n\n**To:** {to_email}\n\n---\n\n{body}\n")
            
        # Match prospect in Sellbird SQLite DB
        cursor.execute("SELECT id FROM prospects WHERE company = ?", (comp_name,))
        pros_row = cursor.fetchone()
        prospect_id = pros_row[0] if pros_row else f"pros_{uuid.uuid4().hex[:12]}"
        
        # Check if already staged in outbox
        cursor.execute("SELECT id FROM outbox WHERE to_email = ? AND subject = ?", (to_email, subject))
        existing_outbox = cursor.fetchone()
        
        if not existing_outbox:
            outbox_id = f"out_{uuid.uuid4().hex[:12]}"
            cursor.execute("""
            INSERT INTO outbox (id, campaign_id, prospect_id, to_email, subject, body, status, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (outbox_id, "camp_onsfc_pilot", prospect_id, to_email, subject, body, "pending_review", now, now))
            staged_count += 1

    conn.commit()
    conn.close()
    
    print(f"SUCCESS: Staged {staged_count} benchmark institutional proposals in Sellbird Outbox table and saved Markdown files in {PROPOSALS_DIR}!")

if __name__ == "__main__":
    main()
