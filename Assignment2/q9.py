# remove zeros from an IP address("216.08.094.196")

import re

ip = "216.08.094.196"

rem_ip = re.sub("0", "", ip)
print(rem_ip)