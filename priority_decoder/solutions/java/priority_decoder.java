import java.io.*;
import java.util.*;


public class priority_decoder {

    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());

        for (int i = 0 ; i < n ; i ++) {
            int line = sc.nextInt();
            if (line == 1) {
                System.out.println(i);
            }
        }

    }
}
