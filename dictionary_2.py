#  Sequence Matcher
import difflib
import json
from difflib import get_close_matches

data = json.load(open("dictionary.json"))


def retrive_definition(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input('Did you mean %s [y or n]: ' %
                       get_close_matches(word, data.keys())[0])
        if (action.lower() == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action.lower() == 'n'):
            print("%s does not exist" % word)
            return retrive_definition(get_input())
    else:
        print("Try again")
        return retrive_definition(get_input())


def get_input():
    word = input("Enter a word: ")
    return word

#  print(retrive_definition(get_input()))
output = retrive_definition(get_input())

if type(output) == list:
    for item in output:
        print("-", item)
else:
    print("-", output)
