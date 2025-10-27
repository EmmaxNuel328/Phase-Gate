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
	globalresult = first_number - second_number
	print(first_number, "-", second_number)
	count = 0
	add = 0
	#for
	return "GoodLuck" 

def add_score(prompt):
	count = 0
	for _ in range(10):		
		if prompt == result:
			count += 1
		return count	