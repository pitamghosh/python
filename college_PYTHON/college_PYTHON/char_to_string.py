def conveter(s):
    upper_case =s.upper()
    lower_case =s.lower()
    return upper_case,lower_case
c=input("enter any number: ")

upper,lower=conveter(c)

print(f"uppercase:{upper}")
print(f"lowercase:{lower}")
