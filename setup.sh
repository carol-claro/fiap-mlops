echo "Create the environment"

echo "Creating docker images for containers"
docker build -t defaultpropensityapi -f parte_01/dockerbuilds/Dockerfile parte_01/docker/
docker build -t customerclusteringapi -f parte_02/dockerbuilds/Dockerfile parte_02/docker/
docker build -t modelmanager -f parte_03/dockerbuilds/Dockerfile parte_03/docker/
docker build -t frontendstreamlit -f parte_04/dockerbuilds/Dockerfile parte_04/docker/

echo "Creating network"
docker network create plat_network

echo "Deploying containers for predictions"
docker run -d --restart always --network plat_network --name defaultpropensityapi defaultpropensityapi
docker run -d --restart always --network plat_network --name customerclusteringapi customerclusteringapi

echo "Updating microservices.json for expose APIs for predicting"
bash ./parte_03/update_config.sh

echo "Config model manager"
docker run -d --restart always --network plat_network -v $(pwd)/parte_03/docker/config:/myServer/config -v $(pwd)/parte_03/docker/log:/myServer/log --name modelmanager modelmanager
