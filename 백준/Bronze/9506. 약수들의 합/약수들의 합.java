import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int n = sc.nextInt();
            if (n==-1) break;
            System.out.println(solve(n));
        }
    }

    private static String solve(int n) {
        ArrayList<Integer> arrayList = new ArrayList<>();
        int num = 1;
        while (num<n){
            if (n%num==0)
                arrayList.add(num);
            num++;
        }
        int sum = 0;
        for (int i: arrayList){
            sum+=i;
        }

        String answer = Integer.toString(n);
        if (sum==n){
            answer+=" = ";
            for (int i = 0; i < arrayList.size()-1; i++){
                answer+=arrayList.get(i)+" + ";
            }
            answer+=arrayList.get(arrayList.size()-1);
        }
        else
            answer+=" is NOT perfect.";
        return answer;
    }

}