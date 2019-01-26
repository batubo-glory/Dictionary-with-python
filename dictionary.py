# Import Data

import json

# loading json data into a python variable
data = json.load(open("data.json"))

# use type() to see what data type the json data is in
print(type(data))

# function to retrieve definition
def retrive_definition(word):
    return data[word]

# get word from user
word_user = input("Enter word here: ")

# retrive definition using function and print the result
print(retrive_definition(word_user))

