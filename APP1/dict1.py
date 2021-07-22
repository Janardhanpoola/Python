import json
import difflib
from difflib import get_close_matches




def mean(word):
    f=open("data.json")
    data=json.load(f)

    word=word.lower()

    if word in data:
        return data[word]
    
    elif word.title() in data:    
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]    
    
    elif len (get_close_matches(word,data.keys())) >0:

        userip=input(f"did you mean {get_close_matches(word,data.keys())[0]} instead? press y or n ")

        if userip=='y':
            return data[get_close_matches(word,data.keys())[0]]
        
        elif userip=='n':
            return "your word not found"
        else:
            return "invalid input"

    else:
        return "sorry word doesnt exists"
                     
            

word=input("enter word to find its meaning: ")

translate=mean(word)

if isinstance(translate,list):
    print("Meaning is \n----------------")
    for index,i in enumerate(translate,start=1):
        print(str(index)+")",i)
else:
    print(translate)



