# Write a function that takes a list value as an argument and returns a string 
# with all the items separated by a comma and a space, with and inserted before
# the last item. 
# 
# e.g. spam = ['apples', 'bananas', 'tofu', 'cats']
# For example, passing the previous spam list to the function would return 
# 'apples, bananas, tofu, and cats'. But your function should be able to work 
# with any list value passed to it. 
# 
# Be sure to test the case where an empty list [] is passed to your function.

def commaCode(theList):
    op=""
    idx=0
    for i in theList:
        op=op + str(i)
        if idx < len(theList)-1:
            op+=", "
        idx+=1

    return(op)
        

#spam = ['apples', 'bananas', 'tofu', 'cats']
spam = ['apples', 'bananas', 'tofu', 32, 'cats']
#spam = ['apples']
# spam = []

print(">"+commaCode(spam)+"<")