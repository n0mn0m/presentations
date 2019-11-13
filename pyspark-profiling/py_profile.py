from pyspark.sql import SparkSession

if __name__ == '__main__':

    spark = SparkSession.builder.appName("profiler_test") \
            .config("spark.python.profile", "true") \
            .config("spark.python.profile.dump", "./test_dump/") \
            .config("spark.rdd.compress", "true") \
            .config("spark.dynamicAllocation.enabled", "true") \
            .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
            .config("spark.kryoserializer", "64") \
            .getOrCreate()

    rdd = spark.sparkContext.parallelize(range(100)).map(str)
    rdd.count()
    spark.sparkContext.show_profiles()
    spark.stop()
