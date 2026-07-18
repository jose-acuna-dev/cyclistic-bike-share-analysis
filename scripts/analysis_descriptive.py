import pandas as pd
import sqlite3

conn = sqlite3.connect('../cyclistic_tripdata.db')

# Query to extract total volume, average duration, and max duration by user type
query = """
SELECT 
    member_casual,
    COUNT(*) AS total_rides,
    time(CAST(AVG(ride_length_seconds) AS INTEGER), 'unixepoch') AS avg_ride_length,
    time(MAX(ride_length_seconds), 'unixepoch') AS max_ride_length
FROM cleaned_tripdata
GROUP BY member_casual;
"""

print("Executing Descriptive Analysis...")
df = pd.read_sql_query(query, conn)

# Print the resulting dataframe to the terminal
print(df.to_string(index=False))

conn.close()