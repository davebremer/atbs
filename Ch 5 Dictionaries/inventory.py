#Write a function named displayInventory() that would take any possible
#  “inventory” stored as a dictionary of the form {'ItemName': 3} (ie name & quantity) 
# and display it like the following:
#
# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62



def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(str(v) + " " + k)
    print("Total number of items: " + str(item_total))


# def addToInventory(inventory, addedItems):
#     for i in range(len(addedItems)):
#         # item=addedItems[i]
#         itemnum=inventory.get(addedItems[i])

#         #i keep thinking this should be able to be done in one line with setdefault
#         if itemnum == None: itemnum=0 
#         inventory[addedItems[i]] = itemnum + 1
#     return(inventory)

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i]+=1
    return(inventory)


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
print('Original inventory:')
displayInventory(inv)
print('\n')

#inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

