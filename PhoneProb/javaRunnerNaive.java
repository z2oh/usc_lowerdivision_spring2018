import java.util.*;
import java.lang.*;
import java.io.*;

public class javaRunnerNaive{
public static void main(String[] args) {
	long start = System.currentTimeMillis();
	
	Scanner in = new Scanner(System.in);
	int H = Integer.parseInt(in.next());
	int K = Integer.parseInt(in.next());
	
	int[] dict = new int[H];
	for (int i=0; i<H; i++) {
		dict[i] = in.nextInt();
	}
		
	int count = 0;
	for (int i=0; i<K; i++) {
		int check = in.nextInt();
		for (int j=0; j<H; j++) {
			if (check == dict[j]) {
				count++;
				break;
			} 
		} 	
	}
	System.out.println(count);
	long end = System.currentTimeMillis();
	System.out.println("Execution time: " + (end-start) + "ms");
}
}
