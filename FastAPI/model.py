# Imports
import pandas as pd
import numpy as np
import pickle
from spacy.lang.en import English
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

class TheStash:

    strains = pd.read_csv('./DS_MedCab_Unit4/lemmatized_strains.csv')
    
    KNN = "./DS_MedCab_Unit4/KNN_Model.pkl"
    CNN = "./DS_MedCab_Unit4/CNN_Model.pkl"

    # Loading pickled model from file
    loaded_knn = pickle.load(open(KNN, 'rb'))
    # Loading pickled model from file
    loaded_cnn = pickle.load(open(CNN, 'rb'))

    def predict(self, request_text):
        transformer = TfidfVectorizer(stop_words="english", min_df=0.025, max_df=0.98, ngram_range=(1,3))
        dtm = transformer.fit_transform(self.strains['lemmas'])
        transformed = transformer.transform([request_text])
        dense = transformed.todense()
        recommendations = self.loaded_knn.kneighbors(dense)[1][0]
        output_array = []
        for recommendation in recommendations:
            strain = self.strains.iloc[recommendation]
            output = strain.drop(['Unnamed: 0', 'name', 'ailment', 'all_text', 'lemmas']).to_dict()
            output_array.append(output)
        return output_array

# if __name__ == "__main__":
#     text = "help me i need some stinky sweet indica"
#     pred = predict(text)
#     print(pred)