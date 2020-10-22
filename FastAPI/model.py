# Imports

import pandas as pd
import numpy as np
import pickle
from spacy.lang.en import English
from sklearn.feature_extraction.text import TfidfVectorizer
# from flask import request, jsonify

strains = pd.read_csv('lemmatized_strains.csv')

transformer = TfidfVectorizer(stop_words="english", min_df=0.025, max_df=0.98, ngram_range=(1,3))

KNN = "../DS_MedCab_Unit4/KNN_Model.pkl"
CNN = "../DS_MedCab_Unit4/CNN_Model.pkl"



# Loading pickled model from file
loaded_knn = pickle.load(open(KNN, 'rb'))

# Loading pickled model from file
loaded_cnn = pickle.load(open(CNN, 'rb'))

# Predict function:

def predict(request_text):
    transformed = transformer.transform([request_text])
    dense = transformed.todense()
    recommendations = model.kneighbors(dense)[1][0]
    output_array = []
    for recommendation in recommendations:
        strain = strains.iloc[recommendation]
        output = strain.drop(['Unnamed: 0', 'name', 'ailment', 'all_text', 'lemmas']).to_dict()
        output_array.append(output)
    return output_array

# Predict strain function that uses the predict function within:

def predict_strain():
        text = request.get_json(force=True)
        predictions = predict(text)
        return jsonify(predictions)
    

if __name__ == "__main__":
    pred = predict("help me i need some stinky sweet indica")
    print(pred)