"""Write a program to check if a given string is a palindrome."""

def palindrome(string):
    clear_string=string.lower().replace(" "," ")
    return clear_string==clear_string[::-1]
user=input("enter any number: ")
if palindrome(user):
    print(f" {user} is palindrome")
else:
    print(f" {user} is not palindrome")
