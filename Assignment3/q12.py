# a sequence of comma separated 4 digit binary numbers as its input
# and then check whether they are divisible by 5 or not


def bin_dec(bin_string):
    dec = 0
    for b in range(0, len(bin_string)):
        if bin_string[b] == "1":
            pos = len(bin_string) - 1 - b
            dec = dec + (2 ** pos)

    return dec


inp = input("Enter comma-separated words: ").split(",")

for i in inp:
    if bin_dec(i) % 5 == 0:
        print(i)
