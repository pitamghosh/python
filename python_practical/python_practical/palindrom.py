def palindrome(p):
    str_num=str(p)
    if str_num==str_num[::-1]:
     return True
    else:
     return False
n=input("enter any number: ")
if  palindrome(n):
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")
