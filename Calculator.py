print("Opertaion Menu:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

print ("Answer Menu")
print("1 - Yes")
print("2 - No")

question = int(input("Would you like to make a caluclation? "))


while question == 1 :
	firstnumber = float(input("Please enter first number here: "))
	operation = int(input("Enter Operation for Operation Menu: "))
	secondnumber = float(input("Please enter second number here: "))
	if operation == 1:
		print(firstnumber+secondnumber)
	elif operation == 2:
		print(firstnumber-secondnumber)
	elif operation == 3:
		print(firstnumber*secondnumber)
	elif operation == 4:
		print(firstnumber/secondnumber)
	else:
		print("Invalid Entry")	
	print("Thank you for using the Calculator")
	question = int(input("Would you like to make a caluclation? "))
else:
	print("Thank you for using the Calculator")
