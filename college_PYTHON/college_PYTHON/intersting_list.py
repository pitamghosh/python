    #  Write a program to find the intersection of two lists

def intersectrion_list(list1,list2):

    intersection=[]
    
    for item in list1:
        if item in list2:
            intersection.append(item)
            return intersection
        
list1 =input("enter list1 by sepereted by space: ").split()
list2 =input("enter list2 by sepereted by space: ").split()

intersectrion=intersectrion_list(list1,list2)

print("intersection of the two list: ",intersectrion)