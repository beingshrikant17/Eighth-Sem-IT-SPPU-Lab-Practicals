import java.rmi.Naming;

public class ArithmeticClient {
    public static void main(String[] args) {
        try {
            String url = "rmi://localhost/ArithmeticService";
            ArithmeticService arithmeticService = (ArithmeticService) Naming.lookup(url);

            int a = 10;
            int b = 5;

            System.out.println("Adding: " + a + " + " + b + " = " + arithmeticService.add(a, b));
            System.out.println("Subtracting: " + a + " - " + b + " = " + arithmeticService.subtract(a, b));
            System.out.println("Multiplying: " + a + " * " + b + " = " + arithmeticService.multiply(a, b));
            System.out.println("Dividing: " + a + " / " + b + " = " + arithmeticService.divide(a, b));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
