import connect
def create_tables():
    conn = connect.connect_mysql()
    cursor = conn.cursor()
    # 创建数据表
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS book_info (
        `key` INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(50),
        score VARCHAR(20),
        typeN VARCHAR(50),
        price VARCHAR(20),
        author VARCHAR(50),
        published_at VARCHAR(50),
        page_number VARCHAR(50),
        publisher VARCHAR(50),
        isbm VARCHAR(50)
    )
'''
    cursor.execute(create_table_sql)
    conn.commit()
    conn.close()
    cursor.close()
create_tables()