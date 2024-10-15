"""Write a program to count the number of occurrences of a substring within a given string."""

# Function to count occurrences of a substring in a string
def count_substring(main_string, substring):
    return main_string.count(substring)

# Take user input for the main string and the substring
main_string = input("Enter the main string: ")
substring = input("Enter the substring to count: ")

# Call the function and display the result
count = count_substring(main_string, substring)
print(f"The substring '{substring}' occurs {count} time(s) in the main string.")
