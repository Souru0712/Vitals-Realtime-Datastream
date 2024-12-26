import random as r

from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, lit, from_json, col
from pyspark.sql.types import StringType
from pyspark.sql.types import StructType, StructField, IntegerType, DoubleType


def create_random_id():
    id = 'UIP'
    for i in range(9):
        id += str(r.randint(0, 9))

    return id


def create_spark():
    try:
        spark = SparkSession.builder \
            .appName("vitals_datastream") \
            .getOrCreate()

        return spark

    except Exception as e:
        print(f"Error creating a SparkSession: {e}")


def create_schema():
    schema = StructType([
        StructField("patient_id", StringType(), True),
        StructField("heart_rate", IntegerType(), True),
        StructField("spo2", IntegerType(), True),
        StructField("systolic", IntegerType(), True),
        StructField("diastolic", IntegerType(), True),

    ])

    return schema


def define_vitals(id: str):
    starting_vitals = {
        "patient_id": id,
        "heart_rate": 80,
        "spo2": 96,
        "systolic": 120,
        "diastolic": 80,
    }

    return starting_vitals


def define_fluctuations():
    fluctuations = {
        "heart_rate": 30,  # ±20 bpm 50-110
        "spo2": 4,  # ±4%  92%-100%
        "systolic": 25,  # ±10 mmHg 95-145
        "diastolic": 15,  # ±15 mmHg 65-95
    }

    return fluctuations


def simulate_vitals(spark: SparkSession, schema: StructType, starting_vitals: dict, fluctuations: dict):
    df = spark.range(1).select(
        lit(starting_vitals["patient_id"]).alias("patient_id"),
        (lit(starting_vitals["heart_rate"]) + rand() * 2 * fluctuations["heart_rate"] - fluctuations[
            "heart_rate"]).cast("int").alias("heart_rate"),
        (lit(starting_vitals["spo2"]) + rand() * 2 * fluctuations["spo2"] - fluctuations["spo2"]).cast("int").alias(
            "spo2"),
        (lit(starting_vitals["systolic"]) + rand() * 2 * fluctuations["systolic"] - fluctuations["systolic"]).cast(
            "int").alias("systolic"),
        (lit(starting_vitals["diastolic"]) + rand() * 2 * fluctuations["diastolic"] - fluctuations["diastolic"]).cast(
            "int").alias("diastolic"),
    )

    return df


def send_messages(updated_df, broker: str, kafka_topic: str):
    kafka_output = updated_df.writeStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", broker) \
        .option("topic", kafka_topic) \
        .option("checkpointLocation", "/tmp/spark_checkpoints") \
        .outputMode("append") \
        .start()

    kafka_output.awaitTermination()


def extract_consumer(spark: SparkSession.builder, kafka_topic: str):
    patient_vitals = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "broker:29092") \
        .option("subscribe", kafka_topic) \
        .option("startingOffsets", "earliest") \
        .load()

    return patient_vitals


def send_alarms(patient_vitals: extract_consumer, schema: StructType, kafka_topic: str):
    patient_data = patient_vitals.selectExpr("CAST(value AS STRING)") \
        .select(from_json(col("value"), schema).alias("data")) \
        .select("data.*")

    alarms = patient_data.filter(
        (col("heart_rate") < 60) | (col("heart_rate") > 100) |
        (col("spo2") < 95) |
        (col("systolic") < 105) | (col("blood_pressure") > 130) |
        (col("diastolic") < 70) | (col("diastolic") > 90)
    )

    alarms.selectExpr("CAST(patient_id AS STRING) AS key", "to_json(struct(*)) AS value") \
        .writeStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "broker:29092") \
        .option("topic", kafka_topic) \
        .option("checkpointLocation", "/tmp/spark_checkpoints") \
        .outputMode("append") \
        .start() \
        .awaitTermination()
