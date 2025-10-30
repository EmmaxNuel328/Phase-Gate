import java.util.Scanner;
public class SimpleArithmeticApp{
public static void main(String[] args){
	int first = (int)(Math.random() * 101);
	int second= (int)(Math.random() * 101);
	

	for(int count = 1; count <= 10; count ++){
		int firstNumber = (int)(Math.random() * first);
		int secondNumber = (int)(Math.random() * second);
		
		if(firstNumber < secondNumber){
			System.out.println(secondNumber+ "-"+ firstNumber);
			int formula = secondNumber - firstNumber;
		}
		else{
			System.out.println(firstNumber+ "-"+ secondNumber);
			int formula = secondNumber - firstNumber;
		}

	}
}
}