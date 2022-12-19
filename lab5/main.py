import json

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option") \
    .getOrCreate()
sc = spark.sparkContext
data_file = "data.txt"
df = sc.textFile(data_file, minPartitions=100).map(lambda x: eval(x))


most_len_comment = df.map(lambda x: x['driver_comment']).takeOrdered(10, lambda x: -len(x))
print(most_len_comment)
with open("most_len_comment.json", "w") as f:
    json.dump(most_len_comment, f, indent=4, sort_keys=True)
