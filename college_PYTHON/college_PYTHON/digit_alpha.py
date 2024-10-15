def is_digit(char):
    if char.isdigit():
        return True
    else:
        return False


character = input("Enter a character: ")

if is_digit(character):
    print(f"'{character}' is a digit.")
else:
    print(f"'{character}' is not a digit.") 
