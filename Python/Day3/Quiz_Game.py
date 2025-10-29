number_picked = []	
counter = 1
index = 0
score_counter = 0
for counter in range(10):	
	first_user_input = input("Enter number(1 - 10):")
	number_picked.append(first_user_input)
	counter += 1
	
	match first_user_input:
		case "1":
			question_one = """
1. What is the capital of France?
A. Paris B. Abuja C. London D. Tokyo
		"""			
			print(question_one)
			question_one_user_input = input("Enter your answer(A,B,C,D,E):").upper()
			match question_one_user_input:
				case "A":
					print("You are correct!!!")
					score_counter += 1		
				case "B":
					print("You are wrong!!!")
				case "C":
					print("You are wrong!!!")		
				case "D":
					print("You are wrong!!!")
				case _: 
					print("Wrong input!!!","\n","it will be assumed that you failed the question!!!")
		

	
					

		case "2":
			question_two = """
2. How many planets are on earth?
   A. 1 B. 8 C. 0 D. 9
		"""
			print(question_two)
			question_two_user_input = input("Enter your answer(A,B,C,D,E):").upper()
			match question_two_user_input:
				case "A":
					print("You are wrong!!!")		
				case "B":
					print("You are wrong!!!")
				case "C":
					print("You are correct!!!")
					score_counter += 1		
				case "D":
					print("You are wrong!!!")
				case _: 
					print("Wrong input!!!","\n","it will be assumed that you failed the question!!!"
)




		case "3":
			question_three = """
3. When did Nigeria gain independence?
   A. October 1st 1960 B. June 23rd 2009 C. October 1st 1963 D. June 30th 1934
		"""
			print(question_three)
			question_three_user_input = input("Enter your answer(A,B,C,D,E):").upper()
			match question_three_user_input:
				case "A":
					print("You are correct!!!")
					score_counter += 1
		
				case "B":
					print("You are wrong!!!")
				case "C":
					print("You are wrong!!!")		
				case "D":
					print("You are wrong!!!")
				case _: 
					print("Wrong input!!!","\n","it will be assumed that you failed the question!!!"
)



		case "4":
			question_four = """
4. Which of the following programming language in Dynamically typed?
   A. Java B. Python C. C++ D. JavaScript
"""
			print(question_four)
			question_four_user_input = input("Enter your answer(A,B,C,D,E):").upper()
			match question_four_user_input:
				case "A":
					print("You are wrong!!!")
				case "B":
					print("You are correct!!!")
					score_counter += 1
				case "C":
					print("You are wrong!!!")		
				case "D":
					print("You are wrong!!!")
				case _: 
					print("Wrong input!!!","\n","it will be assumed that you failed the question!!!"
)



		case "5":
			question_five = """
5. What does this "Arigato"mean in Japanese?
   A. thank you B. Welcome C. ByeBye D. Good morning 

"""
			print(question_five)
			question_five_user_input = input("Enter your answer(A,B,C,D,E):").upper()
			match question_five_user_input:
				case "A":
					print("You are correct!!!")
					score_counter += 1
				case "B":
					print("You are wrong!!!")
				case "C":
					print("You are wrong!!!")		
				case "D":
					print("You are wrong!!!")
				case _: 
					print("Wrong input!!!","\n","it will be assumed that you failed the question!!!"
)



		case "6":
			question_six = """
5. What is the percentage of Nitrogen in the atmosphere?
   A. 28% B. 1.3%  C. 78% D. 21% 

"""
			print(question_six)
			question_six_user_input = input("Enter your answer(A,B,C,D,E):").upper()
			match question_six_user_input:
				case "A":
					print("You are wrong!!!")
				case "B":
					print("You are wrong!!!")
				case "C":
					print("You are correct!!!")
					score_counter += 1		
				case "D":
					print("You are wrong!!!")
				case _: 
					print("Wrong input!!!","\n","it will be assumed that you failed the question!!!"
)

		case "7":
			question_seven = """
7. What is the chemical formula for laughing gas?
   A. H2O B. NO C. 2NO D. N2O 

"""
			print(question_seven)
			question_seven_user_input = input("Enter your answer(A,B,C,D,E):").upper()
			match question_seven_user_input:
				case "A":
					print("You are wrong!!!")
				case "B":
					print("You are wrong!!!")
				case "C":
					print("You are wrong!!!")		
				case "D":
					print("You are correct!!!")
					score_counter += 1
				case _: 
					print("Wrong input!!!","\n","it will be assumed that you failed the question!!!"
)

		case "8":
			question_eight = """
8. Where is the statue of liberty located?
   A. New York,USA B. Washington DC,USA C. Lagos,NIGERIA D. UNILAG,NIGERIA

"""
			print(question_eight)
			question_eight_user_input = input("Enter your answer(A,B,C,D,E):").upper()
			match question_eight_user_input:
				case "A":
					print("You are correct!!!")
					score_counter += 1
				case "B":
					print("You are wrong!!!")
				case "C":
					print("You are wrong!!!")		
				case "D":
					print("You are wrong!!!")
				case _: 
					print("Wrong input!!!","\n","it will be assumed that you failed the question!!!"
)

		case "9":
			question_nine = """
9. Who is the founder of TIKTOK?
   A. Zhang Yiming B. Bill Gates C. Bola Ahmed Tinubu D. Mark Zuckerberg
"""
			print(question_nine)
			question_nine_user_input = input("Enter your answer(A,B,C,D,E):").upper()
			match question_nine_user_input:
				case "A":
					print("You are correct!!!")
					score_counter += 1
				case "B":
					print("You are wrong!!!")
				case "C":
					print("You are wrong!!!")		
				case "D":
					print("You are wrong!!!")
				case _: 
					print("Wrong input!!!","\n","it will be assumed that you failed the question!!!"
)


		case "10":
			question_ten = """
9. who won Ballon d'or of 1956?
   A. Omar Sivori B. Lionel Messi C. Luis Suarez D. Stanley Matthews
"""
			print(question_ten)
			question_ten_user_input = input("Enter your answer(A,B,C,D,E):").upper()
			match question_ten_user_input:
				case "A":
					print("You are wrong!!!")
				case "B":
					print("You are wrong!!!")
				case "C":
					print("You are wrong!!!")		
				case "D":
					print("You are correct!!!")
					score_counter += 1
				case _: 
					print("Wrong input!!!","\n","it will be assumed that you failed the question!!!")
		case _:
			print("Wrong input!!!","\n","You have failed!!!")
	

print("You got",score_counter,"Out of 10")

		