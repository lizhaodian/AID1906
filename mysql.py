import pymysql


# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

# 获取游标，用来操作数据库，执行sql语句，用于承载执行结果
cur = db.cursor()

# 执行sql语句
sql = "insert into class_1 values (7,'Emma', 17, 'w', 76.5, '2019-7-18');"  # 分号可加可不加

cur.execute(sql)    # 执行语句

db.commit()     # 将写操作提交，多次写操作一同提交也可以，只有commit可才对数据库进行操作，不commit数据库是不会发生变化的，select查询操作不是写操作

# 关闭数据库
cur.close()
db.close()
