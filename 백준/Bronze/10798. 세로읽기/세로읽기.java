import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char [][] arr = new char[5][15];
        int [] max_length_in_array = new int[5];

        int max_size = 0;
        for (int i=0;i<5;i++){
            String str = sc.next();
            char[] charArray = str.toCharArray();
            int len = charArray.length;
            if (len>max_size)
                max_size=len;
            max_length_in_array[i]=len;

            for (int j=0;j<len;j++)
                arr[i][j]=charArray[j];
        }
        for(int i=0; i<max_size; i++){
            for(int j=0; j<5; j++) {
                if (max_length_in_array[j]-1<i)
                    continue;
                System.out.print(arr[j][i]);
            }
        }
    }
}