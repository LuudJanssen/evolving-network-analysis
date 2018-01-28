@ECHO OFF
cd ../

for /f "tokens=*" %%i in ('docker ps -a -q --filter ancestor^=evolving-graph') do (
    set CONTAINER_ID=%%i
    goto:skip
)

:skip
ECHO Copying from container id: %CONTAINER_ID%
docker cp %CONTAINER_ID%:root/results .
PAUSE