from grammarbot import GrammarBotClient
import json

def checkGrammar(text):
    # Creating the client
    client = GrammarBotClient()
    
    # or, signup for an API Key to get higher usage limits here: https://www.grammarbot.io/
    #client = GrammarBotClient(api_key='my_api_key_here') # GrammarBotClient(api_key=my_api_key_here)    
    res = client.check(text)
    
    mistakes = []
    for mistake in res.matches:
        value = {}
        value['offset'] = mistake.replacement_offset
        value['length'] = mistake.replacement_length
        value['message'] = mistake.message
        value['replacements'] = mistake.replacements
        value['corrections'] = mistake.corrections
        value['rule'] = mistake.rule
        value['category'] = mistake.category
        
        mistakes.append(value)
        
    ret = mistakes
    
    #language = res.detected_language
    #result_is_incomplete = res.result_is_incomplete
    #num_error = len(res.matches)
    #ret = {'language': language, 'result_is_incomplete': result_is_incomplete, 'errors':num_error, 'mistakes': mistakes}

    
    return json.dumps(ret)

