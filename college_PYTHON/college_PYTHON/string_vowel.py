"""Write a program that reads a
string and counts the vowels (a, e, i, o, u)."""

def count_vowels(string):
    # Define a set of vowels
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:

        if char in vowels:
            count += 1

    return count
user_input = input("Enter a string: ")
vowel_count = count_vowels(user_input)
print(f"The number of vowels in the string is: {vowel_count}")


