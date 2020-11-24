import pickle
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
from numpy import argmax

MODEL = load_model('./models/sentiment.h5')
TOKENIZER = pickle.load(open('./models/tokenizer.pkl','rb'))
CLASS_NAME = ['positive', 'neutral', 'negative']

def analyze(sentence):
    tokenized = TOKENIZER.texts_to_sequences([sentence])
    sequences = pad_sequences(tokenized, maxlen=50, padding='pre', truncating='pre')
    
    model_result = argmax(MODEL.predict(sequences)[0], axis=0)
    description = CLASS_NAME[model_result]

    return model_result, description