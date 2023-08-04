# Markdown 极简入门


!!! note
    - [Markdown 语法的扩展使用](https://markdown.com.cn/extended-syntax/availability.html)
    - [Markdown Basics](https://daringfireball.net/projects/markdown/basics)
    - [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)

------------


## 小标题

```

# 这是一个大标题

## 这是小标题

### 这是更小的标题

```


-------------



## 要点 

```
- 这是一个要点 
- 这是第二个要点 
    - 这是一个子要点 
    - 这也是一个子要点
        - 这是子要点的子要点
- 这是第三个要点
```

> 上述内容显示如下：

- 这是一个要点 
- 这是第二个要点 
    - 这是一个子要点 
    - 这也是一个子要点
        - 这是子要点的子要点
- 这是第三个要点


----------

## 引用 

```
> 这是一个引用
> 
> 这也是一个引用 
> > 这是引用的引用！ 
> 
> 这还是一个引用

```

!!! note 
    上述内容显示如下：
> 这是一个引用
> 
> 这也是一个引用 
> > 这是引用的引用！ 
> > > 这是引用的引用的引用！ 
> 
> 这还是一个引用

-------------
## 引用中的要点

> 这是第一句话
> - 这是第一句话的一个要点
> - 这是第一句话的第二个要点

```
> 这是第一句话
> 
> - 这是第一句话的一个要点
> - 这是第一句话的第二个要点
```


-----------------

## 超链接

<https://markdown.com.cn>

```
<https://markdown.com.cn> 

<!-- 只需要加上 < > 即可 -->
```


------

## 带格式化的超链接


I love supporting the **[EFF](https://eff.org)**.
This is the *[Markdown Guide](https://www.markdownguide.org)*.
See the section on [`code`](./MarkdownQuickStart.md).

```
I love supporting the **[EFF](https://eff.org)**.
This is the *[Markdown Guide](https://www.markdownguide.org)*.
See the section on [`code`](./MarkdownQuickStart.md).
```

-----------

## 带超链接的图片

[![沙漠中的岩石图片](../../picx/Example-7x7-30-2000.jpg "Shiprock")](https://markdown.com.cn)

----------------------

## 删除线

~~Nooooo!!~~

```
~~Nooooo!!~~
```


---------


## CriticMap 的新增格式

!!! example "内容展开"
    - [参考链接](https://github.com/CriticMarkup/CriticMarkup-toolkit)，一种新的 Markdown 编码风格
    - 在这里打总是会自己渲染，呈现原来的方式略显奇怪了～

   

    
----------

## 分割线


- 专起一行输入`---------`，只要大于等于3个“-”就行。


---------


## 行内代码块

- 用`\`` 符号对代码进行包裹即可；如： 

> `Hello!`


## 代码块

```text 
    
    ```Python
    print("Hi! This is Python")
    ```

```

- 用三个"`" 对多行代码块进行包裹，如上代码显示为：



```Python
print("Hi! This is Python")
```

---------------

## 任务列表


```text 
- [x] 刷牙
- [x] 洗漱
- [ ]  归还图书
```

> 以上内容显示如下：

- [x] 刷牙
- [x] 洗漱
- [ ]  归还图书


------

## 输入上下标


=== "下标"

    ```H~2~O```

    > 显示为H~2~O


=== "上标"

    ```19^th^century```

    > 显示为： 19^th^century


---------


## Admonition

```text 
!!! note / question / abstract / quote / answer / question "你的标题"
    这里是内容
```

规范一点写就是如下的：

```text 
!!! note "这是我的标题"
    这里是我的内容
```

> 显示如下：

!!! note "这是我的标题"
    这里是我的内容

------




## 添加Annotations

> 尝试失败，尚不知具体原因。
>
> 失败链接：[传送门](https://squidfunk.github.io/mkdocs-material/reference/annotations/)




