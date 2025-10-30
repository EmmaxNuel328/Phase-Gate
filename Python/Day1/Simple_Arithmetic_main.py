from Simple_Arithmetic_functions import *
count = 0
prompt = 1
for item in range(10):
	#print(first_number, "-", second_number)
	generator = (generate_subtraction_problem(prompt))
	prompt1 = int(input("Enter your answer: "))
	if prompt1 != generator:
		print("Try again!!!")
	prompt2 = int(input("Enter your answer: "))
	if prompt2 == generator:
		print(prompt2,"is the correct answer")
	else:
		print("Correct answer equals to",generator)			
	if prompt1 == generator or prompt2 == generator:
		count +=1
	else
if count >=  0 and count <= 5:
	print("your final score is:",count,"/",10)
	print("You can do better!!!")
	sad_face = """
			*****************
	               *                 *
		      *     o       o     *
	 	     *                     *
		     *                     *
		      *     ..........    *
		       *                 *
			*****************
		   """
	print(sad_face)

if count >= 8 and count == 10:
	print("your final score is:",count,"/",10)
	print("You must be a math genius!!!")
	happy_face = """
			*****************
	               *                 *
		      *     o       o     *
	 	     *                     *
		     *                     *
		      *     "       "     *
		       *    ''''''''     *
			*****************
		   """
	print(happy_face)

if count >= 6 and count <= 7:
	print(count)
	print("You can do better!!!")
	little_happy_face = """
			*****************
	               *                 *
		      *     o       o     *
	 	     *                     *
		     *                     *
		      *     ""_____""     *
		       *                 *
			*****************
		   """
	print(little_happy_face)
		
	

	
		
