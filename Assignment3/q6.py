# convert a list of Fahrenheit temperatures to Celsius

inp = input("Enter comma-separated words: ").split(",")
fahrenheit = [float(i) for i in inp]
celsius = [(i - 32) * (5/9) for i in fahrenheit]
print(celsius)
