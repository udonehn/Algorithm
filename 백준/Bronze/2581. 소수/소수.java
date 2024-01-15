import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();
        int N = sc.nextInt();

        solve(M, N);
    }

    private static void solve(int M, int N) {
        boolean[] eratos = new boolean[N + 1];
        for (int i = 2; i <= N; i++) {
            eratos[i] = true;
        }
        for (int i = 2; i <= N; i++) {
            if (!eratos[i]) continue;
            eratos[i] = true;
            int index = 2;
            while (i * index <= N) {
                eratos[i * index] = false;
                index++;
            }
        }
        int sum = 0;
        for (int i = M; i <= N; i++) {
            if(eratos[i])
                sum+=i;
        }
        if (sum==0)
            System.out.println(-1);
        else {
            System.out.println(sum);
            int i = M;
            while(true){
                if (eratos[i]) {
                    System.out.println(i);
                    break;
                }
                i++;
            }
        }
    }
}