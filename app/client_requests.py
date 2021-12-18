import requests
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Example of parser. ')
    parser.add_argument('--url', type=str, default='http://localhost:5000/', help = 'url of the Flask server')
    parser.add_argument('--dir', type=str, default='resources/images/mnist/mnist_test_0.png', help = 'local directory of your test image')
    args = parser.parse_args()

    url = args.url
    input = {}
    input['dir'] = args.dir

    response = requests.post(url, json=input)
    result = response.json()['label']
    print('The test image is of number: ' + result)
