import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class DepreciationTest{
@Test
public void testThatDepreciationFunctionReturnsCorrectValue(){
Depreciation depreciation = new Depreciation();

int result = depreciation.depreciate(50000);
assertEquals(result,0);


}



}