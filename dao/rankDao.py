from dao.dbConnect import connect

# 根据用户id返回用户排名
def showRank():
    try:
        db, cursor = connect()
        sql = "select * from user ORDER BY score DESC"
        cnt = cursor.execute(sql)
        db.commit()
        if(cnt == 0):
            return None
        else:
            data = cursor.fetchall()
    except Exception:
        db.rollback()
        return None
    finally:
        db.close()
        cursor.close()
    return data

# 根据用户id返回用户排名（Android端）
def showRank2():
    try:
        db, cursor = connect()
        sql = "select * from user2 ORDER BY score DESC"
        cnt = cursor.execute(sql)
        db.commit()
        if(cnt == 0):
            return None
        else:
            data = cursor.fetchall()
    except Exception:
        db.rollback()
        return None
    finally:
        db.close()
        cursor.close()
    return data
