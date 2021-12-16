
# init a base image (Alpine is small Linux distro)
FROM tensorflow/tensorflow
# define the present working directory
WORKDIR /pythonProject3
# copy the contents into the working dir
ADD . /pythonProject3
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# define the command to start the container
CMD ["python3.8","app/app.py"]

