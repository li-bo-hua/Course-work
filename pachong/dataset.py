# 此代码为数据库的创建，如果已经有数据库，则可忽略
import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    charset='utf8mb4',
)
# 创建数据库test
create_db_sql = "CREATE DATABASE IF NOT EXISTS Scrape_book;"  # 此处创建了名为：Scrape_book的数据库
cursor = conn.cursor()
cursor.execute(create_db_sql)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()