def questions():
	questions = ["What is the capital of France?","How many planets are on earth?","When did Nigeria gain independence?","Which of the following programming language in Dynamically typed?"]
	
	return questions

def options():
	options = ["A. Paris B. Abuja C. London D. Tokyo","A. 1 B. 8 C. 0 D. 9","A. October 1st 1960 B. June 23rd 2009 C. October 1st 1963 D. June 30th 1934"," A. Java B. Python C. C++ D. JavaScript"]
	return options


def answers():
	answers = ["A","C","A","B"]
	return answers

def check_if_prompt_is_wrong(prompt):
	answer = answers()
	index = -1
	count = 0
	for __ in answer:
		index += 1
		if prompt == answer[index]:
			return "You are correct!!!"
			count += 1
			print("Final score",count)
		else: 
			return "You are wrong!!!"

def score():
	 check_if_prompt_is_wrong(prompt)
	