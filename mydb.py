# Install Mysql on your computer 
# download mysql
# install mysql 
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Ladric.99'
    )

# prepare a cursor object 
cursorObject = dataBase.cursor()


#Create a dataBase 
cursorObject.execute("CREATE DATABASE ladricko")

print("All Done!")

