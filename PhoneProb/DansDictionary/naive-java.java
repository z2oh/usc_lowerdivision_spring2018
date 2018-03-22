import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n, k;
        n = in.nextInt();
        k = in.nextInt();
        
        String[] dict = new String[n];
        for (int i=0; i<n; i++) {
            dict[i] = in.next();
        }
        
        for (int i=0; i<k; i++) {
            String word = in.next();
            for (int j=0; j<n; j++) {
                if (word.equals(dict[j])) {
                    System.out.println("True");
                    break;
                }
                if (j == n-1) {
                    System.out.println("False");
                }
            }
        }
    }
}
