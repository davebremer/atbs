def collatz(number):
    if number % 2 == 0:
        op = number // 2
    else:
        op = (3 * number) + 1
    print(op)
    return op

strNum = ""
# this works for data validation but doesn't allow negatives
#turns out that collatz requires positive input
while not strNum.isnumeric(): strNum = input("Enter a number: ")
num = int(strNum)

# Aaaannnnndddddd.... this allows negatives but collatz breaks with negatives
# while strNum == "":
#     strNum = input("Enter a number: ")
#     try:
#         num = int(strNum)
#     except ValueError:
#         print("That wasn't a number, try again")
#         strNum = ""


while num != 1:
    num = collatz(num)

