-- 8-index_my_names.sql
-- index my names

CREATE INDEX idx_name_first ON names (name(1) );
