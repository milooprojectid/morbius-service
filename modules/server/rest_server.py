from flask import Flask, jsonify, make_response,request,jsonify
from os import getenv, path
import modules.sentiment as sentiment

app = Flask(__name__)

@app.route('/',methods = ['POST'])
def handler():
    try:
        body = request.get_json()

        sentence = body['text'] if 'text' in body else ''
        if sentence == '':
            return jsonify({'message': 'text is required'})

        # sentiment process
        model_result, description = sentiment.analyze(sentence)

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
