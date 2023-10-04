class sqr:
    def area(x):
        sidelength = float(x)
        return sidelength * sidelength
    
    def perimeter(x):
        sidelength = float(x)
        return sidelength * 4

input = input("Enter the square's side length: ")

area = sqr.area(input)
perimeter = sqr.perimeter(input)

print("Square's area is: ", area)
print("Square's perimeter is: ", perimeter)
