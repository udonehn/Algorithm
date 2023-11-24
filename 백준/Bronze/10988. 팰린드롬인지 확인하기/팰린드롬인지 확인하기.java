import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        char[] charArray = s.toCharArray();
        System.out.println(solve(charArray));
    }
    static int solve(char[] charArray){
        int left = 0;
        int right = charArray.length-1;

        while (left<right){
            if (charArray[left]!=charArray[right]){
                return 0;
            }
            right-=1;
            left+=1;
        }
        return 1;
    }

}
