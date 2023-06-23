# Offer-49_丑数

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    动态规划

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。


```
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
```

------

> 解析

-------------

=== "Python"

    ```Python
    class Solution:
        def nthUglyNumber(self, n: int) -> int:
            arr = [1 for _ in range(n )]
            idx2, idx3, idx5 = 0, 0, 0
            for i in range(1, n ):
                n2, n3, n5 = arr[idx2] * 2,  arr[idx3] * 3, arr[idx5] * 5
                fill = min(n2, min(n3, n5))
                if fill == n2: 
                    idx2 += 1
                if fill == n3: 
                    idx3 += 1
                if fill == n5: 
                    idx5 += 1
                arr[i] = fill 
                # print(arr[i])
            return arr[-1]
    
    ```

=== "C++"

    ```C++
    class Solution {
        public:
            int nthUglyNumber(int n) {
                vector<int> ans(n,0);
                int a = 0, b = 0, c = 0;
                ans[0]  = 1;
                for(int i = 1; i < n; i ++ ){
                    int temp = min(ans[a] * 2, min(ans[b] * 3, ans[c] * 5));
                    if(temp == ans[a] * 2){
                        a ++ ;
                    }
                    if(temp == ans[b] * 3){
                        b ++ ;
                    }
                    if(temp == ans[c] * 5){
                        c ++ ;
                    }
                    ans[i] = temp;
                }
                return ans[n - 1];
            }
        };
    
    ```