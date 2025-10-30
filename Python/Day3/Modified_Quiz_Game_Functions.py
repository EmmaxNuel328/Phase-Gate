def questions():
	questions = ["1. What is the capital of France?","2. How many planets are on earth?","3. When did Nigeria gain independence?","4. Which of the following programming language in Dynamically typed?"]	
	return questions

def options():
	options = ["A. Paris B. Abuja C. London D. Tokyo","A. 1 B. 8 C. 0 D. 9","A. October 1st 1960 B. June 23rd 2009 C. October 1st 1963 D. June 30th 1934"," A. Java B. Python C. C++ D. JavaScript"]
	return options


def answers():
	answers = ["A","C","A","B"]
	return answers

def check_if_prompt_is_wrong(prompt):
	answer = answers()
	question = questions()
	index = 0
	for a in answer:
		#print("Answer: ",a)
		if answer[index] == prompt:
			return "You are correct!!!"
	index += 1
	
		
	#	else:
	#		return "You are wrong!!!"
#	 check_if_prompt_is_wrong(prompt)
	