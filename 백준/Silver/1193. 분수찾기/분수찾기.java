import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int X = sc.nextInt();
        System.out.println(solve(X));
    }

    private static String solve(int X) {
        HashMap<String, Integer> map = findMin(X);
        int count = map.get("minNum");
        int bigNum = map.get("bigNum");
        int smallNum = 1;
        while (count != X){
            bigNum--;
            smallNum++;
            count++;
        }
        if (map.get("isRightBig") == 1)
            return smallNum + "/" + bigNum;
        else
            return bigNum + "/" + smallNum;
    }

    private static HashMap<String, Integer> findMin(int X) {
        HashMap<String, Integer> resultMap = new HashMap<>();
        int minNum = 1;
        int num = 1;
        int isRightBig = 0;
        while (true){
            if (minNum + num > X) {
                resultMap.put("minNum", minNum);
                resultMap.put("isRightBig", isRightBig);
                resultMap.put("bigNum", num);
                return resultMap;
            }
            minNum = minNum + num;
            num++;
            if (isRightBig == 0)
                isRightBig = 1;
            else
                isRightBig = 0;
        }
    }
}