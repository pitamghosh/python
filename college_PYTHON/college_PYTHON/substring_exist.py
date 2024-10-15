"""Write a program to check if a substring exists within a given string."""


def check_substring(string, substring):
    # Check if the substring exists in the string
    return substring in string

# Get input from the user
main_string = input("Enter the main string: ")
search_substring = input("Enter the substring to search for: ")

# Call the function to check for the substring
if check_substring(main_string, search_substring):
    print(f"The substring '{search_substring}' exists in the string.")
else:
    print(f"The substring '{search_substring}' does not exist in the string.")
