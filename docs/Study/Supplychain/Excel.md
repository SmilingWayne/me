# 一些简单易学好上手的 Excel 小功能


> 本文所有的Excel相关内容均在Excel For mac 上实现，如有版本问题，需要自行搜索解决方案；

- 数据透视表(Pivot Table)

- 数据切片器(slicer)
  - 可以支持多个Pivot Table之间的联动

- Excel 设置月份自动填充 ✅ （下拉时候弹出的小方框里可以设置）
- Excel Randbetween 函数 ✅ （只支持Int）
- Excel 删除一列里的重复元素 ✅ （data -> filter -> Advanced filter）
- Excel 时间戳转换成具体时间 ✅ 
- Excel 时间戳转为时间格式：

```
=TEXT((XX/1000+8*3600)/86400+70*365+19,"yyyy/mm/dd hh:mm:ss.000")
```
- Excel GetPIVOTDATA：通过数据透视表获得数据 ✅
  - =GetPIVOTDATA("你要求的数据在表格里的名称（如：平均成绩"）, 透视表的位置, x_1, y_1, x_2, y_2)
  - 后面的x_1 - y_1 对应一个 “你需要的名称 - 你给定的数值”的映射～

- (XX 表示你所要处理的数据所在的单元格)
- 如果没有东八区时区要求就把8 * 3600 删除掉
- 如果不需要显示毫秒，就把最后的.000删掉
- 杜邦分析仪