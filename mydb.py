import mysql.connector


dataBase = mysql.connector.connect(

	host = "localhost",
	user = "root",
	password ="Saiddeagle8",
)


# create cursor

cursorObject = dataBase.cursor()

# create the db

cursorObject.execute("CREATE DATABASE mydb")

print("Everything is set up")