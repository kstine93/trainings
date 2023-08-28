#!/usr/bin/env python

from configparser import ConfigParser
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import KafkaException
from time import sleep

cfg_path="./kafka.cfg"


#------------
def await_kafka_admin(res:dict, message:str="Processed: "):
    for name,future in res.items():
        try:
            #It appears we need to await the future result here before the action can be completed.
            future.result()
            print(f"{message}{name}")
        except KafkaException as e:
            print(f"Action failed: ({message}{name})")
            print(e)


#==================
if __name__ == '__main__':
    # Parse the configuration.
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    config_parser = ConfigParser()
    config_parser.read_file(open(cfg_path))
    default_config = dict(config_parser['default'])

    # Create Producer instance
    kafka_admin = AdminClient(default_config)

    topic_name = config_parser['topic']['topic']

    #Deleting topic:
    delete_res = kafka_admin.delete_topics([topic_name],
                              operation_timeout=1,
                              request_timeout=1
                              )

    await_kafka_admin(delete_res,"Deleted: ")

    print("Sleeping for a few seconds to allow Kafka to complete delete action - is there a better way?")
    sleep(5)
                             
    #Recreating topic:
    new_topic_def = NewTopic(topic=topic_name,
                              num_partitions = 2,
                              replication_factor = 1,
    )
    
    create_res = kafka_admin.create_topics([new_topic_def],
                              operation_timeout=1,
                              request_timeout=1
                              )

    await_kafka_admin(create_res,"Created: ")