import random
generator1 = random.randint(2000,10000)
generator2 = random.randint(1,10000)
def generate_random_first_number():
	first_number = random.randint(generator1,400000)
	return first_number
	
def generate_random_second_number():
	second_number = random.randint(generator2,400000)
	return second_number

def generate_subtraction_problem():
	first_number = generate_random_first_number()
	second_number = generate_random_second_number()
	result = first_number - second_number
	print(first_number, "-", second_number)
	return "you have two attempts!!!"
	
def calculate_score(prompt):
	first_number = random.randint(generator1,400000)

	second_number = generate_random_second_number()
	#result = first_number - second_number
	print(first_number, "-", second_number)
	#return "you have two attempts!!!"


			
	
		