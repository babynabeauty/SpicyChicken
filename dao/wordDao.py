import string

from dao.dbConnect import connect

def vagueSearch(name:string):
    try:
        db, cursor = connect()
        sql="select * from kind where name like '%{name}%'".format(name=name)
        cursor.execute(sql)
        data = cursor.fetchall()
    except Exception:
        db.rollback()
        return None, False
    finally:
        db.close()
        cursor.close()
    return data, True

def detailSearch(name:string):
    try:
        db, cursor = connect()
        sql="select * from kind where name like '{name}'".format(name=name)
        print(sql)
        cursor.execute(sql)
        data = cursor.fetchone()
    except Exception:
        db.rollback()
        return None, False
    finally:
        db.close()
        cursor.close()
    return data, True