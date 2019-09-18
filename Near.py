word1= input("type word here: ")
word2 = input("type word here: ")

length1= len(word1)
length2= len(word2)

Difference= length1 -length2
x= search ([word2], word1)
print(x)

if Difference== 1:
	print (True)
else:
	print(False)
