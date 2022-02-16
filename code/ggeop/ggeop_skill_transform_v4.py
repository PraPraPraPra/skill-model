# import from nltk the functions that split a text into sentences and tokens
from nltk.tokenize import sent_tokenize, word_tokenize

import pandas as pd
import numpy as np
from nltk import word_tokenize, pos_tag, chunk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from gensim.test.utils import common_texts, get_tmpfile


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

def skill_transform(data):

    """
    1.- Transformar em Lista, com 1 linha por elemento da lista ["primeira coisa blah", "Depois blah blah blah", (...)], retirando as virgulas;
    2.- Separar em Tokens ex: [["primeira", "coisa", blah"], ["Depois", "blah", "blah", blah"]];
    3.- Por tudo em lower case;
    4.- Lematizar;
    5.- Tirar stop-words;
    6.- Substituir símbolos;
    7.- Gravar num ficheiro o numero de ocurrencias;
    """

    version = "v4"

    #Synonym:
    # Special cases replace
    special_case = {}
    special_case["javascript"] = [ "java script" ]
    #special_case["wireframe"] = [ "wireframes", "wire frame", "wire frames", "wire-frame", "wirefram", "wire fram", "wireframing" ]
    special_case["ood"] = [ "object oriented design", ]
    special_case["oop"] = [ "object oriented programming", ]
    special_case["olap"] = [ "online analytical processing" ]
    special_case["ecommerce"] = [ "e commerce" ]
    #special_case["consultant"] = [ "consulting"  ]
    special_case["ux"] = [ "user experience", "web user experience design", "user experience design", "ux designer", "user experience/ux" ]
    special_case["html5"] = [ "html 5" ]
    special_case["j2ee"] = [ "jee" ]
    special_case["osx"] = [ "mac os x", "os x" ]
    special_case["senior"] = [ " sr ", " sr. " ]
    special_case["qa"] = [ "quality" ]
    special_case["bigdata"] = [ "big data"]
    special_case["webservice"] = [ "webservices", "website", "webapps" ]
    special_case["xml"] = [ "xml file", "xml schemas", "xml web service" ]
    special_case["nlp"] = [ "natural language process", "natural language", "nltk" ]
    special_case["aws"] = [ "amazon web service"]
    special_case["java"] = [ "java ee"]


    #Create Job description list
    job_descriptions=[]
    for job in data.Description:
        j = job.replace(',', '')
        i = j.replace('/', ' ')
        k = i.lower()
        for root_skill in special_case:
            for synonym in special_case[root_skill]:
                k.replace(synonym, root_skill)

        job_descriptions.append(k)

    #Remove Capitalization
    #no_capitals =[]
    #for job in job_descriptions:
    #    no_capitals.append([j.lower() for j in job])






    #Words tokenization
    jobs = [word_tokenize(d) for d in job_descriptions]



    #Lemmatize
    #lemmatizer = WordNetLemmatizer()
    #lem=[]
    #for job in no_capitals:
    #    lem.append([lemmatizer.lemmatize(j) for j in job])

    #Remove stopwords
    filtered_words = []
    stopwords_dict = {key : "" for key in stopwords.words('english')}
    for job in jobs:
        filtered_words.append([j for j in job if not j in stopwords_dict])




    #Remove symbols
    cleaned_description=[]
    extra_dict = {key : "" for key in ['(',')','.',',',':','%']}
    for job in filtered_words:
        cleaned_description.append([j for j in job if not j in extra_dict])



    from collections import Counter

    count = Counter(x for xs in cleaned_description for x in set(xs))
    ordered_count_list = count.most_common()

    with open(f'data/ggeop/counter_{version}.txt', 'w') as f:
        for item in ordered_count_list:
            f.write(f'{item[0]} : {item[1]}\n')

    max_size = len(max(cleaned_description, key=len))

    return (cleaned_description, max_size, version)
