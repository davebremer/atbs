# Write a function that uses regular expressions to make sure the
# password string it is passed is strong. 
#
# A strong password is defined as one that is at least eight characters long, 
# contains both uppercase and lowercase characters, and has at least one digit.

import re
passcheck = re.compile("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])([a-zA-Z0-9]+){8,}$") 
result = passcheck.search("aA2iiiiiiiiiiiiii")
if result:
    print("matched")
else:
    print("no match")