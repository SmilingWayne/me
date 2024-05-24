### 182 查找重复的邮箱


```sql
select email 
from Person 
group by email
having count(email) > 1
```

!!! warning "使用groupby的场合：存在重复？ 使用Having的场合"


### 184 查找部门工资最高的员工

```
表： Employee

+--------------+---------+
| 列名          | 类型    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
在 SQL 中，id是此表的主键。
departmentId 是 Department 表中 id 的外键（在 Pandas 中称为 join key）。
此表的每一行都表示员工的 id、姓名和工资。它还包含他们所在部门的 id。
 

表： Department

+-------------+---------+
| 列名         | 类型    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
在 SQL 中，id 是此表的主键列。
此表的每一行都表示一个部门的 id 及其名称。
 

查找出每个部门中薪资最高的员工。
按 任意顺序 返回结果表。
查询结果格式如下例所示。
```


```sql
SELECT
    Department.name AS 'Department',
    Employee.name AS 'Employee',
    Salary
FROM
    Employee
        JOIN
    Department ON Employee.DepartmentId = Department.Id
WHERE
    (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
    )
;

```

!!! warning "首先需要找到，每个部门的最高工资；然后将表合并。查找那个（部门，工资）元组在 “每个部门最高的工资”"


### 196 删除重复的电子邮箱

```sql
delete p1 from person p1, person p2
where p1.email = p2.email and p1.Id > p2.id
```


### 197 上升的温度

找到比前一天的温度要高的日期的id。

```sql
select A.id
from Weather as A cross join Weather as B 
on datediff(A.recordDate, B.recordDate) = 1
where A.temperature > B.temperature
```

!!! warning "注意，这种需要和前面的日期比的都需要灵活使用cross join。 再次注意 on 的使用，再次注意：datediff的使用：衡量过了多少日期"

### 577 员工奖金


```sql
select name, bonus
from Employee left join Bonus
on Employee.EmpId = Bonus.EmpId
where bonus is null or bonus < 1000
```

!!! warning "on的使用， is null的使用"