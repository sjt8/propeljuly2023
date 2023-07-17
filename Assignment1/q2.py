# the frequency of occurrence of each word

def getfrequency(tofind):
    frequency = {}
    for word in tofind.split(" "):
        if frequency.get(word) != None:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


string = input("Enter string ")

frequency = getfrequency(string.title())

print(frequency)
