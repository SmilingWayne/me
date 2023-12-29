# Pandas 中一些常用的数据预处理以及特征工程方法



!!! example "来源" 
    
    主要来自研一上一次失败的冷链物流销量预测预测比赛。


### 各种输入输出的文件格式

- parquet：

```python
sales_df.to_parquet(output_path + 'sales_sum.parquet', index=False)
```

### 通过浮点数数据类型修正减小内存消耗


```Python 

def reduce_mem_usage(df, verbose=True):
	"""_summary_
    	整个函数是为了减少数据读取的内存损耗，我们不需要修改
	Args:
		df (_type_): _description_
		verbose (bool, optional): _description_. Defaults to True.

	Returns:
		_type_: _description_
	"""
	numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
	start_mem = df.memory_usage().sum() / 1024**2
	for col in df.columns:
		col_type = df[col].dtypes
		if col_type in numerics:
			c_min = df[col].min()
			c_max = df[col].max()
			if str(col_type)[:3] == 'int':
				if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
					df[col] = df[col].astype(np.int8)
				elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
					df[col] = df[col].astype(np.int16)
				elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
					df[col] = df[col].astype(np.int32)
				elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
					df[col] = df[col].astype(np.int64)
			else:
				if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
					df[col] = df[col].astype(np.float16)
				elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
					df[col] = df[col].astype(np.float32)
				else:
					df[col] = df[col].astype(np.float64)
	end_mem = df.memory_usage().sum() / 1024**2
	if verbose:
		print('Mem. usage decreased to {:5.2f} Mb ({:.1f}% reduction)'.format(end_mem, 100 * (start_mem - end_mem) / start_mem))
	return df
```
