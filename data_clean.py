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

def clean(input_file):
    wiki_train_df = pd.read_csv(input_file_1)
    wiki_train_df = wiki_train_df.dropna()
    tokenized_train_items = []
    stop_words=set(stopwords.words('english'))

    for text in tqdm(wiki_train_df.original_text):
        matches=re.findall(r'\w+',text)
        matches = re.findall(r"\D+",text)
        matches=[w for w in matches if not w.lower() in stop_words]
        tokenized_train_items.append(matches)
    #print(tokenized_train_items[:50])
    return pd.DataFrame(tokenized_train_items)

if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('input_file_1', help='Filename to be cleaned')

	parser.add_argument('output_file_1', help='Cleaned output filename')
	args = parser.parse_args()

	# wiki_train_df = pd.read_csv(input_file_1) Moved above - KB
	cleaned_wiki_train_df=clean(args.input_file_1) #changed input from wiki_train_df to input_file_1
	cleaned_wiki_train_df.to_csv(args.output_file_1,index=False) #added 'args' in front of output
