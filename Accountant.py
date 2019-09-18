value= 100
interest = 0.1
year=0

while value <= 1000:
	year+=1
	value = round(value*interest+ value,2)
	print("Year", year, value, "pounds")
