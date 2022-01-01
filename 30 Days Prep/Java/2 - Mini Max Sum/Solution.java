import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'miniMaxSum' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void miniMaxSum(List<Integer> arr) {
    // Write your code here
        long[] m = new long[arr.size()];
        long sum = 0;
        for(int i=0;i<arr.size();i++){
            sum += arr.get(i);
        }
        for(int i = 0; i < arr.size(); i++){
            m[i] = sum - arr.get(i);
        }
        long min = m[0];
        long max = m[0];
        for(int k=1;k<arr.size();k++){
            if(m[k]<min){
                min=m[k];
            }
            if(m[k]>max){
                max=m[k];
            }
        }
        System.out.print(min + " " + max);
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.miniMaxSum(arr);

        bufferedReader.close();
    }
}
