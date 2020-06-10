"""
    read_db.py
    pymysql 读操作　（select）
"""

import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='stu',charset='utf8')

# 获取游标　（操作数据库，执行sql语句）
cur = db.cursor()

# 执行sql语句
sql = "select * from class;"
cur.execute(sql)    # 执行正确后,cur通过调用函数获取结果

# 获取一个查询结果
# onerow = cur.fetchone()
# print(onerow)
# print(onerow[5])

# 获取多个查询结果
# manyrow = cur.fetchmany(3)
# print(manyrow)
# print(manyrow[2][1])

# 获取所有查询结果
allrow = cur.fetchall()
print(allrow)

# 关闭数据库
cur.close()
db.close()