from Modified_Quiz_Game_Functions import *

counter = 0
questions = questions()
options = options()
index = 0
while counter <= 10:
	print(questions[index])
	print(options[index])
	prompt = input("Enter answer: ")
	index += 1
	print(check_if_prompt_is_wrong(prompt))
	
	
counter += 1
