import pymysql
import re

f = open("dict.txt",mode='r')

# 连接数据库
db = pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='dict',charset='utf8')

# 获取游标　（操作数据库，执行sql语句）
cur = db.cursor()

sql = "insert into words values (%s,%s)"

for line in f:
    tup = re.findall(r"(\S+)\s+(.*)",line)[0]
    try:
        cur.execute(sql,tup)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

f.close()

# 关闭数据库
cur.close()
db.close()

