// Java End of File

import java.io.*;
import java.util.*;

public class EndOfFile {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = 0;
        while (sc.hasNext()){
            System.out.println(++n + " " + sc.nextLine());
        }
    }
}