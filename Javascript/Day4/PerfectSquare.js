function isPerfectSquare(prompt){
		for(number = 1;number <= prompt;number += 1){
			if(prompt ** 0.5 == number){
			return true
				}
			}
			return false
			
			
	}
			



const myArray = [2,169,4,16,25,100] 
let index = 0
while(index < myArray.length){	
	answer = isPerfectSquare(myArray[index])
	myArray[index] = answer
	index++
	}
console.log(myArray)


