def sub_string(string,substring):
    count=string.count(substring)
    return count
ori_string=input("enter any string: ")
cou_string=input("enter substring count: ")
result=sub_string(ori_string,cou_string)
print(f"The substring '{cou_string}' occurs {result} time(s) in the string.")