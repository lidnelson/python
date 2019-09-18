f = open("users.txt","r")
# print(f.read())


l= []
masterlist = {}
counter= 0
iden= 0

for x in f:
	l.append((x).strip("\n"))
	counter += 1
	if counter == 7:
		print(l)
		for x in range(1):
			masterlist[iden]= l
		iden += 1
		counter= 0
		l=[]

print(masterlist)
#creates lists within a dictionary


def nextnumber():
	for x in range(1,1000000):
			b = masterlist[x]
			if x != int(b[0]):
				return x
				break





add = input("Would you like to add a person details?: ") #input for whether the person would like to add details 
add = add.lower() #input to lower case

if add == "yes":
	a = nextnumber() #AUTO increment version of ID
	print("ID: ", a)
	b = input("First Name: ") #input gets saved as b and get written on the next line
	c = input("Second Name: ")
	d = input("Address line 1: ")
	e = input("Address line 2: ")
	f = input("Post code: ")
	g = input("Telephone Number: ")
	a= a +"\n" #added on to string is the opperation to start a new line
	b= b +"\n"
	c= c +"\n"
	d= d +"\n"
	e= e +"\n"
	f= f +"\n"
	g= g +"\n"

	t = open("user.txt", "a")
	t.write(a)
	t.write(b) # writes on its own line 
	t.write(c)
	t.write(d)
	t.write(e)
	t.write(f)
	t.write(g)
	t.close()


# else:
# 	continue

z= len(masterlist)
y= int(z)*7

def check(n):
	found = False
	h = open("users.txt", "r")
	li = []
	for i in range(y):
		li.append((h.readline()).strip("\n"))

	for m in li:
		if m == n:
			found = True
			break
	h.close()
	return found




dlt = input("Would you like to delete someone off the list?: ")
dlt = dlt.lower()

# print("-----------")
# print(masterlist)
# print(masterlist[1])

print("-----------")
# dlt = "yes"
if dlt == "yes":
	a = input("ID: ")
	if check(a)== True:
		c= int(a) -1
		b = masterlist[c]
		print(b[c])
		del b
		h = open("uesrs.txt", "r")

print("Menu")	
print("1 - Identification Number")
print("2 - Firstname")
print("3 - Surname")
print("4 - Address 1")
print("5 - Address 2")
print("6 - Postcode")
print("7 - Telephone Number")




search = int(input("Search by: "))

if search == 1:
	a = input("ID: ")
	if a in masterlist:
		a= int(a)-1
		print(masterlist(a))
elif search == 2:
	a = input("Firstname: ")
	if a in masterlist:
		for x in masterlist:
			b = masterlist[x]
			if b.index(a) == 1:
				print(b)

elif search == 3:
	a = input("Surname: ")
	if a in masterlist:
		for x in masterlist:
			b = masterlist[x]
			if b.index(a) == 2:
				print(b)
elif search == 4:
	a = input("Address Line 1: ")
	if a in masterlist:
		for x in masterlist:
			b = masterlist[x]
			if b.index(a) == 3:
				print(b)
elif search == 5:
	a = input("Address Line 2: ")
	if a in masterlist:
		for x in masterlist:
			b = masterlist[x]
			if b.index(a) == 4:
				print(b)
elif search == 6:
	a = input("Post Code: ")
	if a in masterlist:
		for x in masterlist:
			b = masterlist[x]
			if b.index(a) == 5:
				print(b)
elif search == 7:
	a = input("Telephone Number: ")
	if a in masterlist:
		for x in masterlist:
			b = masterlist[x]
			if b.index(a) == 6:
				print(b)
else:
	print("Try Again, Read Menu")


# user = open("users.txt","r")

# user2 = copy(user)
# print(l)
# print("--------")
# print(masterlist)






