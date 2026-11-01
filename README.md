# UK Police Crime Lakehouse

## Project ovrview

This project is an end-to-end data lakehouse built on Databricks, using open crime data from the UK police. It follows the same practices and workflows that data engineering teams use day to day.

It covers the whole pipeline: extracting raw data, loading it into the lakehouse, then cleaning, transforming and combining it into structured tables ready for analysis.

The lakehouse follows a **Medallion Architecture** with **Bronze**, **Silver** and **Gold** layers, and uses an **ELT** approach. Along the way it shows key data engineering concepts such as data transformation, data quality, data modelling and scalable pipelines.

The main goal is to build a practical data engineering solution, and to show the skills needed to design and build a reliable data lakehouse.

---
## Project requirements

### Building the data lakehouse

#### Objective
Build a data lakehouse on Databricks using open crime data from the UK police. The aim is to take millions of messy rows spread over thousands of CSV files, and turn them into clean, trustworthy tables that can answer real questions about crime in England, Wales and Northern Ireland.

#### Specifications 
-  **Data Sources** : Bring in data from several sources and formats: police CSV files, a JSON API, and government Excel and CSV files.
-  **Data Quality** : Identify and resolve data quality issues across thousands of files .
-  **Integration** : Combine all sources into a single data model built for analytical queries.
-  **Documentation** : Provide a clear documentation of the data model to support business stekholders and analytical teams.

## About me 
I'm Islam, a data engineer from Morocco, now based in London. I have an engineering degree in Computer Science with a specialisation in Big Data, and a Master's in Business and Data Analytics from Ravensbourne University London.

I focus on building data pipelines, data lakehouses and warehouses, and scalable data solutions, using tools like Python, SQL, PySpark, Databricks and Azure.

