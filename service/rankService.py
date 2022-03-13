from dao import rankDao
from model.responseCode import responseCode


# 根据id返回题目信息
def showRank(user_id: str):
    data = rankDao.showRank()
    data = list(data)

    user_total = len(data)  # 用户总数
    user_exist = 0  # 判断数据库中是否有该用户
    user_rank = 0  # 用户排名

    for i in range(1, user_total):  # 冒泡排序
        for j in range(0, user_total - i):
            if data[j][1] < data[j + 1][1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    for i in range(user_total):  # 查找
        if data[i][0] == user_id:
            user_exist = 1
            user_rank = i + 1
            break

    if user_total > 20:  # 前20名
        data = data[:20]

    rank_list = []
    for i in range(len(data)):
        rank_list.append([data[i][2], data[i][1], i + 1])

    if user_exist:
        result = {
            "user_rank":user_rank,
            "rank_list":rank_list
        }
        return responseCode(200, result, "success")
    elif not user_exist and data!=None:
        return responseCode(400,None,"此用户不存在")
    else:
        return responseCode(500,None,"数据库操作错误")
