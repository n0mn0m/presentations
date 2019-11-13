import pyspark.sql.functions as f
from pyspark.sql import SparkSession
from pyspark.sql.types import ArrayType, StringType
from pyspark.ml.feature import Word2Vec

if __name__ == '__main__':

    spark = SparkSession.builder.appName("rdme_to_vec") \
            .config("spark.python.profile", "true") \
            .config("spark.python.profile.dump", "./vec_dump/") \
            .config("spark.rdd.compress", "true") \
            .config("spark.dynamicAllocation.enabled", "true") \
            .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
            .config("spark.kryoserializer", "64") \
            .getOrCreate()

    lndf = spark.read.format("text").load("./SAMPLES/SPARKREADME.md")
    lndf = lndf.select(f.split("value", " ").alias("text"))

    missing = [["MISSING_TOKEN"]]
    mtk_row = spark.createDataFrame(missing, ArrayType(StringType()))

    lndf = lndf.union(mtk_row)
    lndf.write.mode("overwrite").parquet("./data/token.parquet")

    word2Vec = Word2Vec(vectorSize=3, minCount=0, inputCol="text", outputCol="result")
    model = word2Vec.fit(lndf)
    model.write().overwrite().save('./data/word_vectors')

    result = model.transform(lndf)
    for row in result.collect():
        text, vector = row
        print("Text: [%s] => \nVector: %s\n" % (", ".join(text), str(vector)))
