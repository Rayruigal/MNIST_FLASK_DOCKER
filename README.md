# DL model deployment using Flask and Docker
Deploying a pre-trained Keras model with Flask and Docker.
## Flask:
Here is how to start the Flask service:

python3.8 app/app.py

## Docker:
Alternatively, we can run the service with Docker.
### Build docker image:
docker image build -t image_name:v1 .
### Create container:
docker run -it --name container_name --network host image_name:v1
###


## Call the service:
Two ways to call the service:
### 1. Call with curl:
curl -H "Content-Type: application/json" -X POST -d '{"dir":"resources/images/mnist/mnist_test_0.png"}' http://127.0.0.1:5000/
### 2. Call with python Requests function:
python3.8 app/client_requests.py --url 'http://localhost:5000/' --dir 'resources/images/mnist/mnist_test_0.png'