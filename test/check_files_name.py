## Pre-Ingestion: Source File Inspection

"""
Before loading anything, I looked at the raw files in the Databricks Volume to understand their structure. 
Each month folder contains 3 types of CSV (street crimes, outcomes, stop and search). 
They have different schemas, so they must be loaded into separate DataFrames.
"""

base = "/Volumes/police/raw/police_files/police_data"

''' Look at one month per year to check file names stay consistent over time '''

display(dbutils.fs.ls(f"{base}/2023-09/"))
display(dbutils.fs.ls(f"{base}/2024-09/"))
display(dbutils.fs.ls(f"{base}/2025-09/"))
display(dbutils.fs.ls(f"{base}/2026-08/"))


"""
Every month uses the same naming pattern: `*-street.csv`, `*-outcomes.csv` and `*-stop-and-search.csv`.
I use these patterns to read each file type separately.
"""

