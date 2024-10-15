#  Write a program to generate a new list based on a given list using list comprehensions.

def new_list(input_list,operation):

    if operation=='square':
        new_list = [x**2 for x in input_list]
    elif operation=='double':
        new_list = [x*2 for x in input_list]
    elif operation=='increment':
        new_list = [x+1 for x in input_list]
    else:
        raise ValueError("Unsupported operation. Choose 'square', 'double', or 'increment'.")
    
    return new_list

user_input=input("enter any list: ")
operation=input("enter a operation: ")

input_list=eval(user_input)

try:
    result = new_list(input_list, operation)

    print("New list based on the operation:", result)

except ValueError as e:

    print(e)