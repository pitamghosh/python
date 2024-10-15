#    Write a program to filter out even or odd numbers from a list.

def filter_numbers():
    # Input: List of numbers from the user
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    
    # Input: Even or odd filter choice
    choice = input("Type 'even' to filter even numbers or 'odd' to filter odd numbers: ").lower()

    # Create an empty list to store filtered numbers
    filtered_numbers = []

    # Filter numbers based on the choice
    if choice == 'even':
        for number in numbers:
            if number % 2 == 0:
                filtered_numbers.append(number)
        print("Even numbers:", filtered_numbers)
    elif choice == 'odd':
        for number in numbers:
            if number % 2 != 0:
                filtered_numbers.append(number)
        print("Odd numbers:", filtered_numbers)
    else:
        print("Invalid input! Please enter 'even' or 'odd'.")

# Call the function
filter_numbers()




