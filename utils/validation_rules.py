from pyspark.sql.functions import col

def validate_bronze(df):
    return df.filter(col("id").isNotNull())

def validate_silver(df):
    return df.filter(col("clean_price") > 0)
