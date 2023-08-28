#!/usr/bin/env python

from random import choice
from configparser import ConfigParser
from confluent_kafka import Producer

cfg_path="./kafka.cfg"

#------------
# Optional per-message delivery callback (triggered by poll() or flush())
# when a message has been successfully delivered or permanently
# failed delivery (after retries).
def delivery_callback(err:str, msg:str) -> None:
    if err:
        print('ERROR: Message failed delivery: {}'.format(err))
    else:
        print("Produced event to topic {topic}: key = {key:12} value = {value:12}".format(
            topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))

#------------
def make_rand_data(n:int=10) -> list[tuple[str,str]]:
    user_ids = ['eabara', 'jsmith', 'sgarcia', 'jbernard', 'htanaka', 'awalther','kstine']
    products = ['book', 'alarm clock', 't-shirts', 'gift card', 'batteries','mothballs']

    rand_purchases = [(choice(user_ids),choice(products)) for _ in range(n)]
    return rand_purchases


#==================
if __name__ == '__main__':
    # Parse the configuration.
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    config_parser = ConfigParser()
    config_parser.read_file(open(cfg_path))
    default_config = dict(config_parser['default'])

    # Create Producer instance
    producer = Producer(default_config)


    topic = config_parser['topic']['topic']
    rand_purchases = make_rand_data(10)
 
    for user,prod in rand_purchases:
        #NOTE: It appears that 'produce' does not actually send the messages
        producer.produce(
            topic=topic,
            value=prod,
            key=user,
            callback=delivery_callback
        )
        
    # Wait for all messages in the Producer queue to be delivered.
    # Flush is a convenience method that calls poll() until len() is zero or the optional timeout elapses.
    # NOTE: poll() (or flush() which wraps it) seems to be REQUIRED for actually sending the messages.
    # When this is removed, no messages appear to be sent, suggesting that 'producer.produce() only stages messages
    # , and poll() actually sends them to Kafka.
    producer.flush(timeout = 120)