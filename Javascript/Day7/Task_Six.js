let first_number;
let second_number;
let multiples_of_4 = 1;
let multiples_of_8 = 1;
for(let number = 1; number < 11; number++){
if(number % 4 == 0){
for(let count = 1; count <= 5; count++){
if(number / 4 == 1){
multiples_of_4 *= number;
console.log(multiples_of_4);
}
else{
multiples_of_8 *= number; 
console.log(multiples_of_8);

}

}
console.log(" ");
}
}