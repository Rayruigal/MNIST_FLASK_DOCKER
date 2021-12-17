# init a base image
FROM python:3.8

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv ven -p python3.8
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# define the present working directory
WORKDIR /MNIST_FLASK_DOCKER

# copy the contents into the working dir
ADD . /MNIST_FLASK_DOCKER

# run pip to install the dependencies of the flask app
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt # pip setuptools

## define the command to start the container
CMD ["python","app/app.py"]
