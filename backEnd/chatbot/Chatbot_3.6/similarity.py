import string
import nltk.corpus
from nltk import word_tokenize, pos_tag

target_sentence = "What is a chatbot?"
sentences = ["Chatbot is a AI Agent.",
             "Chatbot is computer program.",
             "I dont know what is chatbot. ",]

# Get default English stopwords and extend with punctuation
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
#print(target_sentence.strip(string.punctuation))
stopwords.append('')

print("--------------------------------------")
print('Q: ', target_sentence )
print("--------------------------------------")

def is_exact_match(a, b):
    """Check if a and b are matches."""
    return (a == b)

def token_match(a, b):
    # Question-> tokens_a --> target_sentence  
    tokens_a = [token.lower().strip(string.punctuation) for token in nltk.tokenize.word_tokenize(a) \
                if token.lower().strip(string.punctuation) ]
                #if token.lower().strip(string.punctuation) not in stopwords]
    # Answers -> tokens_b -> ans_sentence 
    tokens_b = [token.lower().strip(string.punctuation) for token in nltk.tokenize.word_tokenize(b) \
                if token.lower().strip(string.punctuation) ]
    print(tokens_a )       
    print(tokens_b )            
    # Calculate Jaccard similarity
    ratio = len(set(tokens_a).intersection(tokens_b)) / float(len(set(tokens_a).union(tokens_b)))
    return ratio

threshold=0.7
for ans_sentence in sentences:
    #print(is_exact_match(target_sentence, ans_sentence), ans_sentence)
    similarity_ratio = token_match(target_sentence, ans_sentence)
    print(ans_sentence,"\t", similarity_ratio)

