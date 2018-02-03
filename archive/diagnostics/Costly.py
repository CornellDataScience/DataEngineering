from pyspark.sql import DataFrame
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

import numpy as np
import pandas as pd

# from IPython.display import display

import json
from pyspark.sql import SparkSession
spark = SparkSession \
         .builder \
         .master("yarn") \
         .appName("testing") \
         .config("spark.executor.instances", "10") \
         .config("spark.executor.memory","8g") \
         .config("spark.driver.memory","30g") \
         .config("spark.executor.cores",'1') \
         .config("spark.scheduler.mode","FIFO") \
         .config("spark.driver.maxResultSize", "4g") \
         .getOrCreate()

dat = spark.read.json('hdfs://master:9000/user/serverteam_1/FinalFrontier/checkin.json').repartition(150)
print('Finished repartition')
review= spark.read.json('hdfs://master:9000/user/serverteam_1/FinalFrontier/review.json').repartition(150)
print('Finished repartition')
bus = spark.read.json('hdfs://master:9000/user/serverteam_1/FinalFrontier/business.json')
print('Finished repartition')
_yyy = review.join(bus, review.business_id == bus.business_id, 'inner').drop(bus.business_id).drop(bus.stars)
print('Finished simple join')

print("begin remane columns")
review_business = _yyy.withColumnRenamed("stars", "business_avg_stars").withColumnRenamed("attributes", "business_type").withColumnRenamed("review_count", "business_review_count")
print('end review_business creation')
from pyspark import StorageLevel
review_business.persist(StorageLevel.MEMORY_ONLY)
from pyspark.java_gateway import launch_gateway
print("start gateway")
launch_gateway()
import time
start_time = time.time()
print("begin to pandas")
_review_business = review_business.toPandas()
print("--- %s seconds ---" % (time.time() - start_time))

