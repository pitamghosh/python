
def area(length, breadth):
    return length * breadth


def perimeter(length, breadth):
    return 2 * (length + breadth)


length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

rectangle_area = area(length, breadth)
rectangle_perimeter = perimeter(length, breadth)

print(f"Area of the rectangle: {rectangle_area}")
print(f"Perimeter of the rectangle: {rectangle_perimeter}")
