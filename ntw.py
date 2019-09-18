unit1 = {0:"zero"}
unit2 = {0: " ",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
unit3 = {0:" ",2:"twenty",3:"thirty",4:"forty",5:"fifty",6: "sixty",7:"seventy",8:"eighty",9:"ninty"}
unit4 = {3:"hundred", 6:"thousand", 9:"million", 12:"billion", 15:"trillion"}

num = str(input("Input:"))
numLen = len(num)
# print("" + str(num) + " is " + str(numLen) + " chars long")
revNum = num[::-1]
# print("" + str(num) + " reversed : " + str(revNum))
remainder = int(len(num)) % 3
print("numLen : " + str(numLen) + "\r\nremainder : " + str(remainder))
if remainder == 0:
	i = 0
	counter = 0
	masterList = []
	l = []
	while i < numLen:
		print(num[i])
		l.append(num[i])
		i+=1
		counter += 1
		if counter == 3:
			counter = 0
			masterList.append(l)
			l = []
elif remainder == 1:
	print("rem1")
	i = 0
	counter = 0
	masterList = []
	l = []
	while i < numLen:
		print(revNum[i])
		l.append(revNum[i])
		i+=1
		counter += 1
		if counter == 3:
			counter = 0
			masterList.append(l[::-1])
			l = []
	masterList.append(list(num[0]))
elif remainder == 2:
	print("rem2")
	i = 0
	counter = 0
	masterList = []
	l = []
	while i < numLen:
		print(revNum[i])
		l.append(revNum[i])
		i+=1
		counter += 1
		if counter == 3:
			counter = 0
			masterList.append(l[::-1])
			l = []
	masterList.append(list(num[0:2]))


print("---------------")
print(masterList)
print("---------------")
for li in masterList:
	if len(li) == 3:
		if int(masterList[1]+masterList[2]) <  20:
			a = int(masterList[0])
			b = int(num1[1]+num1[2])
			print(unit2[a], unit4[3], unit2[b], unit4[z],",")
		elif int(num1[12])==0:
			a = int(num[14])
			b= int(num1[13])
			print(unit2[a], unit4[3], unit2[b], unit4[z],",")
		#turn the numbers in to words
	elif len(li) == 2:
		#different processing
	elif len(li) == 1:
		#another different processing



# def roundup(n):
# 	if n % 3 == 1:
# 		return(n+2)
# 	elif n % 3 == 2:
# 		return(n+1)
# 	else:
# 		return(n)



# x = len(num)
# z = roundup(x)






def oldWay():
	if z==15:
		if int(num[14])==0 and int(num1[13]+num1[12]) < 20:
			b = int(num1[13]+num1[12])
			print(unit2[b], unit4[z],",")
		elif int(num[14])==0 and int(num1[12])==0:
			b= int(num1[13])
			print(unit2[b], unit4[z],",")
		elif int(num1[13]+num1[12]) <  20:
			a = int(num[14])
			b = int(num1[13]+num1[12])
			print(unit2[a], unit4[3], unit2[b], unit4[z],",")
		elif int(num1[12])==0:
			a = int(num[14])
			b= int(num1[13])
			print(unit2[a], unit4[3], unit2[b], unit4[z],",")
		else:
			a = int(num[14])
			b= int(num1[13])
			c= int(num1[12])
			print(unit2[a], unit4[3], unit3[b], unit2[c], unit4[z],",")
		x = x-3
		z = z-3
	if z== 12:
		a=int(num[11])
		if int(num[11])==0 and int(num1[10]+num1[9]) < 20:
			b = int(num1[10]+num1[9])
			print(unit2[b], unit4[z],",")
		elif int(num[11])==0 and int(num1[9])==0:
			b= int(num1[10])
			print(unit2[b], unit4[z],",")
		elif int(num1[10]+num1[9]) <  20:
			a=int(num[11])
			b = int(num1[10]+num1[9])
			print(unit2[a], unit4[3], unit2[b], unit4[z],",")
		elif int(num1[9])==0:
			a=int(num[11])
			b= int(num1[10])
			print(unit2[a], unit4[3], unit2[b], unit4[z],",")
		else:
			a=int(num[11])
			b= int(num1[10])
			c= int(num1[9])
			print(unit2[a], unit4[3], unit3[b], unit2[c], unit4[z],",")
		x = x-3
		z = z-3
	if z== 9:
		if int(num[8])==0 and int(num1[7]+num1[6]) < 20:
			b = int(num1[7]+num1[6])
			print(unit2[b], unit4[z],",")
		elif int(num[8])==0 and int(num1[6])==0:
			b= int(num1[7])
			print(unit2[b], unit4[z],",")
		elif int(num1[7]+num1[6]) <  20:
			a=int(num[8])
			b = int(num1[7]+num1[6])
			print(unit2[a], unit4[3], unit2[b], unit4[z],",")
		elif int(num1[6])==0:
			a=int(num[8])
			b= int(num1[7])
			print(unit2[a], unit4[3], unit2[b], unit4[z],",")
		else:
			a=int(num[8])
			b= int(num1[7])
			c= int(num1[6])
			print(unit2[a], unit4[3], unit3[b], unit2[c], unit4[z],",")
		x = x-3
		z = z-3	
	if z== 6: 
		if int(num[5])==0 and int(num1[4]+num1[3]) < 20:
			b = int(num1[4]+num1[3])
			print(unit2[b], unit4[z],",")
		elif int(num[5])==0 and int(num1[3])==0:
			b= int(num1[4])
			print(unit2[b], unit4[z],",")
		elif int(num1[4]+num1[3]) <  20:
			a=int(num[5])
			b = int(num1[4]+num1[3])
			print(unit2[a], unit4[3], unit2[b],unit4[z],",")
		elif int(num1[3])==0:
			a=int(num[5])
			b= int(num1[4])
			print(unit2[a], unit4[3], unit2[b], unit4[z],",")
		else:
			a=int(num[5])
			b= int(num1[4])
			c= int(num1[3])
			print(unit2[a], unit4[3], unit3[b], unit2[c], unit4[z],",")
		x = x-3
		z = z-3
	if z== 3:
		if int(num[2])==0 and int(num1[1]+num1[0]) < 20:
			b = int(num1[1]+num1[0])
			print(unit2[b], unit4[z],",")
		elif int(num[2])==0 and int(num1[0])==0:
			b= int(num1[1])
			print(unit2[b], unit4[z],",")
		elif int(num1[1]+num1[0]) <  20:
			a=int(num[2])
			b = int(num1[1]+num1[0])
			print(unit2[a], unit4[3], unit2[b])
		elif int(num1[0])==0:
			a=int(num[2])
			b= int(num1[1])
			print(unit2[a], unit4[3], unit2[b])
		else:
			a=int(num[2])
			b= int(num1[1])
			c= int(num1[0])
			print(unit2[a], unit4[3], unit3[b], unit2[c])

	else:
		print(unit1[0])

#look at the numbers in the code and change it to the corresponding ones!!!!
