import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int[] x = new int[n];
        for(int x_i=0; x_i < n; x_i++){
            x[x_i] = in.nextInt();
        }
        
        Arrays.sort(x);
        
        int left = 0,right,mid, ans = 0;
        int end;
        
        while(left < n) {
            right = left;
            mid = left;
            ans++;
            
            while(mid < n && x[mid] - x[left] <= k) {
                mid++; // mid will be out
            }
            mid--;
            end = x[mid] + k;
            right = mid + 1;
            
            while(right < n && x[right] <= end) {
                right++;
            }
            left = right;
        }
        
        System.out.println(ans);
    }
}