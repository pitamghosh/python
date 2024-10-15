# Write a program to find the maximum and minimum elements in a list.

a = []  #empty list
n = int(input("enter no. of elements: "))
MAX = 0
MIN=0
for i in range(n):
    e = int(input("enter element: "))   #user input
    a.append(e) #adding element to list
    

print(a)
print("min = {0}".format(min(a)))
print("max = {0}".format(max(a)))

