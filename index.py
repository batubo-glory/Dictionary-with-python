import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def get_meaning(word):
    if word in data:
        return data[word]
     elif word.title() in data:  
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())) > 0:
            yn = str.upper(input("Please double-check your spelling. Did you mean %s instead? Enter Y for Yes and N for No: " % get_close_matches(word, data.keys())[0]))
            if yn == "Y":
                return data[(get_close_matches(word, data.keys()))[0]]
            elif yn == "N":
                return"Sorry your word does not exist. Please double check"
            else:
                return"We did not understand your input. Please enter Y or N"


    else:
        return "Sorry the word does not exist"

user_input = str.lower(input("Please enter word here: "))

output = get_meaning(user_input)

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)
