# Employee Databases bu James Page 4/1/2020

import sqlite3
from sqlite3 import Error

con = sqlite3.connect('mydatabase')
cursorObj = con.cursor()

def sql_connection():
    try:
       con = sqlite3.connect(':memory:')
       print('Connection Established.  Database is created in memory')
    
    except Error:
        print(Error)
    
    finally:
        con.close()
        
sql_connection()

def sql_table(con):

    cursorObj = con.cursor()

    cursorObj.execute("CREATE TABLE IF NOT EXISTS employees(employee_id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")

    con.commit()
    
    cursorObj.execute("CREATE TABLE IF NOT EXISTS addresses(address_id integer PRIMARY KEY, address text, city text, state text, zip text)")

    con.commit()

    
    con = sql_connection()

sql_table(con)

cursorObj.execute("INSERT OR IGNORE INTO employees VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')")

cursorObj.execute("INSERT OR IGNORE INTO addresses VALUES(1, '752 SE Pine Street', 'Roseburg', 'OR', '97470')")

con.commit()

cursorObj.execute('''SELECT employee_id FROM employees
INNER JOIN addresses ON employees.employee_id = addresses.address_id
where employee_id >= 1''')
