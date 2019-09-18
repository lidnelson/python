def roundup(n):
	if n % 3 == 1:
		return(n+2)
	elif n % 3 == 2:
		return(n+1)
	else:
		return(n)


print(roundup(4))
