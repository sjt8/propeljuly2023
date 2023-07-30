# Using list comprehension, return the number of even integers in the given array.

inp = input("Enter comma-separated numbers: ").split(",")
nums = [int(i) for i in inp if int(i) % 2 == 0]
print(nums)