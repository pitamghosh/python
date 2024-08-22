def max(list):
    index=1
    max=list[0]
    while index<len(list):
        if list[index]>max:
            max=list[index]
        index +=1
    return max
list=[7,5,3,1,9,6,8,4,2]
print("max",max(list))


def min(list):
    index=1
    min=list[0]
    while index<len(list):
        if list[index]<min:
            min=list[index]
        index +=1
    return min
list=[7,5,3,1,9,6,8,4,2]
print("min",min(list))


#same program using for loop only

def max(list):

    max=list[0]
    for value in list[1:]:
        if value >max:
            max=value
    return max
list=[7,5,3,1,9,6,8,4,2]
print("max",max(list))


def min(list):

    min=list[0]
    for value in list[1:]:
        if value <min:
            min=value
    return min
list=[7,5,3,1,9,6,8,4,2]
print("min",min(list))


