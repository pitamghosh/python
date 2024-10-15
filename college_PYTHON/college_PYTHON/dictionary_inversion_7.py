# Dictionary Inversion

def invert_digit(m):
    return {p: k for k,p in m.items()}

sample_digit={'a':1,'b':2,'c':4}
inverted_digit=invert_digit(sample_digit)

print(inverted_digit)