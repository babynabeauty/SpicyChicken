import string

from dao.dbConnect import connect

def objectResearch(name:string):
    try:
        db, cursor = connect()
        # 选择带数据库中带有这个关键词的
        sql="select * from kind where name like '%{name}%'".format(name=name)
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
    except Exception:
        db.rollback()
        return None, False
    finally:
        db.close()
        cursor.close()
    return data, True


def ClassifyResearch(name:string):
    try:
        db, cursor = connect()
        sql="select * from classifyInfo where kind like '%{name}%'".format(name=name)
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
    except Exception:
        db.rollback()
        return None, False
    finally:
        db.close()
        cursor.close()
    return data, True



