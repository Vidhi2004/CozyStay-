import os
import pymysql

hostname = 'localhost'
user = 'root'
password = 'dbms'

try:
    db = pymysql.connections.Connection(
        host=hostname,
        user=user,
        password=password,
        db='cozy'
    )
    print('Connection successful')
except Exception as e:
    print(e)