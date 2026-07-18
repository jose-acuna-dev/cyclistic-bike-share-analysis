import os
import pandas as pd
import sqlite3

# Initialize database connection (creates the file if it does not exist)
conn = sqlite3.connect('../cyclistic_tripdata.db')

# Define the target directory
data_folder = '../01_Raw_Data'

# Loop through directory, read CSVs, and append to SQL table
for file in os.listdir(data_folder):
    if file.endswith('.csv'):
        file_path = os.path.join(data_folder, file)
        print(f"Loading {file}...")
        
        df = pd.read_csv(file_path)
        df.to_sql('raw_tripdata', conn, if_exists='append', index=False)

print("All 12 files loaded into SQLite successfully.")
conn.close()