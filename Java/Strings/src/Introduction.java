import java.io.*;
import java.util.*;

public class Introduction {

    private static String capitalize(String s){
        return Character.toUpperCase(s.charAt(0)) + s.substring(1);
    }
    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        sc.close();
        System.out.println(A.length() + B.length());
        System.out.println(A.compareTo(B)>0 ? "Yes":"No");
        System.out.println(capitalize(A) + " " + capitalize(B));
        
    }
}