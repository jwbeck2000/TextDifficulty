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
from sklearn.dummy import DummyClassifier

def clean(input_file):
    input_file = input_file.dropna()
    stop_words=set(stopwords.words('english'))
    
    input_file['text_processed'] = (input_file['original_text']
                .apply(lambda x: x.lower())                   #lower text
                .apply(lambda y: re.sub(r'[^\w\s]', '', y) )  #removes special characters
                .apply(lambda n: re.sub(r'[\W+\d+]',' ', n))  #remove non-alpha numeric charcaters
                .apply(lambda z: re.sub(r'\n','', z))         #remove new line
                .apply(lambda i: re.sub(r'\s+',' ', i))       #removes extra whitespace
                .apply(lambda d: re.sub('lrb','',d))          #remove double lrb
                .apply(lambda sd: re.sub('rrb','',sd))        #remove single rrb
                .apply(lambda ss: re.sub('å','',ss))
                .apply(lambda s: [i for i in s.split() if not i in stop_words])   #remove stopwords
                .apply(lambda j: " ".join(j)))                #join all text back together                     
        
    #print(input_file.head(20))
    return input_file


    #KB's data cleaning

    #combined_df = pd.read_csv(input_file_1)

    #combined_df['text_processed'] = \
    #combined_df['original_text'].map(lambda x: re.sub('[,\.!?\-;:]','',x))

    #combined_df['text_processed'] = \
    #combined_df['text_processed'].map(lambda x: x.lower())

    #combined_df['text_processed'] = \
    #combined_df['text_processed'].map(lambda x: re.sub('lrb','',x))

    #combined_df['text_processed'] = \
    #combined_df['text_processed'].map(lambda x: re.sub('rrb','',x))

    #return combined_df


if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('input_file_1', help='Filename to be cleaned')

	parser.add_argument('output_file_1', help='Cleaned output filename')
	args = parser.parse_args()

	# wiki_train_df = pd.read_csv(input_file_1) Moved above - KB
	cleaned_wiki_train_df=clean(args.input_file_1) #changed input from wiki_train_df to input_file_1
	cleaned_wiki_train_df.to_csv(args.output_file_1,index=False) #added 'args' in front of output
