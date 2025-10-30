function isPerfectSquare(prompt){
		factor = 0
		for(number = 1;number <= prompt;number += 1){
			if(prompt ** 0.5 == number){
			return true
				}
			}
			return false
			
			
	}
			



const myArray = [2,4,16,25,12] 
let index = 0
while(index < myArray[index]){	
	answer = isPerfectSquare(myArray[index])
	myArray[index] = answer
	index++
	}
console.log(myArray)


