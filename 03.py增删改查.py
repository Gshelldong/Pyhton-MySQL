import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='126.comM',
    database='mybase',
    charset='utf8',  # 编码一定要写对，不然会报错
    autocommit=True   # 自动提交事物，如果不配置每次修改数据需要手动提交
)

cursor = conn.cursor(pymysql.cursors.Cursor)

"""
增删改操作 都必须加一句
conn.commit()操作 
和这个参数的功能是一致的
autocommit=True
"""

# sql = 'insert into user(`username`,`password`,`describe`) values("admin","admin123","管理员")'
# sql = 'update user set lock_status = 0 where id =2'
sql = 'delete from user where id =3'
cursor.execute(sql)