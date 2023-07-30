# prints the words in a comma-separated sequence after sorting them alphabetically

inp = input("Enter comma-separated words: ").split(",")
inp.sort()

string = ""
for i, s in enumerate(inp):
    string += s

    if i < (len(inp) - 1):
        string += ","


print(string)
