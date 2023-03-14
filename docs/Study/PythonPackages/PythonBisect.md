# Python 中的列表二分排序函数：Bisect 


!!! Tip
    下面的所有内容一定要基于有序的列表才可以！


> 分下面几种情况写

## 如果列表中没有要查找的元素：

- bisect_left 和  bisect_right 和bisect 表示的意义完全相同，都是“在数组中插入数字s，使得数组有序”； ls[res] > s 

```Python
import bisect
ls = [1,5,9,13,17]
index1 = bisect.bisect(ls,7)
index2 = bisect.bisect_left(ls,7)
index3 = bisect.bisect_right(ls,7)
print("index1 = {}, index2 = {}, index3 = {}".format(index1, index2, index3))
```

结果是:
```
index1 = 2, index2 = 2, index3 = 2
```

## 如果列表中有且仅有一个要查找的元素：

- bisect_left 表示该元素的下标；
- bisect_right 表示该元素下标 + 1，也就是该元素后面的元素；

```Python
import bisect
ls = [1,5,9,13,17]
index1 = bisect.bisect(ls,9)
index2 = bisect.bisect_left(ls,9)
index3 = bisect.bisect_right(ls,9)
print("index1 = {}, index2 = {}, index3 = {}".format(index1, index2, index3))
```

结果是:
```
index1 = 3, index2 = 2, index3 = 3
```

## 如果列表中有且有多个要查找的元素：

- 如果列表中存在多个元素等于x，那么bisect_left(ls, x)返回最左边的那个索引，此时ls[index2] = x。
- bisect_right(ls, x)返回最右边的那个索引加1，此时ls[index3] > x。
- 专业地说，bisect_left返回小于等于x的最小索引，而bisect_right 返回大于x的最小索引；

```Python
import bisect
ls = [1,5,5,5,17]
index1 = bisect.bisect(ls,5)
index2 = bisect.bisect_left(ls,5)
index3 = bisect.bisect_right(ls,5)
print("index1 = {}, index2 = {}, index3 = {}".format(index1, index2, index3))
```

结果是:
```
index1 = 4, index2 = 1, index3 = 4
```

## 对于bisect 函数：
- 始终保证返回idx，能使左边的所有数字均不大于该数字，并且右边的数字均大于该数字；
