import math

print("Area Calculator")
print("1. Circle")
print("2. Triangle")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius * radius
    print("Area of the circle is:", area)

elif choice == 2:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("Area of the triangle is:", area)

else:
    print("Invalid choice")
