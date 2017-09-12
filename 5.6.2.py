def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory:
            inventory[addedItems[i]] += 1
        else:
            inventory[addedItems[i]] = 1
    print('Inventory:')
    total_item = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total_item += int(v)
    print('Total number of items: ' + str(total_item))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)
