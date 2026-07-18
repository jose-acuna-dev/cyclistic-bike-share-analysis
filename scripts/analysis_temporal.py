import pandas as pd
import sqlite3

conn = sqlite3.connect('../cyclistic_tripdata.db')

# Query 1: Volume by Day of the Week
query_dow = """
SELECT 
    member_casual,
    day_of_week,
    COUNT(*) AS total_rides
FROM cleaned_tripdata
GROUP BY member_casual, day_of_week
ORDER BY member_casual, day_of_week;
"""

# Query 2: Volume by Hour of the Day
query_hour = """
SELECT 
    member_casual,
    hour_of_day,
    COUNT(*) AS total_rides
FROM cleaned_tripdata
GROUP BY member_casual, hour_of_day
ORDER BY member_casual, hour_of_day;
"""

print("--- RIDES BY DAY OF WEEK (0=Sun, 1=Mon... 6=Sat) ---")
df_dow = pd.read_sql_query(query_dow, conn)
print(df_dow.to_string(index=False))

print("\n--- RIDES BY HOUR OF DAY (00-23) ---")
df_hour = pd.read_sql_query(query_hour, conn)
print(df_hour.to_string(index=False))

conn.close()