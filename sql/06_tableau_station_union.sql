-- Query: Combine Top 10 Stations for Casuals and Members for Tableau Visualization
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