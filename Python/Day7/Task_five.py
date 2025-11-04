number = 0
count = 0
for _ in range(10):
	number += 1
	if number % 4 == 0:
		for _ in range(5):
			if number / 4 == 1:
				first_number = number
				print(first_number,end= "")
			else:
				second_number = number
				print(second_number,end = "")
					
