import os
import re
# import from nltk the functions that split a text into sentences and tokens
from nltk.tokenize import sent_tokenize, word_tokenize
from pprint import pprint
import zipfile

import pandas as pd
import numpy as np
from nltk import word_tokenize, pos_tag, chunk
from pprint import pprint
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer

from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)



# The first time using nltk, you should run:
# import nltk
# nltk.download()
# ---- OR ----
# import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('stopwords')



"""
Problems:

Erros na lematização:
    ex.: EE e Java EE não são a mesma coisa (Electrical Engeneering e Java Enterprise Edition);
    ex.: muitas palavras com "/" -> A barra tem que ser " "(espaço)


"""
#Load the entire dataset
data = pd.read_csv('data/ggeop/JobsDataset.csv', header = 0, names = ['Query', 'Job Title', 'Description'])

#Create Job description list
job_descriptions=[]
for job in data.Description:
    j = job.replace(',', '')
    job_descriptions.append(j)



#for i in range(3):
#    print(job_descriptions[i] + "\n")
#    print(word_tokenize(job_descriptions[i]) + ["\n"])
#    print("\n")


#Words tokenization
jobs = [word_tokenize(d) for d in job_descriptions]

#Remove Capitalization
no_capitals =[]
for job in jobs:
    no_capitals.append([j.lower() for j in job])

#Lemmatize
lemmatizer = WordNetLemmatizer()
lem=[]
for job in no_capitals:
    lem.append([lemmatizer.lemmatize(j) for j in job])

#Remove stopwords
filtered_words = []
stopwords_dict = {key : "" for key in stopwords.words('english')}
for job in lem:
    filtered_words.append([j for j in job if not j in stopwords_dict])





#Remove symbols
cleaned_description=[]
extra_dict = {key : "" for key in ['(',')','.',',',':','%']}
for job in filtered_words:
    cleaned_description.append([j for j in job if not j in extra_dict])


from collections import Counter

count = Counter(x for xs in cleaned_description for x in set(xs))
ordered_count_list = count.most_common()

with open('data/ggeop/counter.txt', 'w') as f:
    for item in ordered_count_list:
        f.write(f'{item[0]} : {item[1]}\n')

max_size = len(max(cleaned_description, key=len))

#Create model
#model = Word2Vec(cleaned_description , size=100, window=5, min_count=1, workers=4)
# There was this error: TypeError: __init__() got an unexpected keyword argument 'size'
# Assumo size is now vector_size....

#Mudeio window_size para englobar a oferta toda - Funciona muito melhor!!!
model = Word2Vec(cleaned_description , vector_size=100, window=max_size, min_count=5, workers=4)
#model = Word2Vec(cleaned_description , vector_size=100, window=5, min_count=5, workers=4)


#Para o outro modelo era:
#model = gensim.models.Word2Vec(my_list,  min_count=5, workers=4, epochs=25, sg=1, window=960)


#Skills Similarity
for seed_word in [ 'python', 'java', 'data', 'c']:
    print(seed_word, model.wv.most_similar(positive=[seed_word], topn=10))
    print("\n")
