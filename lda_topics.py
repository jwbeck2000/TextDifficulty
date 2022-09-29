import pandas as pd
import numpy as np
import pickle
from sklearn.decomposition import LatentDirichletAllocation
# import gensim, spacy, logging, warnings
# import gensim.corpora as corpora
# from gensim.utils import lemmatize, simple_preprocess
# from gensim.models import CoherenceModel
# import matplotlib.pyplot as plt
#
# %matplotlib inline
# warnings.filterwarnings("ignore",category=DeprecationWarning)
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

def lda_init(input_file_1):

	X_train = pickle.load(open(input_file_1, "rb"))

	random_seed = 42

	n_topics = 10

    # This will take a couple of minutes to run...

    lda = LatentDirichletAllocation(n_components = n_topics, random_state=random_seed)
    lda.fit(X_train)
    # topic_models = lda.components_

    return lda

def display_topics(model, input_file_2, no_top_words = 8):

    tf_feature_names = pickle.load(open(input_file_2, "rb"))

    topic_dict = {}
    for topic_idx, topic in enumerate(model.components_):
        term_list = [feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]
        topic_dict["topic %d:" % (topic_idx)] = term_list

        # print("topic %d:" % (topic_idx), term_list)
    return topic_dict

if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser()
    parser.add_argument('input_file_1', help='CountVector for the training data (pkl)')
    parser.add_argument('input_file_2', help='Feature names of training data (pkl)')

    parser.add_argument('output_file_1', help='LDA trained model (pkl)')
	parser.add_argument('output_file_2', help='Dict of top words in n_topics (pkl)')
	args = parser.parse_args()

    model = lda_init(input_file_1)
    pickle.dump(model, open(args.output_file_1, "wb"))

    topic_dict = display_topics(lda_init(input_file_1), tf_feature_names)
    pickle.dump(model, open(args.output_file_2, "wb"))
    
