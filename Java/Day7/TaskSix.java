public class TaskSix{
public static void main(String[] args){
int numbers = 0;
int multiplesOf4 = 1;
int mulitplesOf8 = 1;
for(numbers = 1; numbers < 11; numbers ++){
if(numbers % 4 == 0){
for(int count = 1; count < 6; count++){
if(numbers / 4 == 1){
multiplesOf4 *= numbers;
System.out.print(" " + multiplesOf4 + " ");
}
else{
mulitplesOf8 *= numbers;
System.out.print("\t" + mulitplesOf8 + " ");
}

}


}

}

}



}