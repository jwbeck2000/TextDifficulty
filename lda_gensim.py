# Start writing code here...import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

import gzip
import json
import matplotlib.pyplot as plt
import numpy as np
import re
import pandas as pd
from collections import Counter
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from tqdm import tqdm
from sklearn.dummy import DummyClassifier

import os
from wordcloud import wordcloud
import gensim
from gensim.utils import simple_preprocess
import gensim.corpora as corpora
from pprint import pprint
import pickle
import pyLDAvis

def lda_gensim(input_file_1): #take in combined_cleaned.csv and make list of lists with docs

    def sent_to_words(sents):
    for sent in sents:
        yield(gensim.utils.simple_preprocess(str(sent),deacc = True))

    df = pd.read_csv(input_file_1)
    d_list = df.text_processed.values.tolist()

    data_words = list(sent_to_words(d_list))
    id2word = corpora.Dictionary(data_words)
    texts = data_words
    corpus = [id2word.doc2bow(text) for text in texts]

    num_topics = 10
    lda_model = gensim.models.LdaMulticore(corpus = corpus,id2word = id2word, num_topics = num_topics)
    doc_lda = lda_model[corpus]

    import pyLDAvis.gensim_models

    pyLDAvis.enable_notebook()

    LDAvis_data_filepath = '/work/reults/ldavis_prepared_10.pickle'
    # # this is a bit time consuming - make the if statement True
    # # if you want to execute visualization prep yourself
    if 1 == 1:
        LDAvis_prepared = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word)
        with open(LDAvis_data_filepath, 'wb') as f:
            pickle.dump(LDAvis_prepared, f)
    # load the pre-prepared pyLDAvis data from disk
    with open(LDAvis_data_filepath, 'rb') as f:
        LDAvis_prepared = pickle.load(f)
    pyLDAvis.save_html(LDAvis_prepared, '/work/reults/ldavis_prepared_10.html')
    LDAvis_prepared
