# Use map and a lambda function to convert a list of Fahrenheit temperatures
# to a list of Celsius temperatures

inp = input("Enter comma-separated words: ").split(",")
fahrenheit = [float(i) for i in inp]
celsius = map(lambda x: (x - 32) * (5/9), fahrenheit)

for i in celsius:
    print(i)