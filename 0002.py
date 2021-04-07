import pymysql
import string
import random

db = pymysql.connect('localhost', 'root', '123', 'show_me_code')

cursor = db.cursor()

cursor.execute('DROP TABLE IF EXISTS show_me_code_table')

sql = """CREATE TABLE show_me_code_table (
         jihuoma  CHAR(12) NOT NULL
         )"""

cursor.execute(sql)

base_str = string.ascii_letters+string.digits

for i in range(20):
    #random.sample 返回 list，所以要组合成一个字符串
    #利用join对一个可迭代对象进行插入指定字符
    ss = ''.join(random.sample(base_str, 12))
    sql_insert = f"INSERT INTO show_me_code_table (jihuoma) VALUES ('{ss}')"

    try:
        # 执行sql语句
        cursor.execute(sql_insert)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()


db.close()
