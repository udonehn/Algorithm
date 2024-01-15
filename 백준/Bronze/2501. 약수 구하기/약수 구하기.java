import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        System.out.println(solve(N, K));
    }

    private static int solve(int N, int K) {
        int count = 0;
        int number = 1;
        while (number<=N){
            if ((N % number) == 0)
                count++;
            if (count==K)
                return number;
            number++;
        }
        return 0;
    }
}