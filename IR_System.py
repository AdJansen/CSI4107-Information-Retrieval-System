#implement an Information Retrieval (IR) system based on the vector space model, for a collection of documents
#For weighting, you can use the tf-idf weighting scheme (wij = tfij∙idfi)
#For each query, your system will produce a ranked list of documents, starting with the most similar to the query and ending with the least similar. For the query terms you can use a modified tf-idf weighting scheme wiq = (0.5 + 0.5 tfiq)∙idfi
#For the ranking, you can use the cosine similarity measure
import Porter_Stemming as ps
import pandas as pd
from bs4 import BeautifulSoup
import os
import xml.etree.cElementTree as et
import string

#Step 1 Preprocessing
#Input: Documents that are read one by one from the collection
#Output: Tokens to be added to the index (vocabulary)

coll_files = [f for f in os.listdir(r"./coll/") if os.path.isfile(os.path.join(r"./coll/", f))]
stop_words = open(r"./stopwords.txt", "r").read().split()

def collect_info(coll_files, stop_words):
    files = []
    list_of_words = []
    for file in coll_files:
        with open(r"./coll/" + file, "r") as f:
            soup = BeautifulSoup(f, 'lxml') 
            
            for doc in soup.find_all('doc'):
                temptxt = str(doc.find('text')).replace('<text>', ' ').replace('</text>', ' ').replace('\n', ' ')
                temptxt = temptxt.lower()
                temptxt = temptxt.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))
                temptxt = temptxt.translate(str.maketrans(string.digits, " " * len(string.digits)))
                
                list_of_words = temptxt.split()
                
                porter = ps.PorterStemmer()
                list_of_words = [porter.stem(word, 0, len(word)-1) for word in list_of_words]
                
                temptxt = list(set(list_of_words) - set(stop_words))

                files.append({doc.find_all('docno')[0].text.strip(): temptxt}) #We cannot check the length of the list of words because we don't know how many words are in the stop words list
    return files


print(collect_info(coll_files, stop_words)[-1]['AP881231-0146'])

#Step 2 Indexing
#Input: Tokens from the preprocessing step
#Output: An inverted index for fast access

#Step 3. Retrieval and Ranking:
# Use the inverted index (from step 2) to find the limited set of documents that contain at least one of the query words. 
# Compute the cosine similarity scores between a query and each document. 
#Input: One query and the Inverted Index (from Step2)
#Output: Similarity values between the query and each of the documents. Rank the documents in decreasing order of similarity scores.