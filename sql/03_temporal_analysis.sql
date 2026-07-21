-- Query 1: Volume by Day of the Week (Identifies weekend vs. weekday trends)
SELECT 
    member_casual,
    day_of_week,
    COUNT(*) AS total_rides
FROM cleaned_tripdata
GROUP BY member_casual, day_of_week
ORDER BY member_casual, day_of_week;

-- Query 2: Volume by Hour of the Day (Identifies commuter spikes)
SELECT 
    member_casual,
    hour_of_day,
    COUNT(*) AS total_rides
FROM cleaned_tripdata
GROUP BY member_casual, hour_of_day
ORDER BY member_casual, hour_of_day;