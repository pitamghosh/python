"""Write a program to convert all characters in a string to uppercase and lowercase."""

def convert(string):
    uppere_str=string.upper()
    lower_str=string.lower()
    return uppere_str,lower_str
user=input("enter any string: ")
upper_result,lower_result=convert(user)
print(f"uppercase: {upper_result}")
print(f"lowercase: {lower_result}")
