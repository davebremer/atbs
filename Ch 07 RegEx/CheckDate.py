# Write a regular expression that can detect dates in the DD/MM/YYYY format. 
# Assume that the days range from 01 to 31, the months range from 01 to 12, 
# and the years range from 1000 to 2999. 
# 
# Note that if the day or month is a single digit, it’ll have a leading zero.
#
# The regular expression doesn’t have to detect correct days for each month or
# for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021.
# 
#  Then store these strings into variables named month, day, and year, 
#  and write additional code that can detect if it is a valid date. 
#  April, June, September, and November have 30 days, February has 28 days, 
#  and the rest of the months have 31 days. February has 29 days in leap years. 
#  Leap years are every year evenly divisible by 4, except for years evenly divisible
#  by 100, unless the year is also evenly divisible by 400. 
#  Note how this calculation makes it impossible to make a reasonably sized 
#  regular expression that can detect a valid date.

import re
# regex1 = re.compile('RoboCop')
# print(regex1.search('RoboCop is part man, part machine, all cop.'))

#generic regex for date
dateRegex=re.compile(
    # Day: (0[1-9]|[12]\d|3[01]) - 0 followed by 1-9 (01-09)
    #      or a 1 or 2 followed by a number (10-29)
    #       or 3 followed by 0-1 ie (30 or 31)
    #
    # Month: (0[1-9]|1[0-2]) - 0 followed by 1-9 (01-09) or 1 foloowed by 0-2 (10-12)
    #
    # Year: ([12]\d{3}) - begins with 1 or 2 followed by 3 digits 1000-2999
    r'(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/([12]\d{3})'
)
#result = dateRegex.search("31/03/2999").group()
theDate = "29/02/2000"
result = dateRegex.search(theDate)
if result:
    print("matched")
else:
    print("no match")



def validDate(theDate):
    Day,Month,Year = map(int, theDate.split("/"))
    valid = True
    # April, June, September, and November 30
    if Month in [4,6,9,11]:
        if Day > 30: valid = False

    # Leap years are every year evenly divisible by 4, except for years evenly divisible
    # by 100, unless the year is also evenly divisible by 400. 
    elif Month == 2:
        if (Year % 4 == 0 and not Year % 100 == 0) or (Year % 400 == 0):
            if Day > 29: valid = False
        else:
            if Day > 28: valid = False
    
    # the rest have 31
    else:
        if Day > 31:
            valid = False
    return(valid)

if validDate(theDate):
    print(f"{theDate} is a valid date")
else:
    print(f"{theDate} is NOT a valid date")