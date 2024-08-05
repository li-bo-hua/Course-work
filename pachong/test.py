# 数据库连接测试
import connect

def test_connect_mysql():
    conn = connect.connect_mysql()
    assert conn is not None
    conn.close()

test_connect_mysql()


# 数据表创建测试
import create_table

def test_create_tables():
    create_table.create_tables()

test_create_tables()


# 数据插入测试
import insert_info

def test_insert_info():
    info = ["Test Title", "9.0", "Test/Type", "$10", "Test Author", "2021-01-01", "Test Publisher", "100", "1234567890"]
    insert_info.insert_info(info)

test_insert_info()

