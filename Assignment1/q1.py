# solving quadratic equations using the quadratic formula

import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter b: "))

d = b * b - 4 * a * c

if a == 0:
    print("a can't be zero")
elif d < 0:
    print("root is complex")
else:
    x = (-b + math.sqrt(d)) / (2 * a)
    y = (-b - math.sqrt(d)) / (2 * a)
    print(f"The roots are {x} {y}")
