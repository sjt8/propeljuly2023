# calculate the number of letters and digits

def calculate(toFind):
    l = 0
    d = 0
    for c in toFind:
        if c.isalpha():
            l += 1
        elif c.isdigit():
            d += 1

    print("Letters: ", l)
    print("Digits: ", d)


string = input("Enter sentence ")
calculate(string)
