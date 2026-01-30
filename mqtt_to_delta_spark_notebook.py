#!/usr/bin/env python
# coding: utf-8

# ## IoT & DE
# 
# null

# In[ ]:


# The command is not a standard IPython magic command. It is designed for use within Fabric notebooks only.
# %pip install paho-mqtt


# In[ ]:


# ==============================
# ESP32 → HiveMQ → Fabric Spark → Delta
# ==============================

# ---- Imports ----
import json
import threading
from datetime import datetime

import paho.mqtt.client as mqtt
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,
    TimestampType
)

# ---- Spark session ----
spark = SparkSession.builder.getOrCreate()

# ---- MQTT Configuration (HiveMQ Cloud) ----
BROKER = "smallboss-9582bb6a.a03.euc1.aws.hivemq.cloud"
PORT = 8883
TOPIC = "esp32/dht11"
USERNAME = "esp32"
PASSWORD = "PASSWORD"

# ---- Delta Table Name ----
TABLE_NAME = "iot_temperature"

# ---- Schema ----
schema = StructType([
    StructField("deviceId", StringType(), True),
    StructField("temperature", DoubleType(), True),
    StructField("humidity", DoubleType(), True),
    StructField("event_time", TimestampType(), True)
])

# ---- MQTT Message Callback (NEW API - no warnings) ----
def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode("utf-8"))
        payload["event_time"] = datetime.utcnow()

        df = spark.createDataFrame([payload], schema=schema)

        df.write.format("delta").mode("append").saveAsTable("lh_raw.iot_temperature")

        print("Written:", payload)

    except Exception as e:
        print("Error processing message:", e)

# ---- MQTT Client (Callback API v2) ----
client = mqtt.Client(
    protocol=mqtt.MQTTv5,
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()
client.on_message = on_message

client.connect(BROKER, PORT)
client.subscribe(TOPIC)

# ---- Run MQTT loop in background thread ----
def start_mqtt():
    client.loop_forever()

thread = threading.Thread(target=start_mqtt, daemon=True)
thread.start()

print("MQTT listener started. Waiting for ESP32 messages...")


# In[ ]:


df = spark.sql("SELECT * FROM lh_raw.iot_temperature LIMIT 1000")
display(df.count())

