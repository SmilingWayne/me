# PyEcharts

## 3D 柱状图 by PyEcharts


```python
import pyecharts.options as opts
from pyecharts.charts import Bar3D
import random

hours = [ f"{i}a" for i in range(1,13)] + [f"{i}p" for i in range(1,13)]
days = ["Saturday", "Friday", "Thursday",
        "Wednesday", "Tuesday", "Monday", "Sunday"]
data = [
    [i, j, random.randint(2, 20)] for i in range(7) for j in range(24)
]
data = [[d[1], d[0], d[2]] for d in data]
# hours: list()表示X轴刻度
# days: list()表示Y轴刻度
# data: list(list(x, y, z)) 分别表示(x,y,z)坐标
(
    Bar3D()
    .add(
        series_name="",
        data=data,
        xaxis3d_opts=opts.Axis3DOpts(type_="category", data=hours),
        yaxis3d_opts=opts.Axis3DOpts(type_="category", data=days),
        zaxis3d_opts=opts.Axis3DOpts(type_="category"),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            max_=20,
            range_color=[
                "#313695",
                "#4575b4",
                "#74add1",
                "#abd9e9",
                "#e0f3f8",
                "#ffffbf",
                "#fee090",
                "#fdae61",
                "#f46d43",
                "#d73027",
                "#a50026",
            ],
        )
    )
    .render("bar3d_punch_card.html")
)

```


<figure markdown>

![3D柱状图](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202310251130709.png)(./OUT_FOLDER/3Dcolumns.png)

</figure>


## 桑基图

```Python

import pandas as pd

df1 = pd.read_excel("Task 1.xlsx", sheet_name = "流入")
df2 = pd.read_excel("Task 1.xlsx", sheet_name = "流出")
data = {}

all_nodes = set(list(df1["from"]))
all_nodes |= set(list(df1["to"]))
all_nodes |= set(list(df2["from"]))
all_nodes |= set(list(df2["to"]))

nodes_ = []
links_ = []
for index, row in df1.iterrows():
    if row["count"] > 1:
        links_.append({"source" : row['from'],\
             "target" : row['to'], "value" : row["count"]})
        nodes_.append( row['from'])
        nodes_.append( row['to'])

for index, row in df2.iterrows():
    if row["count"] > 1:
        links_.append({"source" : row['from'], \
            "target" : row['to'], "value" : row["value"]})
        nodes_.append( row['from'])
        nodes_.append( row['to'])

nodes_ = list(set(nodes_))
nodes__ = []
for i in nodes_:
    nodes__.append({'name' : i})

data['nodes'] = nodes__
data['links'] = links_

# ==================== 👆数据处理部分 ========================
# ==================== 👇可视化部分 ========================
import pyecharts.options as opts
from pyecharts.charts import Sankey
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType


s = Sankey(init_opts=opts.InitOpts(width="800px",\
     height="800px", bg_color = "ffffff",\
     theme=ThemeType.PURPLE_PASSION))
s.add(
        series_name="",
        nodes=data["nodes"],
        links=data["links"],
        itemstyle_opts=opts.ItemStyleOpts(
            border_width=1,
            border_color="#aaa"),
        linestyle_opt=opts.LineStyleOpts(
            color="source", 
            curve=0.7, 
            opacity=0.4),
        tooltip_opts=opts.TooltipOpts(
            # trigger_on="mousemove",
            is_show=True,
            trigger_on='mousemove|click', formatter=JsCode(
                """function(params){
                    
                    return params.data.source + params.data.target;
                }
                """)
            ),

        label_opts=opts.LabelOpts(
            position="right",
            font_size=20,
            # color="white"),
        ),
    )
s.render("sankey_diagram12.html") # 也支持保存为图片

```




<figure markdown>

![](https://cdn.jsdelivr.net/gh/SmilingWayne/picsrepo/202310251130711.png){: style height=350 }

</figure>