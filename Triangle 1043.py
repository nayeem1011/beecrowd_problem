# Read three floating-point values
A, B, C = map(float, input().split())

# Check if it's possible to form a triangle
if A + B > C and A + C > B and B + C > A:
    # Calculate the perimeter of the triangle
    perimeter = A + B + C
    print("Perimetro = {:.1f}".format(perimeter))
else:
    # Calculate the area of the trapezium
    area = 0.5 * (A + B) * C
    print("Area = {:.1f}".format(area))