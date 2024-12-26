from etls.monitor_etl import (connect_to_monitor, read_monitor_data,
                              close_serial, create_producer, send_message,
                              close_producer)
from utils.constants import PORT_NUMBER, BAUDRATE, KAFKA_BROKER, VITAL_TOPIC

def monitor_pipeline():


    ser = connect_to_monitor(PORT_NUMBER, BAUDRATE)
    data = read_monitor_data(ser)

    producer = create_producer(KAFKA_BROKER)
    send_message(producer, VITAL_TOPIC, data)


