echo '\n==========================================================='
echo -e '\e[34m\n\t # Building Spark Images\e[0m'
echo '\n==========================================================='

docker build -t spark-base ./spark/images/spark-base/
echo -e '\e[32m\n# Building spark-master\e[0m'
docker build -t spark-master ./spark/images/spark-master/
echo -e '\e[32m\n# Building spark-worker\e[0m'
docker build -t spark-worker ./spark/images/spark-worker/

echo '\n==========================================================='
echo -e '\e[34m\n\t # Building Kafka Images\e[0m'
echo '\n==========================================================='

docker build -t kafka-base ./kafka/kafka-base/
echo -e '\e[32m\n# Building kafka-server\e[0m'
docker build -t kafak-server ./kafka/kafka-server/
echo -e '\e[32m\n# Building kafka-zookeeper\e[0m'
docker build -t kafka-zookeeper ./kafka/kafka-zookeeper/
