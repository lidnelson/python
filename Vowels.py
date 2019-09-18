word = input("enter word here: ")
vowel = "aeiou"
count = 0

for char in word:
	if char in vowel:
		count+=1
		print(count)
print("Total vowels:", count )
