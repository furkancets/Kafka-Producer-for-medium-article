python3.8 -m venv producerenv

source producerenv/bin/activate

pip install -r requirements-producer.txt

/opt/kafka/bin/kafka-topics.sh --create --bootstrap-server master:9092,node1:9092,node2:9092 --replication-factor 3 --partitions 1 --topic newsapiproducerv1

/opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server master:9092,node1:9092,node2:9092 --topic newsapiproducerv1