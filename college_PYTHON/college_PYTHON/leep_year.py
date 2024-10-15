a=int(input("enter any number"))
if(a%4==0 and a%400==0 and a%100==0):
    print("this year is leap year")
else:
    print("this year is not leap year")
