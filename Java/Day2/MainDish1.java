public class MainDish1{

	public String reverse(String prompt){	
			
		String newWord = "";
		String reversedWord = " ";
		for(int index = 0; index < prompt.length(); index++){
		char letter = prompt.charAt(index);
				 if(letter == 'd'){
			break;
		
		}
		newWord += letter;
		
		}
					
		return newWord;	
	}
							

}