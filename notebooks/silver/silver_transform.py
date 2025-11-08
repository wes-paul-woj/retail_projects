from pyspark.sql.functions import *
from utils.validation_rules import validate_silver

df = spark.table("bronze.sales")
df = df.withColumn("clean_price", col("price").cast("double")).filter(col("clean_price").isNotNull())
df = validate_silver(df)
df.write.format("delta").mode("overwrite").saveAsTable("silver.sales_clean")
