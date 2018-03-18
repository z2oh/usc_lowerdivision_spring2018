/** This is a solution for my CSCE145/146 Division Code-a-thon Problem for Spring 2018
 * 
 */
import java.util.Scanner;

/**
 * @author brady
 *
 */
public class Main {
    public static void main(String args[]) {
        int length = 1;
        int width = 1;
        int start = 0;
        String direction = "SE";
        int playerHits = 0;
        
        Scanner scan = new Scanner(System.in);
        
        length = scan.nextInt();
        width = scan.nextInt();
        start = scan.nextInt();
        direction = scan.next();
        playerHits = scan.nextInt();
        
        String[][] court = new String[width + 2][length + 2];
        
        //System.out.println(length + " " + width + " " + start + " " + direction + " "+ playerHits);
        for (int i = 0; i < court.length; i++) {
            for (int j = 0; j < court[i].length; j++) {
                if (i == 0 || i == court.length - 1 || j == court[i].length - 1) {
                    court[i][j] = "*";
                } else {
                    court[i][j] = " ";
                }
            }
        } 
        
        //court[3][5] = "/";
        
        //printCourt(court);
        int row = start + 1;
        int col = 0;
        
        if (length == 1 && width == 1) {
            court[1][1] = ".";
            printCourt(court);
            return;
        }
        
        boolean north = true, east = true;
        if (direction.length() > 1) {
            north = (direction.substring(0, 1).equals("N"));
            east = (direction.substring(1, 2).equals("E"));
        }
        
        while (playerHits + 1 > 0) {
            court[row][col] = ".";
            
            //printCourt(court);
            
            if (row <= 1) {
                //System.out.println("Top");
                north = false;
            } else if (row >= court.length - 2) {
                //System.out.println("Bottom");
                north = true;
            }
            if (col <= 0) {
                //System.out.println("Left");
                east = true;
                playerHits -= 1;
            } else if (col >= court[0].length - 2) {
                //System.out.println("Right");
                east = false;
            }
            
            if (north) {
                row -= 1;
            } else {
                row += 1;
            }
            
            if (east) {
                col += 1;
            } else {
                col -= 1;
            }
            //System.out.println("R:" + row + " C:" + col + " Direction: " + north + " " + east + " Hits:" + playerHits);
        }
        //System.out.println("END");
        printCourt(court);
    }  
    public static void printCourt(String[][] court) {
        for (int i = 0; i < court.length; i++) {
            for (int j = 0; j < court[i].length; j++) {
                System.out.print(court[i][j]);
            }
            System.out.println("");
        }
    }
}
