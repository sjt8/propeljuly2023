# program to print the list after removing the value 24 using list comprehension

nums = [12, 24, 35, 24, 88, 120, 155]
rem_nums = [i for i in nums if i != 24]

print(rem_nums)