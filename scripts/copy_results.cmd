@ECHO OFF
cd ../
for /f "tokens=*" %%i in ('docker ps -a -q --filter ancestor^=evolving-graph') do set CONTAINER_ID=%%i
docker cp %CONTAINER_ID%:root/results .