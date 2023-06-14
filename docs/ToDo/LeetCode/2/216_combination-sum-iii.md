# 216_组合总和iii

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    ？

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->
找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：

> 只使用数字1到9
> 
> 每个数字 最多使用一次 

返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

> 输入: k = 3, n = 7
> 
> 输出: [[1,2,4]]
> 
> 解释:
> 1 + 2 + 4 = 7，没有其他符合的组合了。

------

> 解析

-------------

=== "Java"

    ```java
    class Solution {
        List<List<Integer>> result = new ArrayList<>();

        public List<List<Integer>> combinationSum3(int k, int n) {
            recursion(1, k, n, new ArrayList<>());
            return result;
        }

        private void recursion(int start, int k, int n, List<Integer> list) {
            if (n == 0 && k == 0) {
                result.add(new ArrayList<>(list));
            }
            if (n <= 0) {
                return;
            }
            if (k > 0) {
                for (int i = start; i < 10; i++) {
                    list.add(i);
                    recursion(i + 1, k - 1, n - i, list);
                    list.remove(list.size() - 1);
                }
            }
        }
    }

    ```