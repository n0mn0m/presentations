from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.types import ArrayType
from pyspark.sql.functions import broadcast, udf
from pyspark.ml.feature import Word2Vec, Word2VecModel
from pyspark.ml.linalg import Vector, VectorUDT

if __name__ == '__main__':

    spark = SparkSession.builder.appName("token_to_vec") \
            .config("spark.python.profile", "true") \
            .config("spark.python.profile.dump", "./main_dump/") \
            .config("spark.rdd.compress", "true") \
            .config("spark.dynamicAllocation.enabled", "true") \
            .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
            .config("spark.kryoserializer", "64") \
            .getOrCreate()

    lines_df = spark.read.parquet("./data/token.parquet")

    vecs = Word2VecModel.load('./data/word_vectors')
    vecs_df = vecs.getVectors()
    vecs_dict = vecs_df.collect()

    vec_dict = spark.sparkContext.broadcast({wv[0]: wv[1] for wv in vecs_dict})
    missing_vec = spark.sparkContext.broadcast(vec_dict.value['MISSING_TOKEN'])

    token_to_vec = udf(lambda r: [vec_dict.value.get(w, missing_vec.value) for w in r], ArrayType(VectorUDT()))

    tdf = lines_df.withColumn("ln_vec", token_to_vec("text"))

    tdf.write.mode("overwrite").parquet(path="./data/token_vecs.parquet", mode="overwrite", compression="snappy")

    spark.sparkContext.show_profiles()
    spark.stop()
