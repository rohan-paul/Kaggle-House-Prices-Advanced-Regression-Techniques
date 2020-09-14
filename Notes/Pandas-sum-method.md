#### Pandas .sum() method

https://www.dataschool.io/pandas-dot-notation-vs-brackets/

Most of my pandas code is a made up of chains of selections and methods. By using dot notation, my code is mostly adorned with periods and parentheses (plus an occasional quotation mark):

```python
df.col_one.sum()
df.col_one.isna().sum()
df.groupby('col_two').col_one.sum()
```

If you instead use bracket notation, your code is adorned with periods and parentheses plus lots of brackets and quotation marks:

```python
df['col_one'].sum()
df['col_one'].isna().sum()
df.groupby('col_two')['col_one'].sum()
```