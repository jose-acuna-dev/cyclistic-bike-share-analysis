SELECT 
    member_casual,
    COUNT(*) AS total_rides,
    time(CAST(AVG(ride_length_seconds) AS INTEGER), 'unixepoch') AS avg_ride_length,
    time(MAX(ride_length_seconds), 'unixepoch') AS max_ride_length
FROM cleaned_tripdata
GROUP BY member_casual;