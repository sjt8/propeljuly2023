# to check the validity of a password

import re

def check(passw):
    if len(passw) < 6 or len(passw) > 12:
        print("Password must be min 6 and max 12 length")
    elif len(re.findall("[0-9]", passw)) == 0:
        print("Password must contain 1 digit")
    elif len(re.findall("[a-z]", passw)) == 0:
        print("Password must contain 1 small letter")
    elif len(re.findall("[A-Z]", passw)) == 0:
        print("Password must contain 1 capital letter")
    elif len(re.findall("[$#@]", passw)) == 0:
        print("Password must contain 1 special character")
    else:
        print("Valid Password")


password = input("Enter a password ")
check(password)
