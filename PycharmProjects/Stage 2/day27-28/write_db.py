"""
    write_db.py
    pymysql　写操作 (insert,update,delete)
"""

import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='student_info',charset='utf8')

# 获取游标　（操作数据库，执行sql语句）
cur = db.cursor()

# 数据库写操作

try:
    # sql语句执行

    # 插入操作
    """
    name = input("Name:")
    age = input("Age:")
    score = input("Score:")
    
    # 第一种sql语句：
    # sql = "insert into class (name,age,score) values ('{}',{},{});".format(name,age,score)
    
    # 第二种sql语句：可以使用列表给sql语句的values赋值
    sql = "insert into class (name,age,score) values (%s,%s,%s);"

    cur.execute(sql,[name,age,score])
    db.commit()
    """

    # 修改操作
    """
    sql = "update class set sex='M' where id>11;"
    cur.execute(sql)
    db.commit()
    """

    # 删除操作
    """
    sql = "delete from class where id>11;"
    cur.execute(sql)
    db.commit()
    """

except Exception as e:
    db.rollback()   # 发生异常，数据库退回到commit执行之前的状态
    print(e)



# 关闭数据库
cur.close()
db.close()


