# Itertools package

Python中用于进行高效遍历的一个内置包。( Functions creating iterators for efficient looping)。很多返回值都是一个“迭代器”（Iterators）

## chain

创建一个迭代器，从第一个可迭代对象返回元素，然后继续下一个可迭代对象，直到所有可迭代对象都用尽。用于将连续序列视为单个序列。

可以想象成把两个列表串在一起一同遍历。

```Python 

from itertools import chain
b = [j for j in "ACBBSJCDC"]
c = [k for k in "*()"]
for i in chain(b, c):
    print(i, end = "/")

# A/C/B/B/S/J/C/D/C/*/(/)/

```
## product

生成多组数据的笛卡尔积。可以视为： product(A, B) = (a, b) for b in B for a in A
```Python
from itertools import chain, product
b = [j for j in "ABCD"]
c = [k for k in "123"]
for i in product(b, c):
    print(i, type(i))

# ('A', '1') <class 'tuple'>
# ('A', '2') <class 'tuple'>
# ('A', '3') <class 'tuple'>
# ('B', '1') <class 'tuple'>
# ('B', '2') <class 'tuple'>
# ('B', '3') <class 'tuple'>
# ('C', '1') <class 'tuple'>
# ('C', '2') <class 'tuple'>
# ('C', '3') <class 'tuple'>
# ('D', '1') <class 'tuple'>
# ('D', '2') <class 'tuple'>
# ('D', '3') <class 'tuple'>
```


也可以设置重复的次数：

```Python
for i in product(b, c, repeat = 2):
    # product(b, c, repeat = 2) equals: product(b, c, b, c)
    print(i, type(i))
# ('A', '1', 'A', '1') <class 'tuple'>
# ('A', '1', 'A', '2') <class 'tuple'>
# ('A', '1', 'A', '3') <class 'tuple'>
# ('A', '1', 'B', '1') <class 'tuple'>
# ('A', '1', 'B', '2') <class 'tuple'>
# ('A', '1', 'B', '3') <class 'tuple'>
# ('A', '1', 'C', '1') <class 'tuple'>
# ('A', '1', 'C', '2') <class 'tuple'>
# ('A', '1', 'C', '3') <class 'tuple'>
# .... 很多很多 
```

## permutations

对应排列组合中的排列。返回可迭代对象中元素的连续 r 长度排列。如果不指定r，默认是r = 可迭代对象的长度。


```Python
from itertools import permutations
b = [j for j in "ABCD"]
for i in permutations(b, 2):
    print(i, type(i))

# ('A', 'B') <class 'tuple'>
# ('A', 'C') <class 'tuple'>
# ('A', 'D') <class 'tuple'>
# ('B', 'A') <class 'tuple'>
# ('B', 'C') <class 'tuple'>
# ('B', 'D') <class 'tuple'>
# ('C', 'A') <class 'tuple'>
# ('C', 'B') <class 'tuple'>
# ('C', 'D') <class 'tuple'>
# ('D', 'A') <class 'tuple'>
# ('D', 'B') <class 'tuple'>
# ('D', 'C') <class 'tuple'>

for i in permutations(b):
    print(i, type(i))

# ('A', 'B', 'C', 'D') <class 'tuple'>
# ('A', 'B', 'D', 'C') <class 'tuple'>
# ('A', 'C', 'B', 'D') <class 'tuple'>
# ('A', 'C', 'D', 'B') <class 'tuple'>
# ('A', 'D', 'B', 'C') <class 'tuple'>
# ('A', 'D', 'C', 'B') <class 'tuple'>
# ('B', 'A', 'C', 'D') <class 'tuple'>
# ('B', 'A', 'D', 'C') <class 'tuple'>
# ('B', 'C', 'A', 'D') <class 'tuple'>
# ('B', 'C', 'D', 'A') <class 'tuple'>
# ('B', 'D', 'A', 'C') <class 'tuple'>
# ('B', 'D', 'C', 'A') <class 'tuple'>
# ('C', 'A', 'B', 'D') <class 'tuple'>
# ('C', 'A', 'D', 'B') <class 'tuple'>
# ('C', 'B', 'A', 'D') <class 'tuple'>
# ('C', 'B', 'D', 'A') <class 'tuple'>
# ('C', 'D', 'A', 'B') <class 'tuple'>
# ('C', 'D', 'B', 'A') <class 'tuple'>
# ('D', 'A', 'B', 'C') <class 'tuple'>
# ('D', 'A', 'C', 'B') <class 'tuple'>
# ('D', 'B', 'A', 'C') <class 'tuple'>
# ('D', 'B', 'C', 'A') <class 'tuple'>
# ('D', 'C', 'A', 'B') <class 'tuple'>
# ('D', 'C', 'B', 'A') <class 'tuple'>
```


## combinations

对应排列组合中的组合数。$C^{2}_{4}$ 的那个。

```Python 
from itertools import combinations 
b = [j for j in "ABCD"]
c = [k for k in "123"]
for i in combinations(b, 2):
    print(i, type(i))

# ('A', 'B') <class 'tuple'>
# ('A', 'C') <class 'tuple'>
# ('A', 'D') <class 'tuple'>
# ('B', 'C') <class 'tuple'>
# ('B', 'D') <class 'tuple'>
# ('C', 'D') <class 'tuple'>
b = [j for j in "ABBCD"]
for i in combinations(b, 2):
    print(i, type(i))
# ('A', 'B') <class 'tuple'>
# ('A', 'B') <class 'tuple'>
# ('A', 'C') <class 'tuple'>
# ('A', 'D') <class 'tuple'>
# ('B', 'B') <class 'tuple'>  
# ('B', 'C') <class 'tuple'> # This 
# ('B', 'D') <class 'tuple'> # This
# ('B', 'C') <class 'tuple'> # This
# ('B', 'D') <class 'tuple'> # This 
# ('C', 'D') <class 'tuple'>
```
从输入可迭代对象中返回元素的 r 长度子序列。组合的元组按照输入可迭代对象的顺序输出。如果输入的可迭代对象是不重复的，那么生成的结果也是不重复的。但如果，如果你输入的（比如b = [i for i in "ABBCD"]）对象是可重复的，那么输出结果就会有重复。


