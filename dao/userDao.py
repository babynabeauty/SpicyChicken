from dao.dbConnect import connect

# 存储用户id
def login(user_id, user_name, avatar):
    try:
        db, cursor = connect()
        # 选择题库所有的题
        sql = "select * from user where user_id = '%s'" % (user_id)
        cnt = cursor.execute(sql)
        db.commit()
        if(cnt == 0):
            # 新加入用户
            sql = "insert into user(user_id, user_name, avatar, score) values('%s','%s','%s', %d)" % (user_id, user_name, avatar, 0)
            cursor.execute(sql)
            db.commit()
    except Exception:
        db.rollback()
        return False
    finally:
        db.close()
        cursor.close()
    return True