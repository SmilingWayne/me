2022.4.16 Leetcode日常刷题

---

#### [1487. 保证文件名唯一](https://leetcode-cn.com/problems/making-file-names-unique/)

<h2 style = "text-align:center">保证文件名唯一</h2>

>  难度：<span style = "color :Pink">Medium</span>
>
>  要点：<u>字符串、哈希表、前缀思想</u>

<center>给你一个长度为` n` 的字符串数组` names` 。

<center>你将会在文件系统中创建 n 个文件夹：在第 `i` 分钟，新建名为 `names[i]` 的文件夹。

<center>由于两个文件 不能 共享相同的文件名，因此如果新建文件夹使用的文件名已经被占用，

<center><span style = "color:yellow">系统会以 (k) 的形式为新文件夹的文件名添加后缀</span>，其中 k 是能保证文件名唯一的 最小正整数 。

<center>返回长度为 n 的字符串数组，其中 ans[i] 是创建第 i 个文件夹时系统分配给该文件夹的<span style = "color:white">实际名称</span>

```
输入：names = ["pes","fifa","gta","pes(2019)"]
输出：["pes","fifa","gta","pes(2019)"]
解释：文件系统将会这样创建文件名：
"pes" --> 之前未分配，仍为 "pes"
"fifa" --> 之前未分配，仍为 "fifa"
"gta" --> 之前未分配，仍为 "gta"
"pes(2019)" --> 之前未分配，仍为 "pes(2019)"
```



- 思路：一个一个走，一个一个保存，如果这个名字已经被占用了，

  就直接往后找直到可以放入的那个数字，然后map里面需要加入（一个是更新，一个是插入新的）两个新的key，一个是加上括号的，一个是之前原名字的当前数字

- 解释：例如`[A,A(1),A(2),A]`最终结果就是`[A,A(1),A(2),A(3)]`.

- 结果：超过48%

```Java
class Solution {
    public String[] getFolderNames(String[] names) {
        String[] ans = new String[names.length];
        Map<String, Integer> map = new HashMap<>();
        for(int i = 0; i < names.length; i ++ ){
            if(!map.containsKey(names[i])){
                map.put(names[i], 0);
                ans[i] = names[i];
            }
            else{
                StringBuilder sb = new StringBuilder();
                sb.append(names[i]);
                sb.append("(");
                int cur = map.get(names[i]);
                for(int j = cur + 1; ; j ++ ){
                    StringBuilder sb2 = new StringBuilder(sb);
                    sb2.append(j);
                    sb2.append(")");
                    if(!map.containsKey(sb2.toString())) {
                        ans[i] = sb2.toString();
                        map.put(names[i], j);
                        map.put(sb2.toString(), 0);
                        break;
                    }
                }
            }  
        }
        return ans;
    }
}
```




