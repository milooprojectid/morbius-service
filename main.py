from dotenv import load_dotenv
from flask import Flask, jsonify, make_response,request,jsonify
from os import getenv, path
import pickle
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences

load_dotenv(path.join(path.dirname(__file__), '.env'))
app = Flask(__name__)


@app.route('/')
def handler():
    data = 345923
    message = 'masuk'
    return make_response(
        jsonify({
            'message': message,
            'data': data  
        })
    )

@app.route('/morbius',methods = ['POST'])
def getSentiment():
    inputData = request.get_json()
    sentenceData = inputData['sentence']
    model = load_model('/home/alo-tedy/Documents/myProject/just-rest/sentiment_save_file/sentiment.h5')
    tokenizer = pickle.load(open('/home/alo-tedy/Documents/myProject/just-rest/sentiment_save_file/tokenizer.pkl','rb'))
    
    class_label = [1, 0, -1]
    name_class = ['positive', 'neutral', 'negative']
    # sentence = sentenceData.tokenizer.texts_to_sequences([sentenceData])
    try:
        # sentence = 'Apaan sih ini, ga jelas'
        sentence = sentenceData
        print('sentence input')
        sentence = tokenizer.texts_to_sequences([sentence])
        sentence = pad_sequences(sentence, maxlen=100, padding='pre', truncating='pre')
        print('sentence pad')
        result= name_class[int(model.predict_classes(sentence))]
        print('sentence result')
        # result = sentenceData
    except:
        print('it doesnt work somehow')
    
    return jsonify(result)

@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    print (request.is_json)
    content = request.get_json()
    print (content)
    values = str(content.values())
    print(type(content))
    print(type(values))
    strvalue = str(values)
    print(strvalue)
    print(type(strvalue))
    return jsonify(content)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=getenv('APP_PORT'))
