# Tuple Immutability

my_tuple=(10,20,30)
try:
    my_tuple[0]=100
except TypeError as e:
    error=str(e)

print(error)