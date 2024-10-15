#   Write a program to find the union of two lists

def union_of_list(list1,list2):
    union_list =[]

    for item in list1:
        if item not in union_list:
            union_list.append(item)

    for item in list2:
        if item not in union_list:
            union_list.append(item)

    return union_list

list1= input("enter list1 sepereted by space: ").split()
list2= input("enter list2 sepereted by space: ").split()

result=union_of_list(list1,list2)

print("union of the two list:",result)
