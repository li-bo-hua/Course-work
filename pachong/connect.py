import pymysql


def connect_mysql():
    # 建立与MySQL数据库的连接
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='Scrape_book',
        charset='utf8mb4'
    )
    return conn