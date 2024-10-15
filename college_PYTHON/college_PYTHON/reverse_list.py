# Write a program to reverse a given list.
# Initialize an empty list
my_list = []

# Get the number of elements to add
n = int(input("Enter the number of elements in the list: "))

# Loop to append user input to the list
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    
    my_list.append(element)

# Print the original list
print("Original list:", my_list)

# Reverse the list
reversed_list = []
for i in range(len(my_list)-1, -1, -1):
    reversed_list.append(my_list[i])

# Print the reversed list
print("Reversed list:", reversed_list)
