import requests
#import json

url = 'http://127.0.0.1:5000/'
input = {'dir': 'resources/images/mnist/mnist_test_0.png'}

response = requests.post(url, json = input)
result = response.json()['label']
print('The test image is of number: ' + result)