#

def char_frequency(string):
    # Initialize an empty dictionary to store frequency
    freq = {}

    # Loop through each character in the string
    for char in string:
        # If the character is already in the dictionary, increment its count
        if char in freq:
            freq[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            freq[char] = 1

    return freq

# Get input from the user
user_input = input("Enter a string: ")

# Call the function and store the result
result = char_frequency(user_input)

# Print the frequency of each character
for char, frequency in result.items():
    print(f"'{char}': {frequency}")



