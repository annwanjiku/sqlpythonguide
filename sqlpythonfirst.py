import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user = "yourusername",
    password = "yourpassword",
    database = "sakila"
)

my_cursor = my_db.cursor()
my_cursor.execute("SHOW TABLES")
print("MY TABLES:")
print("---------------------------------------------------------------------------------------------------------------")
for table in my_cursor:
    print(table[0])
print("---------------------------------------------------------------------------------------------------------------")
my_cursor.close()

my_cursor = my_db.cursor()
my_cursor.execute("select actor_id,first_name,last_name from actor where first_name like 'P%'")
results = my_cursor.fetchall()
print("\n")
print("select actor_id,first_name,last_name from actor where first_name like 'P%")
for result in results:
    print(f"{result[0]},{result[1]},{result[2]}")
print("\n %s database closed"%my_db.database.upper())

my_cursor.close()
my_db.close()

