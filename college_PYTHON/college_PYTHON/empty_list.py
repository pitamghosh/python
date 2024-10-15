#   Write a program that checks if a list is empty.

my_list=[]

if not my_list:
    print("the list is empty: ")

user=input("enter any thing to add: ")

my_list.append(user)

print("update list",my_list)