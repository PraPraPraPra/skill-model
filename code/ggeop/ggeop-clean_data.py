from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import pandas as pd

#Load the entire dataset
data = pd.read_csv('data/ggeop/JobsDataset.csv', header = 0, names = ['Query', 'Job Title', 'Description'])

#Mapping para termos iguais
skill_mapping = {
    "cnn" : ["cnns"],
    }

## Job Descriptions Cleaning
lemmatizer = WordNetLemmatizer()
symbols_to_ignore = ['(', ')', '.', '\\', ':', '%', '’']
to_ignore = stopwords.words('english')
to_ignore.extend(symbols_to_ignore)

cleaned_jobs = []
for job in data.Description:

	#Convert to lowercase and remove some symbols from the start
    lower_job = job.lower().replace(',', '').replace('_', '').replace(';', '')
    
    #Tokenize into words
    words_1 = word_tokenize(lower_job)

    #Lemmatize the words
    words_2 = [lemmatizer.lemmatize(w) for w in words_1]

    #Skip stopwords and some extra symbols (see line 3)
    words_3 = [w for w in words_2 if not w in to_ignore]

    #Join the tokens into a string and store it
    clean_job = " ".join(words_3)
    cleaned_jobs.append(clean_job)

## Job Query Titles Cleaning (for reporting purposes, to deal with search keywords)
cleaned_queries = []
for query in data.Query:

	if query == "Statistics":
		query = "Statistician"
	elif query in ["Artificial Intelligence", "Deep Learning"]:
		query = query + ' Expert'
	elif query in ["Technical Operations", "Machine Learning"]:
		query = query + ' Engineer'
	elif query in ["Data Warehousing", "Technology Integration"]:
		query = query + ' Analyst'

	cleaned_queries.append(query)
                                                            
## Create new df
df = pd.DataFrame({'Query':cleaned_queries, 'Description':cleaned_jobs})

#Create csv 
df.to_csv('../Results/Cleaned_JobDescs.csv')

