from Day4_functions import *
	
list = [41,25,49]
index = 0
for numbers in list:
	answer = is_perfect_square(list[index])
	list[index] = answer
	index += 1
print(list)