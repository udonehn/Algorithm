import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double result = 0;
        double sum = 0;

        for (int i=0; i<20; i++){
            sc.next();
            double credit = sc.nextDouble();
            String grade = sc.next();
            if (grade.equals("P"))
                continue;
            sum+=credit;
            result+=credit*getGrade(grade);
        }

        System.out.println(result/sum);

    }
    
    static double getGrade(String grade){
        if (grade.equals("A+")){
            return 4.5;
        }
        else if (grade.equals("A0")){
            return 4.0;
        }
        else if (grade.equals("B+")){
            return 3.5;
        }
        else if (grade.equals("B0")){
            return 3.0;
        }
        else if (grade.equals("C+")){
            return 2.5;
        }
        else if (grade.equals("C0")){
            return 2.0;
        }
        else if (grade.equals("D+")){
            return 1.5;
        }
        else if (grade.equals("D0")){
            return 1.0;
        }
        else {
            return 0.0;
        }
    }
}
