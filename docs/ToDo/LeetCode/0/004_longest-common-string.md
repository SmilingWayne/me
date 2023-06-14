package javaClass5;

/**
 * s, t: 两个串
 * f[i][j]: s[0-(i-1)]和t[0-(j-1)]的最长公共子串
 * f[i][j] =
 * 1. 0, 当 i = 0, j = 0
 * 2. f[i - 1][j - 1] + 1, 当i > 0 && j > 0 && s[i - 1] = t[j - 1]
 * 3. max{f[i - 1][j], f[i][j - 1]}， 当i > 0 && j > 0 && s[i - 1] != t[j - 1]
 */
public class javaclass5{
    public static void bottom_up(String s, String t){
        int[][] f = new int[s.length() + 1][t.length() + 1];
        for(int i = 0; i < s.length(); i++){
            for(int j = 0; j < t.length(); j++){
                if(s.charAt(i) == t.charAt(j)){
                    f[i + 1][j + 1] = f[i][j] + 1;
                }
                else{
                    f[i + 1][j + 1] = Math.max(f[i][j + 1], f[i + 1][j]);
                }
            }
        }
        System.out.println(f[s.length()][t.length()]);
        int p = s.length();
        int q = t.length();
        String str = "";
        while(p > 0 && q > 0){
            if(s.charAt(p - 1) == t.charAt(q - 1)){
                str = s.charAt(p - 1) + str;
                p --;
                q --;
            }
            else if(f[p][q] == f[p - 1][q]){
                p --;
            }
            else{
                q --;
            }
        }
        System.out.println(str);
    }
    public static int top_down(String s, String t, int i, int j, int[][] f){
        if(i == 0 || j == 0){
            return 0;
        }
        else if(s.charAt(i - 1) == t.charAt(j - 1)){
            if(f[i - 1][j - 1] >= 0){
                return f[i - 1][j - 1] + 1;
            }
            else{
                f[i][j] = top_down(s, t, i - 1, j - 1, f) + 1;
                return f[i][j];
            }
        }
        else{
            int ret1 = 0;
            if(f[i - 1][j] >= 0){
                ret1 = f[i - 1][j];
            }
            else{
                ret1 = top_down(s, t, i - 1, j, f);
            }
            int ret2 = 0;
            if(f[i][j - 1] >= 0){
                ret2 = f[i][j - 1];
            }
            else{
                ret2 = top_down(s, t, i, j - 1, f);

            }
            f[i][j] = Math.max(ret1, ret2);
            return f[i][j];
        }
    }
    public static void main(String[] args){
        String s = "GGCACCACG";
        String t = "ACGGCGGATACG";
        bottom_up(s, t);
        int[][] f = new int[s.length() + 1][t.length() + 1];
        for(int i = 0; i < s.length() + 1; i++){
            for(int j = 0; j < t.length() + 1; j++){
                f[i][j] = -1;
            }
        }
        System.out.println(top_down(s, t, s.length(), t.length(), f));
    }
}
