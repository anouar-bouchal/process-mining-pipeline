Write-Host "`n===========================================================" -ForegroundColor 8
Write-Host "`n`t # Running Hive" -ForegroundColor 1
Write-Host "`n===========================================================" -ForegroundColor 8
docker-compose --project-directory ./hive up -d

Write-Host "`n===========================================================" -ForegroundColor 8
Write-Host "`n`t # Running Kafka" -ForegroundColor 1
Write-Host "`n===========================================================" -ForegroundColor 8
docker-compose --project-directory ./kafka up -d

Write-Host "`n===========================================================" -ForegroundColor 8
Write-Host "`n`t # Running Spark" -ForegroundColor 1
Write-Host "`n===========================================================" -ForegroundColor 8
docker-compose --project-directory ./spark up -d

Write-Host "`n===========================================================" -ForegroundColor 8
Write-Host "`n`t # Running Consumer" -ForegroundColor 1
Write-Host "`n===========================================================" -ForegroundColor 8
docker-compose --project-directory ./consumer up -d

Write-Host "`n===========================================================" -ForegroundColor 8
Write-Host "`n`t # Running Producer" -ForegroundColor 1
Write-Host "`n===========================================================" -ForegroundColor 8
docker-compose --project-directory ./producer up -d