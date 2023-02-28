
### Exist 
exists 用于检查你的子查询是否至少会返回一行数据，该子查询实际上并不返回任何数据，而是返回值True或False,它并不缓存exists后面那个查询的结果集，因为exists()结果集的内容并不重要，重要的是其内查询语句的结果集空或者非空，空则返回false，非空则返回true。
- e.g.现在我们想要查找总访问量(count 字段)大于 200 的网站是否存在。
我们使用下面的 SQL 语句：

```SQL
SELECT Websites.name, Websites.url 
FROM Websites 
WHERE EXISTS (
    SELECT count FROM access_log 
    WHERE Websites.id = access_log.site_id AND count > 200);
```

- 这个执行顺序很特殊，是先执行最开始的主查询(也就是上面的`SELECT Websites.name, Websites.url FROM Websites `)，这时候有一个查询结果了，然后对查询结果进行exists后面的判断。
- 这里第三行的exists (xxxx) 是作为类似“是/否”的bool判断进行的，它实际上是在一行一行地判断主查询的结果是否满足exists后面的条件，然后告诉你“满足/不满足（true/false）”，如果是满足的，主查询的那行结果就保留，否则删除。
- 也可以where not exists ，意思就是“不满足后面需求”xxx


### In  

```SQL

select * from A where id in (select id from B)
```
- IN()只执行一次，它查出B表中的所有id字段并缓存起来。之后，检查A表的id是否与B表中的id相等，如果相等则将A表的记录加入结果集中，直到遍历完A表的所有记录。
  
- 用途是：**确定给定的值是否与子查询或列表中的值相匹配**。
- 它执行的顺序是：in在查询的时候，首先查询子查询的表，然后将查询的到的表和原来的表做一个笛卡尔积，然后按照条件进行筛选。所以相对原来的表比较小的时候，in的速度较快。
- in 返回的是查询的数据，而exists返回的是bool值；



### having

在 SQL 中增加 HAVING 子句原因是，WHERE 关键字无法与聚合函数（也就是最大值啦，最小值啦，平均数啦min / max/ avg)一起使用。


having与where的区别:
- having后面可以使用聚合函数
- where后面不可以使用聚合
- having是在**分组后**对数据进行过滤（也就是先groupby再having）
- where是在分组前对数据进行过滤



- 在查询过程中执行顺序：from>where>group（含聚合）>having>order>select。

- 所以聚合语句(sum,min,max,avg,count)要比having子句优先执行，而where子句在查询过程中执行优先级别优先于聚合语句(sum,min,max,avg,count)。

- where 后面不能用聚合函数，所以下面的是错误的：
```SQL
-- 查找人数大于 5 的部门
select dept_id, count(*)
from employee
where count(*) > 5
group by dept_id;
```

- 应该这样：

```SQL 
select dept_id, count(*)
from employee
group by dept_id
having count(*) > 5; -- 这是正确的
```

- ⚠️另一方面，HAVING子句中不能使用除了**分组字段**和**聚合函数**之外的其他字段。例如，以下语句将会返回错误：

```SQL 
select addtime,name from dw_users where addtime> 1500000000 
-- 👆这个是正确的

select phone,name from dw_users having addtime> 1500000000  
-- 👆错误❌，因为前面没有select addtime 这个字段

select phone,name, addtime from dw_users having addtime> 1500000000  
 -- 👆这个是正确的

```

- ⚠️ 这个语句也会返回错误：

```SQL
select dept_id, count(*)
from employee
group by dept_id
having salary >= 30000; 
👆-- 这一行是错的，因为groupby分组之后没有salary这个字段，只有dept_id这个字段了
```