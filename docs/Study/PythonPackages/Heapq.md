# Heapq: 在Python中灵活地使用数据结构“堆”

!!! quote "参考[官方文档](https://docs.python.org/3/library/heapq.html)"

`heapq` 是 `Python` 标准库中的一个模块，**它提供了堆队列算法的实现，也称为优先队列算法**。堆是一种特殊的树形数据结构，每个节点都比其子节点小（最小堆），使用 heapq 可以高效地实现优先队列，它的插入和删除操作的时间复杂度都是 $O(log(N))$，其中 $N$ 是堆中元素的数量。

使用时候有个细节，你可以直接针对原先有的列表进行堆操作。见下面的代码。

- **向堆中压入元素：`heappush`**

```python
import heapq
heap = []
# 向堆中插入元素
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)
print(heap)  # 输出: [1, 3, 4]
```

-----

- **从堆中弹出最小元素：`heappop(heap)`**

从堆 heap 中弹出并返回最小的元素，同时保持堆的特性。如果堆为空，会抛出 `IndexError` 异常。时间复杂度为 $O(log(N))$ 。

```python
import heapq
heap = [1, 3, 4]
# 弹出最小元素
smallest = heapq.heappop(heap)
print(smallest)  # 输出: 1
print(heap)  # 输出: [3, 4]
```

-----

- **插入并弹出最小元素 : `heappushpop(heap, item)`**

将 `item` 元素插入到堆 `heap` 中，然后弹出并返回堆中最小的元素。这个操作比先调用 `heappush()` 再调用 `heappop()` 更高效。时间复杂度为 $O(logN)$ 。

```python
import heapq

heap = [1, 3, 4,7,39,12,438,456]
# 插入元素并弹出最小元素
result = heapq.heappushpop(heap, 2)
print(result)  # 输出: 1
print(heap)  # 输出: [2, 3, 4]
```

> 这个数据结构在维持 K 顶堆的时候很常见。总之就是限制元素的数量即可。每次push再pop，保证元素始终是 K 个。

----

- **弹出并插入最小元素 : `heapreplace(heap, item)`**

先弹出并返回堆 `heap` 中最小的元素，然后将 `item` 元素插入到堆中。时间复杂度为 $O(logN)$ 。

```python
import heapq

heap = [1, 3, 4]
# 弹出最小元素并插入新元素
result = heapq.heapreplace(heap, 2)
print(result)  # 输出: 1
print(heap)  # 输出: [2, 3, 4]
```

-----

- **返回最大N个元素：`nlargest(k, iter, key=None)`**

返回可迭代对象 `iter` 中最大的 `k` 个元素组成的列表。如果指定了 `key` 参数，则根据 key 函数来比较元素（参考排序函数 `sort`） 。时间复杂度为 $Nlog(K)$，其中 $k $是返回元素的数量。


```python
import heapq
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# 获取最大的 3 个元素
largest_three = heapq.nlargest(3, nums)
print(largest_three)  # 输出: [9, 6, 5]
```

> 同样地，你也可以用 `nsmallest` 返回最小的 `k` 个元素组成的列表。不赘述。

-----

- **大顶堆**

heapq默认实现的是小顶堆，我们可以插入的时候选择将负数插入，这样可以模拟大顶堆的行为。

```python
import heapq
# 定义一个空列表作为堆
max_heap = []
# 要插入堆中的元素列表
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# 插入元素到最大堆
for num in numbers:
    # 插入取负后的元素
    heapq.heappush(max_heap, -num)

# 从最大堆中取出元素
while max_heap:
    # 取出元素并取负还原
    max_num = -heapq.heappop(max_heap)
    print(max_num)
```

豆包大模型同样提供了一种很好的封装：

```python
import heapq

class MaxHeap:
    def __init__(self):
        # 初始化一个空列表作为堆
        self.heap = []

    def push(self, item):
        # 插入取负后的元素
        heapq.heappush(self.heap, -item)

    def pop(self):
        if self.heap:
            # 取出元素并取负还原
            return -heapq.heappop(self.heap)
        else:
            return None

    def peek(self):
        if self.heap:
            # 查看堆顶元素并取负还原
            return -self.heap[0]
        else:
            return None

    def __len__(self):
        return len(self.heap)

# 使用自定义最大堆类
max_heap = MaxHeap()
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# 插入元素到最大堆
for num in numbers:
    max_heap.push(num)

# 从最大堆中取出元素
while len(max_heap) > 0:
    print(max_heap.pop())
```

-----

- **对于自定义的类进行堆操作**


可以将某个类的实例当作堆中的元素，但需要满足一定的条件，因为 `heapq` 模块在进行堆操作（如比较元素大小）时依赖元素之间的比较规则。以下详细介绍相关内容。

**`heapq` 模块默认使用元素的小于运算符（`<`）来确定元素的顺序，因此如果要将类的实例放入堆中，这个类必须实现 `__lt__` 方法（即小于比较方法），这样 `heapq` 才能知道如何比较这些实例的大小。**


```python
import heapq

# 定义一个自定义类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        # 定义比较规则，这里以年龄作为比较依据
        return self.age < other.age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

# 创建一个空堆
heap = []

# 创建 Person 类的实例
person1 = Person("Alice", 25)
person2 = Person("Bob", 20)
person3 = Person("Charlie", 30)

# 将实例插入堆中
heapq.heappush(heap, person1)
heapq.heappush(heap, person2)
heapq.heappush(heap, person3)

# 从堆中依次弹出元素
while heap:
    print(heapq.heappop(heap))
```

解释：

1. **`Person` 类**：
    - `__init__` 方法：用于初始化 `Person` 类的实例，包含 `name` 和 `age` 两个属性。
    - `__lt__` 方法：定义了比较规则，这里以 `age` 属性作为比较依据，当一个 `Person` 实例的 `age` 小于另一个实例的 `age` 时，认为该实例更小。
    - `__repr__` 方法：用于定义实例的字符串表示形式，方便打印输出。

2. **堆操作**：
    - 创建一个空堆 `heap`。
    - 创建 `Person` 类的三个实例 `person1`、`person2` 和 `person3`。
    - 使用 `heapq.heappush` 方法将这些实例插入堆中。
    - 使用 `heapq.heappop` 方法从堆中依次弹出元素并打印，由于我们定义了 `__lt__` 方法，堆会按照年龄从小到大的顺序排列元素。

