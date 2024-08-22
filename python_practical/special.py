import math
def special(number):
    temp=number
    sum=0
    while temp>0:
     d=temp%10
     sum+=math.factorial(d)
     d//=10
    if sum==number:
        return True
    else:
        return False
num=input("enter any number: ")
if special==num:
    print("this is a special number")
else:
    print("this is not a special number")