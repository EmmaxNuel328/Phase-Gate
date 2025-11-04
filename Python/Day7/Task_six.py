number = 0
count = 0
multiples_of_4 = 1;
multiples_of_8 = 1;
for _ in range(10):
	number += 1
	if number % 4 == 0:
		for _ in range(5):
			if number / 4 == 1:
				multiples_of_4 *= number
				print(" ",multiples_of_4,end= "")
			else:
				multiples_of_8 *= number;
				print(" ",multiples_of_8,end = "")
					
