import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        while (N!=1){
            int i = 2;
            while (N%i!=0){
                i++;
            }
            N/=i;
            System.out.println(i);
        }
    }
}