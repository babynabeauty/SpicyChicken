from dao.dbConnect import connect
# 存储新闻
def saveNews(title, author, time, url, picture, type, tag):
    try:
        db, cursor = connect()
        # 插入新闻
        sql = "insert into news (title, author, time, url, picture, type, tag) values('%s','%s','%s','%s','%s','%s','%s')"%(title, author, time, url, picture, type, tag)
        cursor.execute(sql)
        db.commit()
    except Exception:
        db.rollback()
        return False
    finally:
        db.close()
        cursor.close()
    return True