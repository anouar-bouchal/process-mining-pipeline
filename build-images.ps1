Write-Host "`n===========================================================" -ForegroundColor 8
Write-Host "`n`t # Building Spark Images" -ForegroundColor 1
Write-Host "`n===========================================================" -ForegroundColor 8

docker build -t spark-base ./spark/images/spark-base/
Write-Host "`n# Building spark-master" -ForegroundColor 2
docker build -t spark-master ./spark/images/spark-master/
Write-Host "`n# Building spark-worker" -ForegroundColor 2
docker build -t spark-worker ./spark/images/spark-worker/

Write-Host "`n===========================================================" -ForegroundColor 8
Write-Host "`n`t # Building Kafka Images" -ForegroundColor 1
Write-Host "`n===========================================================" -ForegroundColor 8

docker build -t kafka-base ./kafka/kafka-base/
Write-Host "`n# Building kafka-server" -ForegroundColor 2
docker build -t kafka-server ./kafka/kafka-server/
Write-Host "`n# Building kafka-zookeeper" -ForegroundColor 2
docker build -t kafka-zookeeper ./kafka/kafka-zookeeper/

Write-Host "`n===========================================================" -ForegroundColor 8
Write-Host "`n`t # Building Consumer Image" -ForegroundColor 1
Write-Host "`n===========================================================" -ForegroundColor 8
docker build -t consumer ./consumer

Write-Host "`n===========================================================" -ForegroundColor 8
Write-Host "`n`t # Building Producer Image" -ForegroundColor 1
Write-Host "`n===========================================================" -ForegroundColor 8
docker build -t producer ./producer