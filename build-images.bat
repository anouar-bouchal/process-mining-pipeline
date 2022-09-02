@echo off
echo     ===========================================================
echo:
echo               # Building Spark Images
echo:
echo     ===========================================================
echo:

docker build -t spark-base ./spark/images/spark-base/
echo    ## Building spark-master
echo:
docker build -t spark-master ./spark/images/spark-master/
echo    ## Building spark-worker
echo:
docker build -t spark-worker ./spark/images/spark-worker/

echo:
echo    ===========================================================
echo:
echo               # Building Kafka Images
echo:
echo    ===========================================================
echo:

docker build -t kafka-base ./kafka/kafka-base/
echo    ## Building kafka-server
echo:
docker build -t kafka-server ./kafka/kafka-server/
echo    ## Building kafka-zookeeper
echo:
docker build -t kafka-zookeeper ./kafka/kafka-zookeeper/
