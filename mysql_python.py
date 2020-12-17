import mysql.connector
import datetime
import time
import random

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="newuser",
  password="1234",
  database="hoc_sql"
)
while True:
  t = datetime.datetime.now()
  y = random.randint(1,10)#lấy giá trị random
  x= t.strftime("%X")
  mycursor = mydb.cursor()

  sql = "INSERT INTO doan2 (cot1, cot2) VALUES (%s, %s)"
  val = (x,y)
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted.")


  print(t.strftime("%X"))
  time.sleep(3)