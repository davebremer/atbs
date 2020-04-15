# Write a program that asks users for their sandwich preferences. 
# The program should use PyInputPlus to ensure that they enter valid input, 
# such as:

# done    Using inputMenu() for a bread type: wheat, white, or sourdough.
# done    Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
# done    Using inputYesNo() to ask if they want cheese.
# done            If so, using inputMenu() to ask for a cheese type: 
#             cheddar, Swiss, or mozzarella.
# done    Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
#  done   Using inputInt() to ask how many sandwiches they want. 
#             Make sure this number is 1 or more.

# Come up with prices for each of these options, and have your program
# display a total cost after the user enters their selection.

import pyinputplus as pyip

def getPrice(food,prices):
    theprice = 0
    for i,k in enumerate(food):
        try: 
            theprice+= prices[k][food[k]]
        except KeyError:
            theprice+=0
    theprice *= food['Count']
    return theprice

pricelist={'Bread':{'Wheat':1, 'White':1.5, 'Sourdough':2},
    'Protien':{'Chicken':1, 'Turkey':1.5, 'Ham':2, 'Tofu':3},
    'CheeseType':{'Cheddar':1, 'Swiss':1.5, 'Mozzarella':2}
        
}

sandwhich = {}
sandwhich['Bread'] = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], 
    numbered=True,limit=3, default='White')
sandwhich['Protien']= pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'],
    numbered=True,limit=3,default='Chicken')
sandwhich['Cheese']= pyip.inputYesNo(prompt='Do you want Cheese? ',
    default='no')

if sandwhich['Cheese'] == 'yes':
    sandwhich['CheeseType'] = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'],
        numbered=True,limit=3,default='Chedder')

sandwhich['Mayo']= pyip.inputYesNo(prompt='Do you want mayo? ',
    default='no')
sandwhich['Mustard']= pyip.inputYesNo(prompt='Do you want mustart? ',
    default='no')
sandwhich['Lettuce']= pyip.inputYesNo(prompt='Do you want lettuce? ',
    default='no')
sandwhich['Tomato']= pyip.inputYesNo(prompt='Do you want tomato? ',
    default='no')

sandwhich['Count'] = pyip.inputInt(prompt='How many sandwhiches: ',min=1)

totalprice = getPrice(sandwhich,pricelist)

print(sandwhich)
print(f"This sandwhich costs ${totalprice:.2f}")