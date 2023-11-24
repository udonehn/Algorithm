import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean[][] paper = new boolean[101][101];

        for (int i = 1; i < 101; i++) {
            for (int j = 1; j < 101; j++)
                paper[i][j] = false;
        }

        int N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            int X = sc.nextInt();
            int Y = sc.nextInt();
            for (int row = 0; row < 10; row++) {
                for (int col = 0; col < 10; col++)
                    paper[Y + row][X + col] = true;
            }
        }

        int answer=0;

        for (int i = 1; i < 101; i++){
            for(int j = 1; j < 101; j++)
                if (paper[i][j])
                    answer++;
        }

        System.out.println(answer);
    }
}