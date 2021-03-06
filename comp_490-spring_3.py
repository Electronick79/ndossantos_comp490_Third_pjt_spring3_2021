import sqlite3
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
  )
# creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor()
# executing cursor with execute method and pass SQL query
db_cursor.execute("CREATE DATABASE comp490_spring_3")
# get list of all databases
db_cursor.execute("SHOW DATABASES")
#print all databases
for db in db_cursor:
	print(db)

df = pd.read_csv(r'Path where the XLSX file is stored\COMP490_SPRING_3.XLSX')
print(df)

conn = sqlite3.connect('TestDB.db')
c = conn.cursor()

# Create table - occupation occupational
c.execute('''CREATE TABLE OCCUPATIONAL
             ([generated_id] INTEGER PRIMARY KEY,[Occupational_Name] text, [Title] text, [Date_start] dates, [Occupation] occupation, [Wage] integer, [State] text,,)''')

db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)

# Create table - STATES
c.execute('''CREATE TABLE STATES
             ([generated_id] INTEGER PRIMARY KEY,[States_ID] integer, [States_Name] text)''')

db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)

# Create table - EMPLOYMENT
c.execute('''CREATE TABLE EMPLOYMENT_STATUS
             ([Employment_Name] text, [STATE_Name] text, [Date] date), [ Field_in_that_state] text''')
db_cursor.execute("SHOW TABLES")

for table in db_cursor:
	print(table)

# Create table - 25TH_PERCENTILE_SALARY
c.execute('''CREATE TABLE 25TH_PERCENTILE_SALARY
             ([25th_percent_salary] integer, [Employment_Name] text, [Date] date), [ Field_in_that_state] text''')

db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)


conn.commit()






#df = pd.DataFrame({'States':['California', 'Florida', 'Montana', 'Colorado', 'Washington', 'Virginia'],
    #'Capitals':['Sacramento', 'Tallahassee', 'Helena', 'Denver', 'Olympia', 'Richmond'],
    #'Population':['508529', '193551', '32315', '619968', '52555', '227032']})
