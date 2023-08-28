# Kakfa

## Introduction
Kakfa is an open-source event-streaming / event broker service that operates with a pub/sub architecture across various subscribable 'channels'.

https://kafka.apache.org/


## Additional Reading:
- [Confluent Kafka Blog (lots of topics)](https://www.confluent.io/blog/?categories=apache-kafka)
  - [How to optimize Kafka producers for throughput](https://developer.confluent.io/tutorials/optimize-producer-throughput/confluent.html)
  - [Window aggregations with Kafka](https://www.confluent.io/blog/windowing-in-kafka-streams/)
  - [Importance of standardizing partition-selection across clients](https://www.confluent.io/blog/standardized-hashing-across-java-and-non-java-producers/)
  - [Kafka + Python developer guide](https://www.confluent.io/blog/kafka-python-developer-guide/)
  - [Kafka's infrastructure costs](https://www.confluent.io/blog/understanding-and-optimizing-your-kafka-costs-part-1-infrastructure/)


## Open questions:
1. What exactly does 'zookeeper' do?
   1. Zookeeper is being deprecated - in favor of 'KRaft' (integrated service rather than a separate service).
   2. See the 'Zookeeper Ensemble' header here for an overview of Zookeeper: `bi-learning\kafka\kafka_fundamentals_training\notes.md`
2. What do 'groups' in Kafka do?
   1. Consumer groups allow multiple consumers to 'share' topics - so they all consume from the same topics, but being in the same 'group' means that Kafka will split all topic messages between the group members - so there are no duplicated topics.
   2. Read more under the 'Consumer Groups' header here: `bi-learning\kafka\kafka_fundamentals_training\notes.md`
3. What is the right level of replication for a Kafka topic?
   1. A standard value is '3'. Replication protects against data loss by storing the data across multiple (e.g., 3) Kafka brokers.
4. How do partitions work in Kafka?
   1. Partitions are used to split Kafka topics amongst multiple brokers to allow topics to grow without in a scalable way (i.e., in a way where multiple brokers can share consumer and producer requests).
   2. Read more under the 'Partitions' header here: `bi-learning\kafka\kafka_fundamentals_training\notes.md`
5. How can we implement Kafka in a secure way to:
   1. limit access
      1. Kafka has password-based authentication by default. It also supports encryption.
      2. Read more under the 'Security in Kafka' header here: `bi-learning\kafka\kafka_fundamentals_training\notes.md`
   2. enforce schemas for messages in certain topics.