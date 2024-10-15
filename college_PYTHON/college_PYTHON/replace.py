def replace_substring(string,old_sub,new_sub):
    update=string.replace(old_sub,new_sub)
    return update
string=input("enter any string: ")
old_string=input("enter old string: ")
new_string=input("enter new string: ")
result=replace_substring(string,old_string,new_string)
print(f"updated string: {result}")