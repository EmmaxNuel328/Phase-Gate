import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestMainDish1{
	@Test
	public void testThatReversefunctionReturnsReverse(){
	MainDish1 mainDish = new MainDish1();
	String result = mainDish.reverse("Emdma");
	assertEquals("Em",result);



}


}