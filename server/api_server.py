#!/usr/bin/env python3
"""
ONSFC Agri Solutions - Enterprise REST API Server
Built with FastAPI & SQLite (PostgreSQL compatible)
Provides live endpoints for React Web Portal, Farmer Inward Slips & B2B Commercial RFQs.
"""

import os
import sqlite3
import uuid
import datetime
from typing import Optional, List
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr

DATA_DIR = r"C:\Users\rakes\.gemini\antigravity\scratch\onsfc-agri-solutions\data"
DB_PATH = os.path.join(DATA_DIR, "onsfc_database.db")

app = FastAPI(
    title="ONSFC Agri Solutions API",
    description="Live REST API for Rayalaseema Farmer First-Mile Aggregation, 1-Acre Gooty Processing Hub & 1,040 B2B Commercial Buyers.",
    version="1.0.0"
)

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# -----------------------------------------------------------------------------
# PYDANTIC SCHEMAS
# -----------------------------------------------------------------------------
class RfqCreate(BaseModel):
    institution_name: str
    contact_person: str
    designation: Optional[str] = "Procurement / Catering Lead"
    corporate_email: str
    phone_number: str
    target_commodity: str
    sample_size_kg: Optional[int] = 50
    delivery_city: str
    monthly_tonnage_potential: Optional[str] = "10 to 25 MT"
    kitchen_notes: Optional[str] = ""

# -----------------------------------------------------------------------------
# API ENDPOINTS
# -----------------------------------------------------------------------------
@app.get("/")
def root():
    return {
        "enterprise": "ONSFC Agri Solutions Private Limited",
        "consecration": "हर हर महादेव, शंभो शंकर! With the Divine Blessings of Lord Shiva, Lord Venkateswara Swamy, Lord Murugan, and Lord Nandiswara.",
        "hub": "1-Acre First-Mile Mechanical Hub, NH-44 Corridor, Gooty Mandal (24 Villages)",
        "mandate": "100% Dry Agricultural Produce & Cash Crops (Zero Perishables)",
        "verified_buyers": 1040,
        "market_tiers": 24,
        "docs_url": "/docs"
    }

@app.get("/api/stats")
def get_stats():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM b2b_buyers")
    total_buyers = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM gooty_villages")
    total_villages = cur.fetchone()[0]

    cur.execute("SELECT SUM(active_farming_families) FROM gooty_villages")
    total_farmers = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM commodities")
    total_commodities = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM b2b_market_tiers")
    total_tiers = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM sample_inquiries")
    total_inquiries = cur.fetchone()[0]
    conn.close()

    return {
        "total_verified_buyers": total_buyers,
        "total_market_tiers": total_tiers,
        "total_gooty_villages": total_villages,
        "active_dryland_farmers": total_farmers,
        "dry_commodities_count": total_commodities,
        "total_sample_inquiries": total_inquiries,
        "hub_capacity": "1 Acre on NH-44 Expressway",
        "destoned_guarantee": "0.00% Stones & Silica",
        "cooked_expansion_yield": "1:2.8 Volumetric Ratio (BPT 5204 Aged Sona Masoori)"
    }

@app.get("/api/commodities")
def get_commodities():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM commodities ORDER BY aging_months DESC, name ASC")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return {"count": len(rows), "commodities": rows}

@app.get("/api/tiers")
def get_tiers():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM b2b_market_tiers ORDER BY tier_number ASC")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return {"count": len(rows), "tiers": rows}

@app.get("/api/villages")
def get_villages():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM gooty_villages ORDER BY distance_from_hub_km ASC")
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return {"count": len(rows), "villages": rows}

@app.get("/api/buyers")
def get_buyers(
    q: Optional[str] = Query(None, description="Search query across name, town, crops, or profile"),
    tier: Optional[int] = Query(None, description="Filter by tier number 1-24"),
    category: Optional[str] = Query(None, description="Filter by category"),
    town: Optional[str] = Query(None, description="Filter by city/town"),
    limit: int = Query(50, ge=1, le=1040),
    offset: int = Query(0, ge=0)
):
    conn = get_db()
    cur = conn.cursor()

    query = "SELECT * FROM b2b_buyers WHERE 1=1"
    params = []

    if tier is not None:
        query += " AND tier_number = ?"
        params.append(tier)
    if category:
        query += " AND category LIKE ?"
        params.append(f"%{category}%")
    if town:
        query += " AND town LIKE ?"
        params.append(f"%{town}%")
    if q:
        query += " AND (business_name LIKE ? OR town LIKE ? OR key_crops_demanded LIKE ? OR procurement_profile LIKE ?)"
        term = f"%{q}%"
        params.extend([term, term, term, term])

    # Count total matching
    count_query = query.replace("SELECT *", "SELECT COUNT(*)")
    cur.execute(count_query, params)
    total_matching = cur.fetchone()[0]

    # Fetch page
    query += " ORDER BY tier_number ASC, business_name ASC LIMIT ? OFFSET ?"
    params.extend([limit, offset])

    cur.execute(query, params)
    buyers = [dict(r) for r in cur.fetchall()]
    conn.close()

    return {
        "total_matching": total_matching,
        "limit": limit,
        "offset": offset,
        "buyers": buyers
    }

@app.post("/api/rfq")
def create_rfq(rfq: RfqCreate):
    conn = get_db()
    cur = conn.cursor()

    inquiry_id = f"rfq_{uuid.uuid4().hex[:12]}"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cur.execute("""
    INSERT INTO sample_inquiries (
        id, institution_name, contact_person, designation, corporate_email,
        phone_number, target_commodity, sample_size_kg, delivery_city,
        monthly_tonnage_potential, kitchen_notes, inquiry_status, created_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'new', ?)
    """, (
        inquiry_id, rfq.institution_name, rfq.contact_person, rfq.designation,
        rfq.corporate_email, rfq.phone_number, rfq.target_commodity,
        rfq.sample_size_kg, rfq.delivery_city, rfq.monthly_tonnage_potential,
        rfq.kitchen_notes, now
    ))

    conn.commit()
    conn.close()

    return {
        "status": "success",
        "inquiry_id": inquiry_id,
        "message": f"Sample inquiry for {rfq.sample_size_kg} kg test lot of '{rfq.target_commodity}' registered successfully for {rfq.institution_name}!",
        "dispatch_hub": "ONSFC Central Hub, NH-44 Expressway, Gooty Mandal, AP",
        "contact_phone": "+91 8558 277100"
    }

@app.get("/api/rfq")
def list_rfqs(limit: int = 20):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM sample_inquiries ORDER BY created_at DESC LIMIT ?", (limit,))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return {"count": len(rows), "inquiries": rows}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
