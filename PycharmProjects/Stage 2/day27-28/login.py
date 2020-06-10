"""
    注册登录模拟
"""


import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='stu',charset='utf8')

# 获取游标　（操作数据库，执行sql语句）
cur = db.cursor()

def do_register():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    sql = "select * from user where username='%s'" % (username)
    cur.execute(sql)
    if cur.fetchone():
        return False
    try:
        sql = "insert into user (username,password) values (%s,%s)"
        cur.execute(sql,[username,password])
        db.commit()
        return True
    except:
        db.rollback()
        return False

def do_login():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    sql = "select * from user where username='%s' and password='%s'" % (username,password)
    cur.execute(sql)
    db.commit()
    if cur.fetchone():
        return True

while True:
    print("1.注册\n2.登录\n3.退出")
    cmd = int(input("输入命令:"))
    if cmd == 1:
        # 注册
        if do_register():
            print("注册成功")
        else:
            print("注册失败")
    elif cmd == 2:
        # 登录
        if do_login():
            print("登录成功")
            break
        else:
            print("登录失败")
    elif cmd == 3:
        print("谢谢使用")
        break
    else:
        print("输入错误，请重新输入")
# 执行sql语句


# 关闭数据库
cur.close()
db.close()

