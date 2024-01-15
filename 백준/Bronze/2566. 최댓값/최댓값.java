import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] matrix = new int[9][9];
        for(int i=0; i<9; i++){
            for (int j = 0; j < 9; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }
        int maxNum=0;
        int maxNumColumn=1;
        int maxNumRow=1;
        for(int i=0; i<9; i++){
            for (int j = 0; j < 9; j++) {
                if (matrix[i][j] > maxNum) {
                    maxNum = matrix[i][j];
                    maxNumRow = i + 1;
                    maxNumColumn = j + 1;
                }
            }
        }
        System.out.println(maxNum);
        System.out.println(maxNumRow+" "+maxNumColumn);
    }
}