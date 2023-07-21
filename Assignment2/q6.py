# Reversing a list

lst = []

inp = int(input("Enter no. of elements: "))

for i in range(inp):
    value = int(input("value: "))
    lst.append(value)

rev_lst = lst[::-1]

print("Reversed List", rev_lst)