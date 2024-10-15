"""Write a program to concatenates two given strings."""

def concatenates(string1,string2):
    add_string=string1+string2
    return add_string
string1=input("enter 1st string: ")
string2=input("enter 2st string: ")
result=concatenates(string1,string2)
print(f"Concatenated string:{result}")
