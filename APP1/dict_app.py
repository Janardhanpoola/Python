import json
import difflib
from difflib import get_close_matches
data=json.load(open("data.json"))


def translate(word):
    word=word.lower() # Converting to inputs to lowers to check case sensitivity 
    if word in data:
        return (data[word])
    elif (word.title() in data):#for words that starts with start letter with CAPS.like Texas,Delhi
        return data[word.title()]
    elif word.upper() in data:# for words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        un=input("did you mean %s instead ?press 'y' or 'n' " %get_close_matches(word,data.keys())[0])
        if un=='y':
            return data[get_close_matches(word,data.keys())[0]]    
        elif un=='n':
            return "word doesnt exists"
        else:
                return "please try again"
    else:
        return "word doesnt exists"


word=input("enter word to find its meaning: ")
output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)