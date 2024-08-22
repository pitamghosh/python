def si(p,t,r):
    si=(p*t*r)/100
    amount=p+si
    return si,amount
p=int(input("enter any number: "))
t=int(input("enter any number: "))
r=int(input("enter any number: "))
a,i=si(p,t,r)
print("amount:",a)
print("interest",i)

