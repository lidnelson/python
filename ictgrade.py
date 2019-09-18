Name = input("Enter your name here: ")
Homework = int(input("Enter your homework mark here: "))
Assessment = int(input("Enter your assessment mark here: "))
Exam = int(input("Enter your exam mark here:"))

def percentage(number1, number2):
	value = (number1/number2)*100
	return value

print("Homework", percentage(Homework, 25), "%")
print("Assessment", percentage(Assessment,50), "%")
print("Exam", percentage(Exam, 100), "%")

a=percentage(Homework, 25)
b=percentage(Assessment,50)
c=percentage(Exam, 100)

print(Name)
if (a+b+c)/3>=90:
	print("A")
elif(a+b+c)/3>=80:
	print("B")
elif(a+b+c)/3>=70:
	print("C")
elif(a+b+c)/3>=60:
	print("D")
elif(a+b+c)/3>=50:
	print("E")
elif(a+b+c)/3<=40:
	print("F")

OverallWeightedGrade= round(a*0.25 + b*0.35 +c*0.4,2)

print(OverallWeightedGrade, "%")