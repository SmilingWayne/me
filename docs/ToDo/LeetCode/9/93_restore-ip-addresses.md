#### [93. 复原 IP 地址](https://leetcode-cn.com/problems/restore-ip-addresses/)

难度：【Medium】

标签：回溯、字符串

有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。

```
输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35
```

- 重难点：如何表示每一个阶段的四个数字
- 重难点：如何表示头是0的情况
- 重难点：dfs函数

- 一个想法：一定要设置一个限定初值（也就是总大小）的数组或者static value才可以

```Java
class Solution {
    static final int SEG_COUNT = 4;
    List<String> ans = new ArrayList<String>();
    int[] segments = new int[SEG_COUNT];

    public List<String> restoreIpAddresses(String s) {
        segments = new int[SEG_COUNT];
        dfs(s, 0, 0);
        return ans;
    }

    public void dfs(String s, int segId, int segStart) {
        // 如果找到了 4 段 IP 地址并且遍历完了字符串，那么就是一种答案
        if (segId == SEG_COUNT) {
            if (segStart == s.length()) {
                StringBuffer ipAddr = new StringBuffer();
                for (int i = 0; i < SEG_COUNT; ++i) {
                    ipAddr.append(segments[i]);
                    if (i != SEG_COUNT - 1) {
                        ipAddr.append('.');
                    }
                }
                ans.add(ipAddr.toString());
            }
            return;
        }

        // 如果还没有找到 4 段 IP 地址就已经遍历完了字符串，那么提前回溯
        if (segStart == s.length()) {
            return;
        }

        // 由于不能有前导零，如果当前数字为 0，那么这一段 IP 地址只能为 0
        if (s.charAt(segStart) == '0') {
            segments[segId] = 0;
            dfs(s, segId + 1, segStart + 1);
        }

        // 一般情况，枚举每一种可能性并递归
        int addr = 0;
        for (int segEnd = segStart; segEnd < s.length(); ++segEnd) {
            addr = addr * 10 + (s.charAt(segEnd) - '0');
            if (addr > 0 && addr <= 0xFF) {
                segments[segId] = addr;
                dfs(s, segId + 1, segEnd + 1);
            } else {
                break;
            }
        }
    }
}
```



3.26 补充：为什么一定要设置一四位数组：因为每次进行回溯的结果一定是前面确定好的n（n < 4)数字，并且这些数字在现在肯定还需要使用到，所以就这样设置了.

```C++
class Solution {
public:

    int MAX_LENGTH = 4;
    vector<string> ans;
    vector<int> segment;

    vector<string> restoreIpAddresses(string s) {
        if(s.size() > 12){
            return ans;
        }

        segment.resize(MAX_LENGTH);
        dfs(s, 0, 0);
        return ans;
    }


    void dfs(const string &s, int idx, int start){
        if(idx == MAX_LENGTH){
            if(start == s.size()){
                string temp = "";
                for(int i = 0; i < MAX_LENGTH; i ++ ){
                    temp += to_string(segment[i]);
                    if(i != MAX_LENGTH - 1)
                        temp += "."; 
                }
                ans.push_back(temp);
                // temp.clear();
            }
            return;
        }

        if(start == s.size()){
            return;
        }
        
        if(s[start] == '0'){
            segment[idx] = 0;
            dfs(s, idx + 1, start + 1);
            return;
        }
        int judge = 0;
        for(int i = start; i < s.size(); i ++ ){
            judge = judge * 10 + (s[i] - '0' );
            if(judge > 255){
                return;
            }
            else{
                segment[idx ] = judge;
                // segment.push_back(judge);
                dfs(s, idx + 1, i + 1);
            }
        }


    }
};
```

