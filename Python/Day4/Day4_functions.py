def is_perfect_square(numbers):
	number = 0
	for factor in range(numbers):
		number += 1
		if numbers ** 0.5 == number:
			return True
	return False
				
			
				
#print( is_perfect_square(prompt = []))