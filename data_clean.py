import gensim
import gzip
import json
import matplotlib.pyplot as plt
import numpy as np
import re
import pandas as pd
from collections import Counter
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from sklearn.dummy import DummyClassifier


wiki_train_df = pd.read_csv('data/WikiLarge_Train.csv')
def clean(input_file):
    input_file = input_file.dropna()
    tokenized_train_items = []
    stop_words=set(stopwords.words('english'))

    for text in tqdm(wiki_train_df.original_text):
        matches=re.findall(r'\w+',text)        
        matches = re.findall(r"\D+",text)
        matches=[w for w in matches if not w.lower() in stop_words]
        tokenized_train_items.append(matches) 
    #print(tokenized_train_items[:50])
    return pd.DataFrame(tokenized_train_items)

cleaned_wiki_train_df=clean(wiki_train_df)
cleaned_wiki_train_df.to_csv('data/cleaned_wiki_train.csv',index=False) 
    
