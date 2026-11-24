-- ==============================================================================
-- ONSFC AGRI SOLUTIONS - SUPABASE PERMISSIONS & ACCESS POLICIES
-- Run this in your Supabase SQL Editor to enable public web submissions
-- ==============================================================================

-- 1. Grant schema usage and table privileges to anon and authenticated roles
GRANT USAGE ON SCHEMA public TO anon, authenticated;
GRANT ALL ON ALL TABLES IN SCHEMA public TO anon, authenticated;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO anon, authenticated;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO anon, authenticated;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO anon, authenticated;

-- 2. Enable Row Level Security (RLS) & Policies for Sample Inquiries (Web RFQ)
ALTER TABLE sample_inquiries ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Allow public sample inquiry submissions" ON sample_inquiries;
CREATE POLICY "Allow public sample inquiry submissions" 
ON sample_inquiries 
FOR INSERT 
TO anon, authenticated 
WITH CHECK (true);

DROP POLICY IF EXISTS "Allow reading sample inquiries" ON sample_inquiries;
CREATE POLICY "Allow reading sample inquiries" 
ON sample_inquiries 
FOR SELECT 
TO anon, authenticated 
USING (true);

-- 3. Public Read Policies for Commodities, Villages, and B2B Buyers Directory
ALTER TABLE commodities ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS "Allow public read commodities" ON commodities;
CREATE POLICY "Allow public read commodities" 
ON commodities 
FOR SELECT 
TO anon, authenticated 
USING (true);

ALTER TABLE gooty_villages ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS "Allow public read villages" ON gooty_villages;
CREATE POLICY "Allow public read villages" 
ON gooty_villages 
FOR SELECT 
TO anon, authenticated 
USING (true);

ALTER TABLE b2b_market_tiers ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS "Allow public read market tiers" ON b2b_market_tiers;
CREATE POLICY "Allow public read market tiers" 
ON b2b_market_tiers 
FOR SELECT 
TO anon, authenticated 
USING (true);

ALTER TABLE b2b_buyers ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS "Allow public read buyers" ON b2b_buyers;
CREATE POLICY "Allow public read buyers" 
ON b2b_buyers 
FOR SELECT 
TO anon, authenticated 
USING (true);
