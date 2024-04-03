from pyspark.sql import SparkSession


def runSpark():
    spark = SparkSession.builder.appName("demo").getOrCreate()

    df = spark.createDataFrame(
    [
        ("sue", 32),
        ("li", 3),
        ("bob", 75),
        ("heo", 13),
    ],
    ["first_name", "age"],
    )

    df.show()

runSpark()