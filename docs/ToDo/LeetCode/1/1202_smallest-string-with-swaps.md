<h2>2022.3.26 Leetcode刷题 - 并查集



---



#### [1202. 交换字符串中的元素](https://leetcode-cn.com/problems/smallest-string-with-swaps/)

给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。

你可以 任意多次交换 在 pairs 中任意一对索引处的字符。

返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。



```输入：s = "dcab", pairs = [[0,3],[1,2]]
输出："bacd"
解释： 
交换 s[0] 和 s[3], s = "bcad"
交换 s[1] 和 s[2], s = "bacd"
```

- 思路：每一个可以互换的组合内的字母都可以实现两两互换：[0,1]、[1,2]，0可以被换到1和2，同理，1->0,2 ， 2->0，1
- 为的是从头到尾遍历的过程中，字典序要求最开始一定要尽可能小；所以需要把从0开始的每一个节点，它能换到的所有其他的字母
- 都列出来，同时还要按照列出来的顺序选字典序最小的（这里用到PriorityQueue了 ）
- 并查集模板：

```Java 
public int find(int x, int[] p){
        if(p[x] != x){
            p[x] = find(p[x], p);
        }
        return p[x];
    }

public void union(int x, int y, int[] p){
    int px = find(x, p);
    int py = find(y, p);
    if(px != py){
      p[px] = py;
    }
}
```



- Code

```Java
class Solution {


    public int find(int x, int[] p){
        if(p[x] != x){
            p[x] = find(p[x], p);
        }
        return p[x];
    }

    public void union(int x, int y, int[] p){
        int px = find(x, p);
        int py = find(y, p);
        if(px != py){
            p[px] = py;
        }
    }
    public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
        int length = s.length();
        int[] p = new int[length];
        Map<Integer, PriorityQueue<Character> > map = new HashMap<>();
        for(int i = 0; i < length; i++ ){
            p[i] = i;    
        }
        for(List<Integer> pair: pairs){
            union(pair.get(0), pair.get(1), p);
        }
        for(int i = 0; i < length; i ++ ){
            int cur = find(i, p);
            if(!map.containsKey(cur)){
                map.put(cur, new PriorityQueue<>());
            }
            map.get(cur).offer(s.charAt(i));
        }
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < length; i ++ ){
            sb.append(map.get(find(i, p)).poll());
        }
        return sb.toString();
    }
}
```
