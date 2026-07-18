import pandas as pd
import sqlite3

conn = sqlite3.connect('../cyclistic_tripdata.db')

# Query: Top 10 Stations for Casual Riders
query_casual = """
SELECT 
    start_station_name,
    COUNT(*) AS total_rides
FROM cleaned_tripdata
WHERE member_casual = 'casual' 
  AND start_station_name != 'Unknown Station'
GROUP BY start_station_name
ORDER BY total_rides DESC
LIMIT 10;
"""

# Query: Top 10 Stations for Annual Members
query_member = """
SELECT 
    start_station_name,
    COUNT(*) AS total_rides
FROM cleaned_tripdata
WHERE member_casual = 'member' 
  AND start_station_name != 'Unknown Station'
GROUP BY start_station_name
ORDER BY total_rides DESC
LIMIT 10;
"""

print("--- TOP 10 START STATIONS: CASUAL RIDERS (TOURISTS/LEISURE) ---")
df_casual = pd.read_sql_query(query_casual, conn)
print(df_casual.to_string(index=False))

print("\n--- TOP 10 START STATIONS: ANNUAL MEMBERS (COMMUTERS) ---")
df_member = pd.read_sql_query(query_member, conn)
print(df_member.to_string(index=False))

conn.close()