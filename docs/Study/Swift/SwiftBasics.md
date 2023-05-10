# Swift Basics


- `guard` “守护”，其实也是一种if条件判断，如果布尔值是否，那么执行else后面的语句
    - guard只有一个代码块，但是if 有多个
    - 好处：
        - 1.guard可以把不符合条件的处理事件前置，以免程序猿在开发中有遗漏的情况出现。
        - 2.guard还可以减少条件语句中的嵌套数量，使代码更简洁易读。

- `String(X)` ：把X转化成string类型

- 判断字符类型：

```Swift
type(of : x)

if x is Double {
    print("\{x} is double")
}
```

- 判断字符串长度`.count`

```Swift

let a = "1217684"
print(a.count)
// 7
```


- 在print中直接输出变量`\()`


```Swift

let yourSen = "125748"
print("\(yourSen)")

// 125748
```


- 保留字符串第一个值并输出


```Swift

var st = "37298y" // Must be var
print(st.removeFirst())
print(st.removeLast())
// 3
// y
```


- 遍历

```Swift

var a = [[Int]]
for idx in 1..< a.count { a in 
    print(in)
}
```

- 声明一个空列表

```Swift
var used = [Bool](repeating: false, count: n)
var tasks : [Int] = []

```

- inout 参数： 函数传入地址而不是值

```Swift

    func backtrack(_ track: inout [Int], _ nums: [Int], _ used: inout [Bool]) {
    }

    // 引用的时候：

    backtrack(&track, nums, &used)
```