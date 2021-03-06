import tensorflow as tf
import numpy as np
import matplotlib.image as mpimg

from flask import Flask, jsonify, request

app = Flask('mnist')

@app.route('/', methods=['GET', 'POST'])
def infer():
    if (request.method == 'POST'):
        image_dir = request.get_json()
        # image_dir = jsonify({'test image': some_json}), 201
        dir = image_dir['dir']
        label = mnist_infer(dir)
        return jsonify({'label': str(label)})
    else:
        return jsonify({"MNIST":"Recognize hand-written digits!"})

### inference
def mnist_infer(dir):
    # load saved model
    model_load = tf.keras.models.load_model('saved_model/model.h5')
    # get test image
    test = pre_process(dir)
    # inference
    probability = model_load.predict(test.reshape(1,test.shape[0], test.shape[1], 1))
    result = np.argmax(probability)
    return result

### readin test image and pre-process test image into mnist format
def pre_process(dir):
    # get test image
    test = mpimg.imread(dir)
    # pre-process into mnist format
    # test = test[:,:,1]
    return test


if __name__ == '__main__':
    app.run(debug=True)