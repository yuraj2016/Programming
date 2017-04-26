stack = []
choice = 0
while choice != 4:
      print()
      print()
      print("1 push")
      print()
      print("2 pop")
      print()
      print("3 print")
      print()
      print("4 Exit")
      choice = int(input("Enter your choice"))
      if choice == 1:
	      Answer = raw_input("What do you want to add")
	      stack.append(Answer)
      if choice == 2:
	      print("The last one in was deleted")
	      del stack[0]
      if choice == 3:
	      print("This is my Stack", stack) 
