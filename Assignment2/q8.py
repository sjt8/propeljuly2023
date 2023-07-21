# count Even and odd numbers in a list

lst = []

inp = int(input("Enter no. of elements: "))

for i in range(inp):
    value = int(input("value: "))
    lst.append(value)

even = 0
odd = 0

for i in lst:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("no. of Even numbers", even)
print("no. of Odd numbers", odd)