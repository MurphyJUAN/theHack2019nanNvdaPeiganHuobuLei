# _____TF-IDF libraries_____
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# _____helper Libraries_____
import pickle
import csv
import timeit
import random
#import os

def talk_to_lina_primary(test_set_sentence):
   
    csv_file_path = "randychat.csv"
    tfidf_vectorizer_pikle_path = "tfidf_vectorizer.pickle"
    tfidf_matrix_train_pikle_path ="tfidf_matrix_train.pickle"

    i = 0
    sentences = []

    # enter your test sentence
    test_set = (test_set_sentence, "")

    # 3ashan yzabt el indexes
    sentences.append(" No you.")
    sentences.append(" No you.")

    try:
        ##--------------to use------------------#
        f = open(tfidf_vectorizer_pikle_path, 'rb')
        tfidf_vectorizer = pickle.load(f)
        f.close()

        f = open(tfidf_matrix_train_pikle_path, 'rb')
        tfidf_matrix_train = pickle.load(f)
        f.close()
        # ----------------------------------------#
    except:
        # ---------------to train------------------#
        start = timeit.default_timer()

        # enter jabberwakky sentence
        with open(csv_file_path, "r") as sentences_file:
            reader = csv.reader(sentences_file, delimiter=',')
            # reader.next()
            # reader.next()
            for row in reader:
                # if i==stop_at_sentence:
                #    break
                sentences.append(row[0])
                i += 1

        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix_train = tfidf_vectorizer.fit_transform(sentences)  # finds the tfidf score with normalization
        # tfidf_matrix_test =tfidf_vectorizer.transform(test_set)
        stop = timeit.default_timer()
        print ("training time took was : ")
        print stop - start

        f = open(tfidf_vectorizer_pikle_path, 'wb')
        pickle.dump(tfidf_vectorizer, f)
        f.close()

        f = open(tfidf_matrix_train_pikle_path, 'wb')
        pickle.dump(tfidf_matrix_train, f)
        f.close()
        # -----------------------------------------#

    tfidf_matrix_test = tfidf_vectorizer.transform(test_set)

    cosine = cosine_similarity(tfidf_matrix_test, tfidf_matrix_train)

    cosine = np.delete(cosine, 0)
    max = cosine.max()
    response_index = 0
    if (max > 0.7):
        new_max = max - 0.01
        list = np.where(cosine > new_max)
        # print ("number of responses with 0.01 from max = " + str(list[0].size))
        response_index = random.choice(list[0])

    else:
        #print ("not sure")
        #print ("max is = " + str(max))
        response_index = np.where(cosine == max)[0][0] + 2  # no offset at all +3
       

    j = 0

    with open(csv_file_path, "r") as sentences_file:
        reader = csv.reader(sentences_file, delimiter=',')
        for row in reader:
            j += 1  # we begin with 1 not 0 &    j is initialized by 0
            if j == response_index:

                #if delimeter in row[1]:
                #    # get newest suggestion
                #    answer_row = row[1].split(delimeter)
                #    row[1] = answer_row[1]

                #else:  # add new suggestion
                #    note = "just return old original suggestion"

                return row[1], response_index,
                break



while 1:
    sentence = raw_input("talk to Lina : ")

    response_primary, line_id_primary = talk_to_lina_primary(sentence)
    print response_primary
    print 