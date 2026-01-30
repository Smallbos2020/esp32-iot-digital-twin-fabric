<img width="1926" height="1078" alt="image" src="https://github.com/user-attachments/assets/8cfe111f-c9df-497a-b4c4-f9678fa330f6" /># esp32-iot-digital-twin-fabric
End-to-end IoT pipeline using ESP32 and DHT22, streaming real-time sensor data via MQTT into Microsoft Fabric Delta Lake for analytics and visualization.


# ESP32 IoT Digital Twin with Microsoft Fabric (Delta Lake)

This repository demonstrates an end-to-end IoT data pipeline that streams real-time sensor data from an **ESP32** device into **Microsoft Fabric Delta Lake** using **MQTT** and **Apache Spark**.  
The solution serves as a practical foundation for **Digital Twin**, **smart building**, and **connected asset** scenarios.

---

## Solution Overview

The project captures temperature and humidity data from a DHT22 sensor connected to an ESP32, publishes the telemetry via MQTT, and ingests the data into Microsoft Fabric for persistent storage and analytics.

---

## Architecture

ESP32 + DHT22 Sensor -> MQTT (JSON payload) -> HiveMQ Cloud (Managed MQTT Broker) -> Python MQTT Client -> Microsoft Fabric Spark Notebook -> Delta Lake Table -> Analytics & Visualization (Fabric / Power BI)


---

## Key Capabilities

- Real-time IoT telemetry ingestion
- MQTT-based device communication
- Secure, cloud-managed MQTT broker (HiveMQ Cloud)
- Spark-based ingestion in Microsoft Fabric
- Persistent storage using Delta Lake
- Scalable foundation for Digital Twin architectures

---

## Technology Stack

### Hardware
- ESP32 Dev Module
- DHT22 Temperature & Humidity Sensor

### Software & Platforms
- Arduino IDE (ESP32 firmware)
- HiveMQ Cloud (MQTT broker)
- Python (paho-mqtt)
- Microsoft Fabric
  - Spark Notebook
  - Delta Lake

---

## Data Flow Description

     ESP32 reads temperature and humidity from the DHT22 sensor
      
     Sensor data is published to an MQTT topic as JSON
      
     HiveMQ Cloud receives and brokers the MQTT messages
      
     A Microsoft Fabric Spark notebook subscribes to the topic
      
     Messages are parsed and written to a Delta Lake table
      
     Data becomes available for analytics and visualization

## Usecases

     Smart building monitoring
      
     HVAC and environmental analytics
      
     Digital Twin telemetry ingestion
      
     Time-series sensor analysis
      
     Foundation for predictive analytics and alerting


## Telemetry Payload Format

ESP32 publishes sensor readings in JSON format:

```json
{
  "deviceId": "esp32-01",
  "temperature": 25.7,
  "humidity": 73.9
}

