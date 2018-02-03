package main.scala

import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.ml.classification.LogisticRegression
import org.apache.spark.ml.regression.LinearRegression

object Main extends App {

  //create spark contetxt
  val conf = new SparkConf().setAppName("kaggle").setMaster("local")
  val sc = new SparkContext(conf)

  //connect to database
  val sqlContext = new org.apache.spark.sql.SQLContext(sc)
  val dataframe_mysql = sqlContext.read.format("jdbc").option("url", "jdbc:mysql://localhost:3306/spark_data")
                        .option("driver", "com.mysql.jdbc.Driver").option("user", "spark").option("password", "spark")
                        .option("dbtable","train").load()

  //print cols
  println(dataframe_mysql.columns.mkString("Cols: [",", ","]"))

  //select target and id cols
  //dataframe_mysql.select("id", "target").show()

  //dataframe_mysql.repartition(8) //Only do this if you have a running spark session

  //dataframe_mysql.groupBy("target").count().collect()

  
}
