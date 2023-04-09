# CSI4107-Information-Retrieval-System

## Adam Jansen 300076841, Brian Zhang 300070168, Nika Ribnitski 300121606

# Task Split
We split the tasks equally. Each method/portion of the project was written as we all sat around Adam's Desktop computer. We are all living in the same apartment, so this arrangement made sense.

This method ensured we all knew how each part of the project worked. It also allowed us to collaboratively build each part with input from all parties.

# Functions

### collect_info(coll_files, stop_words)
This function covers preprocessing (Step 1)

It iterates through the files in the collection (denoted by 'coll_files'). For each file: it finds the documents within, iterates through them, and splits them using the python library 'beautifulSoup'. The docno and text are extracted from each document using beautifulSoup. This text is then set to lowercase, has punctuation & digits removed, and is stemmed via PorterStemmer. The stopwords are then removed and the vocabulary is updated with any new terms found in that document. 


The documents are stored in a Pyton dictionary (i.e hashtable) where the key is the docno, and the value is the processed text. This allows subsequent functions to rapdily access the processed text by document id. The output vocabulary is a Python set, in other words, a python set is a way to **efficiently** store a collection of unique elements, like a dictionary but without the value part of a key value pair.

### create_inverted_index(files, vocabulary, output_csv : bool = False)
This function covers Indexing (Step 2)

This function is responsible for populating our inverted index. It intakes the files and vocabulary as output by collect_info, as well as a flag that tells the function to write a csv inverted index or not. It is recommended to leave this flag False, since writing the csv is a computationally intense operation.

Our inverted index is also stored in a dictionary, although it is a 2-d dict (a dictionary of dictionaries) where each key is a token from the vocabulary. There are 2 static values for each key in the vocabulary: the document frequency of the token, and most token occurances in any one document, and then a set of key value pairs of a docno, and the number of times the current term appear in that document, or *tf*. 

Again, storing the index as a dictionary is to optimize access speed, it allows rapid access of any word's DF, and any document's tf for that word 

### collect_queries() and expand_tokens()

This acts as preprocessing, but for the query files

The function acts almost identically to collect_files, but it instead reads through the "topics1-50.txt" and doesn't need to iterate over many files. It is passed in one file and iterates over the found <top> tags, applying similar operations to collect_info.

Further, this function was expanded to also output a set of expanded queries. The expansion is done using wordnet via a helper function (expand_tokens) that operates on each query iteratively. 

It outputs 2 dictionaries, one dictionary with the key value pair of {query number : [processed query text]}, and another, with the key value pair of {query number : [expanded prcoessed query text]}

### read_inverted_index()

A very simply function that reads the inverted index from a csv file into the Python environment. It is also rather slow, so it's recomended to keep everything in memory rather than writing and reading to disk.

### create_tfidf_index(inverted_index, total_documents)

We precompute the tfidf of each inverted_index word. The ifidf index is represented similarly to the inverted_index dictionary, but the tf value is replaced with a tfidf value. The tfidf is calculated using the modified euqation as provided in the assignment description.
 
The inverted_index dictionary is copied, then modified iteratively to replace the word-document tf scores with tfidf scores. This results in a quick-running generator for these scores.

### query_tfidf_index(queries, inverted_index, total_documents)

Operates much like create_tfidf_index, but iterates over the queries, and calculates the tfidf accordingly.

### calculate_doc_lengths(files,tfidf_index)

Creates another dictionary where each docno is a key, and the value is that document's computed length. These lengths are later used to compute the set of cosine similarities.

This allows us to access the length of any of the numerous documents with speed.
### calculate_query_lengths(queries,queries_tfidf)

Creates a similar dictionary to the previous function, but the keys are replaced with the query numbers, and the each query's comupted length.

This again allows us quickly access the length of any given query number.

### compute_cosine_similarities(queries, files, tfidf_index, query_tfidf_index, doc_lengths, q_lengths)

This function is the culmination of all the other functions above it. It takes in the docno/key and tokened content via the files & queries prameters, the tfidf indexes, and finally the lengths of the queries and documents.

The function outputs a 2-d dictionary, the most significant key is the query number, then the docno. The value stored per docno is the cosine similarity of the query to the document.

This is computed by taking each docno in files, and for each query in queries, then computing the similarity for each word in that query (via tfidf_index and query_tfidf_index). The word similarties are summed then divided by the doc_length of that document times the query length. These values are retrieved from doc_lengths and q_lengths respectively. This final similarity is then sent to the dictionary.

### display_results(similarities, run_id)

Takes in the cosine similarites, and a string and outputs the final results into a formatted document.

# How to Run
The main file of this project is IR_System.ipynb

Using Jupyter notebooks, simply run all cells in order from top to bottom (or click Run All). This will define all functions, then execute them in order, assigning variables as needed. The display_results function will execute last and output the results data to the 'results.csv' file.

Because the file is output as a csv, we converted the file to be seperated with spaces rather than commas. Thus, the final output results file is **results.txt**

# Optimizations

Throughout our implementation, we used dictionaries when possible. Python dictionaries are easily implemented hash tables, which are known for their efficiency. For the many different values that had to be stored and re-accessed, dictionaries seemed to be the most efficient option available in Python.

# Vocabulary Size
The vocabulary holds 151729 unique tokens.

# Vocabulary Sample
'keansburg',
 'tolson',
 'faint',
 'richwin',
 'lagoon',
 'unliv',
 'canino',
 'maskerensi',
 'convergencia',
 'wasserstein',
 'lopa',
 'papand',
 'throug',
 'therfectin',
 'bayonn',
 'reeb',
 'springtim',
 'samchulli',
 'muchnik',
 'linxi',
 'jayaratna',
 'winterl',
 'lissak',
 'ibpo',
 'musolf',
 'kasar',
 'collarless',
 'baksh',
 'strategest',
 'necesarili',
 'angier',
 'sizer',
 'aldershot',
 'poussaint',
 'aiyetoro',
 'hughli',
 'tantalizingli',
 'franken',
 'saarsalu',
 'buktenica',
 'minsk',
 'conneaut',
 'wheless',
 'majka',
 'untarnish',
 'romanczuk',
 'oyment',
 'bayless',
 'emert',
 'crusco',
 'kapp',
 'geniun',
 'rossmoor',
 'colladai',
 'tambrand',
 'katsouda',
 'demand',
 'samim',
 'nugzarov',
 'scientolog',
 'alvyn',
 'neubrandenburg',
 'chinchilla',
 'wilferd',
 'dauda',
 'vulpio',
 'gambita',
 'shipstead',
 'sirlin',
 'milman',
 'hovi',
 'wig',
 'hourcad',
 'widlif',
 'sand',
 'disbeliev',
 'cutawai',
 'shakai',
 'diazinon',
 'oboist',
 'seidel',
 'jamali',
 'hapuna',
 'hanemann',
 'tomali',
 'wornum',
 'lantau',
 'hartwig',
 'dexin',
 'ratish',
 'topolog',
 'manjoon',
 'southhaven',
 'dci',
 'kuop',
 'kuwashima',
 'fabola',
 'unfind',
 'clayton',
 'mulanai'
 
 # First 10 answers to Queries 1 and 25
 
| TopicId | Q0 | Docno         | Ranking | Cosine Similarity   | RunId |
|---------|----|---------------|---------|---------------------|-------|
| 3       | Q0 | AP880805-0039 | 1       | 0.29648358661499785 | 0     |
| 3       | Q0 | AP880518-0053 | 2       | 0.23429067036557988 | 0     |
| 3       | Q0 | AP880513-0106 | 3       | 0.22023379937638904 | 0     |
| 3       | Q0 | AP880815-0051 | 4       | 0.2189042277779582  | 0     |
| 3       | Q0 | AP880726-0126 | 5       | 0.202539172243783   | 0     |
| 3       | Q0 | AP880915-0190 | 6       | 0.20184707746601574 | 0     |
| 3       | Q0 | AP880419-0133 | 7       | 0.20098529327621664 | 0     |
| 3       | Q0 | AP880423-0088 | 8       | 0.1991282072637553  | 0     |
| 3       | Q0 | AP880217-0150 | 9       | 0.19864710850257702 | 0     |
| 3       | Q0 | AP880722-0185 | 10      | 0.1955730024167017  | 0     |

| TopicId | Q0 | Docno         | Ranking | Cosine Similarity   | RunId |
|---------|----|---------------|---------|---------------------|-------|
| 20      | Q0 | AP881110-0035 | 1       | 0.3826220931308371  | 0     |
| 20      | Q0 | AP881122-0171 | 2       | 0.3679209745670312  | 0     |
| 20      | Q0 | AP881111-0092 | 3       | 0.2859335911245842  | 0     |
| 20      | Q0 | AP880627-0239 | 4       | 0.281132062682521   | 0     |
| 20      | Q0 | AP881123-0037 | 5       | 0.2594277585670614  | 0     |
| 20      | Q0 | AP880504-0233 | 6       | 0.19856863929511562 | 0     |
| 20      | Q0 | AP880906-0186 | 7       | 0.19844587297642932 | 0     |
| 20      | Q0 | AP880518-0359 | 8       | 0.18054008205719027 | 0     |
| 20      | Q0 | AP880316-0324 | 9       | 0.15976063301105925 | 0     |
| 20      | Q0 | AP880316-0325 | 10      | 0.15379808730541553 | 0     |

Our cosign similarites are fairly consistent throughout the rankings from 1 to 10. The top result's cosine similarity of both queries does not exceed 0.4.
 
 # Mean Average Precision on Test Queries
 
 MAP on Query Title only: 0.1834
 MAP on Query Title and Description: 0.1778

 MAP on Query Title and Description Expanded: 0.1367
 
 # Title vs Description Discussion
 
 The title only runs of our code tended to perform better. The MAP score on title was superior, and was higher by around 0.006. Overall, when using only the query title, we found the cosine similarity scores to be closer to the ideal as provided in the ideal example.

 # Discussion on advanced Neural Information retrieval methods

 Unfortunately, neither query expansion (using synonyms), nor BERT-based cosine-evaluation achieved better results than our original implementation. The query expansion value was comparable, but slightly lower by a few MAP score points. Depending on system parameters, it hovered around 0.14 compared to the 0.1834 that we achieved without it. It is hard to say exactly what caused this lowering of score, but we believe it could be related to the fact that the synoyms generated using the wordnet library were topically unrelated even when using synonyms with very high similarity scores to multiple query terms. When analyzing the query strings before and after expansion, of the words added, the synonyms were obviously related to one term, but not in the context of the greater string. This seemed to obfuscate the clarity and directness of the query, making the topic of the string less clear to both human and machine. Initial implemenations that used BERT to calculate query-document similarity were far too slow, taking either days to run a single instance, or 2 WEEKS under one calculation. This long computation time persisted despite many attempts to reduce operations. I even cried a little bit, and the computer didn't care. I resorted to bargaining, but my computer didn't speed up even when I promised to clean it after. We then changed tracks, and attempted to use a different library. We attempted to use paraphrase mining, but even when we had it operate on a very small subset of data, it still would have taken multiple days to complete execution. This was not a feasible strategy. Unfortunately, due to this immense runtime, we were not able to get a deep learning model to generate the similarity scores necessary to create a results ranking for this method.