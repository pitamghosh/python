#  Write a program that identifies duplicates in a list.

# Initialize an empty list
my_list = []

# Get input from the user
user_input = input("Enter items to add to the list, separated by spaces: ")

# Split the input string into a list and append to my_list
my_list.extend(user_input.split())

# Find duplicates using a set
duplicates = set([item for item in my_list if my_list.count(item) > 1])

# Show the updated list
print("Updated list:", my_list)

# Show duplicates
if duplicates:
    print("Duplicates found:", duplicates)
else:
    print("No duplicates found.")
