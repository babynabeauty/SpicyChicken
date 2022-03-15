from dao import questionDao, userDao
from model.responseCode import responseCode
import time
import datetime
import calendar

# 根据id返回题目信息
def showone(id:int):
    data, issuccess = questionDao.showone(id)
    if(issuccess):
        result = {
            "id" : data[0][0],
            "type" : data[0][1],
            "description" : data[0][2],
            "option" : data[0][3].split(";"),
        }
        return responseCode(200, result, "success")
    elif (data == None):
        return responseCode(400, None, "此题目不存在")
    else:
        return responseCode(400, None, "数据库操作错误")

# 根据用户提交的答案进行判断并返回信息
def submitAnswer(user_id: str, question_id: int, selected: str):
    data, issuccess = questionDao.showone(question_id)
    if(issuccess):
        right_anwer = data[0][4]
        explanation = data[0][5]
        issuccess = questionDao.saveSubmit(user_id, question_id, selected)
        if(not issuccess):
            return responseCode(400, None, "请勿重复提交")
        # 判断选择是否正确
        if(right_anwer == selected):
            judge_correct = True
            issuccess = userDao.add_score(user_id)
        else:
            judge_correct = False
        # 返回数据
        result = {
            "question_id":question_id,
            "juege_correct": judge_correct,
            "answer": right_anwer,
            "explanation": explanation
        }
        return responseCode(200,result, "success")
    else:
        return responseCode(400, None, "数据库操作错误")
    
# 判断用户今日是否完成每日一题
def ifTodayProblem(user_id: str):
    question_id = int(time.strftime("%Y%m%d", time.localtime()))
    data, issuccess = questionDao.checkRecord(user_id, question_id)
    if(issuccess):
        result = {
            "judge_finish": data
        }
        return responseCode(200, result, "success")
    else:
        return responseCode(400, None, "数据库操作错误")

# 根据月份查询用户做题情况，并返回列表
def history(user_id:str, year:int, month:int): 
    month_start = int(str(datetime.datetime(year, month, 1).date()).replace("-",""))
    month_end = int(str(datetime.datetime(year, month, calendar.monthrange(year, month)[1]).date()).replace("-",""))
    data, issuccess = questionDao.getHistory(user_id, month_start, month_end)
    if(issuccess):
        month_len = month_end - month_start + 1
        print("month_len", month_len)
        check = [0 for i in range(month_len)]
        for each_record in data:
            check[each_record[2] - month_start] = 1
        result = {}
        for i in range(len(check)):
            if(check[i]):
                result[month_start + i] = True
            else:
                result[month_start + i] = False
    else:
        return responseCode(400, None, "数据库操作错误")
    return responseCode(200, result, "success")

# 根据情况返回做过题的详细情况
def showHistoryOne(user_id: str, question_id: int):
    now = int(time.strftime("%Y%m%d", time.localtime()))
    if(question_id > now):
        return responseCode(400,None,"无权限访问")
    data, issuccess1 = questionDao.getRecord(user_id, question_id)
    qdata, issuccess2 = questionDao.showone(question_id)
    if(issuccess2 and qdata):
        question_info = {
            "id" : qdata[0][0],
            "type" : qdata[0][1],
            "description" : qdata[0][2],
            "option" : qdata[0][3].split(";"),
            "answer" : qdata[0][4],
            "explanation":qdata[0][5]
        }
    else:
        return responseCode(400, None, "数据库操作错误")
    if(issuccess1 and issuccess2):
        if(data == None):
            # 没有做题记录
            result = {
                "record":{"status": False, "selected":None},
                "question_info":question_info
            }
            
        else:
            # 有做题记录
            result = {
                "record":{"status": True, "selected":data[3]},
                "question_info":question_info
            }
    else:
        return responseCode(400, None, "数据库操作错误")
    return responseCode(200, result, "success")