# Usage of Set / frozenset

Python 中，集合 (set)，包括不可变集合 (frozenset) 是一个重要的数据结构。可以总结其若干用法（快速入门版）：

## set

话不多说，直接上代码：

`union()`
:   返回两个集合的并集；

`intersection()`
:   返回两个集合的交集；

`A.difference(B)`
:   返回属于A但不属于B的元素集合；

`A.symmetric_difference(B)`
:   返回A和B的并集中不同时属于A和B的元素的集合；

`A.issuperset(B)`
:   判断A是否是B的超集；

`A.issubset(B)`
:   判断A是否是B的子集；

`A.disjoint(B)`
:   判断A和B是否不相交；

`A.update(B)`
:   更新集合 A，将 B 中元素加入 A；

`A.symmetric_difference_update(B)`
:   更新集合 A，剔除 A和B交集中的元素，将原先A中不存在但B中存在的元素加入A；

`A.difference_update(B)`
:   保留仅出现在 A 中的所有元素；

`A.intersection_update(B)`
:   保留 A 和 B 的交集。


```python
# Usage of `set`

if __name__ == "__main__": 
    setA = set([1,2,3,4,5])
    setB = set([6,7,8,9,10])
    setC = set([1,2,3])
    setD = set([4,5,6,7])
    
    # 1) .union()
    print(setA.union(setB))
    # Method.1: Output the Union (setA or setB)
    # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    print(setA | setB)
    # Method.2: Output the Union (setA or setB)
    # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    
    # 2) .intersection()
    print("The common element of setA and setD:", setA.intersection(setD))
    # Method.1: Output the Union (setA or setB)
    # {4, 5}
    print("The common element of setA and setD:", setA & setD)
    # Method.2: Output the Union (setA or setB)
    # {4, 5}
    
    # 3) difference():
    print("The difference of setA and setD:", setA - setD)
    # Method.1: Output the element in setA but not in setD
    print("The difference of setA and setD:", setA.difference(setD))
    # Method.2: Output the element in setA but not in setD
    
    # 4) .issuperset():
    print(f"SetA is a superset of setB?", setA.issuperset(setB)) 
    # Test whether every element in setB is in the setA.
    # {1, 2, 3}
    print(f"SetA is a superset of setC?", setA.issuperset(setC))
    # Test whether every element in setC is in the setA.
    # {1, 2, 3}
    
    # 5) .issubset()
    print(f"SetA is a subset of setB?", setA.issubset(setB))
    # Test whether every element in setA is in setB.
    # False
    print(f"SetC is a subset of setA?", setC.issubset(setA))
    # Test whether every element in setA is in setB.
    # True

    # 6) .disjoint()
    print(f"Each element in setA is NOT in setB?", setA.isdisjoint(setB))
    # Test whether setA and setB are disjoint.
    # True
    print(f"Each element in setD is NOT in setA?", setD.isdisjoint(setA))
    # False
    
    # 7) .symmetric_difference()
    print(setA.symmetric_difference(setD))
    # Output the element in setA or setD but not in both, equals: (setA - (setA & setD)) | (setD - (setA & setD))
    # {1, 2, 3, 6, 7}
    print((setA - (setA & setD)) | (setD - (setA & setD)))
    # {1, 2, 3, 6, 7}
```

```python
# Set Update
if __name__ == "__main__": 
    setA = set([1,2,3,4,5])
    setB = set([1,2,3,4,5])
    setC = set([1,2,3,4,5])
    setD = set([1,2,3,4,5])
    setE = set([4,5,6,7])

    setA.update(setE) 
    # Update the set, adding elements from all others.
    print(setA) # {1, 2, 3, 4, 5, 6, 7}
    
    setB.symmetric_difference_update(setE) 
    # Update the set, keeping only elements found in either set, but not in both.
    print(setB) # {1, 2, 3, 6, 7}
    
    setC.intersection_update(setE)
    # Update the set, keeping only elements found in it and all others.
    print(setC) # {4, 5}
    
    setD.difference_update(setE)
    # Update the set, removing elements found in others.
    print(setD) # {1, 2, 3}
```


```python
# Set Removal

if __name__ == "__main__": 
    setA = set([1,2,3,4,5])
    setA.add(6)
    # {1,2,3,4,5,6}
    setA.remove(3)
    # {1,2,4,5,6}
    print(setA)
```


## frozenset

是一种特殊的set，声明后无法增加、调整、删除、修改集合中的元素。而且，可以作为字典的 key，因此适合保存一些不变的数据。其初级用法和set完全一样。事实上，你可以将第一个代码块中的所有内容原封不动地运行，除了将最开始的声明修改成：

```python
# Usage of `frozenset`

if __name__ == "__main__": 
    setA = frozenset([1,2,3,4,5])
    setB = frozenset([6,7,8,9,10])
    setC = frozenset([1,2,3])
    setD = frozenset([4,5,6,7])
```

此时所有返回的集合都将是frozenset，原先的判断True/False的依然可以正常运行。

重要的是，frozenset 是可哈希的。我们可以在字典中使用frozenset，也可以利用集合，判断某个frozenset是否在集合中。比如：

```python
# Usage of `frozenset`

if __name__ == "__main__": 
    setA = frozenset([1,2,3,4,5])
    setB = frozenset([6,7,8,9,10])
    setC = frozenset([1,2,3])
    setD = frozenset([4,5,6,7])
    bigSet = set([setA, setB, setC, setD])
    print(frozenset([1,2,3,4,5]) in bigSet)
```

此时会正常输出 "True"。

而如果你用set表示这几个元素，会报错：

```txt
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[38], line 8
      6 setC = set([1,2,3])
      7 setD = set([4,5,6,7])
----> 8 bigSet = set([setA, setB, setC, setD])
      9 print(set([1,2,3,4,5]) in bigSet)

TypeError: unhashable type: 'set'
```

我第一次知道frozenset，就是在做图论相关的内容时候了解到的。

