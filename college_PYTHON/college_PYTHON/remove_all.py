# Write a program to remove all occurrences of a specific element from a list

def remove_occurrences(input_list, element_to_remove):
    
    result_list = []
    
    
    for item in input_list:
        if item != element_to_remove:
            result_list.append(item)
    
    return result_list


user_input = input("Enter a list : ")
element_to_remove = eval(input("Enter the element to remove: "))

input_list = eval(user_input)

result = remove_occurrences(input_list, element_to_remove)

print("List after removing occurrences of", element_to_remove, ":", result)

