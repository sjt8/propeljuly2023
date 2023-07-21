# Replace all occurrence of 6 with 'six' and 10 with 'ten' for the given string 'They ate 6 apples and 10 banana'

import re

string = "They ate 6 apples and 10 banana"

replaced_string = re.sub("6", "six", string)
replaced_string = re.sub("10", "ten", replaced_string)
print(replaced_string)

