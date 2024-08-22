def char_or_digit(char):
    if char.isalpha():
      return "alphabet"
    elif char.isdigit():
        return "digit"
    else:
        return "this is not alphabet or digit"

c=input("enter any character or digit: ")
result=char_or_digit(c)
print(f"the character is'{c}'is a '{result}'")