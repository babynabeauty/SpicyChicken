from dao.dbConnect import connect

# 存储用户id
def login(user_id):
    try:
        db, cursor = connect()
        # 选择题库所有的题
        sql = "select * from user where user_id = '%s'" % (user_id)
        cnt = cursor.execute(sql)
        db.commit()
        if(cnt == 0):
            # 新加入用户
            sql = "insert into user(user_id, score) values('%s', %d)" % (user_id, 0)
            cursor.execute(sql)
            db.commit()
    except Exception:
        db.rollback()
        return False
    finally:
        db.close()
        cursor.close()
    return True