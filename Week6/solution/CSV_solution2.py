from sqlite3 import *

conn = connect("c:\sqlite\week6.db")

curobj = conn.cursor()

query = "insert into result\
                    values(?,?,?,?,?,?,?)"

data = []
for i in range(3):
    sid = int(input("Enter Student ID :"))
    sname = input("Enter Student Name : ")
    mark1 = int(input("Enter Mark1 :"))
    mark2 = int(input("Enter Mark2 :"))
    mark3 = int(input("Enter Mark3 :"))
    mark4 = int(input("Enter Mark4 :"))
    mark5 = int(input("Enter Mark5 :"))
    inside_data = [sid,sname,mark1,mark2,mark3,mark4,mark5]
    data.append(inside_data)

curobj.executemany(query,data)

conn.commit()

conn.close()
