def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
a=int(input("enter anuy number: "))
result=factorial(a)
print(result)