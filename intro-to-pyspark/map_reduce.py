import numbers
from operator import add
from pyspark.sql import SparkSession


if __name__ == "__main__":
    spark = SparkSession\
            .builder\
            .appName("so-country-count")\
            .getOrCreate()

    lines = spark.read.csv('./data/so-developer-survey-2017/survey_results_public.csv',
                               sep=',',
                               escape='"',
                               header=True,
                               inferSchema=True,
                               multiLine=True).rdd

    count = lines.map(lambda x: {x[3], 1}).reduceByKey(add)
    clean = count.filter(lambda x: isinstance(x[1], numbers.Number))
    output = clean.collect()

    for (country, count) in output:
            print("{0:s}: {1:d}".format(country, count))

    spark.stop()
