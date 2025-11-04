let first_number;
let second_number;
let multiples_of_4 = 1;
let multiples_of_8 = 1;
let sum_of_multiples_of_4 = 0;
let sum_of_multiples_of_8 = 0;


for(let number = 1; number < 11; number++){
if(number % 4 == 0){
for(let count = 1; count <= 5; count++){
if(number / 4 == 1){
multiples_of_4 *= number;
sum_of_multiples_of_4 += multiples_of_4
}
else{
multiples_of_8 *= number;
sum_of_multiples_of_8 += multiples_of_8;

}

}

}
}
let sum_of_multiples_of_4_and_8 = sum_of_multiples_of_4 + sum_of_multiples_of_8;
console.log(sum_of_multiples_of_4_and_8);

