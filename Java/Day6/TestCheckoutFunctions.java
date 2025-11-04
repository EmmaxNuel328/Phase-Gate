import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;


public class TestCheckoutFunctions{
@Test
public void testThatGetVatReturnsCorrectValue(){
CheckOutFunctions checkout = new CheckOutFunctions();

double result = checkout.getVat(200);
assertEquals(result,15.0);
}

@Test
public void testThatGetSubtotalReturnsCorrectValue(){
CheckOutFunctions checkout = new CheckOutFunctions();

double result = checkout.getSubtotal(200,15);
assertEquals(result,215);
}

@Test
public void testThatGetTotalReturnsCorrectValue(){
CheckOutFunctions checkout = new CheckOutFunctions();

double result = checkout.getTotal(1000,15);
assertEquals(result,1015);
}


@Test
public void testThatGetBalanceReturnsCorrectValue(){
CheckOutFunctions checkout = new CheckOutFunctions();

double result = checkout.getBalance(20,15);
assertEquals(result,5);
}








}