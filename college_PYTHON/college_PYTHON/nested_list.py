# Write a program to flatten a nested list

def flatten_list(nested_list):
    # Create an empty list to store the flattened elements
    flat_list = []
    
    # Function to flatten the nested list
    def flatten(sublist):
        for item in sublist:
            if isinstance(item, list):
                flatten(item)  # If item is a list, recursively flatten it
            else:
                flat_list.append(item)  # Append non-list item to flat_list
    
    # Call the recursive flatten function on the nested list
    flatten(nested_list)
    
    return flat_list

# Get input from user
user_input = input("Enter a nested list (e.g. [1, [2, 3], [4, [5]]]): ")

# Convert the user input to an actual Python list
nested_list = eval(user_input)  # Using eval to convert the input string to a list

# Flatten the nested list
result = flatten_list(nested_list)

print("Flattened list:", result)
