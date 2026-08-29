from loguru import logger
import mysql.connector

connection = mysql.connector.connect(host="localhost",user="root",passwd="ADMIN",database="home_builder")
cursor = connection.cursor()

# logger.info(f"{connection}")

cursor = connection.cursor()  # this helps in executing the mysql query

# cursor.execute("SELECT * FROM labours_table")

insert_query = "delete from labours_table where id =7"
# cursor.execute(insert_query, ('Rahul','labour',700))
cursor.execute(insert_query)
connection.commit()
cursor.execute("SELECT * FROM labours_table")
result = cursor.fetchall()
logger.info(f"{result}")