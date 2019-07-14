
from search import *

#####################
#     Search Web    #
#####################
def search(message):
    result = ''
    
    '''Wikipedia'''
    ### Need to Identify Entity before search from Wiki
    if message.find(message) != -1:
        result += get_wikipedia(message)
        return result
    
    
    '''Britannica'''
    ### Need to Identify Entity before search from Wiki
    if message.find(message) != -1:
        result += get_britannica(message)
        return result
    
        
    '''Joke'''
    if message.find('joke') != -1:
        result += 'Ok, here is a joke for you~~~\n'
        result += get_joke()
        return result

    return result


if __name__ == '__main__':
    message = "RazChatbot"
    print search(message)
