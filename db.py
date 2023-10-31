import mysql.connector as db

dataBase = db.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'root'
    # auth_plugin='mysql_native_password'

	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE dcrm")

print("All Done!")



