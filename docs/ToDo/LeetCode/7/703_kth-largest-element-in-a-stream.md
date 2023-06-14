<h2>2022.03.31 日常刷题</h2>

---

#### [703. 数据流中的第 K 大元素](https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/)

🔑🔑 考点：堆 ｜ Kth ｜ 固定大小Heap 

🚴‍♀️🚴‍♀️ 难度： <span style = "color:darkgreen; font-weight:bold">Easy</span>

🔗🔗 链接：https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/

📖📖 题目：

设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。

请实现 KthLargest 类：

KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。

💻💻 测试用例：

```
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
输出：
[null, 4, 5, 5, 8, 8]
```

💡💡思路：

- 解题思路：一个大顶堆
- 始终保持堆的大小是k，那么最大的就一定是头节点。

👩🏻‍💻🧑🏻‍💻 代码：

```Java
// 一些优化结果12ms
class KthLargest {
    final PriorityQueue<Integer> q ;
    final int k;
    public KthLargest(int k, int[] nums) {
        this.k = k;
        q = new PriorityQueue<>(k);
        for(int i : nums){
            add(i);
        }
    }
    public int add(int val) {
        q.offer(val);
        if(q.size() > k){
            q.poll();
        }
        return q.peek();
    }
}
```
