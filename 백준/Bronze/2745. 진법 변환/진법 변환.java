import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] str = sc.next().toCharArray();
        int B = sc.nextInt();
        int result = 0;
        for (int i = 0; i<str.length; i++){
            int temp = (int)(str[i]-'0');
            if (temp>=17){ //문자
                result+=Math.pow(B,str.length-1-i)*(temp-7);
            }
            else { //숫자
                result+=Math.pow(B,str.length-1-i)*temp;
            }
        }
        System.out.println(result);
    }
}