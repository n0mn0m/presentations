import os
import pyodbc
from pprint import pprint

if __name__ == "__main__":

    with pyodbc.connect("DSN=MSSQLDockerODBCDemo;UID=SA;PWD=d3m0p@ssw0rd;", autocommt=True) as conn:
        print(f"Process ID: {os.getpid()}")
        breakpoint()
        with conn.cursor() as cursor:
            for table in cursor.execute("select * from sys.tables"):
                pprint(table)

    with pyodbc.connect("DSN=PostgresDockerODBCDemo;UID=postgres;PWD=example;", autocommt=True) as conn:
        conn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
        conn.setencoding(encoding='utf-8')
        with conn.cursor() as cursor:
            for db in cursor.execute("select * from pg_user;"):
                columns = [column[0] for column in cursor.description]
                pprint(columns)
                pprint(db)
