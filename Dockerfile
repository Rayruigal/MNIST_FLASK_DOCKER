
# init a base image (Alpine is small Linux distro)
FROM python:3.8.10-alpine
# define the present working directory
WORKDIR /MNIST_FLASK_DOCKER
# copy the contents into the working dir
ADD . /MNIST_FLASK_DOCKER
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# define the command to start the container
CMD ["python3.8","app/app.py"]
