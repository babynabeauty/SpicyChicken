from dao import questionDao

def showall():
    data, issuccess = questionDao.showall()
    if(issuccess):
        result = []
        for i in range(len(data)):
            temp = {
                "id" : data[i][0],
                "type" : data[i][1],
                "description" : data[i][2],
                "option" : data[i][3].split(";"),
                "answer" : data[i][4],
                "explanation" : data[i][5]
            }
            result.append(temp)
    return {"code": 200, "data" : result}

def showone():
    data, issuccess = questionDao.showall()
    if(issuccess):
        result = {
            "id" : data[0][0],
            "type" : data[0][1],
            "description" : data[0][2],
            "option" : data[0][3].split(";"),
            "answer" : data[0][4],
            "explanation" : data[0][5]
        }
    return {"code": 200, "data" : result}

