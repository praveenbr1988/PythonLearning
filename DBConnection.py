import mysql.connector

myDb = mysql.connector.connect(
     host="localhost",
     user="root",
     passwd="Mangisangi1!",
     database="globalelectronicsretailer"
)

mycursor = myDb.cursor()
mycursor.execute("select * from customers limit 10")
results = mycursor.fetchall()

print (results)

for x in  results:
    print (x)

myDb.close()


