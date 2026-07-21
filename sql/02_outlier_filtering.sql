CREATE TABLE cleaned_tripdata AS
SELECT *
FROM enriched_tripdata
WHERE ride_length_seconds > 0 
  AND ride_length_seconds <= 2042;