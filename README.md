# DL model deployment using Flask and Docker
Deploying a pre-trained Keras model with Flask and Docker
## Flask:
curl -H "Content-Type: application/json" -X POST -d '{"dir":"resources/images/mnist/mnist_test_0.png"}' http://127.0.0.1:5000/
## Docker:
### build image:
docker image build -t image_name:v1 .
### create container:
docker run -it --name container_name --network host image_name:v1