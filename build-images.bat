echo '\n==========================================================='
echo '\n# Building Spark Images'
echo '\n==========================================================='

docker build -t spark-base ./spark/images/spark-base/
echo '\n# Building spark-master'
docker build -t spark-master ./spark/images/spark-master/
echo '\n# Building spark-worker'
docker build -t spark-worker ./spark/images/spark-worker/

echo '\n==========================================================='
echo '\n# Building Kafka Images'
echo '\n==========================================================='

docker build -t kafka-base ./kafka/kafka-base/
echo '\n# Building kafka-server'
docker build -t kafka-server ./kafka/kafka-server/
echo '\n# Building kafka-zookeeper'
docker build -t kafka-zookeeper ./kafka/kafka-zookeeper/
