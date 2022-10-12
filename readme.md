# PDPG
A faster pipeline between Pandas and Postgresql via psycopg.

### Why?
Data engineers and data scientists heavily rely on pandas. Loading tons of data to and from a database, i.e., PostgreSQL, is a heavy and time-consuming task.

### Traditional approach:
`Postgresql <> psycopg <> ORM <> Pandas`

In this example, we tried to dicth ORM and directly contact psycopg as it is the go-to driver for Python.


### Benchmark
Pandas default IO vs PDPG.
|     |     |
| --- | --- |
| Method | Performance Bump |
| Pull | 20% -30% |
| Push | 40x - 60x |

\* We have used a 1 million row dataset with 15 columns of various data types, including date and datetime.

For more information, please visit [speed_test.ipynb](speed_test.ipynb).
