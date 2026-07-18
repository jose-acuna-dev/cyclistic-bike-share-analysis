import pandas as pd
import sqlite3

conn = sqlite3.connect('../cyclistic_tripdata.db')
print("Extracting summary tables for Tableau...")

# 1. Volume and Duration
df_volume = pd.read_sql_query("""
SELECT member_casual, COUNT(*) AS total_rides, AVG(ride_length_seconds) / 60.0 AS avg_ride_minutes
FROM cleaned_tripdata GROUP BY member_casual;
""", conn)
df_volume.to_csv('../data/summary_volume.csv', index=False)

# 2. Day of Week
df_dow = pd.read_sql_query("""
SELECT member_casual, day_of_week, COUNT(*) AS total_rides
FROM cleaned_tripdata GROUP BY member_casual, day_of_week;
""", conn)
df_dow.to_csv('../data/summary_day_of_week.csv', index=False)

# 3. Hour of Day
df_hour = pd.read_sql_query("""
SELECT member_casual, hour_of_day, COUNT(*) AS total_rides
FROM cleaned_tripdata GROUP BY member_casual, hour_of_day;
""", conn)
df_hour.to_csv('../data/summary_hour_of_day.csv', index=False)

# 4. Top Stations (Top 10 for each group)
df_stations = pd.read_sql_query("""
SELECT * FROM (
    SELECT start_station_name, member_casual, COUNT(*) AS total_rides
    FROM cleaned_tripdata 
    WHERE start_station_name != 'Unknown Station' AND member_casual = 'casual'
    GROUP BY start_station_name
    ORDER BY total_rides DESC LIMIT 10
)
UNION ALL
SELECT * FROM (
    SELECT start_station_name, member_casual, COUNT(*) AS total_rides
    FROM cleaned_tripdata 
    WHERE start_station_name != 'Unknown Station' AND member_casual = 'member'
    GROUP BY start_station_name
    ORDER BY total_rides DESC LIMIT 10
);
""", conn)
df_stations.to_csv('../data/summary_stations.csv', index=False)

print("Export complete. 4 CSV files generated successfully.")
conn.close()