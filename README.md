# DL model deployment using Flask and Docker
Deploying a pre-trained Keras model with Flask and Docker
## Flask:
curl -H "Content-Type: application/json" -X POST -d '{"dir":"resources/images/test.png"}' http://127.0.0.1:5000/
## Docker:
### build image:
docker image build -t "image_name:vx" .
### create container:
docker run -it --name "container_name"" --network "image_name:vx"