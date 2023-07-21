# find second-largest number in a list

lst = []

inp = int(input("Enter no. of elements: "))

for i in range(inp):
    value = int(input("value: "))
    lst.append(value)

sort_list = sorted(lst, reverse=True)

print("Second largest element is", sort_list[1])
