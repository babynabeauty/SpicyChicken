from dao import wordDao

def wordSearch(word):
    data, issuccess = wordDao.vagueSearch(word)
    if(issuccess):
        backup_list = []
        if data == ():
            return {"code": 404, "backup_list": backup_list}
        for i in range(len(data)):
            temp={
                "thing_name":data[i][1],
                "kind":data[i][2]
            }
            backup_list.append(temp)
    return {"code": 200, "backup_list" : backup_list}

def getThingDetail(word):
    data, issuccess = wordDao.detailSearch(word)
    if (issuccess):
        if data==None:
            return {"code":404, "data":{}}
        rst = {
            "thing_name": data[1],
            "garbage_kind": data[2],
            "garbage_description": data[3],
        }
    print("rst",rst)
    return {"code": 200, "data": rst}
