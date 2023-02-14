# CSI4107-Information-Retrieval-System

## Adam Jansen 300076841, Brian Zhang 300070168, Nika Ribnitski 300121606

# Task Split
We split the tasks equally. Each method/portion of the project was written as we all sat around Adam's Desktop computer. We are all living in the same apartment, so this arrangement made sense.

This method ensured we all knew how each part of the project worked, and could collaboratively build each part with input from all parties.

# Functions

### collect_info(coll_files, stop_words)

Iterates through the files in the collection (denoted by 'coll_files'). In each it finds the documents within, iterates through them, and splits them using the python library 'beautifulSoup'. Using beautifulSoup the docno and text are extracted from each document. This text is then sent to lowercase, has punctuation & digits removed, and is stemmed. The stopwords are then removed and the vocabulary is updated with any new terms found in that document. 
The documents are stored in a Pyton dictionary (i.e hashtable) where the key is the docno, and the value is the processed text.

### create_inverted_index(files, vocabulary, output_csv : bool = False)

### collect_queries()

### read_inverted_index()

### create_tfidf_index(inverted_index, total_documents)

### query_tfidf_index(queries, inverted_index, total_documents)

### calculate_doc_lengths(files,tfidf_index)

### calculate_query_lengths(queries,queries_tfidf)

### compute_cosine_similarities(queries, files, tfidf_index, query_tfidf_index, doc_lengths, q_lengths)

### display_results(similarities, run_id)

# How to Run

Using Jupyter notebooks, simply run all cells in order from top to bottom (or click Run All). This will define all functions, then execute them in order, assigning variables as needed. The display_results function will execute last and output the results data to the 'results.csv' file.

# Optimizations
:)

# Vocabulary Size

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
 
 # Title vs Description Discussion
