#### [380. O(1) 时间插入、删除和获取随机元素](https://leetcode-cn.com/problems/insert-delete-getrandom-o1/)

----

难度：【Medium】

实现RandomizedSet 类：

RandomizedSet() 初始化 RandomizedSet 对象
bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。
你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。

```Java

class RandomizedSet {
    Map<Integer, Integer> map = new HashMap<>();
    ArrayList<Integer> t = new ArrayList<>();
    Random random = new Random();
    
    public RandomizedSet() {

    }
    
    public boolean insert(int val) {
        if(map.containsKey(val)){
            return false;
        }
        t.add(val);
        map.put(val, t.size() - 1);
        return true;
    }
    
    public boolean remove(int val) {
        if(!map.containsKey(val)){
            return false;
        }
        int lastKey = t.get(t.size() - 1);
        int curLoc = map.get(val);
        map.put(lastKey, curLoc);
        t.set(curLoc, lastKey);
        map.remove(val);
        t.remove(t.size() - 1);
        return true;
    }
    
    public int getRandom() {
        return t.get(random.nextInt(t.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
```

- 关键在：如何在O(1)时间内实现删除？
- 原理类似于洗牌算法，可以把要删除的那个和数组最后一个互换位置，从而只删除最后一个，而中间的那些数据（已经存在Map里面）的value就不需要修改了。

类似题目

> 

