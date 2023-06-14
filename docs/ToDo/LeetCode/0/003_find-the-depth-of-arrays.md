```java


package dshomework72;
import java.util.*;
public class dshomework72 {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int total = scan.nextInt();
        String[] judgeCircles = new String[10000];
        Arrays.fill(judgeCircles,"");
        String[] record= new String[total];
        Map<Character,Integer> hash = new HashMap<>();
        for(int i = 0 ; i < total; i++){
            record[i] = scan.next();
        }
        scan.close();
        if(total == 0){
            System.out.println("0");
        }
        for(int i = 0; i < total;i++){
            hash.put(record[i].charAt(0),i);
        }
        boolean[][] judge = new boolean[total][total];
        int[] count = new int[26];

        for(int i = 0 ; i < total; i++){
            String answer = judgeTarget(record[i],count,record[i].charAt(0),judge,judgeCircles);

            if(answer.equals("infity"))
                count[record[i].charAt(0) - 'A'] = Integer.MAX_VALUE;
            else{
                count[record[i].charAt(0) - 'A'] = Integer.parseInt(answer);
            }

        }
        for(int i = 0; i < total; i++){
            for(int j = 0; j < total; j++){
                if(judge[i][j] == true && judge[j][i] == true){
                    count[record[i].charAt(0) - 'A'] = Integer.MAX_VALUE;
                    count[record[j].charAt(0) - 'A'] = Integer.MAX_VALUE;
                }
            }
        }
        int pk = 0;

        while(judgeCircles[pk].length()>2){
            if(judgeCircles[pk].substring(0,1).equals(judgeCircles[pk].substring(judgeCircles[pk].length() - 1))){
                int z = hash.get(judgeCircles[pk].charAt(0));
                count[z] = Integer.MAX_VALUE;
                for(int ui = 1; ui < judgeCircles[pk].length() - 1 ;ui+=2){
                    int Tf = hash.get(judgeCircles[pk].charAt(ui));
                    count[Tf] = Integer.MAX_VALUE;
                }
            }
            pk++;
        }
        for(Character test : hash.keySet()){
            if(count[test - 'A'] != Integer.MAX_VALUE){
                for(String judgeCircle : judgeCircles){
                    for(int i = 1 ; i < judgeCircle.length(); i++){
                        if(count[judgeCircle.charAt(i) - 'A'] == Integer.MAX_VALUE){
                            count[test - 'A'] = Integer.MAX_VALUE;
                        }
                    }
                }
            }
        }
        for(int i = 0 ; i < total; i++){
            String answer = judgeTarget(record[i],count,record[i].charAt(0),judge,judgeCircles);

            if(answer.equals("infity"))
                count[record[i].charAt(0) - 'A'] = Integer.MAX_VALUE;
            else{
                count[record[i].charAt(0) - 'A'] = Integer.parseInt(answer);
            }

        }
        for(int i = 0; i < total; i++){
            if(count[record[i].charAt(0) -'A'] == Integer.MAX_VALUE){
                System.out.println("infity");
            }
            else {
                System.out.println(count[record[i].charAt(0) - 'A']);
            }
        }
    }
    public static String judgeTarget(String target, int[] count,char flag,boolean[][] judge,String[] judgeCircles){
        int temp = 0;
        String cut = target.substring(2);
        temp = countTarget(cut,count,flag,judge,judgeCircles);

        if(temp == Integer.MAX_VALUE){
            return "infity";
        }
        else{
            return temp +"";
        }
    }
    public static int countTarget(String target, int[] count ,char flag,boolean[][] judge,String[] judgeCircles){
        int res = 0;
        int compare2 = 0;
        int compare = 0;

        boolean hasCountered = false;
        for(int i = 0; i < target.length(); i++){
            if(target.charAt(i) == '(' && hasCountered == false){
                res ++;
                hasCountered = true;
            }
            else if(target.charAt(i) == '(' && hasCountered){
                int start = i;
                int balance = 0;
                while(target.charAt(i) !=')' || balance != 0){
                    i++;
                    if(target.charAt(i) == '('){
                        balance ++;
                    }
                    else if(balance >0 && target.charAt(i) == ')'){
                        balance --;
                    }
                }
                int compare3 = compare2;
                compare2 = countTarget(target.substring(start, i + 1),count,flag,judge,judgeCircles);
                compare2 = Math.max(compare2,compare3);
            }
            else if((target.charAt(i) >='a' && target.charAt(i) <='z') || target.charAt(i) ==','||target.charAt(i) == ')'){
                continue;
            }
            else if(target.charAt(i) >='A' && target.charAt(i) <='Z' && target.charAt(i)!=flag){
                if(count[target.charAt(i) - 'A'] == Integer.MAX_VALUE){
                    return Integer.MAX_VALUE;
                }
                judge[flag - 'A'][target.charAt(i) - 'A'] = true;
                for(int w = 0 ; w < judgeCircles.length; w ++){
                    if(!judgeCircles[w].equals("")){
                        if(judgeCircles[w].charAt(judgeCircles[w].length() - 1) == flag){
                            judgeCircles[w] = judgeCircles[w] + flag + target.charAt(i) + "";
                        }
                    }
                    else if(judgeCircles[w].length() == 0){
                        judgeCircles[w] = flag + Character.toString(target.charAt(i))+ "";
                        break;
                    }
                }
                compare = Math.max(compare,count[target.charAt(i) - 'A']);
            }
            else if(target.charAt(i) == flag) {
                return Integer.MAX_VALUE;
            }
        }
        compare ++;
        res += compare2;
        return Math.max(compare,res);
    }
}

```