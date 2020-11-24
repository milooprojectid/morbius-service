import json
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.preprocessing.text import tokenizer_from_json
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
from numpy import argmax

with open('./models/token','r') as file:
    token = file.read()
    file.close()

TOKENIZER = tokenizer_from_json(token)

MODEL = load_model('./models/sentiment.h5')
CLASS_NAME = ['positive', 'neutral', 'negative']

def analyze(sentence):
    tokenized = TOKENIZER.texts_to_sequences([sentence])
    sequences = pad_sequences(tokenized, maxlen=50, padding='pre', truncating='pre')
    prediction = MODEL.predict(sequences)

    prediction_class = argmax(prediction[0], axis=0)
    description = CLASS_NAME[prediction_class]

    return prediction_class, description

def export_dictonary():
    serialized_data = TOKENIZER.to_json()

    with open('token', 'w') as outfile:
        outfile.write(serialized_data)

def read_dictonary():
    with open('token','r') as file:
        serialized_token = file.read()

    dictonary = json.loads(serialized_token)
    print(dictonary["class_name"])
