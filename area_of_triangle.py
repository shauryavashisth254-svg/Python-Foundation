# ==========================================
# Exercise: Calculate the Area of a Triangle
# ==========================================

'''# Method 1: Base and Height are known
print("--- Method 1: Using Base and Height ---")
base = float(input("Enter the length of the base of your triangle: "))
height = float(input("Enter the height of your triangle: "))

area_method1 = 0.5 * base * height
print(f"The area of the triangle is {area_method1} units squared\n")
'''

# Method 2: All three sides are known (Heron's Formula)
print("--- Method 2: Using Heron's Formula (Three Sides) ---")
# Formula: Semi-perimeter (s) = (a + b + c) / 2
# Area = square root of (s * (s - a) * (s - b) * (s - c))

a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

# Calculate semi-perimeter
s = (a + b + c) / 2

# Calculate area
area_method2 = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("The area of the triangle with the given sides is: ", round(area_method2, 2))
