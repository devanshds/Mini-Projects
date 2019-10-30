# Check high character count words
import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        flag = input("Did you mean %s ? (Y/N)" %get_close_matches(w,data.keys())[0])
        if flag=="y" or flag=="Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif flag=="n" or flag=="N":
            return "The word doesn't exist"
        else:
            return "I didn't understand your query"
    else:
        return "The word doesn't exist"

word=input("Enter word: ")
output=translate(word)

if type(output)== list :
    for item in output:
        print(item)
else:
    print(output)
