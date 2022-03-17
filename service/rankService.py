from dao import rankDao
from model.responseCode import responseCode


# 根据id返回题目信息
def showRank(user_id: str, mode: int):
    data = rankDao.showRank()
    data = list(data)

    user_total = len(data)  # 用户总数
    user_score = 0  # 用户分数
    user_exist = 0  # 判断数据库中是否有该用户
    user_rank = 0  # 用户排名

    for i in range(user_total):  # 查找
        if data[i][0] == user_id:
            user_exist = 1
            user_rank = i + 1
            user_score = data[i][3]
            break


    if user_exist:
        if mode == 1:
            result = {
                "user_score": user_score
            }
        else:
            if user_total > 20:  # 前20名
                data = data[:20]

            rank_list = []
            for i in range(len(data)):
                rank_list.append({
                    "user_name": data[i][1],
                    "avatar": data[i][2],
                    "score": data[i][3],
                    "rank": i + 1
                })
            result = {
                "user_rank": user_rank,
                "user_score": user_score,
                "rank_list": rank_list
            }
        return responseCode(200, result, "success")
    elif not user_exist and data != None:
        return responseCode(400, None, "此用户不存在")
    else:
        return responseCode(500, None, "数据库操作错误")
