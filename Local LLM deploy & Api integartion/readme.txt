Download Ollma locally
https://ollama.com/
Dockerized Env setup for LLM
https://www.docker.com/

docker type in cli so its runining 

check version
docker --version
docker pull busybox
docker run busybox ls 
docker container ps -a
docker container rm <numof container>

----------------------
ollama docker
https://hub.docker.com/r/ollama/ollama

docker run ollama/ollama


for id/port : 

docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
--------------------------
Now open Webui
https://openwebui.com/
https://docs.openwebui.com/getting-started/
For pull the image web gui
docker pull ghcr.io/open-webui/open-webui:main
run on live this command 
docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main
---------------
go to admin setting & select the model of mini gema 
like gemma:2b
====================
https://fastapi.tiangolo.com/#installation
pip install "fastapi[standard]"
pip freeze >requirement.txt

for run fast api command 
fastapi dev <filename>

==================
integartion of ollama
pip install ollama
pip freeze >requirement.txt