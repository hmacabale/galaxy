import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import current_timestamp

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'INPUT_PATH', 'OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

df = spark.read.option("header", "true").csv(args['INPUT_PATH'])

df = df.withColumn("processed_timestamp", current_timestamp())

df.write.mode("overwrite").parquet(args['OUTPUT_PATH'])

print("Job completed")
