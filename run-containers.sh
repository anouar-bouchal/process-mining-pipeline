echo '\n==========================================================='
echo -e '\e[34m\n\t # Running Hive\e[0m'
echo '\n==========================================================='
docker-compose --project-directory ./hive up -d

echo '\n==========================================================='
echo -e '\e[34m\n\t # Running Kafka\e[0m'
echo '\n==========================================================='
docker-compose --project-directory ./kafka up -d

echo '\n==========================================================='
echo -e '\e[34m\n\t # Running Spark\e[0m'
echo '\n==========================================================='
docker-compose --project-directory ./spark up -d

echo '\n==========================================================='
echo -e '\e[34m\n\t # Running Consumer\e[0m'
echo '\n==========================================================='
docker-compose --project-directory ./consumer up -d

echo '\n==========================================================='
echo -e '\e[34m\n\t # Running Producer\e[0m'
echo '\n==========================================================='
docker-compose --project-directory ./producer up -d