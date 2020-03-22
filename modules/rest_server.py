from flask import Flask, jsonify, make_response,request,jsonify
from os import getenv, path

import pickle
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

MODEL = load_model('./models/sentiment.h5')
TOKENIZER = pickle.load(open('./models/tokenizer.pkl','rb'))
CLASS_NAME = ['positive', 'neutral', 'negative']

@app.route('/',methods = ['POST'])
def handler():
    try:
        body = request.get_json()

        sentence = body['text'] if 'text' in body else ''
        if sentence == '':
            return jsonify({'message': 'text is required'})

        tokenized = TOKENIZER.texts_to_sequences([sentence])
        sequences = pad_sequences(tokenized, maxlen=100, padding='pre', truncating='pre')

        model_result = int(MODEL.predict_classes(sequences))
        description = CLASS_NAME[model_result]

        return jsonify({
            'message': 'sentiment analysis finished',
            'data': { 'class': model_result, 'description': description, 'text': sentence }
        })
    except:
        return jsonify({ 'message': 'something went wrong '})

class MorbiusRestServer():
    @staticmethod
    def serve():
        app.run(debug=getenv('APP_PORT') == "true", host='0.0.0.0', port=getenv('APP_PORT') or '5001')
