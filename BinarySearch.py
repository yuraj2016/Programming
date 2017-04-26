def BinarySearch(myItem,myList):
    found = False
    bottom = 0
    top = len(myList) + 1
    count = 0
    while bottom<=top and not found:
        count = count + 1
        middle = (bottom + top)//2
        if myList[middle]==myItem:
            found = True
        elif myList[middle] < myItem:
            bottom = middle + 1
        else:
            top = middle-1
    print ("Number of searches %d" % (count))
    return found
if __name__ == '__main__':
    numberList = [1,3,5,7,8,13,15,17,18,28,37,47]
    item = int (raw_input("What number are you looking for?"))
    isitFound = BinarySearch(item,numberList)
    if isitFound:
        print("Your number is in the list!")
    else: 
        print("Your number is not in the list!")
