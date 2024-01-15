import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        System.out.println(solve(A, B, C));
    }

    private static String solve(int a, int b, int c) {
        if (a+b+c!=180) return "Error";
        if ((a==60)&&(b==60)&&(c==60)) return "Equilateral";
        if ((a==b)||(b==c)||(a==c)) return "Isosceles";
        return "Scalene";
    }
}