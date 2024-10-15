# Write a program to print fibonacci series upto n terms in python

num = int(input("enter any number"))

n1 = 0
n2 = 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()