
# Python sqlite3:
 * https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial


# refs:
 * https://flask.palletsprojects.com/en/2.3.x/patterns/sqlite3/
 * https://stackoverflow.com/questions/23394081/sqlite3-where-clause-in-python
 * https://stackoverflow.com/questions/200309/how-to-create-timestamp-column-with-default-value-now
 * https://stackoverflow.com/questions/1601151/how-do-i-check-in-sqlite-whether-a-table-exists
 * https://www.askpython.com/python-modules/check-if-a-table-exists-python-sqlite3
 * https://tableplus.com/blog/2018/04/sqlite-check-whether-a-table-exists.html
```sql
create table if not exists TableName (col1 typ1, ..., colN typN)
```

```sql
drop table if exists TableName
```

```sql
SELECT name FROM sqlite_master WHERE type='table' AND name='table_name';
SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';

connection.execute("DROP TABLE employee")

cur.execute('''
   CREATE TABLE employee(
       emp_id integer,
       name text,
       designation text,
       email text
       )''')
```