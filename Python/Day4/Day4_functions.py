def is_perfect_square(prompt):
	number = 0
	for numbers in range(prompt):
		number += 1
		if prompt ** 0.5 == number:
			return True
	return False
				
			
				
#print( is_perfect_square(prompt = []))