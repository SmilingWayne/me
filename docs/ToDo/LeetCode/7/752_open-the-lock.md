<h2>2022.3.30 Leetcode 日常刷题
</h2>





#### [752. 打开转盘锁](https://leetcode-cn.com/problems/open-the-lock/)

难度：【Medium】

考点：BFS + 条件剪枝

你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。

```输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/open-the-lock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

- 一个小点：每个数字只可以转动一次。
- 小心deadends里头有0000

- 根本思路：BFS + Set剪枝，模拟解锁过程，每次都要把所有“在这个队列里的可行的情况”列举出来，一旦出现结果就一定是最小的。
- 小细节：如何产生‘0’ -> '1','9'，‘9’->'0','8'的数组映射？

> >
> >
> >API：Java里面将List和数组实现转换：
> >
> >Arrays.asList(a); 
> >
> >List<Integer> ans = new ,,,
> >
> >int[] res = ans.toArray()

```Java 
// 最笨的Java解法
class Solution {
    public int openLock(String[] deadends, String target) {
        if(target.equals("0000") ){
            return 0;
        }
        Set<String> dead = new HashSet<>();
        Set<String> visited = new HashSet<>();
        for(String deadend : deadends){
            dead.add(deadend);
        }
        if(dead.contains("0000")){
            return -1;
        }
        Queue<String> queue = new LinkedList<>();
        queue.offer("0000");
        int count = 0;
        while(!queue.isEmpty()){
            int size = queue.size(); 
            count ++ ;
            for(int i = 0; i < size; i++ ){
                String temp = queue.poll();
                char[] temp2 = temp.toCharArray();
                for(int j = 0; j < 4; j ++ ){
                    char ori = temp2[j];
                    char[] m = new char[2];
                    if(ori == '0'){
                        m[0] = '1';
                        m[1] = '9';
                    }
                    else if(ori == '9'){
                        m[0] = '8';
                        m[1] = '0';
                    }
                    else{
                        m[0] = (char)(ori - 1);
                        m[1] = (char)(ori + 1);
                    }
                    
                    for(int k = 0; k < 2; k ++ ){
                        if(temp2[j] != m[k]){
                            temp2[j] = m[k];
                        }
                        else{
                            continue;
                        }
                        String t = String.valueOf(temp2);
                        if(dead.contains(t)){
                            break;
                            // continue;
                        }
                        else{
                            if(t.equals(target)){
                                return count;
                            }
                            if(!visited.contains(t)){
                                queue.offer(t);
                                visited.add(t);
                            }
                        }
                    }
                    temp2[j] = ori;
                }
            }
        }
        return -1;
    }
}
```



```Java
// 一些优化之后的结果
class Solution {
    public int openLock(String[] deadends, String target) {
        if(target.equals("0000") ){
            return 0;
        }
        Set<String> dead = new HashSet<>();
        Set<String> visited = new HashSet<>();
        for(String deadend : deadends){
            dead.add(deadend);
        }
        if(dead.contains("0000")){
            return -1;
        }
        Queue<String> queue = new LinkedList<>();
        queue.offer("0000");
        int count = 0;
        while(!queue.isEmpty()){
            int size = queue.size(); 
            count ++ ;
            for(int i = 0; i < size; i++ ){
                String temp = queue.poll();
                // char[] temp2 = temp.toCharArray();
                List<String> candidates = get(temp);
                for(String t: candidates){

                    if(dead.contains(t)){
                        continue;
                        // continue;
                    }
                    else{
                        if(t.equals(target)){
                            return count;
                        }
                        if(!visited.contains(t)){
                            queue.offer(t);
                            visited.add(t);
                        }
                    }
                }
        
            }
        }
        return -1;
    }

    public char getPrev(char a){
        return a == '0'? '9':(char)(a  - 1);
    }

    public char getPost(char a){
        return a == '9'? '0':(char)(a  + 1);
    }
    
    public List<String> get(String s){
        char[] t = s.toCharArray();
        List<String> ans = new ArrayList<>();
        for(int i = 0; i < 4; i ++ ){
            char ori = t[i];
            t[i] = getPrev(t[i]);
            ans.add(String.valueOf(t));
            t[i] = getPost(ori);
            ans.add(String.valueOf(t));
            t[i] = ori;
        }
        return ans;

    }
}
```

