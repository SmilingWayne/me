#### [470. 用 Rand7() 实现 Rand10()](https://leetcode-cn.com/problems/implement-rand10-using-rand7/)



---

给定方法 rand7 可生成 [1,7] 范围内的均匀随机整数，试写一个方法 rand10 生成 [1,10] 范围内的均匀随机整数。

你只能调用 rand7() 且不能调用其他方法。请不要使用系统的 Math.random() 方法。

每个测试用例将有一个内部参数 n，即你实现的函数 rand10() 在测试时将被调用的次数。请注意，这不是传递给 rand10() 的参数。

难度：【Medium】

```C++
#include <iostream>
#include <vector>
using namespace std;

// 下面的代码是实现11，难度系数更加高一点
// 一个比较高频率的面试题
int rand7()
{
    return rand() % 7 + 1;
}

int rand11()
{
    int first = 0, second = 0;
    while (true)
    {
        while ((first = rand7()) > 6)
        {
            first = rand7();
        }
        while ((second = rand7()) > 6)
        {
            second = rand7();
        }
        second = (first & 1) == 1 ? second : second + 6;
        if (second < 12)
        {
            return second;
        }
    }
}
int rand11_2()
{
    while (true)
    {
        int ans = (rand7() - 1) * 7 + rand7() - 1;
        if (ans >= 1 && ans <= 44)
        {
            return ans % 11 + 1;
        }
    }
}
int main()
{

    // 按照当前时间给出随机数种子
    // printf("%d", rand7());
    vector<int> t(11, 0);
    for (int i = 0; i < 1000000; i++)
    {
        t[rand11_2() - 1] += 1;
        // printf("%d", t[0]);
    }
    for (int i = 0; i < 11; i++)
    {
        cout << (i + 1) << " " << t[i] << "\n";
    }
}
```



