echo '\n==========================================================='
echo '\n# Building Spark Images'
echo '\n==========================================================='

docker build -t spark-base ./apache-spark-docker/images/spark-base/ --build-arg SPARK_VERSION=2.4.7 --build-arg HADOOP_VERSION=2.7
echo '\n# Building spark-master'
docker build -t spark-master ./apache-spark-docker/images/spark-master/
echo '\n# Building spark-worker'
docker build -t spark-worker ./apache-spark-docker/images/spark-worker/
echo '\n# Building spark-submit'
docker build -t spark-submit ./apache-spark-docker/images/spark-submit/

echo '\n==========================================================='
echo '\n# Building Kafka Images'
echo '\n==========================================================='

docker build -t kafka-base ./apache-kafka-docker/kafka-base/
echo '\n# Building kafka-server'
docker build -t kafak-server ./apache-kafka-docker/kafka-server/
echo '\n# Building kafka-zookeeper'
docker build -t kafka-zookeeper ./apache-kafka-docker/kafka-zookeeper/
