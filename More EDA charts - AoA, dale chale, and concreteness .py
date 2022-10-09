#!/usr/bin/env python
# coding: utf-8

# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import re
import pandas as pd


wiki_train_df = pd.read_csv('outputs/clean_combined.csv')

#for some reason you need to run it twice for the font/chart size parameters to go through
sns.distplot(wiki_train_df['avg_aoa_score'])
sns.set(rc={'figure.figsize':(20,12)})
plt.xlabel('Age of Acquisition', fontsize=16);
plt.ylabel('Density', fontsize=16);
plt.title('Average Age of Acquisition Score', fontsize=20)
plt.show()


# In[4]:


sns.distplot(wiki_train_df['avg_concreteness'])
sns.set(rc={'figure.figsize':(20,12)})
plt.xlabel('Concreteness Score', fontsize=16);
plt.ylabel('Density', fontsize=16);
plt.title('Average Concreteness', fontsize=20)
plt.show()


# In[5]:


sns.distplot(wiki_train_df['perc_dale_chall'])
sns.set(rc={'figure.figsize':(20,12)})
plt.xlabel('Percentage fit', fontsize=16);
plt.ylabel('Density', fontsize=16);
plt.title('Relation to Dale Chall List (%)', fontsize=20)
plt.show()


# In[ ]:




