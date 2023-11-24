import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        int[] arr = new int[N];

        for (int i = 0; i < N; i++){
            arr[i] = i+1;
        }

        for (int index = 0; index < M; index++){
            int i = sc.nextInt()-1;
            int j = sc.nextInt()-1;

            while(i<j){
                int tmp = arr[j];
                arr[j] = arr[i];
                arr[i] = tmp;
                i++;
                j--;
            }
        }
        for (int i=0; i<N; i++){
            System.out.print(arr[i]+" ");
        }
    }
}
