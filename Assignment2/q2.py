# the table (from 1 to 10) of a number getting input from the user

inp = int(input("Enter a number "))

for i in range(1, 10 + 1):
    mul = i * inp
    print(f"{i} * {inp} = {mul}")