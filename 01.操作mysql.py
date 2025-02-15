import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='126.comM',
    database='mybase',
    charset='utf8'  # 编码一定要写对，不然会报错
)

cursor = conn.cursor(pymysql.cursors.DictCursor) # 产生一个游标对象以字典形式返回
sql = 'select * from students'
res = cursor.execute(sql)
print(res)   # 直接查询是返回所有的结果的长度
print(cursor.fetchone())   # 获取结果的一条数据，类似生成器，迭代器原理
print(cursor.fetchone())   # 获取结果的一条数据，类似生成器，迭代器原理
# print(cursor.fetchone())   # 获取结果的一条数据
# cursor.scroll(2,mode='absolute')  # 绝对游标，从开始向后移动两个位置
cursor.scroll(1,mode='relative')  # 相对游标，上面移动到了2，然后再跳过一条，最后的结果还剩一条

print(cursor.fetchall())   # 获取所有数据
"""
4
{'id': 1, 'name': '张三', 'gender': '男', 'class': '高三（1）班', 'hobby': '篮球'}
{'id': 2, 'name': '李四', 'gender': '女', 'class': '高三（2）班', 'hobby': '绘画'}
[{'id': 4, 'name': '赵六', 'gender': '女', 'class': '高三（4）班', 'hobby': '阅读'}]
"""
