# Write a program to sort a list of numbers in ascending or descending order.

def sort_numbers():
    # Input: List of numbers from the user
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    
    # Input: Ascending or descending choice
    order = input("Type 'asc' for ascending or 'desc' for descending order: ").lower()

    # Sort based on the order
    if order == 'asc':
        sorted_numbers = sorted(numbers)
        print("Sorted in ascending order:", sorted_numbers)
    elif order == 'desc':
        sorted_numbers = sorted(numbers, reverse=True)
        print("Sorted in descending order:", sorted_numbers)
    else:
        print("Invalid input! Please enter 'asc' or 'desc'.")
        
# Call the function
sort_numbers()


