# 225_用队列表示栈

<!-- 所有文件名必须是该题目的英文名 -->

!!! note "要点"
    <!-- 这里记载考察的数据结构、算法等 -->
    栈｜队列

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span> 中等
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。
> 
> 实现 MyStack 类：
> 
> void push(int x) 将元素 x 压入栈顶。
> 
> int pop() 移除并返回栈顶元素。
> 
> int top() 返回栈顶元素。
> 
> boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。

> 
```
```

------

??? note 

    
-------------

=== "Java"

    ```java
    
    ```

=== "Python"

    ```Python
    # 这里用到了deque()
    class MyStack:

        def __init__(self):
            self.deq1 = deque()
            self.deq2 = deque()

        def push(self, x: int) -> None:
            self.deq2.append(x)
            while self.deq1:
                self.deq2.append(self.deq1.popleft())
            self.deq1, self.deq2 = self.deq2, self.deq1 

        def pop(self) -> int:
            return self.deq1.popleft()

        def top(self) -> int:
            return self.deq1[0]


        def empty(self) -> bool:
            return len(self.deq1) == 0


    # Your MyStack object will be instantiated and called as such:
    # obj = MyStack()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.empty()
    ```
