import sqlite3

conn = sqlite3.connect('../cyclistic_tripdata.db')
cursor = conn.cursor()

# Teardown old tables to prevent structural conflicts
cursor.execute("DROP TABLE IF EXISTS cleaned_tripdata;")
cursor.execute("DROP TABLE IF EXISTS enriched_tripdata;")

# Execute Staging (Cleaning) and Enrichment in a single pass
query = """
CREATE TABLE enriched_tripdata AS
SELECT 
    -- 1. Staging: Text Cleaning & Null Handling
    ride_id,
    LOWER(TRIM(rideable_type)) AS rideable_type,
    started_at,
    ended_at,
    COALESCE(start_station_name, 'Unknown Station') AS start_station_name,
    start_station_id,
    COALESCE(end_station_name, 'Unknown Station') AS end_station_name,
    end_station_id,
    start_lat,
    start_lng,
    end_lat,
    end_lng,
    LOWER(TRIM(member_casual)) AS member_casual,
    
    -- 2. Enrichment: Temporal Calculations
    time(strftime('%s', ended_at) - strftime('%s', started_at), 'unixepoch') AS ride_length,
    strftime('%w', started_at) AS day_of_week,
    strftime('%H', started_at) AS hour_of_day,
    (strftime('%s', ended_at) - strftime('%s', started_at)) AS ride_length_seconds
FROM raw_tripdata;
"""

print("Executing strict pipeline: Staging and Enrichment...")
cursor.execute(query)
conn.commit()

# Verify row count
cursor.execute("SELECT COUNT(*) FROM enriched_tripdata;")
rows = cursor.fetchone()[0]
print(f"Staging and Enrichment complete. {rows} rows processed.")

conn.close()