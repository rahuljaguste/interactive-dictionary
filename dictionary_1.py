import json

data = json.load(open("dictionary.json"))


def retrive_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        print(word + ' not found in the dictionary')
        return retrive_definition(get_input())


def get_input():
    word = input("Enter a word: ")
    return word


print(retrive_definition(get_input()))
