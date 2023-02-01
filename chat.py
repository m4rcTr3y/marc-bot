import json 
import os
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder

import pickle
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

with open("intents.json") as file:
    data = json.load(file)




def chatBot(query):
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)
    max_len = 20
    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([query]),truncating='post', maxlen=max_len),verbose=0)
    tag = lbl_encoder.inverse_transform([np.argmax(result)])
    response = ''
    for i in data['intents']:
            if i['tag'] == tag:
                response =  np.random.choice(i['responses'])
                # print(response)
    return json.dumps({'bot_response':response})
        
