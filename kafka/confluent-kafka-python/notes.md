# Confluent Kafka Code

This directory holds code related to the use of the `confluent-kafka` module in Python - an API for interacting with a Kafka cluster (producing messages, consuming them, manipulating configuration, etc.)

This module was chosen to use here because it is in Python, is currently maintained (as opposed to other modules like `kafka-python`), and has pretty good documentation.

This module could be a good one to use for future BI projects based in Python.


## Getting started:

### 1. Set up a Kafka cluster on Docker:
Confluent has nice [step-by-step introductions on setting up a Kafka cluster on Docker](https://developer.confluent.io/get-started/python/#introduction). The code in this directory is based on this introduction.

You can also use the local `docker-compose.yml` to set up Kafka locally with `docker compose up -d`

---

### 2. Test setup with the shell inside your Kafka Docker container
These steps will familiarize you with the native CLI for Kafka which is accessible from the Kafka container itself.

**SSH into Container**
1. Identify the name of the Docker container with `docker container ls`. You will also see a container for 'zookeeper' which you can ignore.
2. SSH into the kafka container. For a container with the ID `e25c90ab156a`, you would use `docker exec -it e25c90ab156a /bin/bash`. You'll have access to the container's shell.

**Create new Topic**
3. Once you see the shell prompt in the container, create a new Kafka topic with `kafka-topics --create --topic "test-topic" --bootstrap-server localhost:9092`.
   1. You can name the topic anything you want - here it's "test-topic"
4. List topics with `kafka-topics --list --bootstrap-server localhost:9092`. You should see the name of your newly-created topic

**Produce Messages**
5. Activate a prompt to produce messages with `kafka-console-producer --topic "test-topic" --bootstrap-server localhost:9092`. Once the prompt `>` appears, you can enter as many individual messages as you like. Use CTRL+C to escape the prompt. For example:
   
    ```
    > {"name":"majid"}
    > {"name":"kevin"}
    > I can also put a string with spaces too..
    > Maybe there's a way to enforce a message schema?
    > {"job":"data engineer"}
    >
    ```

**Consume Messages**
1. You can now consume the messages you just produced with `kafka-console-consumer --topic="test-topic" --bootstrap-server=localhost:29092 --from-beginning -max-messages 100`. This will pause and await additional messages until you exit with CTRL + C.

---

### 3. Use the confluent-python API
Now that you've used the built-in bash commands to manipulate the basics of Kafka, you can perform them OUTSIDE of the container with an API like confluent's `confluent-kafka` (see the [module documentation here](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#)).

The existing 'kafka_consume.py', 'kafka_produce.py' and 'kafka_recreate_topic.py' should be executable as-is.

Notes:
- The 'requirements.txt' file here shows the non-native modules necessary for the code to work.
- The 'kafka.cfg' file might need to be edited if you set up Kafka using a different port or you want to use a different topic name.