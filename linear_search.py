def LinearSearch(myItem,myList):
    found = False
    position = 0
    while position < len(myList) and not found:
        if myList[position] == myItem:
	    found = True
	position = position + 1
    return found
if __name__=="__main__":
     Packed_stuff = ["Shirts","Pants","Underwear","toys"]
     item = input("What particular item do you want to find?")
     HaveYouPackedThat = LinearSearch(item,Packed_stuff)
     if HaveYouPackedThat:
         print("You Have packed that")
     else:
         print("Your item has now been added to your list")
         Packed_stuff.insert(0,item)
	 print(Packed_stuff)
     

     
        

