-- Create schemas  

CREATE CATALOG IF NOT EXISTS police;

CREATE SCHEMA IF NOT EXISTS police.raw;
CREATE SCHEMA IF NOT EXISTS police.bronze;
CREATE SCHEMA IF NOT EXISTS police.silver;
CREATE SCHEMA IF NOT EXISTS police.gold;

CREATE VOLUME IF NOT EXISTS police.raw.police_files;
