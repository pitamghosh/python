def is_space(char):
    return char.isspace()


char = input("Enter a character: ")

if is_space(char):
    print(f"'{char}' is a space character.")
else:
    print(f"'{char}' is not a space character.")

