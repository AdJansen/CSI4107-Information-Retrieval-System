#implement an Information Retrieval (IR) system based on the vector space model, for a collection of documents
#For weighting, you can use the tf-idf weighting scheme (wij = tfij∙idfi)
#For each query, your system will produce a ranked list of documents, starting with the most similar to the query and ending with the least similar. For the query terms you can use a modified tf-idf weighting scheme wiq = (0.5 + 0.5 tfiq)∙idfi
#For the ranking, you can use the cosine similarity measure
import time
import Porter_Stemming as ps
import pandas as pd
from bs4 import BeautifulSoup
import os
import string
import csv

from collections import defaultdict

#Step 1 Preprocessing
#Input: Documents that are read one by one from the collection
#Output: Tokens to be added to the index (vocabulary)
#Get Start time 
start_time = time.time()

coll_files = [f for f in os.listdir(r"./coll/") if os.path.isfile(os.path.join(r"./coll/", f))]
stop_words = open(r"./stopwords.txt", "r").read().split()

def collect_info(coll_files, stop_words):
    files = [] 
    list_of_words = [] 
    vocabulary = set([]) #We use a set because we don't want to have duplicates in the vocabulary
    
    for file in coll_files:
        with open(r"./coll/" + file, "r") as f:
            soup = BeautifulSoup(f, 'lxml') 
            
            for doc in soup.find_all('doc'):
                docno = doc.find_all('docno')[0].text.strip()

                temptxt = str(doc.find('text')).replace('<text>', ' ').replace('</text>', ' ').replace('\n', ' ')
                temptxt = temptxt.lower()
                temptxt = temptxt.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))
                temptxt = temptxt.translate(str.maketrans(string.digits, " " * len(string.digits)))
                
                list_of_words = temptxt.split()
                
                porter = ps.PorterStemmer()
                list_of_words = [porter.stem(word, 0, len(word)-1) for word in list_of_words]
                
                temptxt = list(set(list_of_words) - set(stop_words))
                
                vocabulary.update(set(temptxt))
                files.append({docno: temptxt}) #We cannot check the length of the list of words because we don't know how many words are in the stop words list
    return files, vocabulary

files, vocabulary = collect_info(coll_files, stop_words)

# #Send Files to csv file
# df = pd.DataFrame.from_dict(files)
# df.to_csv(r"./files.csv")

# #send vocabulary to csv file
# df = pd.DataFrame.from_dict(vocabulary, orient='index')
# df.to_csv(r"./vocabulary.csv")

# print(vocabulary)
print("vocabulary length: " , len(vocabulary))
print("files length: " , len(files))
#Step 2 Indexing
#Input: Tokens from the preprocessing step
#Output: An inverted index for fast access

def create_inverted_index(files, vocabulary):
    inverted_index = {i:[] for i in vocabulary}
    count = 0
    csv_columns = ['word', 'documents']
    for file in files: #key is the docno, value is the list of words
        count += 1
        key, value = list(file.items())[0]
        for word in value: #if the word is in the document, then we add that document to the inverted index
                inverted_index[word].append(key)
        if count % 100 == 0:
            print(" count: ", count)

    #Use Pandas to send inverted index to csv file
    count = 0
    csv_file = r"./inverted_index.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(csv_columns)
            for data in inverted_index:
                count += 1
                writer.writerow([data, inverted_index[data]])
                if count % 100 == 0:
                    print(" count: ", count)
    except IOError:
        print("I/O error")

    return inverted_index

inverted_index = create_inverted_index(files, vocabulary)
print(inverted_index)
#print elapsed time
print("--- %s seconds ---" % (time.time() - start_time))
#Step 3. Retrieval and Ranking:
# Use the inverted index (from step 2) to find the limited set of documents that contain at least one of the query words. 
# Compute the cosine similarity scores between a query and each document. 
#Input: One query and the Inverted Index (from Step2)
#Output: Similarity values between the query and each of the documents. Rank the documents in decreasing order of similarity scores.