from pyspark.sql.functions import *

df = spark.table("silver.sales_clean")
agg_df = df.groupBy("region").agg(
    sum("clean_price").alias("total_revenue"),
    avg("clean_price").alias("avg_price"),
    count("*").alias("num_sales")
)
agg_df.write.format("delta").mode("overwrite").saveAsTable("gold.sales_aggregates")
