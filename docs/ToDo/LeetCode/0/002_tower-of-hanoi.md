

package towerofHanoi;

import java.io.IOException;

public class towerofhanoi{

    public static int count = 0;
    /**
     *
     * move str from a to b via c
     */
    public static void alg(String str, int n, int a, int b, int c){
        if(n == 1){
            System.out.println("move " + str + " from " + a + " to " + b);
            count ++;
        }
        else{
            alg(str.substring(0, str.length() - 1), n - 1, a, c, b);
            System.out.println("move " + str.substring(str.length() - 1, str.length()) + " from " + a + " to " + b);
            count++;
            alg(str.substring(0, str.length() - 1), n - 1, c, b, a);
        }
    }
    public static void main(String[] args) throws IOException{
        count = 0;
        String str = "ABC";
        alg(str, str.length(), 1, 3, 2);
        System.out.println("total number of moves: " + count);
    }
}
