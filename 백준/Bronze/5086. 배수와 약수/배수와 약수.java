import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true){
            int x = sc.nextInt();
            int y = sc.nextInt();

            if ((x == 0)&&(y == 0))
                break;

            if (isFactor(x, y))
                System.out.println("factor");
            else if (isMultiple(x, y)) {
                System.out.println("multiple");
            }
            else
                System.out.println("neither");
        }
    }

    private static boolean isMultiple(int x, int y) {
        if (x%y==0)
            return true;
        else
            return false;
    }

    private static boolean isFactor(int x, int y) {
        if (x>y)
            return false;
        if (y%x==0)
            return true;
        return false;
    }
}