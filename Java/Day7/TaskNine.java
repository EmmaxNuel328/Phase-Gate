public class TaskNine{
public static void main(String[] args){
int numbers = 0;
int multiplesOf4 = 1;
int multiplesOf8 = 1;
int sumOfMultiplesOf4 = 0;
int sumOfMultiplesOf8 = 0;


for(numbers = 1; numbers < 11; numbers ++){
if(numbers % 4 == 0){
for(int count = 1; count < 6; count++){
if(numbers / 4 == 1){
multiplesOf4 *= numbers;
sumOfMultiplesOf4 += multiplesOf4;
}
else{
multiplesOf8 *= numbers;
sumOfMultiplesOf8 += multiplesOf8;
}

}

}
}
int sumOfMultiplesOf4Of8 = sumOfMultiplesOf4 + sumOfMultiplesOf8;
int squareOfsumOfMultiplesOf4Of8 = sumOfMultiplesOf4Of8 * sumOfMultiplesOf4Of8;
System.out.print(squareOfsumOfMultiplesOf4Of8);
}
}

