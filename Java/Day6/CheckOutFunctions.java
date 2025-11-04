public class CheckOutFunctions{
public double getVat(double price){
double vat = 0.075 * price;
	return vat;
}

public double getSubtotal(double price,double vat){
double subtotal = price + vat;
return subtotal;


}


public double getTotal(double subtotal,double vat){
double total = subtotal + vat;
return total;


}
 
public double getBalance(double payment,double total){
double balance = payment - total;
return balance; 


}

}




