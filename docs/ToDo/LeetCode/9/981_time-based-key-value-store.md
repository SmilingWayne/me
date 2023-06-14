#### [981. 基于时间的键值存储](https://leetcode-cn.com/problems/time-based-key-value-store/)



**难度：【Medium】**

**类型：数据结构设计**

设计一个基于时间的键值数据结构，该结构可以在不同时间戳存储对应同一个键的多个值，并针对特定时间戳检索键对应的值。

实现 TimeMap 类：

TimeMap() 初始化数据结构对象
void set(String key, String value, int timestamp) 存储键 key、值 value，以及给定的时间戳 timestamp。
String get(String key, int timestamp)
返回先前调用 set(key, value, timestamp_prev) 所存储的值，其中 timestamp_prev <= timestamp 。
如果有多个这样的值，则返回对应最大的  timestamp_prev 的那个值。
如果没有值，则返回空字符串（""）。



- 难点：一个key会对应多个value，本质上是根据时间戳动态地选择value 的数值
- 所以思路之一是重新设计HashMap使得一个key能对应一个list的value
- 同时由于value 的输入是按照时间进行的，所以一定是一个排好序的list
- 再对list二分查找就行了

```Java
class TimeMap {



    Map<String, List<Node> > map = new HashMap<>();

    public TimeMap() {
        

    }
    
    public void set(String key, String value, int timestamp) {
        if(!map.containsKey(key)) {
            map.put(key, new ArrayList<>());
        }
        map.get(key).add(new Node(timestamp, value));
    }
    
    public String get(String key, int timestamp) {
        if(!map.containsKey(key)){
            return "";
        }
        List<Node> a = map.get(key);
        if(timestamp < a.get(0).timestamp){
            return "";
        }
        else if (timestamp >= a.get(a.size() - 1).timestamp){
            return a.get(a.size() - 1).val;
        }
        else{
            int start = 0;
            int end = a.size() - 1;
            while(start <= end){
                int mid = start + (end - start) /2;
                if(timestamp >= a.get(mid).timestamp && timestamp < a.get(mid + 1).timestamp){
                    return  a.get(mid).val;
                }
                
                
                else if(a.get(mid).timestamp < timestamp){
                    start = mid + 1;
                }
                else if(a.get(mid).timestamp > timestamp){
                    end = mid - 1;
                }
            }
            return "";
        }
    }


    static class Node{
        int timestamp;
        String val;
        public Node(int timestamp, String val){
            this.timestamp = timestamp;
            this.val = val;
        }
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */
```





