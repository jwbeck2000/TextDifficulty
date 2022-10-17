from nltk import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter, defaultdict
from tqdm import tqdm
import pandas as pd
import numpy as np
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')


def feature_extraction(df):
    avg_aoa_scores = []
    concreteness = []
    percent_dale_chall = []
    word_count = []
    aoa_groups = {'aoa<=5':[],'aoa<=10':[],'aoa<=15':[],'aoa<=20':[],'aoa>20':[]}
    #get tokenized and lemmatized text for each document
    for doc in tqdm(df['text_processed']):
        num_dalechall= 0.0
        lemmas = []
        #tokens = [word.lower() for word in word_tokenize(doc)]
        tokens = word_tokenize(str(doc))
        len_tokens = float(len(tokens))
        word_count.append(len_tokens)

        for token in tokens:
            #get lemmas
            lemma = lemmatizer.lemmatize(token)
            lemmas.append(lemmatizer.lemmatize(token))
            #If token is in Dale Chall add to num_dalechall
            if token in dale_chall_list:
                num_dalechall += 1
        #for each lemma get both: the aoa scores and calc the average, the concreteness scores
        exist_aoas = []
        exist_concretes = []
        for lemma in lemmas:
            if lemma in aoa_dict:
                exist_aoas.append(aoa_dict[lemma][0])
            if lemma in concrete_dict:
                exist_concretes.append(concrete_dict[lemma][0])
        #break aoa into 5 groups in a dictionary
        define_aoa_groups = {'aoa<=5':0,'aoa<=10':0,'aoa<=15':0,'aoa<=20':0,'aoa>20':0}
        if len(exist_aoas) > 0:
            avg_aoa_scores.append(np.mean(exist_aoas))
            #calculate the sub groups
            for aoa in exist_aoas:
                if aoa <= 5:
                    define_aoa_groups['aoa<=5'] +=1
                elif aoa <= 10:
                    define_aoa_groups['aoa<=10'] +=1
                elif aoa > 10 and aoa <= 15:
                    define_aoa_groups['aoa<=15'] +=1
                elif aoa > 15 and aoa <= 20:
                    define_aoa_groups['aoa<=20'] +=1
                else:
                    define_aoa_groups['aoa>20'] +=1
            #using list comprehension to append percentages to each group
            [aoa_groups[key].append(value / len(exist_aoas)) for key, value in define_aoa_groups.items()]
        else:
            #label non words as easy
            avg_aoa_scores.append(0)
            [aoa_groups[key].append(0) for key in define_aoa_groups.keys()]
        if len(exist_concretes) > 0:
            concreteness.append(np.mean(exist_concretes))
        else:
            concreteness.append(0)
        percent_dale_chall.append(num_dalechall / len_tokens)

    return avg_aoa_scores,concreteness,percent_dale_chall,aoa_groups

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='Filename for data extraction')
    parser.add_argument('output_file', help='Output file name')
    args = parser.parse_args()

    #GENERATE FEATURES
    #Age of Acquisition Data
    aoa = pd.read_csv('data/AoA_Words.csv', encoding= 'unicode_escape')
    #drop nans and keep column AoA_Kup_lem
    aoa = aoa[['Word', 'AoA_Kup_lem']].dropna()
    #create a dictionary with Word as the key, [AoA score] as the value
    aoa_dict = dict(zip(aoa.Word, zip(aoa.AoA_Kup_lem.astype(float))))

    #Concreteness
    concreteness = pd.read_csv('data/Concreteness_Ratings.csv')
    concrete_dict = dict(zip(concreteness.Word, zip(concreteness['Conc.M'].astype(float), concreteness.Percent_known.astype(float))))
    #print(list(conc_dict.items())[:10])

    #Dale Chall word list that represents words that 80% of children 5th grade know
    dale_chall_list = pd.read_csv('data/dale_chall.csv').values.flatten().tolist()

    lemmatizer = WordNetLemmatizer()
    wiki_train_df = pd.read_csv(args.file)
    #Extract features and add the corresponding column to clean_combined which is the training data
    combine_aoa,combine_concreteness,combine_dalechall,aoa_groups = feature_extraction(wiki_train_df)
    #Create a column for percents of words in each aoa group
    for aoa_group, percentage in aoa_groups.items():
    	wiki_train_df[aoa_group] = percentage

    wiki_train_df['avg_aoa_score'] = combine_aoa
    wiki_train_df['avg_concreteness'] = combine_concreteness
    wiki_train_df['perc_dale_chall'] = combine_dalechall
    #print(wiki_train_df.head())
    #write it back to the output file
    wiki_train_df.to_csv(args.output_file,index=False)
