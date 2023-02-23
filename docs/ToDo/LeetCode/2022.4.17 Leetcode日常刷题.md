2022.4.17 Leetcode 日常刷题

#### [819. 最常见的单词](https://leetcode-cn.com/problems/most-common-word/)

难度：【Medium】

链接：https://leetcode-cn.com/problems/most-common-word/

考点：哈希表 + 字符串

描述：

```
给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。返回出现次数最多，同时不在禁用列表中的单词。

题目保证至少有一个词不在禁用列表中，而且答案唯一。

禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母。
```

``` 
输入: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
输出: "ball"

```

- 比较简单的字符串+哈希表，注意细节是标点符号会干扰字符的判断
- Java中String无法直接更改，最好修改成char[] 或者StringBuilder / StringBuffer 



```Java
class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        paragraph += ".";
        Set<String> ban = new HashSet<>();
        Map<String , Integer> map = new HashMap<>();
        for(String a:banned){
            ban.add(a);
        }
        String ans = "";
        int time = 0;
        StringBuilder word = new StringBuilder();
        for(int i = 0 ; i < paragraph.length(); i ++ ){
            if(Character.isLetter(paragraph.charAt(i))){
                word.append(Character.toLowerCase(paragraph.charAt(i)));
            }
            else if(word.length() > 0){
                if(!ban.contains(word.toString())){
                    map.put(word.toString(), map.getOrDefault(word.toString(),0) +1);
                    if(map.get(word.toString()) > time){
                        time = map.get(word.toString());
                        ans = word.toString();
                    }
                }
                word = new StringBuilder();
            }
        }
        return ans;
    }
}
```

