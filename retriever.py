import pickle
from pydantic import BaseModel
import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import nltk


nltk.download('stopwords')
stop_words = set(stopwords.words('portuguese'))

class Output(BaseModel):
    title: str
    content: str
    relevance: float

class Retriever:
    def __init__(self, path_csv, path_model):
        self.df = pd.read_csv(path_csv)
        self.df['metadado'] = self.df['content'].apply(lambda x: x.split('\n\n')[0])
        self.df['content'] = self.df['content'].apply(self.preprocess_text)
        self.df['metadata_and_content_clean'] = self.df['metadado'] + '\n\n' + self.df['content']
        try:
            with open(path_model, 'rb') as f_in:
                self.vectorizer = pickle.load(f_in)
            self.X = self.vectorizer.transform(self.df['metadata_and_content_clean'])    
        except:
            self.vectorizer = TfidfVectorizer()
            self.X = self.vectorizer.fit_transform(self.df['metadata_and_content_clean'])
        
    def invoke(self, query, k=3):
        Q = self.vectorizer.transform([query])
        R = self.X.dot(Q.T)
        
        # Get score with np.argsort
        scores = np.array(R.toarray()).flatten()
        idxs = np.argsort(scores)[::-1]
        idxs_and_scores = np.array([[idx, scores[idx]] for idx in idxs])
        
        retrieved = np.array(idxs_and_scores[:k])
        idxs = np.array(retrieved)[:, 0].astype(int)
        output_title = self.df.iloc[idxs][['titles']].values
        output_content = self.df.iloc[idxs][['metadata_and_content_clean']].values
        output_relevance = retrieved[:, 1].reshape(-1, 1)
        output = np.concatenate([output_title, output_content, output_relevance], axis=1)
        return output
    
    def query(self, query, k=3):
        output = self.invoke(query, k)
        output = [Output(title=x[0], content=x[1], relevance=x[2]) for x in output]
        return output
    
    def preprocess_text(self, text):
        text = text.lower()
        text = re.sub(r'\d+', '', text)
        text = re.sub(r'\b\w{1,2}\b', '', text)  
        text = re.sub(r'[^\w\s]', '', text) 
        text = ' '.join(word for word in text.split() if word not in stop_words)
        return text
    
    def save_model(self, filename='tfidf_model.pkl'):
        # Salvar o modelo TF-IDF em um arquivo .pkl
        with open(filename, 'wb') as f_out:
            pickle.dump(self.vectorizer, f_out)