import json
import pymysql

# 连接数据库
def connect():
    with open("dao/config.json", "r") as f:
        config = json.load(f)['database']
        host = config['host']
        user = config['user']
        password = config['password']
        port = config['port']
    db = pymysql.connect(host = host, user = user, password = password, database = "garbage")
    # 使用 cursor() 方法创建一个游标对象 cursor
    return db, db.cursor()