# 0303_堆盘子

<!-- 所有文件名必须是该题目的英文名 -->

!!! note
    <!-- 这里记载考察的数据结构、算法等 -->
    栈

- 🔑🔑 难度：<span style = "color:gold; font-weight:bold">Medium</span>
<!-- <span style = "color:gold; font-weight:bold">Medium</span> 中等 -->
<!-- <span style = "color:crisma; font-weight:bold">High</span> 困难 -->
<!-- <span style = "color:Green; font-weight:bold">Easy</span> 简单 -->

<!-- 题目简介 -->

> 堆盘子。设想有一堆盘子，堆太高可能会倒下来。因此，在现实生活中，盘子堆到一定高度时，我们就会另外堆一堆盘子。请实现数据结构SetOfStacks，模拟这种行为。SetOfStacks应该由多个栈组成，并且在前一个栈填满时新建一个栈。此外，SetOfStacks.push()和SetOfStacks.pop()应该与普通栈的操作方法相同（也就是说，pop()返回的值，应该跟只有一个栈时的情况一样）。 进阶：实现一个popAt(int index)方法，根据指定的子栈，执行pop操作。
> 
> 当某个栈为空时，应当删除该栈。当栈中没有元素或不存在该栈时，pop，popAt 应返回 -1.

```
输入：
["StackOfPlates", "push", "push", "popAt", "pop", "pop"]
[[1], [1], [2], [1], [], []]
 输出：
[null, null, null, 2, 1, -1]
```

------

??? note 
     Python中模拟Stack，用list就可以了。注意一些特殊情况：每次pop之后需要用Pop删除掉那些空的元素。

    
-------------

=== "Python"

    ```Python
    
    class StackOfPlates:

        def __init__(self, cap: int):
            self.cap = cap 
            self.array = []

        def push(self, val: int) -> None:
            if self.cap == 0:
                return
            if len(self.array) == 0 or len(self.array[-1]) == self.cap:
                self.array.append([val])
            else:
                self.array[-1].append(val)
            
        def pop(self) -> int:
            if len(self.array) == 0 or len(self.array[-1]) == 0:
                return -1
            else:
                val = self.array[-1].pop()
                if len(self.array[-1]) == 0:
                    self.array.pop(-1)
                return val

        def popAt(self, index: int) -> int:
            if index >= len(self.array):
                return -1
            val = self.array[index].pop()
            if len(self.array[index] ) == 0:
                self.array.pop(index)
            return val
            
    ```
