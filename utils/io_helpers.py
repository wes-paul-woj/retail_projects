from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

def read_csv_raw(path: str):
    return spark.read.option("header", True).csv(path)
