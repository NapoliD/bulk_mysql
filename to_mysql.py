#https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-executemany.html
import pymysql

conn = pymysql.connect(user="",password="", host="",database="")
print(conn) 
cursor = conn.cursor()

data = [
  ('Jane', date(2005, 2, 12)),
  ('Joe', date(2006, 5, 23)),
  ('John', date(2010, 10, 3)),
]

data=[]
for i,row in data2.iterrows():
    data.append(tuple(row))
    
stmt = "INSERT INTO `test_bulk` (`student_id`,`otro_dato`) VALUES (%s,%s)"
cursor.executemany(stmt, data)

