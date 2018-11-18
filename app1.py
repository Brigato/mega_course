# https://www.udemy.com/the-python-mega-course/learn/v4/content
# The Python Mega Course: Build 10 Real World Applications
import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))

def meaning(w):
    if w in data:
        return data[w]
    elif w.lower() in data:  # Added as exercise
        print("If you meant %s:" % w.lower())
        return data[w.lower()]
    elif w.title() in data:  # Added as exercise
        print("If you meant %s:" % w.title())
        return data[w.title()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s ? " % get_close_matches(w, data.keys())[0])
        if yn.lower() in ["yes", "y", "sim", "ja", "j", "s"]:
            return data[get_close_matches(w, data.keys())[0]]
        else:
            return "The word does not exist. Please, double check it"
    else:
        return "The word does not exist. Please, double check it"


word = input("Enter word: ")

# print(SequenceMatcher(None, "rain", "rainn").ratio())
# print(get_close_matches())

output = meaning(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
# print(pprint.pprint(meaning(word.lower())))


