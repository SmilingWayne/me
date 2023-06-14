<h3>2022.4.01Leetcode 每日一题</h3>

---



#### [954. 二倍数对数组](https://leetcode-cn.com/problems/array-of-doubled-pairs/)

难度：【Medium】

给定一个长度为偶数的整数数组 arr，只有对 arr 进行重组后可以满足 “对于每个 0 <= i < len(arr) / 2，都有 arr[2 * i + 1] = 2 * arr[2 * i]” 时，返回 true；否则，返回 false。



```
输入：arr = [3,1,3,6]
输出：false
```



- 要点：HashMap与正负号讨论

- 数组



先排序：-8，-4，-4，-2，0，0，1，2，3，6这种情况的考虑：首先可以先记录下负数的位置，这里还要考虑到可能全是负数的情况

然后要考虑0的情况：一定要全都都是偶数个才可以

然后就是会有重复的比如-4，-4 谁对应着哪一个的情况；

确保map里面一定所有的value 都是0都被清空了

分别判断当下的数字放进去能否变成可行的进行消去或者不可行的直接入map





```Java
class Solution {
    public boolean canReorderDoubled(int[] arr) {
        Map<Integer, Integer> map = new HashMap<>();
        Arrays.sort(arr);
        int idx_neg = -1;
        for(int i = 0; i < arr.length; i ++ ){
            if(arr[i] >= 0){
                idx_neg = i;
                break;
            }
        }
        // -6 -3

        // -8 -4 -4 -2 -2 
        map.put(arr[0], 1);
        for(int i = 1; i < arr.length; i ++ ){
            if(i < idx_neg || arr[arr.length - 1] < 0){

                if(!map.containsKey(arr[i] * 2) || map.get(arr[i] * 2) == 0){
                    // return false;
                    map.put(arr[i], map.getOrDefault(arr[i] , 0) + 1);
                }
                else{
                    map.put(arr[i] * 2, map.get(arr[i] * 2) - 1);
                }
            }
            else{
                if(arr[i] == 0){
                    map.put(arr[i], (map.getOrDefault(arr[i], 0) + 1 ) % 2);
                }
                else{
                    if(!map.containsKey(arr[i]) && arr[i - 1] <= 0){
                        map.put(arr[i], 1);
                    }
                    else{
                        if(arr[i] % 2 == 0 && map.containsKey((arr[i] / 2 ))){
                            if(map.get(arr[i] / 2) != 0){
                                map.put((arr[i] / 2), map.get((arr[i] / 2 )) - 1);  
                            } 
                            else{
                                map.put(arr[i],map.getOrDefault(arr[i], 0) + 1);
                            }
                            // System.out.println(arr[i] / 2);
                        }
                        else{
                            map.put(arr[i],map.getOrDefault(arr[i], 0) + 1);
                        }
                    }
                }

            }
        }
        // 0 0 1 2 2 4 4 8
        for(Integer a: map.keySet()){
            if(map.get(a) != 0){
                System.out.println(a + " " + map.get(a));
                return false;
            }
        }
        return true;
    }
}
```

```Java
class Solution {
    public boolean canReorderDoubled(int[] arr) {
        Map<Integer, Integer> cnt = new HashMap<Integer, Integer>();
        for (int x : arr) {
            cnt.put(x, cnt.getOrDefault(x, 0) + 1);
        }
        if (cnt.getOrDefault(0, 0) % 2 != 0) {
            return false;
        }

        List<Integer> vals = new ArrayList<Integer>();
        for (int x : cnt.keySet()) {
            vals.add(x);
        }
        Collections.sort(vals, (a, b) -> Math.abs(a) - Math.abs(b));

        for (int x : vals) {
            if (cnt.getOrDefault(2 * x, 0) < cnt.get(x)) { // 无法找到足够的 2x 与 x 配对
                return false;
            }
            cnt.put(2 * x, cnt.getOrDefault(2 * x, 0) - cnt.get(x));
        }
        return true;
    }
}
```

