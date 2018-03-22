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
        Arrays.sort(dict);
        for (int i=0; i<k; i++) {
            //System.out.println(dict[i]);
            String word = in.next();
            int result = Arrays.binarySearch(dict, word);
            if (result < 0)
                System.out.println("False");
            else
                System.out.println("True");
        }
        
    }
}
