num = input("Enter a number: ")
n = len(num)
sum = 0
temp = int(num)

while temp > 0:
    d = temp % 10
    sum += d ** n
    temp //= 10

if sum == int(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
