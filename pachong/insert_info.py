import connect


def insert_info(info):
    conn = connect.connect_mysql()
    cursor = conn.cursor()
    sql = "INSERT INTO book_info(title,score,typeN,price,author,published_at,publisher,page_number,isbm) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (info)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()