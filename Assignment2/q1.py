# numbers which are divisible by 5 and multiple of 8 between 2000 and 2500

for i in range(2000, 2500 + 1):
    if i % 5 == 0 and i % 8 == 0:
        print(i)