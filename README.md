# A Guide into Using SQL with Python (MySQL Connector)
This guide provides a general introduction to using Python to interact with a MySQL database using the `mysql-connector-python` library. It covers setting up a connection, retrieving data, and executing queries.

## Prerequisites
Before using MySQL with Python, ensure you have:
- Python installed (Python 3 recommended)
- MySQL Server installed and running
- The `mysql-connector-python` package installed:

  ```sh
  pip install mysql-connector-python
  ```
- A MySQL database set up with relevant tables

## Connecting to MySQL
To establish a connection to MySQL:

```python
import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)
```
- Replace `yourusername` and `yourpassword` with your MySQL credentials.
- Ensure the database `yourdatabase` exists in your MySQL instance.

## Retrieving Tables from the Database
To list all tables in the database:

```python
my_cursor = my_db.cursor()
my_cursor.execute("SHOW TABLES")
print("Tables in the database:")
for table in my_cursor:
    print(table[0])
my_cursor.close()
```
- This script executes `SHOW TABLES` and prints the table names.

## Executing a SQL Query
To retrieve specific records from a table:

```python
my_cursor = my_db.cursor()
my_cursor.execute("SELECT column1, column2 FROM your_table WHERE condition")
results = my_cursor.fetchall()

print("Query Results:")
for result in results:
    print(f"{result[0]}, {result[1]}")
```
- Modify `your_table` and `column1, column2` to match your database structure.
- Use `WHERE condition` to filter results as needed.

## Inserting Data into a Table
To insert data into a table:

```python
my_cursor = my_db.cursor()
sql = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
values = ("value1", "value2")
my_cursor.execute(sql, values)
my_db.commit()
print("Record inserted successfully.")
my_cursor.close()
```
- Always call `commit()` after executing `INSERT`, `UPDATE`, or `DELETE` queries.

## Updating Data in a Table
To update records:

```python
my_cursor = my_db.cursor()
sql = "UPDATE your_table SET column1 = %s WHERE condition"
values = ("new_value",)
my_cursor.execute(sql, values)
my_db.commit()
print("Record updated successfully.")
my_cursor.close()
```

## Deleting Data from a Table
To delete records:

```python
my_cursor = my_db.cursor()
sql = "DELETE FROM your_table WHERE condition"
my_cursor.execute(sql)
my_db.commit()
print("Record deleted successfully.")
my_cursor.close()
```

## Closing the Database Connection
Always close the cursor and database connection when done:

```python
print("Database connection closed.")
my_cursor.close()
my_db.close()
```

## Running the Script
1. Save the script as `script.py`.
2. Run it using:
   ```sh
   python script.py
   ```
3. Check the output for table names, query results, and other operations.

## Notes
- Ensure your database contains the necessary tables and data before running queries.
- Modify queries to match your database schema.
- Always use `commit()` when making changes to the database.

---


