from dao.dbConnect import connect

# 根据用户id返回用户排名
def showRank():
    try:
        db, cursor = connect()
        # 选择题库所有的题
        sql = "select * from user"
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
