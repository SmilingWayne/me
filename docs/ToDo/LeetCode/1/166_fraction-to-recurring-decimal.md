# 166_分数到小数


!!! note
    字符串 | 模拟

- 🔑🔑 难度： <span style = "color:gold; font-weight:bold">Medium</span>


> 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。
> 
> 如果小数部分为循环小数，则将循环的部分括在括号内。
> 
> 如果存在多个答案，只需返回 任意一个 。
> 
> 对于所有给定的输入，保证 答案字符串的长度小于 $10^4$ 。
> 


```
输入：numerator = 1, denominator = 2
输出："0.5"
输入：numerator = 1, denominator = 3
输出："0.(3)"
```

----------------


??? note

    要点：模拟除法的手动计算过程
    
    难点：如何确定每一个循环节？一旦遇到一个出现过的被除数就停止，遇到0就不需要进行循环了
    
    StringBuilder 同样可以使用insert操作
    
    每次被除数都是原数字 * 10 再除以除数
    
    非常烦恼的Long int转换：建议一开始就直接实现转换以减少错误


----------


=== "Java"

    ```Java
    class Solution {
        public String fractionToDecimal(int numerator, int denominator) {
            StringBuilder sb = new StringBuilder();
            long num1 = (long)numerator;
            long num2 = (long)denominator;
            if(num1 < 0 && num2 > 0){
                num1 = (-1) * num1; 
                sb.append("-");
            }
            else if(num1 > 0 && num2 < 0){
                num2 = (-1) * num2;
                sb.append("-");
            }
            else if(num1 < 0 && num2 < 0){
                num1 = (-1) * num1;
                num2 = (- 1) * num2;
            }
            if(num1 % num2 == 0){
                sb.append((long )(num1 / num2));
                return sb.toString();
            }
            String next = get_underZero((num1 * 10), num2);
            if(num1 > num2){
                next =  get_underZero(((num1 % num2 ) * 10), num2);
            }
            else{
                next = get_underZero((num1 * 10), num2);
            }
            
            sb.append((long)(num1 / num2) );
            sb.append(".");
            sb.append(next);   
            return sb.toString();
        }

        public String get_underZero(Long a, Long b){
            
            Map<Long, Integer> map = new HashMap<>();
            StringBuilder sb = new StringBuilder();
            int idx = 0;
            while(!map.containsKey(a)){
                map.put(a , idx ++ );
                sb.append((int)(a / b));
                a = (a % b) * 10;
                if(a == 0){
                    return sb.toString();
                }
            }
            sb.insert(map.get(a), "(");
            sb.append(")");
            return sb.toString();
            
        }
    }
    ```

