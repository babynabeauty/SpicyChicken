import string

from dao.dbConnect import connect

def objectResearch(name:string):
    try:
        db, cursor = connect()
        # 选择带数据库中带有这个关键词的
        # sql = "select * from kind where name like '% %s %'"%(name)
        sql="select * from kind where name like '%塑料瓶%'"
        print(sql)
        cursor.execute(sql)
        data = cursor.fetchall()
    except Exception:
        db.rollback()
        return None, False
    finally:
        db.close()
        cursor.close()
    print(data)
    return data, True

