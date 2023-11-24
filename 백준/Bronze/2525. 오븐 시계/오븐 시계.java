import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int hour = sc.nextInt();
        int minute = sc.nextInt();
        int time = sc.nextInt();

        minute += time;
        if(minute>=60) {
            hour += (int)(minute/60);
            minute -= (int)((minute/60))*60;
        }
        if(hour>=24){
            hour-=(int)(hour/24)*24;
        }
        System.out.printf("%d %d", hour, minute);
    }
}
