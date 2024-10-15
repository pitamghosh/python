def fibo(count):
    num1 = 0
    num2 = 1
    if count < 1:
        print("Count should be greater than 0")
    elif count == 1:
        print(num1)
    elif count == 2:
        print(num1, num2)
    else:
        print(num1, num2, end=" ")
        count = count - 2  # Two numbers are already printed
        while count > 0:
            next_num = num1 + num2
            print(next_num, end=" ")
            num1 = num2
            num2 = next_num
            count -= 1

# Get user input and convert it to an integer
count = int(input("Enter a number: "))
fibo(count)
