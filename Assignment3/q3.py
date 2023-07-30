# square each odd number in a list using list comprehension

inp = input("Enter comma-separated numbers: ").split(",")
nums = [int(i) ** 2 for i in inp if int(i) % 2 != 0]
print(nums)