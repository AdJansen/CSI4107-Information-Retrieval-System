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

### collect_queries()

This acts as preprocessing, but for the query files

The function acts almost identically to collect_files, but it instead reads through the "topics1-50.txt" and doesn't need to iterate over many files. It is passed in one file and iterates over the found <top> tags, applying similar operations to collect_info.

It outputs a dictionary with the key value pair of {query number : [processed query text]}

### read_inverted_index()

A very simply function that reads the inverted index from a csv file into the Python environment. It is also rather slow, so it's recomended to keep everything in memory rather than writing and reading to disk.

### create_tfidf_index(inverted_index, total_documents)

We precompute the tfidf of each inverted_index word. The ifidf index is represented similarly to the inverted_index dictionary, but the tf value is replaced with a tfidf value. The tfidf is calculated using the modified euqation as provided in the assignment description.
 
The inverted_index dictionary is copied, then modified iteratively to replace the word-document tf scores with tfidf scores. This results in a quick-running generator for these scores.

### query_tfidf_index(queries, inverted_index, total_documents)



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
The vocabulary holds 116854 unique tokens.

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
 
 
 
 # Mean Average Precision on Test Queries
 
 MAP on Query Title only: 0.1834
 MAP on Query Title and Description: 0.1778
 
 # Title vs Description Discussion
 
 The title only runs of our code tended to perform better. The MAP score on title was superior, and was higher by around 0.006. Overall, when using only the query title, we found the cosine similarity scores to be closer to the ideal as provided in the ideal example.
