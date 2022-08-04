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


# 软件端存储用户id（Android端）
def login2(user_name,user_psw,avatar):
    try:
        db, cursor = connect()
        sql = "select * from user2 where user_name = '%s'" % (user_name)
        print(sql)
        cnt = cursor.execute(sql)
        print(cnt)
        db.commit()
        if(cnt == 0):
            # sql = "insert into user2(user_id, user_name, avatar, score,user_psw) values('%d','%s','%s', %d,%s)" % (3, user_name, avatar, 0, user_psw)
            sql = "insert into user2(user_name, avatar, score,user_psw) values('%s','%s', %d,%s)" % (user_name, avatar, 0, user_psw)
            print(sql)
            cursor.execute(sql)
            print("success")
            db.commit()
            # 1注册成功
            data = 0
            fl = 1
            print(fl)
        # 不是新加入的用户检测对不对数据库
        else:
            # 更新用户数据
            sql = "select * from user2 where user_name = '%s'" % (user_name)
            # sql = "select * from user2"
            print(sql)
            cursor.execute(sql)
            db.commit()
            data = cursor.fetchone()
            print(data)
            # 不是新加入的用户
            fl = 2
    except Exception:
        db.rollback()
        return False
    finally:
        db.close()
        cursor.close()
    if fl == 1:
        return fl,data
    else:
        return fl,data


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