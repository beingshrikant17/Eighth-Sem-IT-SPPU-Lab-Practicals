import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class ArithmeticServiceImpl extends UnicastRemoteObject implements ArithmeticService {
    public ArithmeticServiceImpl() throws RemoteException {
        super();
    }

    @Override
    public int add(int a, int b) throws RemoteException {
        return a + b;
    }

    @Override
    public int subtract(int a, int b) throws RemoteException {
        return a - b;
    }

    @Override
    public int multiply(int a, int b) throws RemoteException {
        return a * b;
    }

    @Override
    public double divide(int a, int b) throws RemoteException {
        if (b == 0) {
            throw new RemoteException("Cannot divide by zero");
        }
        return (double) a / b;
    }

    public static void main(String[] args) {
        try {
             ArithmeticService arithmeticService = new ArithmeticServiceImpl();
            java.rmi.Naming.rebind("rmi://localhost/ArithmeticService", arithmeticService);
            System.out.println("ArithmeticService is ready on port.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

