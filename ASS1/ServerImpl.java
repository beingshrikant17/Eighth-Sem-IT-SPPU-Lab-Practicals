import java.rmi.*;
import java.rmi.server.*;
import java.util.concurrent.*;

public class ServerImpl extends UnicastRemoteObject implements ServerIntf {
    private ExecutorService executor;

    public ServerImpl() throws RemoteException {
        executor = Executors.newFixedThreadPool(10); // Adjust the pool size as needed
    }

    public String stringJoin(String str1, String str2) throws RemoteException {
        // Example implementation of the stringJoin method
        return str1 + str2;
    }

    public void processRequest(String str1, String str2) {
        // Process the client request in a separate thread
        executor.execute(() -> {
            try {
                String result = stringJoin(str1, str2);
                System.out.println("Client request processed. Result: " + result);
            } catch (RemoteException e) {
                System.out.println("Error processing client request: " + e.getMessage());
            }
        });
    }

    public static void main(String[] args) {
        try {
            // Create a new instance of the server implementation
            ServerImpl serverImpl = new ServerImpl();

            // Bind the server implementation to the RMI registry
            Naming.rebind("Server", serverImpl);

            System.out.println("Server Started....");
        } catch (Exception e) {
            System.out.println("Exception Occurred At Server!" + e.getMessage());
}}
}