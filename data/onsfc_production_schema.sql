-- ==============================================================================
-- ONSFC AGRI SOLUTIONS PRIVATE LIMITED
-- Enterprise Production Database Schema (PostgreSQL / Supabase / Neon Compatible)
-- Consecrated with the Divine Grace of Lord Shiva, Lord Venkateswara Swamy,
-- Lord Murugan, and Lord Nandiswara.
-- ==============================================================================

-- Enable UUID Extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "postgis"; -- For highway corridor geospatial routing

-- -----------------------------------------------------------------------------
-- 1. FIRST-MILE AGGREGATION: GOOTY MANDAL (24 VILLAGES)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS gooty_villages (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    telugu_name VARCHAR(100) NOT NULL,
    distance_from_hub_km NUMERIC(5, 2) NOT NULL,
    active_farming_families INT NOT NULL,
    soil_type VARCHAR(100) NOT NULL,
    primary_crops TEXT[] NOT NULL,
    aggregation_center VARCHAR(150) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS farmers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    farmer_code VARCHAR(30) UNIQUE NOT NULL, -- e.g. 'FARM-GOOTY-0104'
    name VARCHAR(120) NOT NULL,
    village_id INT REFERENCES gooty_villages(id),
    phone VARCHAR(20) UNIQUE NOT NULL,
    bank_account_number VARCHAR(35) NOT NULL,
    bank_ifsc VARCHAR(15) NOT NULL,
    aadhaar_masked VARCHAR(20),
    land_acres NUMERIC(6, 2) NOT NULL,
    soil_type VARCHAR(60),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- -----------------------------------------------------------------------------
-- 2. 100% DRY COMMODITIES & PROCESSING SPECS (ZERO PERISHABLES)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS commodities (
    id VARCHAR(50) PRIMARY KEY, -- e.g. 'sona-masoori-aged'
    name VARCHAR(150) NOT NULL,
    telugu_name VARCHAR(150) NOT NULL,
    category VARCHAR(60) NOT NULL, -- 'Paddy & Rice', 'Pulses & Dals', etc.
    grade VARCHAR(60) NOT NULL,
    aging_months INT DEFAULT 12,
    cooking_expansion_ratio NUMERIC(4, 2) DEFAULT 2.80, -- e.g. 2.80 (1:2.8)
    max_moisture_percentage NUMERIC(4, 2) NOT NULL, -- e.g. 12.00%
    stone_percentage_limit NUMERIC(4, 2) DEFAULT 0.00, -- Guaranteed 0.00%
    packaging_types TEXT[] NOT NULL,
    target_sectors TEXT[] NOT NULL,
    icon VARCHAR(10) DEFAULT '🌾',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- -----------------------------------------------------------------------------
-- 3. 1-ACRE GOOTY PROCESSING HUB: INWARD TICKETS & PNEUMATIC BATCHES
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS inward_grain_tickets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    ticket_number VARCHAR(35) UNIQUE NOT NULL, -- e.g. 'TKT-2026-11-0084'
    farmer_id UUID REFERENCES farmers(id),
    commodity_id VARCHAR(50) REFERENCES commodities(id),
    vehicle_number VARCHAR(25) NOT NULL,
    gross_weight_kg NUMERIC(10, 2) NOT NULL,
    tare_weight_kg NUMERIC(10, 2) NOT NULL,
    net_weight_kg NUMERIC(10, 2) GENERATED ALWAYS AS (gross_weight_kg - tare_weight_kg) STORED,
    moisture_percentage NUMERIC(4, 2) NOT NULL,
    rate_per_quintal NUMERIC(10, 2) NOT NULL,
    total_payable_inr NUMERIC(12, 2) NOT NULL,
    payment_status VARCHAR(25) DEFAULT 'settled', -- 'pending', 'settled', 'processing'
    settlement_reference VARCHAR(50),
    weighbridge_operator VARCHAR(80) DEFAULT 'Gooty Central Weighbridge #1',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS processing_batches (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    batch_code VARCHAR(35) UNIQUE NOT NULL, -- e.g. 'PNEU-SORTEX-2026-B12'
    commodity_id VARCHAR(50) REFERENCES commodities(id),
    raw_input_kg NUMERIC(10, 2) NOT NULL,
    pneumatic_stones_ejected_kg NUMERIC(8, 2) NOT NULL,
    sortex_defect_ejected_kg NUMERIC(8, 2) NOT NULL,
    clean_bagged_output_kg NUMERIC(10, 2) NOT NULL,
    purity_percentage NUMERIC(5, 2) DEFAULT 99.85,
    storage_bay VARCHAR(30) NOT NULL, -- 'Godown Bay A-4'
    certified_destoned BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- -----------------------------------------------------------------------------
-- 4. B2B COMMERCIAL DEMAND: 24 TIERS & 1,040 VERIFIED BUYERS
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS b2b_market_tiers (
    tier_number INT PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    region VARCHAR(120) NOT NULL,
    buyer_count INT NOT NULL,
    distance_km VARCHAR(40) NOT NULL,
    transit_hours VARCHAR(40) NOT NULL,
    highway_corridor VARCHAR(60) NOT NULL,
    dominant_commodities TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS b2b_buyers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    buyer_code VARCHAR(35) UNIQUE NOT NULL, -- e.g. 'BUYER-P24-001'
    business_name VARCHAR(180) NOT NULL,
    tier_number INT REFERENCES b2b_market_tiers(tier_number),
    category VARCHAR(100) NOT NULL,
    town VARCHAR(80) NOT NULL,
    region VARCHAR(80) NOT NULL,
    key_crops_demanded TEXT NOT NULL,
    procurement_profile TEXT NOT NULL,
    address_landmark TEXT NOT NULL,
    contact_channel TEXT NOT NULL,
    credit_days INT DEFAULT 15,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexing for high-speed multi-column search
CREATE INDEX IF NOT EXISTS idx_b2b_buyers_name ON b2b_buyers(business_name);
CREATE INDEX IF NOT EXISTS idx_b2b_buyers_tier ON b2b_buyers(tier_number);
CREATE INDEX IF NOT EXISTS idx_b2b_buyers_category ON b2b_buyers(category);
CREATE INDEX IF NOT EXISTS idx_b2b_buyers_town ON b2b_buyers(town);

-- -----------------------------------------------------------------------------
-- 5. COMMERCIAL ORDERS & E-WAY BILL LOGISTICS
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS commercial_orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    order_number VARCHAR(35) UNIQUE NOT NULL, -- e.g. 'ONSFC-SO-2026-904'
    buyer_id UUID REFERENCES b2b_buyers(id),
    commodity_id VARCHAR(50) REFERENCES commodities(id),
    quantity_metric_tons NUMERIC(8, 2) NOT NULL,
    rate_per_ton_inr NUMERIC(10, 2) NOT NULL,
    total_order_value_inr NUMERIC(12, 2) NOT NULL,
    eway_bill_number VARCHAR(50),
    truck_vehicle_number VARCHAR(25) NOT NULL,
    highway_corridor VARCHAR(50) NOT NULL,
    delivery_status VARCHAR(30) DEFAULT 'dispatched', -- 'processing', 'dispatched', 'delivered'
    dispatched_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    delivered_at TIMESTAMP WITH TIME ZONE
);

-- -----------------------------------------------------------------------------
-- 6. INBOUND RFQ & COMMERCIAL TRIAL LOT REQUESTS (FROM REACT WEB PORTAL)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS sample_inquiries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    institution_name VARCHAR(160) NOT NULL,
    contact_person VARCHAR(120) NOT NULL,
    designation VARCHAR(100),
    corporate_email VARCHAR(120) NOT NULL,
    phone_number VARCHAR(25) NOT NULL,
    target_commodity VARCHAR(120) NOT NULL,
    sample_size_kg INT DEFAULT 50, -- 50 kg test lot
    delivery_city VARCHAR(80) NOT NULL,
    monthly_tonnage_potential VARCHAR(50) DEFAULT '10 to 25 MT',
    kitchen_notes TEXT,
    inquiry_status VARCHAR(30) DEFAULT 'new', -- 'new', 'verified', 'dispatched', 'contract_won'
    source_ip VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_sample_inquiries_email ON sample_inquiries(corporate_email);
CREATE INDEX IF NOT EXISTS idx_sample_inquiries_status ON sample_inquiries(inquiry_status);
