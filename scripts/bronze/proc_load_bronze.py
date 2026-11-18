"""
Objective: Load the raw CSVs into Delta tables in `police.bronze` 
exactly as they are. No renaming, no type changes, no cleaning. 
All transformations happen in the Silver layer.
"""

base = "/Volumes/police/raw/police_files/police_data"

street_df   = spark.read.option("header", True).csv(f"{base}/*/*-street.csv")
outcomes_df = spark.read.option("header", True).csv(f"{base}/*/*-outcomes.csv")
sas_df      = spark.read.option("header", True).csv(f"{base}/*/*-stop-and-search.csv")

tables = {
    "street": street_df,
    "outcomes": outcomes_df,
    "stop_and_search": sas_df,
}

for table_name, df in tables.items():
    (
        df.writeTo(f"police.bronze.{table_name}")              # target table: catalog.schema.table
        .tableProperty("delta.columnMapping.mode", "name")     
        .createOrReplace()                                     # create it, or replace it if it exists 
    )
    print(f"Done: police.bronze.{table_name}")

"""Result: 3 raw Delta tables were created: `police.bronze.street`, `police.bronze.outcomes` and `police.bronze.stop_and_search`."""
