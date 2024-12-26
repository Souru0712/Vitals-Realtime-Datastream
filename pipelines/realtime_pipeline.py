import sys
sys.path.append('/opt/bitnami/spark/utils')
sys.path.append('/opt/bitnami/spark/config')
sys.path.append('/opt/bitnami/spark/etls')


from utils.constants import KAFKA_BROKER, VITAL_TOPIC
from etls.realtime_etl import create_random_id, create_spark, define_vitals, define_fluctuations, \
                           simulate_vitals, send_messages, create_schema
def realtime_pipeline():
    id = create_random_id()

    starting_vitals = define_vitals(id)
    fluctuations = define_fluctuations()
    schema = create_schema()

    s_conn = create_spark()

    updated_df = simulate_vitals(s_conn, schema, starting_vitals, fluctuations)

    send_messages(updated_df, KAFKA_BROKER, VITAL_TOPIC)

realtime_pipeline()
