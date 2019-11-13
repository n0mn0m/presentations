# Into to PySpark Part 1: Spark Datastructures and manipulation

## Getting Started

To follow along or run the materials in this tutorial you will need to have Spark and PySpark installed locally.

### Setup

You will need to start by having Java installed. At the time of writing you are encouraged to use Java 8 as there are known issues with running Spark and Java 10. To check which version of Java you are running use:

`java -version`

If you are on Linux you can have multiple versions of Java installed and specify the version with:

`$ sudo update-alternatives --config java`

After you have Java installed you will want to download Spark and unpack it to a location executable by your user.

[Spark](https://spark.apache.org/downloads.html)

Once you have Spark unpacked you will want to set `$SPARK_HOME` as well as update `spark-defaults.conf` so that it can load HIVE dependencies for `Spark SQL`.

`export $SPARK_HOME=~/spark-2.3.1-bin-hadoop2.7`

In `/spark-2.3.1-bin-hadoop2.7/conf/spark-defaults.conf` add:

```
spark.sql.hive.metastore.version 1.2.1

spark.sql.hive.metastore.jars maven 
```

### Running the examples

With this done you are ready to install `PySpark`. The `conda.txt` and `requirements.txt` files in this repository have the packages you will need. I suggest installing `PySpark` with Anaconda, but you are welcome to use whichever package manager works best for you.

With PySpark installed you can now either use `spark-submit` to execute `Python` scripts, use the PySpark shell as an interactive repo, or use `Jupyer` as an interactive visual environment for your Spark interactions.

REPL: `pyspark`

Submit:

``spark-submit --master local[1] map_reduce.py``

Jupyer:

Set the following environment variables before calling `pyspark`

```
export PYSPARK_DRIVER_PYTHON=/home/alex/miniconda3/envs/pyspark/bin/jupyter-notebook
export PYSPARK_PYTHON=/home/alex/miniconda3/envs/pyspark/bin/python
```


### Stack Sample
https://1drv.ms/u/s!AiZByDsBsPDTis8_QURzWHsEicGVIw
