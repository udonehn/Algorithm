import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int result=0;
        String st = sc.next();
        for(int s:st.toCharArray()){
            if (s==90)
                s-=2;
            else if (s>=83)
                s-=1;
            int num = s-65;

            result+=num/3+3;
        }
        System.out.println(result);
    }
}
