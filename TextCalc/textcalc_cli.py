data = input("Enter text to analyze : ")


list_of_chars = list(data)
nos = 0
capitals = 0
smalls = 0
spaces = 0
special_symbols = 0
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = list("0123456789")
caps = list(alpha)
smls = list(alpha.lower())

print(list_of_chars)
print("ok1")
for char in list_of_chars :
	if " " in char:
		spaces += 1
	elif char in caps :
		capitals += 1
	elif char in smls :
		smalls += 1
	elif char in nums:
		nos += 1
	else :
		special_symbols += 1



print("Numbers :",nos)
print("Capitals :",capitals)
print("Smalls :",smalls)
print("Spaces :",spaces)
print("Special Symbols :",special_symbols)

