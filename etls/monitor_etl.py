import serial
import json
from kafka import KafkaProducer


def connect_to_monitor(port_number: int, baudrate: int):
    try:
        ser = serial.Serial(
            port=f'COM{port_number}',  # COM port in pc
            baudrate=baudrate,  # monitor's baudrate
            timeout=1  # waits 1 second for data to arrive
        )

        return ser

    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")


def read_monitor_data(ser: serial.Serial):
    try:
        data = ser.readline().decode('utf-8').strip()  #decoding into readable string
        if data:
            return data

    except Exception as e:
        print(f"Error reading from serial: {e}")
        close_serial(ser)

    #     if data:
    #         print(f"Received: {data}")
    # except KeyboardInterrupt:
    #     print("Exiting...")
    # finally:
    #     ser.close()


def close_serial(ser: serial.Serial):
    ser.close()


def create_producer(broker: str):
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    return producer


def send_message(producer: KafkaProducer, topic: str, data: str):
    try:
        producer.send(topic, data)
        producer.flush()

    except Exception as e:
        print(f"Error sending to Kafka: {e}")
        close_producer(producer)


def close_producer(producer: KafkaProducer):
    producer.close()
