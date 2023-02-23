

2022.3.28 Leetcode 每日一题

---

#### [693. 交替位二进制数](https://leetcode-cn.com/problems/binary-number-with-alternating-bits/)



- 难度【Easy】

- 考点：左移 + 异或运算

给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。

```
输入：n = 5
输出：true
解释：5 的二进制表示是：101

```



原理：如果一个数字是1010101

右移之后是0101010

1010101 ^ (异或）01010101 = 01111111 + 1 = 1000000 

10000000  & 01111111 = 0；所以这个数字是符合条件的。 

```Java

class Solution {
    public boolean hasAlternatingBits(int n) {
        int m = n ^ (n >> 1);
        return (m &(m + 1)) == 0;

    }
}
```



```Java
// 并查集的训练
public int find(int x, int[] p){
  if(p[x] != x){
    p[x] = find(p[x]);
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

