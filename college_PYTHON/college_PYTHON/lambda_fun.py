# Define a lambda function to square a number
square = lambda x: x ** 2

# Test the lambda function
number = int(input("enter any number: "))
result = square(number)
print(f"The square of {number} is: {result}")
