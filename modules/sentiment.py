import pickle
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences

MODEL = load_model('./models/sentiment.h5')
TOKENIZER = pickle.load(open('./models/tokenizer.pkl','rb'))
CLASS_NAME = ['positive', 'neutral', 'negative']

def analyze(sentence):
    tokenized = TOKENIZER.texts_to_sequences([sentence])
    sequences = pad_sequences(tokenized, maxlen=100, padding='pre', truncating='pre')

    model_result = int(MODEL.predict_classes(sequences))
    description = CLASS_NAME[model_result]

    return model_result, description