import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double A = sc.nextDouble();
        double B = sc.nextDouble();
        double V = sc.nextDouble();

        System.out.println((int)(Math.ceil((V-A)/(A-B))+1));
    }
}