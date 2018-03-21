import java.util.Enumeration;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Derivatives {    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // trash
        String numLines = sc.nextLine();
        while (sc.hasNext()) {
            String test = sc.nextLine();
            String[] vals = test.split("[+]"); 
            // might be less, but never more.

            List<String> ret = new ArrayList<>();
            
            for(int i = 0; i<vals.length;i++) {
                if(vals[i].contains("x^")) {
                    String[] term = vals[i].split("x\\^");
                    int val1;
                    int val2;

                    if (term.length == 2 && !term[0].isEmpty()) {
                        val1 = Integer.valueOf(term[0]);
                        val2 = Integer.valueOf(term[1]);
    
                        if (val2 == 2) {
                            ret.add(val1 * val2 + "x");
                        }
                        else {
                            ret.add(val1 * val2 + "x^" + (val2 - 1));
                        }
                    } 
                    else if(term.length == 2 && term[0].isEmpty()) {
                        int val = Integer.valueOf(term[1]);
                        if ((val - 1) == 1) {
                            ret.add(val + "x");
                        }
                        else {
                            ret.add(val + "x^" + (val - 1));
                        }
                    }
                    
                }
                else if (vals[i].contains("x")) {
                    String[] term = vals[i].split("x");
                    if(term.length != 0) {
                        ret.add(term[0]);
                    }
                    else {
                        ret.add("" + 1);
                    }
                }
                else { 
                    if (vals.length == 1) {
                        ret.add("0");
                    }
                /* ignore single int */}
            }
            System.out.println(String.join("+", ret));
        }
        sc.close();
    }
}