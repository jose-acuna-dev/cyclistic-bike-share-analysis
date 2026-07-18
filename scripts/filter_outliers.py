import sqlite3

conn = sqlite3.connect('../cyclistic_tripdata.db')
cursor = conn.cursor()

# Drop table if it exists
cursor.execute("DROP TABLE IF EXISTS cleaned_tripdata;")

# Create the cleaned table applying the exact Phase 1 IQR boundaries
query = """
CREATE TABLE cleaned_tripdata AS
SELECT *
FROM enriched_tripdata
WHERE ride_length_seconds > 0 
  AND ride_length_seconds <= 2042;
"""

print("Applying IQR boundaries and purging outliers...")
cursor.execute(query)
conn.commit()

# Verify final row count
cursor.execute("SELECT COUNT(*) FROM cleaned_tripdata;")
rows = cursor.fetchone()[0]
print(f"Gate 2 Complete. {rows} valid rows remain in cleaned_tripdata.")

conn.close()