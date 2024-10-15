def co_frequency(string, char):
    return string.count(char)

# Test the function
string = input("Enter a string: ")
character = input("Enter a character to count its frequency: ")

frequency = co_frequency(string, character)
print(f"The character '{character}' appears {frequency} time(s) in the string.")
