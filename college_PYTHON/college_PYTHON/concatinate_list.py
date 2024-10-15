# rite a program to concatenate two lists into one.

def concate_list():
    
    list1=list(map(int,input("enter first list including space: ").split()))
    list2=list(map(int,input("enter second list including space: ").split()))
    concate_list=list1+list2
    
    print("concatenate list",concate_list)
concate_list()