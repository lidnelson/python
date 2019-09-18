print("Menu")
print("1 - Level 1")
print("2 - Level 2")
print("3 - Level 3")
print("4 - Level 4")

examlevel = int(input("Enter exam level: "))

if examlevel == 1 or examlevel == 2:
	mark = int(input("Enter level 1 or 2 mark here: "))
	if mark >= 75:
		print("Pass")
	else:
		print("Fail")
elif examlevel == 3 or examlevel == 4:
	mark = int(input("Enter level 3 or 4 mark here: "))
	if examlevel == 3 and mark >= 65:
		print("pass")


