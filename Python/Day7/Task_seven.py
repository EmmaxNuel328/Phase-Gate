number = 0
count = 0
multiples_of_4 = 1;
multiples_of_8 = 1;
sum_of_multiples_of_4 = 0;
sum_of_multiples_of_8 = 0;



for _ in range(10):
	number += 1
	if number % 4 == 0:
		for _ in range(5):
			if number / 4 == 1:
				multiples_of_4 *= number
				sum_of_multiples_of_4 += multiples_of_4
			else:
				multiples_of_8 *= number;
				sum_of_multiples_of_8 += multiples_of_8
				
print(sum_of_multiples_of_4,sum_of_multiples_of_8)
					
