# Write a program that calculates the sum of all elements in a list of numbers.


a = []  #empty list
n = int(input("enter no. of elements: "))
s = 0
for i in range(n):
    e = int(input("enter element : "))   #user input
    a.append(e) #adding element to list
    s = s + a[i]    #summing up list elements

print(a)
print("SUM = {0}".format(s))
