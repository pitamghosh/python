def ci(p,t,r):
    amount=p*(1+r)**t
    compound=(amount-p)
    return amount,compound
p=int(input("enter any number: "))
t=int(input("enter any number: "))
r=int(input("enter any number: "))
c,a=ci(p,t,r)
print("compound interest: ",c)
print("amount is: ",a)
