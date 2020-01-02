def updateInventory(arr1, arr2):
    # All inventory must be accounted for or you're fired!
    arr = arr1 + arr2
    names = []
    toReturn = []

    # convert to dict
    items = {}
    for count, name in arr:
        if name in items:
            items[name] += count
        else: 
            items[name] = count
            names.append(name)
    
    names.sort()

    # populate list to return
    for name in names:
        toReturn.append([items[name],name])
    
    # print toReturn
    for i in toReturn:
        print(i)






# Example inventory lists
curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
];

newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
];

updateInventory(curInv, newInv);
