# Define a higher-order function
def apply_operation(func, x, y):
    return func(x, y)

# Define a couple of simple functions to pass
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# Using the higher-order function
x=int(input("enter any number: "))
y=int(input("enter any number: "))
result_add = apply_operation(add, x, y)
result_multiply = apply_operation(multiply, x, y)

print(f"Addition result: {result_add}")         # Output: 8
print(f"Multiplication result: {result_multiply}")  # Output: 15
