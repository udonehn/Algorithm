import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num1 = sc.nextInt();
        String num2 = sc.next();
        char[] num2Array = num2.toCharArray();

        for (int i = num2Array.length - 1; i >= 0; i--) {
            System.out.println(num1 * (num2Array[i]-'0'));
        }
        System.out.println(num1 * Integer.parseInt(num2));

    }
}
