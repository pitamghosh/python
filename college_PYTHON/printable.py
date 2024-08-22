def is_printable(char):
    if char.isprintable():
        return True
    else:
        return False


char = input("Enter a character: ")

if is_printable(char):
    print(f"'{char}' is a printable character.")
else:
    print(f"'{char}' is not a printable character.")
