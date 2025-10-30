from Modified_Quiz_Game_Functions import *

counter = 0
questions = questions()
options = options()
answer = answers()
prompt_list = []
index = 0
while counter < 4:
	print(questions[index])
	print(options[index])
	prompt = input("Enter your answer: ").upper()
	answer[index]
	prompt_list.append(prompt)
	if prompt_list[index] == answer[index]:
		print("You are correct!!!")
	else:
		print("You are wrong!!!")
	index += 1
	counter += 1
	
