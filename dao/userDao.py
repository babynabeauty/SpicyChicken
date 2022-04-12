from dao.dbConnect import connect

# 存储用户id
def login(user_id, user_name, avatar):
    try:
        db, cursor = connect()
        sql = "select * from user where user_id = '%s'" % (user_id)
        cnt = cursor.execute(sql)
        db.commit()
        if(cnt == 0):
            # 新加入用户
            sql = "insert into user(user_id, user_name, avatar, score) values('%s','%s','%s', %d)" % (user_id, user_name, avatar, 0)
            cursor.execute(sql)
            db.commit()
        else:
            # 更新用户数据
            sql = "update user set user_name = '%s', avatar = '%s' where user_id = '%s'" % (user_name, avatar, user_id)
            cursor.execute(sql)
            db.commit()
    except Exception:
        db.rollback()
        return False
    finally:
        db.close()
        cursor.close()
    return True

# 每日一题回答正确加分
def add_score(user_id:str):
    try:
        db, cursor = connect()
        sql = "update user set score = score + 10 where user_id = '%s'" % (user_id)
        cursor.execute(sql)
        db.commit()
    except Exception:
        db.rollback()
        return False
    finally:
        db.close()
        cursor.close()
    return True