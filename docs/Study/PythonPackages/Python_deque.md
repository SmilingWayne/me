# deque

- deque是栈和队列的一种广义实现，deque是`double-end queue`的简称；deque支持线程安全、有效内存地以近似O(1)的性能在deque的两端插入和删除元素;
- API
    - `append()`: 右端添加元素
    - `appendleft()`: 左边添加
    - `pop()`：右端删除
    - `popleft()`：左端删除
    - `insert(idx, ele)`：在第idx个位置插入元素ele;
    - `extend()`:右端插入可迭代对象(list, dict, tuple等)
        - 支持[('a', 'b'), 1,2,3]类似格式；
    - `extendleft()` : 左端插入可迭代对象；