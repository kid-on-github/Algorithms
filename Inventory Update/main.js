function updateInventory(arr1, arr2) {
    // All inventory must be accounted for or you're fired!
    
    let arr = arr1.concat(arr2)
    let names = []
    let toReturn = []

    // convert to dict
    let items = {}
    for (let i in arr){
        let count = arr[i][0]
        let name = arr[i][1]

        if (items[name] != null){
            items[name] += count
        }
        else{
            items[name] = count
            names.push(name)
        }
    }

    names.sort()
    for(let name in names){
        name = names[name]
        toReturn.push([items[name],name])
    }

    return toReturn
}

// Example inventory lists
var curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
];

var newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
];

updateInventory(curInv, newInv);
