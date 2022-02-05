from curses.ascii import isspace
import pandas as pd
import csv
import gensim, logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = [["cat", "say", "meow"], ["dog", "say", "woof"]]

#model = gensim.models.Word2Vec(sentences,  min_count=1)
#Default min_count=5
#default size=100
#default workers=1
#print(model.wv.most_similar('cat'))  # get vector for word
my_list = []

with open('./data/skill2vec_50K.csv', newline='') as f:
    reader = csv.reader(f, skipinitialspace=True)
    for row in reader:
        #my_list.append(row[1:])
        my_list.append([element for element in row[1:] if len(element) != 0])

print(my_list[0:10])

#skills = pd.read_csv('./data/skill2vec_50K.csv', header=None, index_col=0)
#skills.drop(columns=skills.columns[0], axis=1, inplace=True)
#skills.reset_index(inplace=True)
#print(skills.head())
#print("\n")

#skills_list = [row for _, row in skills.iterrows() if pd.isnull(row) == False]
#skills_list = skills.to_numpy().tolist()

#print(skills_list[0])
#print("\n")
#print(skills[0])
model = gensim.models.Word2Vec(my_list,  min_count=5, workers=4, epochs=25, sg=1, window=960)
print("\n---\n")
print(model.wv.most_similar('matlab'))  # get vector for word

"""
NOTES:
(sentences=None, corpus_file=None, vector_size=100, alpha=0.025, window=5, min_count=5, max_vocab_size=None, sample=0.001, seed=1, workers=3, min_alpha=0.0001,
sg=0, hs=0, negative=5, ns_exponent=0.75, cbow_mean=1, hashfxn=<built-in function hash>, epochs=5, null_word=0, trim_rule=None, sorted_vocab=1, batch_words=10000,
compute_loss=False, callbacks=(), comment=None, max_final_vocab=None, shrink_windows=True)

sg ({0, 1}, optional) – Training algorithm: 1 for skip-gram; otherwise CBOW.
"""

#a=1
#for index, row in skills.iter:
#    if(a<5):
#        print(row)
#        print("aaaa\n")
#        a += 1

exit()



job_postings = pd.read_json('./data/jobs.json')
print(job_postings.head())

def convert_job_posting(job):
    converted = []
    
    title_and_requirements  = [normalize_job_title(job['job_title'])] + extract_nouns(job['requirements'])
    converted.append(title_and_requirements)
    
    summary = extract_nouns(job['summary'])
    converted.append(summary)
    
    return converted

inputs = []
for _, p in job_postings.iterrows():
    inputs += convert_job_posting(p)

print("Exit")