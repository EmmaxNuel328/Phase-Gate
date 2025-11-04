function getVat(price){
	let vat = 0.075 * price;
return vat;
}
function totalAmount(vat,subtotal){
let total_amount = vat + subtotal;
return total_amount;	
}
const input = require('prompt-sync')();
let count = 0;
let subtotal = 0;
let product_name = "a";
while(count < 4){
let product_name = input("Enter name of product: ");
let product_price = int(input("Enter product price: "));
subtotal += product_price;

let vat = getVat(product_price);
totalAmount(vat,subtotal)
console.log(vat);
count+= 1;
}
console.log(subtotal);
