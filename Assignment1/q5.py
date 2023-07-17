# shows the position of the target word in the string of words

def showposition(words, tofind):
    pos = []
    for i in range(len(words)):
        if words[i] == tofind:
            pos.append(i)

    if len(pos) == 0:
        return False
    else:
        return pos


sentence = input("Enter sentence ")
target = input("Enter target ")
pos = showposition(sentence.split(" "), target)

print(pos)
