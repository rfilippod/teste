from pyspark.sql import SparkSession
import findspark

import os
os.environ["JAVA_HOME"] = "C:\Program Files (x86)\Java\jre1.8.0_251\bin"
os.environ["SPARK_HOME"] = "D:\rfili\Documents\spark\spark-3.4.1-bin-hadoop3"

findspark.init("D:\rfili\Documents\spark\spark-3.4.1-bin-hadoop3")

spark = SparkSession.builder.master('local[*]').appName('Iniciando com Spark').config('spark.ui.port', '4050').getOrCreate()
print(spark)
