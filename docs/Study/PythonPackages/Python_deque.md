## Python中的deque：双端队列

!!! quote "感谢GPT-4在本页面编写过程中的协助"

- deque是栈和队列的一种广义实现，deque是`double-end queue`的简称；deque支持线程安全、有效内存地以近似O(1)的性能在deque的两端插入和删除元素;
- API
    - `append()`: 右端添加元素
    - `appendleft()`: 左边添加元素
    - `pop()`：右端弹出元素
    - `popleft()`：左端弹出元素
    - `insert(idx, ele)`：在第idx个位置插入元素ele;(idx 从0开始下标)

```Python

import collections
deq1 = collections.deque()

for i in range(10): # 先后加入10个元素
    deq1.append(i)
print(deq1)
for _ in range(3): # 弹出最先加入的3个元素
    deq1.popleft()
print(deq1)
deq1.pop() # 弹出最后一个加入的元素
print(deq1)
deq1.insert(2, 120)
print(deq1)
deq1.pop()
print(deq1) # 如果是Insert一个元素在中间，不在首末尾，pop还是会弹出最后的元素

# ========== 结果为 ===========
# deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# deque([3, 4, 5, 6, 7, 8, 9])
# deque([3, 4, 5, 6, 7, 8])
# deque([3, 4, 120, 5, 6, 7, 8])
# deque([3, 4, 120, 5, 6, 7])
```

--------

## Python中的另类字典： defaultdict


返回一个新的类似字典的对象。 defaultdict 是内置 dict 类的子类。它重写一个方法并添加一个可写实例变量。其余功能与 dict 类相同

```Python
from collections import defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list) 
# 当第一次遇到每个键时，如果尚未在映射中;因此， defaultdict 会给这个键返回空 list 不报错
for k, v in s:
    d[k].append(v)
print(sorted(d.items()))
if "Purple" in d:
    print("Checked!")
if "yellow" in d:
    print("Checked!")    

# ======= 返回结果 ==========
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
# Checked!
```

----------

## Python中的另类元组namedtuple


namedtuple允许创建类似于元组的对象，但每个元素都可以有一个名称，这使得您的代码更加可读和文档化。您可以通过名称而不是索引来访问namedtuple的元素，这增加了代码的可读性。


首先，需要从collections模块导入namedtuple，然后使用namedtuple()工厂函数来创建一个新的namedtuple类。

- 使用场景和优点

namedtuple适合用于需要不可变对象（就像元组）但又希望代码可读性更高的场合。例如，在处理CSV或数据库查询结果时，将每行数据表示为namedtuple，比使用普通元组更加清晰。

- 其优点包括：

> 可读性：通过字段名访问元素比通过索引访问更清晰。
> 
> 不可变性：和普通元组一样，namedtuple是不可变的。
> 
> 轻量级：相比普通类，namedtuple更节省内存。
> 
> 自文档化：代码中使用namedtuple，可以让其他人更容易理解您的数据结构。

一种常用的情况是读取一些静态数据。比如如下格式的csv：

| Name  |  Age  | Height | Weight |  IQ   |  EQ   | Math  | English | Grade |
| :---: | :---: | :----: | :----: | :---: | :---: | :---: | :-----: | :---: |
|  Bob  |  22   |  165   |   66   |  120  |  120  |  153  |   130   |   1   |
|  Aob  |  23   |  169   |   66   |  122  |  127  |  163  |   130   |   1   |
|  Cob  |  24   |  168   |   65   |  122  |  127  |  172  |   133   |   2   |
|  Dob  |  25   |  164   |   62   |  122  |  127  |  172  |   133   |   2   |
|  Eob  |  27   |  162   |   55   |  133  |  157  |  172  |   133   |   2   |
|  Fob  |  22   |  161   |   68   |  133  |  153  |  172  |   133   |   2   |
|  Gob  |  21   |  164   |   89   |  123  |  153  |  172  |   133   |   2   |

可以通过如下方法获取每一行的数据：


```Python
import pandas as pd
from collections import namedtuple

# 读取CSV文件
df = pd.read_csv('your_csv_file.csv')

# 用df的列名创建一个namedtuple类 'Student'
Student = namedtuple('Student', df.columns)

# 将每行转换为一个Student namedtuple实例
students = [Student(*row) for row in df.itertuples(index=False, name=None)]

# 示例：打印第一行数据
print(students[0])

# ===== 输出 =====
# Student(Name='Bob', Age=22, Height=165, Weight=66, IQ=120, EQ=120, Math=153, English=130, Grade=1)
```

--------


!!! note "与collections无关的一些补充：Python中的集合"

    Python 中的集合（set）是一种内置数据类型，非常适合进行集合的各种操作，如并集（union）、交集（intersection）、差集（difference）等。下面我将详细介绍这些操作，并附上相应的代码示例。

    ```Python
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    # 并集
    union_set = set1 | set2  # 或者 set1.union(set2)
    print("并集:", union_set)

    # 交集
    intersection_set = set1 & set2  # 或者 set1.intersection(set2)
    print("交集:", intersection_set)

    # 差集
    difference_set = set1 - set2  # 或者 set1.difference(set2)
    print("差集:", difference_set)
    #  =========== 返回的结果 =========== 
    # 并集: {1, 2, 3, 4, 5, 6, 7, 8}
    # 交集: {4, 5}
    # 差集: {1, 2, 3}
    ```
