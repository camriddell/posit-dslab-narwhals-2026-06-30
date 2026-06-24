# Posit Data Science Lab

```python
print("Let's talk DataFrames & Narwhals!")
```

```Rscript
"Let's talk data.frames!"
```

## What is Narwhals

Narwhals is a lightweight (read as: dependency-free) Data/LazyFrame interface.

Primarily used by
- Libraries whose audience bring their own DataFrames
    - e.g. py-shiny, gt-extras, plotly, altair, bokeh, sklearn, pandera
- Some subset of people who don't like writing SQL

```sh
eog -f images/narwhals-downstream.svg
```

### DataFrame Agnostic Expressions

Columnar sum across different dataframes

```python

```

### Avoiding SQL

```python

```

## Why are DataFrames Challenging in Python?

- DataFrames have only been around for ~15 years in Python
- For 12 of those years, `pandas` was the only choice
∴  many packages were designed to cater specifically to pandas

But looking at the DataFrame horizon today...

```sh
eog -f images/narwhals-dataframes.svg
```

And along the way, they all made different decisions, not just in API
design but also in both the storage and treament of underlying values.

### Index Alignment (pandas only)

```python
from pandas import DataFrame

df_a = DataFrame({'a': [1,2,3]})
df_b = DataFrame({'b': [1,2,3]})

print(df_a + df_b)
```

```python
from pandas import DataFrame

df_a = DataFrame({'a': [1,2,3]}, index=[0, 1, 2   ])
df_b = DataFrame({'a': [1,2,3]}, index=[   1, 2, 3])

print(df_a + df_b)
```

## Null vs NaN Distinctions

```python
import pandas as pd
import polars as pl
import duckdb

from utils import printh

pd_df = pd.DataFrame({'a': [1.0, float('nan'), None]})
pl_df = pl.DataFrame({'a': [1.0, float('nan'), None]})
duck_df = duckdb.sql('''select * from pl_df''')

printh(pd_df, pl_df, duck_df)

# Polars - Validity Buffers

# Arrow - Validity Buffers

# pandas - ??
```

## Grouped Sums

These tools don’t even agree on the results of some basic computations

```python
import narwhals as nw
import pandas as pd
import polars as pl
import numpy as np
import duckdb

from utils import printh

rng = np.random.default_rng(0)

data = {
    "group": rng.choice(["A", "B", "C"], size=20),
    "value": rng.normal(loc=100, scale=15, size=20),
}

# single dispatch/match case

```

## Narwhals is More Than a Syntax

Sure, it's a syntax. But it also smooths over these differences.

```python
import narwhals as nw
import pandas as pd
import polars as pl
import numpy as np
import duckdb

from utils import printh

rng = np.random.default_rng(0)

data = {
    "group": rng.choice(["A", "B", "C"], size=20),
    "value": rng.normal(loc=100, scale=15, size=20),
}


```

## When do we use Narwhals?

When you want to write analytical code that makes use of DataFrames,
but do not have control over the DataFrames that you are being handed.

Some minor nuance
- You enjoy writing expressions, rather than a bespoke DataFrame API
- You don’t like writing SQL and are using DuckDB

## When do we NOT use Narwhals?

When you are writing your own analytical pipeline.
If you are the one reading, analyzing, and manipulating the data
you’re likely better off to use one of the "native" DataFrame tools (pandas, Polars, etc.)

```python
import pandas as pd
import polars as pl
import narwhals as nw

df = pd.DataFrame({'a': [None,5,7,10], 'b':[ 1, 3, 4, 2], 'c': [5, 4, 3, 2]})
print(df.corr(method='pearson'))
```

## How does Narwhals Even Work?

Many Layers of _Composition_

```python
# goal: df.select(col('a').mean()) on a pandas DataFrame
```

