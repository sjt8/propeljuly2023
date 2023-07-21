# sort the list in ascending order and print first element

lst = []

inp = int(input("Enter no. of elements: "))

for i in range(inp):
    value = int(input("value: "))
    lst.append(value)

sort_list = sorted(lst)

print("First Element is", sort_list[0])