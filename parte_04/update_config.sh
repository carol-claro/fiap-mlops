
echo '{                                                     ' >  $(pwd)/parte_04/docker/config/microservices.json
echo '  "model_manager": {                                         ' >> $(pwd)/parte_04/docker/config/microservices.json
echo '    "endpoint": "http://'$(sudo docker inspect modelmanager | python3 -c "import sys, json; print(json.load(sys.stdin)[0]['NetworkSettings']['Networks']
['plat_network']['IPAddress'])")':8080"          ' >> $(pwd)/parte_04/docker/config/microservices.json
echo '  }                                                   ' >> $(pwd)/parte_04/docker/config/microservices.json
echo '}                                                     ' >> $(pwd)/parte_04/docker/config/microservices.json

echo "[PARTE 04] Arquivo de configuração atualizado com sucesso. Veja seu conteúdo: "

cat $(pwd)/parte_04/docker/cossnfig/microservices.json
