package src;

import java.util.Scanner;

public class IfElse {
    private static final Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        int n = sc.nextInt();
        sc.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        sc.close();
        if (n % 2 == 1){
            System.out.println("Weird");
        }
        else{
            if (n >= 2 && n <= 5){
                System.out.println("Not Weird");
            }
            else if(n >= 6 && n <=20){
                System.out.println("Weird");
            }
            else{
                System.out.println("Not Weird");
            }
        }
    }
}
