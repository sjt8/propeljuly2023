# Use filter() to eliminate all words that are shorter than 4 letters from a list of words.

inp = input("Enter comma-separated words: ").split(",")
out = filter(lambda x: len(x) > 4, inp)

for i in out:
    print(i)