# [433. 最小基因变化](https://leetcode-cn.com/problems/minimum-genetic-mutation/)

难度：【Medium】

一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。

假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。

例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。

与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。

现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。如果无法实现目标变化，请返回 -1。

注意：

起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
如果一个起始基因序列需要多次变化，那么它每一次变化之后的基因序列都必须是合法的。
假定起始基因序列与目标基因序列是不一样的

```jinja2
start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
```



```Java
// 原理和上面一样
class Solution {
    public int minMutation(String start, String end, String[] bank) {
        Set<String> set = new HashSet<>();
        Set<String> set1 = new HashSet<>();
        for(int i = 0; i < bank.length; i ++ ){
            set.add(bank[i]);
        }
        if(!set.contains(end)){
            return -1;
        }
        char[] map = {'A','G','C','T'};
        Queue<String> queue = new LinkedList<>();
        queue.offer(start);
        int count = 0;
        while(queue.size() > 0){
            int size = queue.size();
            count ++ ;           
            for(int k = 0; k < size; k ++ ){
                char[] temp = queue.poll().toCharArray();
                for(int i = 0; i < 8; i ++ ){
                    char ori_char = temp[i];
                    for(int j = 0; j < 4; j ++ ){
                        temp[i] = map[j];
                        String cur = new String(temp);
                        if(cur.equals(end)){
                            return count;
                        }
                        if(set.contains(cur) && !set1.contains(cur)) {
                            queue.offer(cur);
                        }
                        set1.add(cur);
                    }
                    temp[i] = ori_char;
                }
            }
        }
        return -1;
    }
}
```

