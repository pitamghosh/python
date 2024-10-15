#  Write a program to rotate a list by a given number of positions.

def rotate_list(input_list, positions):
   
    positions = positions % len(input_list)
    
    rotated_list = []
    
   
    for i in range(positions, len(input_list)):
        rotated_list.append(input_list[i])
    
   
    for i in range(positions):
        rotated_list.append(input_list[i])
    
    return rotated_list


user_input_list = input("Enter a list : ")
positions = int(input("Enter the number of positions to rotate: "))


input_list = eval(user_input_list)


result = rotate_list(input_list, positions)

print("List after rotation:", result)
