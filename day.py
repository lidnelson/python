Date_day = int(input("Enter the day number: "))
Date_month = int(input("Enter month number:"))
Date_year = int(input("Enter year:"))

days_month = {1:31,2:59,3:90,4:120,5:151,6:181,7:212,8:243,9:273,10:304,11:334,0:365}

a= Date_day
b= (Date_month-1)%12
c = int(days_month[b])
d= (Date_year-1)*365

def rounddown(n,m):
	if n%m != 0:
		return		(round(n/m)-1)
	else:
		return		(int(n/m))


e= rounddown(Date_year, 4)

f= a + c + d + e
if f%7 == 2:
 	print("Monday")
elif f%7 == 3:
 	print("Tuesday")
elif f%7 == 4:
 	print("Wednesday")
elif f%7 == 5:
 	print("Thursday")
elif f%7 == 6:
 	print("Friday")
elif f%7 == 0:
 	print("Saturday")
elif f%7 == 1:
 	print("Sunday")