
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
example_sent = "the cat is a pet animal."
  
stop_words = set(stopwords.words('english')) 
  
word_tokens = word_tokenize(example_sent) 
  
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
final_sentence = [] 
for w in word_tokens: 
    if w not in stop_words: 
        final_sentence.append(w) 

print(final_sentence) 

 