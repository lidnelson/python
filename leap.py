year = int(input("enter year here: "))

if year% 4 ==0:
	if year%400 == 0 or year%100 != 0:
		print("this is a leap year")
else:
	print("this is NOT a leap year")
