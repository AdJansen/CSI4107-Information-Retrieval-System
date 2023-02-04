#implement an Information Retrieval (IR) system based on the vector space model, for a collection of documents
#For weighting, you can use the tf-idf weighting scheme (wij = tfij∙idfi)
#For each query, your system will produce a ranked list of documents, starting with the most similar to the query and ending with the least similar. For the query terms you can use a modified tf-idf weighting scheme wiq = (0.5 + 0.5 tfiq)∙idfi
#For the ranking, you can use the cosine similarity measure
import Porter_Stemming as ps


#Step 1 Preprocessing
#Input: Documents that are read one by one from the collection
#Output: Tokens to be added to the index (vocabulary)


#Step 2 Indexing
#Input: Tokens from the preprocessing step
#Output: An inverted index for fast access

#Step 3. Retrieval and Ranking:
# Use the inverted index (from step 2) to find the limited set of documents that contain at least one of the query words. 
# Compute the cosine similarity scores between a query and each document. 
#Input: One query and the Inverted Index (from Step2)
#Output: Similarity values between the query and each of the documents. Rank the documents in decreasing order of similarity scores.