import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='126.comM',
    database='mybase',
    charset='utf8'  # 编码一定要写对，不然会报错
)

cursor = conn.cursor(pymysql.cursors.DictCursor)

username = input('username>>>: ')
password = input('password>>>: ')

# sql = "select * from user where username='%s' and password='%s'"%(username,password)
sql = "select * from user where username=%s and password=%s"
print(sql)

"""
sql 注入问题，要屏蔽这个问题，需要把重要的变量拿给代码去操作，而不是自己封装
username>>>: user1' or 1=1 -- dfad
password>>>: 
select * from user where username='user1' or 1=1 -- dfad' and password=''
[{'id': 1, 'username': 'user1', 'password': 'pass123', 'lock_status': 0, 'describe': '这是用户 1 的描述'}, {'id': 2, 'username': 'user2', 'password': 'pass456', 'lock_status': 1, 'describe': '这是用户 2 的描述'}, {'id': 3, 'username': 'user3', 'password': 'pass789', 'lock_status': 0, 'describe': '这是用户 3 的描述'}]

"""


res = cursor.execute(sql,(username,password)) # 代码会自动识别变量
if res:
    print(cursor.fetchall())
else:
    print('用户名和密码错误.')

"""
屏蔽了sql注入的问题
username>>>: user1' or 1=1 -- adfadf
password>>>: 
select * from user where username=%s and password=%s
用户名和密码错误.
"""