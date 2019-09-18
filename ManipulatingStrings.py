string= list(range(51))
del string[0]

string1 = list(range(51,61))

string.extend(string1)
#string.append(51)
#string.append(52)
#string.append(53)
#string.append(54)
#string.append(55)
#string.append(56)
#string.append(57)
#string.append(58)
#string.append(59)
#string.append(60)
print(string)
print(string[1:61:2])
print(string[2:61:3])
