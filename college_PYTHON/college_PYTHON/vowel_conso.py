def vow_const(alph):
    vowel='aeiouAEIOU'
    if alph.isalpha():
        if alph in vowel:
            return "vowel"
        else:
            return "consonant"
    else:
       return "it is not a chatracter"

v=input("enter any alphabet: ")
result=vow_const(v)
print(f"the charecter '{v} is a '{result}'")