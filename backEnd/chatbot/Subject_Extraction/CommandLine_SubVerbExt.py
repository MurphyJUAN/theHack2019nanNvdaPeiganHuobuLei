import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer



custom_sent_tokenizer = PunktSentenceTokenizer("How are you")

tokenized = custom_sent_tokenizer.tokenize("My name is mohammad")

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            print(len(chunked)) 
            print(chunked[0][0])
            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'NN'):
                print(subtree)

            #chunked.draw()

    except Exception as e:
        print(str(e))

process_content()