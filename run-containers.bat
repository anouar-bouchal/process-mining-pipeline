@echo off
echo     ===========================================================
echo:
echo               # Runing hive
echo:
echo     ===========================================================
echo:
docker-compose --project-directory ./hive up -d

@echo off
echo     ===========================================================
echo:
echo               # Runing Kafka
echo:
echo     ===========================================================
echo:
docker-compose --project-directory ./kafka up -d

@echo off
echo     ===========================================================
echo:
echo               # Runing Spark
echo:
echo     ===========================================================
echo:
docker-compose --project-directory ./spark up -d

@echo off
echo     ===========================================================
echo:
echo               # Runing Consumer
echo:
echo     ===========================================================
echo:
docker-compose --project-directory ./consumer up -d

@echo off
echo     ===========================================================
echo:
echo               # Runing Producer
echo:
echo     ===========================================================
echo:
docker-compose --project-directory ./producer up -d