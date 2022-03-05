from dao.dbConnect import connect
def showall():
    try:
        db, cursor = connect()
        # 选择题库所有的题
        sql = "select * from question"
        cursor.execute(sql)
        data = cursor.fetchall()
    except Exception:
        db.rollback()
        return None, False
    finally:
        db.close()
        cursor.close()
    return data, True

def showone(id:int):
    try:
        db, cursor = connect()
        # 选择题库所有的题
        sql = "select * from question where id = %d"
        cursor.execute(sql, (id))
        data = cursor.fetchall()
    except Exception:
        db.rollback()
        return None, False
    finally:
        db.close()
        cursor.close()
    return data, True
showall()