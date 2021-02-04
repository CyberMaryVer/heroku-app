from flask import Flask, request, jsonify, flash, render_template
import numpy as np
import pickle
import json
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images/'
filename = 'finalized_model.sav'
model = pickle.load(open(filename, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict/',methods=['POST'])
def predict_one():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

@app.route('/predictm/',methods=['POST'])
def predict_many():
    data = request.get_json()
    print(data)
    prediction = list(model.predict(data))
    print(prediction)
    return jsonify(prediction)

if __name__ == '__main__':
    # Heroku provides environment variable 'PORT' that should be listened on by Flask
    port = os.environ.get('PORT')

    if port:
        # 'PORT' variable exists - running on Heroku, listen on external IP and on given by Heroku port
        app.run(host='0.0.0.0', port=int(port))
        filename = 'finalized_model.sav'
        model = pickle.load(open(filename, 'rb'))
    else:
        # 'PORT' variable doesn't exist, running not on Heroku, presumabely running locally, run with default
        #   values for Flask (listening only on localhost on default Flask port)
        app.run()
        filename = 'finalized_model.sav'
        model = pickle.load(open(filename, 'rb'))