def sym(*args):
    symDiff = []
    lastItem = -1

    # loop through arguments
    for arg in args:
        arg.sort()
        for i in arg:
            if i == lastItem:   pass
            elif i in symDiff:  symDiff.remove(i)
            else:               symDiff.append(i)

            lastItem = i
        lastItem = -1
    
    symDiff.sort()
    print(symDiff)


sym([1, 2, 3], [5, 2, 1, 4, 4]) 
sym([1, 2, 3, 3], [5, 2, 1, 4])
sym([1, 2, 3], [5, 2, 1, 4, 5])
sym([1, 2, 5], [2, 3, 5], [3, 4, 5])
sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5])
sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3])
sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1])