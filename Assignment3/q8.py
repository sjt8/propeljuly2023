# Input two lists and convert the two list to dictionary

list1 = input("Enter comma-separated list1: ").split(",")
list2 = input("Enter comma-separated list2: ").split(",")

if len(list1) == len(list2):
    list_dict = {list1[i]: list2[i] for i in range(len(list1))}
    print(list_dict)
else:
    print("Can't create dictionary from list with different length")
