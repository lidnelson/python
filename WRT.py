file = open("teams.txt","w")

file.write("Aresnal \n")
file.write("Tottenham \n")
file.write("Manchester Uninted \n")
file.write("Manchester City \n")
file.write("Liverpool \n")

file = open ("teams.txt", "r")
print(file.readline())
print(file.readline())

file.close()