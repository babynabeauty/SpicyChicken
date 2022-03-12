from dao.dbConnect import connect

# 根据题目id返回题目信息
def showone(id:int):
    try:
        db, cursor = connect()
        # 选择题库所有的题
        sql = "select * from question where id = %d" % (id)
        cnt = cursor.execute(sql)
        db.commit()
        if(cnt == 0):
            return None, False
        else:
            data = cursor.fetchall()
    except Exception:
        db.rollback()
        return None, False
    finally:
        db.close()
        cursor.close()
    return data, True

# 存储用户做题记录
def saveSubmit(user_id, question_id, selected):
    try:
        db, cursor = connect()
        # 先判断记录是否正确
        sql = "select * from record where user_id = '%s' and question_id = %d"%(user_id, question_id)
        cnt = cursor.execute(sql)
        db.commit()
        print("cnt", cnt)
        if(cnt != 0):
            return False
        # 插入做题记录
        sql = "insert into record(user_id, question_id, selected) values('%s', '%d', '%s')"%(user_id, question_id, selected)
        cursor.execute(sql)
        db.commit()
    except Exception:
        db.rollback()
        return False
    finally:
        db.close()
        cursor.close()
    return True

# 查询用户某一天是否做题记录
def checkRecord(user_id, question_id):
    try:
        db, cursor = connect()
        sql = "select * from record where user_id = '%s' and question_id = %d" % (user_id, question_id)
        cnt = cursor.execute(sql)
        db.commit()
        data = True
        if(cnt == 0):
            data = False
    except Exception:
        db.rollback()
        return None, False
    finally:
        db.close()
        cursor.close()
    return data, True

# 根据月份返回该用户的做题记录
def getHistory(user_id, month_start, month_end):
    try:
        db, cursor = connect()
        # 选择题库所有的题
        sql = "select * from record where user_id = '%s' and question_id >= %d and question_id <= %d" % (user_id, month_start, month_end)
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

# 查询用户某一题记录
def getRecord(user_id, question_id):
    try:
        db, cursor = connect()
        sql = "select * from record where user_id = '%s' and question_id = %d" % (user_id, question_id)
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except Exception:
        db.rollback()
        return None, False
    finally:
        db.close()
        cursor.close()
    return data, True