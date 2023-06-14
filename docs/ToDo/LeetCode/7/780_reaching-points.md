2022.4.09 Leetcode 日常刷题

#### [780. 到达终点](https://leetcode-cn.com/problems/reaching-points/)

🔑🔑 考点：数学

🚴‍♀️🚴‍♀️ 难度： <span style = "color:red; font-weight:bold">Hard</span>

🔗🔗 链接：https://leetcode-cn.com/problems/reaching-points/

📖📖 题目：

给定四个整数 sx , sy ，tx 和 ty，如果通过一系列的转换可以从起点 (sx, sy) 到达终点 (tx, ty)，则返回 true，否则返回 false。

从点 (x, y) 可以转换到 (x, x+y)  或者 (x+y, y)。

💻💻 测试用例：

```
输入: sx = 1, sy = 1, tx = 3, ty = 5
输出: true
解释:
可以通过以下一系列转换从起点转换到终点：
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)
```

💡💡思路：

- 注意几个特点：每个数字都是正数。所以一旦数字更大就一定错
- 直接针对结果做处理
- 1 16 999999 16的情况，直接取余数

👩🏻‍💻🧑🏻‍💻 代码：

```Java
class Solution {
    public boolean reachingPoints(int sx, int sy, int tx, int ty) {
        if(sx == tx && sy == ty){
            return true;
        }
        if(tx == ty){
            return false;
        }
        if(tx == sx){
            if(sy > ty){
                return false;
            }
            if(sy < ty){
                if((ty - sy) % sx != 0){
                    return false;
                }
                return true;
            }

        }
        if(ty == sy){
            if(sx > tx){
                return false;
            }
            if(sx < tx){
                if((tx - sx) % sy != 0){
                    return false;
                }
                return true;
            }

        }
        while(true){
            if(tx == ty)
                break;
            if(tx > ty){
                tx = tx - ty;
                if(tx == sx && ty == sy)
                    return true;
            }
            if(tx < ty){
                ty = ty- tx;
                if(tx == sx && ty == sy)
                    return true;
            }
        }
        return false;
    }
}
```

