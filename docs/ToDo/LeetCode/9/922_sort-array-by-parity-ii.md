# 922_中文题目

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    哈希表 | 动态规划

- 🔑🔑 难度：
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
> Write Here 

------

> 解析

-------------

=== "Java"

    ```java
    class Solution {
        public int[] sortArrayByParityII(int[] A) {
            int j = 1;
            for (int i = 0; i < A.length; i += 2)
                if (A[i] % 2 == 1) {
                    while (A[j] % 2 == 1)
                        j += 2;
                    int tmp = A[i];
                    A[i] = A[j];
                    A[j] = tmp;
                }
            return A;
        }
    }

    //如果有不满足“序号为偶数的位为偶数的”，那么一定有“序号为奇数的不为奇数”；
    //不需要开辟额外空间//

    // Java.vision2:(Double Traversals)

    class Solution {
        public int[] sortArrayByParityII(int[] A) {
            int N = A.length;
            int[] ans = new int[N];

            int t = 0;
            for (int x: A) if (x % 2 == 0) {
                ans[t] = x;
                t += 2;
            }

            t = 1;
            for (int x: A) if (x % 2 == 1) {
                ans[t] = x;
                t += 2;
            }

            return ans;
        }
    }


    ```