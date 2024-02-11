-- Creating external table referring to gcs path
CREATE OR REPLACE EXTERNAL TABLE `taxi-rides-ny.nytaxi.fhv_green_tripdata`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://nyc-tl-data/trip data/green_tripdata_2022-*.parquet', 'gs://nyc-tl-data/trip data/yellow_tripdata_2020-*.csv']
);


--Count of records for the 2022 Green Taxi Data
SELECT count(*) FROM `taxi-rides-ny.nytaxi.fhv_green_tripdata`;

--Count the distinct number of PULocationID
SELECT COUNT(DISTINCT(PULocationID)) FROM `taxi-rides-ny.nytaxi.fhv_green_tripdata`;
 

 --Fare_amount of 0
SELECT count(*) FROM  `taxi-rides-ny.nytaxi.fhv_green_tripdata`
WHERE fare_amount = 0;

#### Clusters and Partitions
When creating an optimized table in BigQuery for a query that will always order results by PUlocationID and filter based on lpep_pickup_datetime, consider the following strategies:

Cluster on lpep_pickup_datetime and Partition by PUlocationID:
Clustered tables organize data physically to improve query performance. Clustering on lpep_pickup_datetime ensures that rows with similar pickup dates are stored together. This can speed up queries that filter or sort by this column.
Partitioning by PUlocationID further enhances performance. Partitioning divides the table into smaller segments based on a specific column (in this case, PUlocationID). Queries that filter by PUlocationID will only scan relevant partitions, reducing data processed.
This strategy is effective when your queries frequently filter by lpep_pickup_datetime and order by PUlocationID.
Partition by lpep_pickup_datetime and Cluster on PUlocationID:
Partitioning by lpep_pickup_datetime ensures efficient data organization based on pickup dates. Queries that filter by date will scan only relevant partitions.
Clustering on PUlocationID groups rows with similar location IDs together. Queries that order by PUlocationID benefit from this arrangement.
Use this strategy if your queries primarily filter by date and order by location ID.
Avoid combining both partitioning and clustering:
While it’s technically possible to use both partitioning and clustering, it may not provide significant benefits. Choose one strategy based on your query patterns.
Combining both might lead to unnecessary complexity and increased storage costs.
In summary, consider either clustering on lpep_pickup_datetime and partitioning by PUlocationID or partitioning by lpep_pickup_datetime and clustering on PUlocationID, depending on your specific query requirements. Regularly monitor query performance and adjust your table design as needed to optimize for your workload


