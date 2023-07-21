# matches a string that has an 'a' followed by anything, ending 's'

import re

string = input("Enter a string ")

if re.match("a[a-zA-z]+s", string):
    print("Match found")
else:
    print("No match")