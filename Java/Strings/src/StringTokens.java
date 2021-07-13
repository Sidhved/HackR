import java.io.*;
import java.util.*;

public class StringTokens {

    public static String remNonLetters(String s){
        int i;
        for(i = 0; i<s.length(); i++){
            if(Character.isLetter(s.charAt(i)))
                break;
        }
        return s.substring(i);
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        scan.close();
        s = remNonLetters(s);

        if (s.length() == 0){
            System.out.println(0);
            return;
        }

        String [] words = s.split("[^a-zA-Z]+");

        System.out.println(words.length);
        for (String word : words){
            System.out.println(word);
        }
    }
}
