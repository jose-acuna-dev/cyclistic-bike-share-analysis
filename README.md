# 🚲 Cyclistic Bike-Share: Behavioral Data Analysis

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)

**Live Interactive Dashboard:** https://public.tableau.com/views/CyclisticTripDataSummary/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

![Cyclistic Dashboard Overview](https://raw.githubusercontent.com/jose-acuna-dev/cyclistic-bike-share-analysis/main/cyclistic_dashboard.png)

*Note: The image above is a static preview. Please click the Live Interactive Dashboard link to filter and explore the data.*

---

## 📌 Executive Summary
**Objective:** Analyze 12 months of historical trip data (5.5 million+ records) to identify distinct behavioral patterns between Annual Members and Casual Riders. The insights derived from this analysis are designed to inform a targeted digital marketing strategy aimed at converting high-volume casual riders into profitable annual members.

---

## ⚙️ Data Architecture & Pipeline
This project utilizes a custom, fully automated ETL (Extract, Transform, Load) pipeline to handle millions of rows locally without memory crashes. 

1. **Extract (`os`, `pandas`):** Python scripts iterate through a raw directory of 12 separate monthly CSV files, extracting trip data.
2. **Transform (`sqlite3`):** Data is pushed into a local SQLite database where SQL queries are used to clean null values, filter geographical outliers, and standardize data types.
3. **Load (`pandas`):** Complex SQL aggregation queries summarize the 5-million-row database into lightweight, actionable metrics (Volume, Geography, Time Trends). These are exported as clean `.csv` files.
4. **Visualize (`Tableau`):** The summarized extracts power a responsive, high-fidelity Tableau dashboard utilizing dynamic cross-filtering.

---

## 📊 Key Insights: The Commuter vs. The Tourist

*   **Volume Distribution:** Annual Members account for the vast majority of overall system utilization, taking roughly double the total amount of rides compared to Casual Users (3.5M vs 1.7M).
*   **Temporal Trends (Time & Day):** 
    *   **Members** exhibit strict commuter behavior. Usage violently spikes on weekdays at exactly 8:00 AM and 5:00 PM.
    *   **Casuals** exhibit leisure behavior. Volume forms a smooth, gradual bell curve peaking in the middle of Saturday and Sunday afternoons.
*   **Geographical Hotspots:** 
    *   **Casuals** exclusively dominate coastal tourist and leisure destinations (e.g., Navy Pier, Shedd Aquarium, DuSable Harbor). 
    *   **Members** predominantly start their rides near major transit hubs and corporate centers (e.g., Clinton St, Canal St, Kingsbury St).

---

## 💡 Strategic Recommendations

Based on the quantitative findings, I recommend the following actionable marketing initiatives:

1. **Geo-Fenced Weekend Campaigns:** Deploy targeted digital advertising exclusively on Saturday and Sunday afternoons, geographically restricted to the Top 5 Casual stations (Navy Pier, Shedd Aquarium, Millennium Park). 
2. **The "Commuter Conversion" Pitch:** Design a specialized ad campaign demonstrating the precise cost savings of an annual membership compared to daily single-ride purchases, deployed at transit-heavy stations like Canal St. during the 5:00 PM rush hour.
3. **Seasonal Leisure Passes:** Introduce a "Summer Weekend Pass" as an intermediary step for casual riders who heavily use the bikes for weekend recreation but are not yet ready to commit to a full annual commuter membership.

---

## 📁 Repository Structure
*   `/scripts`: Contains all Python ETL scripts (`load_raw_data.py`, `enrich_data.py`, `export_tableau.py`, etc.) used to process the 5.5 million records.
*   `/sql`: Contains the raw SQL queries extracted from the Python pipeline, demonstrating staging, mathematical filtering, aggregations, and subqueries.
*   `/data`: Contains the aggregated, lightweight `.csv` summaries that feed the Tableau visualization.
