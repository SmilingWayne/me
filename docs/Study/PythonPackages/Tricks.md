# 一些Python的小技（踩）巧（坑）分（经）享（验）

## Pandas 篇

读取数据表的时候，路径没有错误，文件名也没有错误，sheet_name 没有错误，但是读取不了，

执行代码:

```Python
import pandas as pd
xl = pd.read_excel('./nurses_data.xlsx', sheet_name="Skills")
print(xl)

```

报错显示：

```
ValueError: Worksheet index 0 is invalid, 0 worksheets found
```

或者 

```
Worksheet named 'Skills' not found
```

最后[在这里](https://stackoverflow.com/questions/69948897/pandas-valueerror-worksheet-index-0-is-invalid-0-worksheets-found)找到了答案：原来是用Excel软件保存表格的时候需要选择另存为的格式，

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202311101641157.png)


千万不能选那个strict XML的！不然打不开！

如果用Excel Book的xlsx格式保存，执行同样的代码就能跑了！