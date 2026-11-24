#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Ingestion Engine for Phase 24 & 1,040-Buyer Consolidation
"""

import os
import csv
import sqlite3
import uuid
import datetime
import re

WORKSPACE_DIR = r"C:\Users\rakes\.gemini\antigravity\scratch\onsfc-agri-solutions\data"
QUAD_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Target_Buyers_Gooty_Guntakal_Anantapur.csv")
KURNOOL_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Kurnool_High_Ticket_Buyers.csv")
PHASE2_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase2_Bengaluru_Hyderabad_Buyers.csv")
PHASE3_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase3_Bengaluru_Institutions.csv")
PHASE4_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase4_Bengaluru_Contract_Buyers.csv")
PHASE5_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase5_Hyderabad_Contract_Buyers.csv")
PHASE6_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase6_Bengaluru_Supermarkets_FoodMfg.csv")
PHASE7_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase7_Hyderabad_Supermarkets_FoodMfg.csv")
PHASE8_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase8_Hyderabad_Film_Production_Buyers.csv")
PHASE9_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase9_Bengaluru_Film_Production_Buyers.csv")
PHASE10_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase10_Hyderabad_Hotels_Restaurants.csv")
PHASE11_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase11_Bengaluru_Hotels_Restaurants.csv")
PHASE12_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase12_EXIM_Export_Import_Buyers.csv")
PHASE14_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase14_Sovereign_Divine_Industrial_Buyers.csv")
PHASE15_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase15_Conventions_Prisons_Ethanol_SEZ_Buyers.csv")
PHASE16_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase16_Industrial_Whales_Buyers.csv")
PHASE17_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase17_Aquafeed_Pharma_Textiles_Sovereign_Buyers.csv")
PHASE18_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase18_Deep_Industrial_Whales_Buyers.csv")
PHASE19_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase19_Tirupati_Commercial_Buyers.csv")
PHASE20_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase20_Chennai_Commercial_Buyers.csv")
PHASE21_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase21_Kurnool_Nandyal_Commercial_Buyers.csv")
PHASE22_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase22_Kadapa_Chittoor_Commercial_Buyers.csv")
PHASE23_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase23_Thousand_Summit_Commercial_Buyers.csv")
PHASE24_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Phase24_Bellary_Commercial_Buyers.csv")

CONSOLIDATED_1040_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Master_Consolidated_1040_B2B_Buyers.csv")
CONSOLIDATED_1000_CSV = os.path.join(WORKSPACE_DIR, "ONSFC_Master_Consolidated_1000_B2B_Buyers.csv")

SELLBIRD_DIR = r"C:\Users\rakes\.gemini\antigravity\scratch\sellbird"
SELLBIRD_DB = os.path.join(SELLBIRD_DIR, "data", "sellbird.db")
PROSPECTS_EXPORT_CSV = os.path.join(SELLBIRD_DIR, "prospects.csv")

def load_csv(path):
    rows = []
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                rows.append(r)
    return rows

def main():
    csv_sources = [
        ("Quad", QUAD_CSV),
        ("Kurnool", KURNOOL_CSV),
        ("Phase2", PHASE2_CSV),
        ("Phase3", PHASE3_CSV),
        ("Phase4", PHASE4_CSV),
        ("Phase5", PHASE5_CSV),
        ("Phase6", PHASE6_CSV),
        ("Phase7", PHASE7_CSV),
        ("Phase8", PHASE8_CSV),
        ("Phase9", PHASE9_CSV),
        ("Phase10", PHASE10_CSV),
        ("Phase11", PHASE11_CSV),
        ("Phase12", PHASE12_CSV),
        ("Phase14", PHASE14_CSV),
        ("Phase15", PHASE15_CSV),
        ("Phase16", PHASE16_CSV),
        ("Phase17", PHASE17_CSV),
        ("Phase18", PHASE18_CSV),
        ("Phase19", PHASE19_CSV),
        ("Phase20", PHASE20_CSV),
        ("Phase21", PHASE21_CSV),
        ("Phase22", PHASE22_CSV),
        ("Phase23", PHASE23_CSV),
        ("Phase24", PHASE24_CSV),
    ]

    all_rows = []
    for label, path in csv_sources:
        rows = load_csv(path)
        print(f"Loaded {label}: {len(rows)} buyers from {os.path.basename(path)}")
        all_rows.extend(rows)

    print(f"\n=======================================================")
    print(f"TOTAL MASTER CONSOLIDATED BUYERS: {len(all_rows)} BUYERS!")
    print(f"=======================================================\n")

    # 1. Save Consolidated CSVs
    if all_rows:
        fieldnames = ["Category", "Business Name", "Town", "Region", "Key Crops Demanded", "Procurement Profile", "Address / Landmark", "Contact Channel"]
        for target_path in [CONSOLIDATED_1040_CSV, CONSOLIDATED_1000_CSV]:
            with open(target_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
                writer.writeheader()
                for r in all_rows:
                    writer.writerow(r)
        print(f"Saved master consolidated CSV: {CONSOLIDATED_1040_CSV}")

    # 2. Ingest into Sellbird SQLite DB
    conn = sqlite3.connect(SELLBIRD_DB)
    cursor = conn.cursor()

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    inserted_companies = 0
    inserted_prospects = 0

    for item in all_rows:
        comp_name = item.get("Business Name", "").strip()
        category = item.get("Category", "").strip()
        town = item.get("Town", "").strip()
        region = item.get("Region", "").strip()
        crops = item.get("Key Crops Demanded", "").strip()
        proc_profile = item.get("Procurement Profile", "").strip()
        address = item.get("Address / Landmark", "").strip()
        contact = item.get("Contact Channel", "").strip()

        if not comp_name:
            continue

        location_str = f"{town}, {region}".strip(", ")
        notes_str = f"Target Crops: {crops} | Profile: {proc_profile} | Address: {address}"

        # Check if company exists
        cursor.execute("SELECT id FROM companies WHERE name = ?", (comp_name,))
        comp_row = cursor.fetchone()

        if comp_row:
            company_id = comp_row[0]
        else:
            company_id = f"comp_{uuid.uuid4().hex[:12]}"
            cursor.execute("""
            INSERT INTO companies (id, name, industry, location, description, notes, source, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, 'ONSFC_Consolidated_Audit', ?, ?)
            """, (company_id, comp_name, category, location_str, crops, notes_str, now, now))
            inserted_companies += 1

        # Check if prospect exists by company
        cursor.execute("SELECT id FROM prospects WHERE company = ?", (comp_name,))
        pros_row = cursor.fetchone()

        if not pros_row:
            # Extract real email from contact if present, or synthesize unique email
            email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', contact)
            if email_match:
                email_guess = email_match.group(0).lower()
            else:
                domain_guess = "".join(c for c in comp_name.lower() if c.isalnum())[:15] + ".org"
                email_guess = f"procurement@{domain_guess}"

            cursor.execute("SELECT id FROM prospects WHERE email = ?", (email_guess,))
            if cursor.fetchone():
                email_guess = f"procurement.{uuid.uuid4().hex[:5]}@ballari-trade.com"

            prospect_id = f"pros_{uuid.uuid4().hex[:12]}"
            title_guess = contact if contact else f"Director of Catering / Materials & Facilities"
            first_name = "Commercial"
            last_name = "Lead"

            cursor.execute("""
            INSERT INTO prospects (
                id, company_id, first_name, last_name, email, title, department, company,
                industry, status, personalization_notes, source, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'new', ?, 'ONSFC_Phase24_Bellary_Audit', ?, ?)
            """, (
                prospect_id, company_id, first_name, last_name, email_guess,
                title_guess, "Commercial Sourcing Directorate", comp_name, category,
                f"Requirements: {crops}. Delivery: Direct from Gooty Dry Godown Hub via NH-67 Expressway (75 km, under 1 hr 15 min transit).",
                now, now
            ))
            inserted_prospects += 1

    conn.commit()

    # 3. Export all prospects from SQLite DB to sellbird/prospects.csv
    cursor.execute("""
    SELECT first_name, last_name, email, title, company, industry, department, status, personalization_notes
    FROM prospects
    """)
    db_prospects = cursor.fetchall()
    with open(PROSPECTS_EXPORT_CSV, "w", newline="", encoding="utf-8") as f:
        export_writer = csv.writer(f)
        export_writer.writerow(["first_name", "last_name", "email", "title", "company", "industry", "department", "status", "personalization_notes"])
        for p in db_prospects:
            export_writer.writerow(p)

    conn.close()
    print(f"SUCCESS: Inserted {inserted_companies} new companies and {inserted_prospects} new prospects into Sellbird SQLite database!")
    print(f"Exported {len(db_prospects)} total active prospects to {PROSPECTS_EXPORT_CSV}")

if __name__ == "__main__":
    main()
