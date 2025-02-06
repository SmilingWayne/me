# Random: 管理你的随机数

`random` 是 Python 的一个内置库，用于生成伪随机数。这里的 “伪随机” 意味着这些随机数是通过确定性算法生成的，并不是真正意义上的随机数，但在大多数应用场景中，它们的表现就像是随机的。random 库提供了多种随机数生成函数，涵盖了整数、浮点数、序列等不同类型的随机选择操作。

### 核心功能及用法

1. **生成随机浮点数**

**`random.random()`**：生成一个范围在 `[0.0, 1.0)` 之间的随机浮点数。
    - **示例代码**：
```python
import random
random_float = random.random()
print(random_float)
```

**`random.uniform(a, b)`**：生成一个范围在 `[a, b]` 之间的随机浮点数，其中 `a` 和 `b` 可以是任意实数，且 `a` 可以大于 `b`。

```python
import random
# 生成一个范围在 [5, 10] 之间的随机浮点数
random_uniform = random.uniform(5, 10)
print(random_uniform)
```

2. **生成随机整数**

**`random.randint(a, b)`** ：生成一个范围在 **`[a, b]`** 之间的随机整数，其中 `a` 和 `b` 必须是整数，且 `a <= b`。

```python
import random
# 生成一个范围在 [1, 10] 之间的随机整数
random_int = random.randint(1, 10)
print(random_int)
```

**`random.randrange(start, stop[, step])`**：从 `range(start, stop, step)` 所表示的序列中随机选择一个整数。`start` 是起始值（默认为 0），`stop` 是结束值（不包含），`step` 是步长（默认为 1）。


```python
import random
# 从 0 到 10 中每隔 2 取一个数，然后随机选择一个
random_range = random.randrange(0, 10, 2)
print(random_range)
```

3. **随机选择序列元素**

**`random.choice(seq)`**：从非空序列 `seq`（如列表、元组、字符串等）中随机选择一个元素。


```python
import random
# 定义一个列表
my_list = [1, 2, 3, 4, 5]
# 从列表中随机选择一个元素
random_choice = random.choice(my_list)
print(random_choice)
```

**`random.choices(population, weights=None, *, cum_weights=None, k=1)`**：从 `population` 序列中进行**有放回的随机抽样**，返回一个长度为 `k` 的列表。`weights` 是一个与 `population` 长度相同的权重列表，用于指定每个元素被选中的概率；`cum_weights` 是累积权重列表。如果都不提供，则每个元素被选中的概率相等。

```python
import random

# 定义一个列表
my_list = [1, 2, 3, 4, 5]
# 从列表中有放回地随机选择 3 个元素
random_choices = random.choices(my_list, k=3)
print(random_choices)
```
**`random.sample(population, k)`**：从 `population` 序列中进行无放回的随机抽样，返回一个长度为 `k` 的列表。要求 `k` 不能大于 `population` 的长度。


```python
import random
# 定义一个列表
my_list = [1, 2, 3, 4, 5]
# 从列表中无放回地随机选择 2 个元素
random_sample = random.sample(my_list, 2)
print(random_sample)
```

4. **打乱序列顺序**

**`random.shuffle(x[, random])`** ：将可变序列 `x`（如列表）中的元素随机打乱顺序。


```python
import random

# 定义一个列表
my_list = [1, 2, 3, 4, 5]
# 打乱列表元素的顺序
random.shuffle(my_list)
print(my_list)
```


**- 由于 `random` 库生成的是伪随机数，其结果是可重复的。可以通过 `random.seed(a=None, version=2)` 函数设置随机数种子，当 `a` 相同时，后续生成的随机数序列也相同**。

例如：
```python
import random

# 设置随机数种子
random.seed(42)
print(random.random())  # 每次运行都会得到相同的结果, for reproducibility
```
