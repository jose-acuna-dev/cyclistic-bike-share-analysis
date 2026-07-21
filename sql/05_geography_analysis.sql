-- Query 1: Top 10 Start Stations for Casual Riders (Tourists)
SELECT 
    start_station_name,
    COUNT(*) AS total_rides
FROM cleaned_tripdata
WHERE member_casual = 'casual' 
  AND start_station_name != 'Unknown Station'
GROUP BY start_station_name
ORDER BY total_rides DESC
LIMIT 10;

-- Query 2: Top 10 Start Stations for Annual Members (Commuters)
SELECT 
    start_station_name,
    COUNT(*) AS total_rides
FROM cleaned_tripdata
WHERE member_casual = 'member' 
  AND start_station_name != 'Unknown Station'
GROUP BY start_station_name
ORDER BY total_rides DESC
LIMIT 10;