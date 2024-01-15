import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int B = sc.nextInt();
        String answer="";
        while (N>=B){
            int remainder = N%B;
            N=N/B;
            if (remainder<10)
                answer=Integer.toString(remainder)+answer;
            else{
                answer=String.valueOf((char)(remainder+55))+answer;
            }
        }
        if (N<10)
            answer=Integer.toString(N)+answer;
        else{
            answer=String.valueOf((char)(N+55))+answer;
        }
        System.out.println(answer);
    }
}