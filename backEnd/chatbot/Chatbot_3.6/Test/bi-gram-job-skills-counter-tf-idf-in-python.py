#Program to collect user input and display list of relevant job skills based on their search.
# to be used with dataset collected by scraper --> https://www.kaggle.com/itesla/webscraper-in-python-for-seek-com-au

#include libraries
import csv # to open/close/append CSV
import os # to check if file exists
import nltk #natural language toolkit
import pandas as pd
import numpy as np
from datetime import datetime
import re
from collections import Counter, defaultdict

#User inputs search term.
print('Please enter a job to search for: ')
userInput = "data entry" #input()#'account'
print(userInput)

# - load csv ====================================================================================================================================================================================
file_exists = os.path.isfile('data.csv') ################ for testing purposes (use "Account")

# loop to check if file exists
if file_exists == 0:
    print('Error: seek_data.csv does not exist!')
elif file_exists == 1:
    try:
        CSV_buffer = pd.read_csv('data.csv', sep=',', header='infer')# read CSV file into buffer ################ for testing purposes (use "Account")
    except Exception as e:
        Date_Advertised = None
        print('Exists, but failed to open.')

#convert user input and all Main_Job_Title to lowercase for better match ========================================================================================================================
userInput = str.lower(userInput)
CSV_buffer2 = CSV_buffer.apply(lambda x: x.astype(str).str.lower())
CSV_buffer2 = CSV_buffer2[CSV_buffer2['Main_Job_Title'].str.contains(userInput)] #case sensitive copy only matching rows

# clean for punctuation =========================================================================================================================================================================
# Job_Description in each row has stop words removed.
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
CSV_buffer2['Job_Description_Without_Stopwords'] = CSV_buffer2['Job_Description'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))

def clean_string(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('([!#?\',.$])','', value)
        value = re.sub("\d+", "", value)
        result.append(value)
    return result

# creates list where each document is an element
CSV_buffer2['Job_Description_Without_Stopwords'] = clean_string(CSV_buffer2['Job_Description_Without_Stopwords'])

# build bigram list ============================================================================================================================================================================
bigram_list = []
for index, row in CSV_buffer2.iterrows():
    bigram_list = bigram_list + [b for b in nltk.bigrams(row['Job_Description_Without_Stopwords'].split())]

# Bi-gram Term Frequency =======================================================================================================================================================================
bigram_tf = Counter(bigram_list) # list all bigram TF
bigram_tf_df = pd.DataFrame.from_dict(bigram_tf, orient='index').reset_index() #turn class collections.Counter into Pandas DataFrame
bigram_tf_df = bigram_tf_df.rename(columns={'index':'index2', 0:'count'}) #index is immutable tuple and will need to be changed to list/string and cleaned to allow combining with IDF dataframe

index_list = []
for index, row in bigram_tf_df.iterrows():
    index_list.append(str(row[0][0]) + ' ' + str(row[0][1]))

bigram_tf_df['index'] = index_list
bigram_tf_df = bigram_tf_df.drop(['index2'], axis=1) # delete bigram tuple column
bigram_tf_df = bigram_tf_df.sort_values(by='count', ascending=False) #sort based on vec_sum

# Bi-gram Inverse-Document Frequency ===========================================================================================================================================================
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(2,2), min_df = 0, stop_words = 'english')
TFIDF_terms = vectorizer.fit_transform(CSV_buffer2['Job_Description_Without_Stopwords']).toarray()
TFIDF_df = pd.DataFrame(TFIDF_terms, columns=vectorizer.get_feature_names()) #pull terms into a dataframe
IDF_df = TFIDF_df.T.reset_index() # rotate DataFrame
IDF_df[IDF_df.columns[::-1]]
IDF_df['vec_sum'] = IDF_df.sum(axis=1) #add column which is a sum of all other columns
IDF_df = IDF_df.sort_values(by='vec_sum', ascending=False) #sort based on vec_sum
IDF_TF = pd.DataFrame()
IDF_TF = IDF_df[['index', 'vec_sum']].copy() #copy only the index and vector sum to the new dataframe

# PRINT lists ==================================================================================================================================================================================
print('\nTop skills for your searched job based on TF:\n', bigram_tf_df.head(n=20)) # print dataframe

print('\n\nTop skills for your searched job based on addition of IDF: \n', IDF_TF.head(n=20))# print only index and vec_sum
