def case_convert(case):
    if case.islower():
        return case.upper()
    elif case.isupper():
        return case.lower()
    else:
        return "not an alphabet"

l=input("enter any character: ")
result=case_convert(l)
print(f"the case converted charcter is:{result}")