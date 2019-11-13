from operator import add
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    SPARK_MASTER = "local[*]"

    sparkConf = SparkConf().setAll([("spark.cores.max", "4"),
                                    ("spark.executor.memory", "2G"),
                                    ("spark.ui.port", "4041")
                                   ]).setMaster(SPARK_MASTER) \
                                     .setAppName("word_count")

    sc = SparkContext(conf=sparkConf)

    lines = sc.textFile("./data/so-developer-survey-2017/README_2017.txt")

    counts = lines.flatMap(lambda r: [(w.lower(), 1) for w in r.split()]) \
                  .reduceByKey(add)

    output = counts.collect()

    for (word, count) in output:
        print("{0:s}: {1:d}".format(word, count))

    sc.stop()
