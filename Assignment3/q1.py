# sort a list of numbers with the odd numbers coming first and the even numbers coming second

def sort_odd_even(list_num):
    list_num.sort()
    list_odd = []
    list_even = []

    for i in list_num:
        if i % 2 == 0:
            list_even.append(i)
        else:
            list_odd.append(i)

    return list_odd + list_even


inp = input("Enter comma-separated words: ").split(",")
nums = [int(i) for i in inp]

print(sort_odd_even(nums))