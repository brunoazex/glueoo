from pyspark.sql import SparkSession
from awsglue.context import GlueContext


class Glue:
    def __init__(
        self,
        spark: SparkSession,
        glue: GlueContext
    ):
        self.spark = spark
        self.glue = glue
