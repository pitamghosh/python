"""Write a program that removes
punctuation marks from a string."""

import string
def remove(input_string):
    translator=str.maketrans('','',string.punctuation)
    no_string=input_string.translate(translator)
    return no_string
user=input("enter any string: ")
result=remove(user)
print(f"string without punctuation: {result}")