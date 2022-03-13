'''对文字识别的操作'''

from dao import wordDao

def wordSearch(word):
    data, issuccess = wordDao.vagueSearch(word)
    if(issuccess):
        backup_list = []
        if data == ():
            return {"code": 404, "backup_list": backup_list}
        for i in range(len(data)):
            backup_list.append(data[i][1])
    return {"code": 200, "backup_list" : backup_list}

def getThingDetail(word):
    data, issuccess = wordDao.detailSearch(word)
    if (issuccess):
        rst = []
        if data==None:
            return {"code":404, "data":rst}
        print(data)
        temp = {
            "thing_name": data[1],
            "garbage_kind": data[2],
            "garbage_description": data[3],
        }
        rst.append(temp)
    print("rst",rst)
    return {"code": 200, "data": rst}
