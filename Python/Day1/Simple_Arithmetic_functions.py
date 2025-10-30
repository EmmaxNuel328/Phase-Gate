import random
generator1 = random.randint(1,20)
generator2 = random.randint(1,20)
def generate_random_first_number():
	first_number = random.randint(generator1,30)
	return first_number
	
def generate_random_second_number():
	second_number = random.randint(generator2,30)
	return second_number




def generate_subtraction_problem(prompt):
	first_number = generate_random_first_number()
	second_number = generate_random_second_number()
	if first_number < second_number:
		print(second_number, '-', first_number)
		result = second_number - first_number
	else:
		print(first_number, "-", second_number)
		result = first_number - second_number
	return result