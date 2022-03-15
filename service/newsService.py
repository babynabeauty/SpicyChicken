from model import news
import time
from dao import newsDao
from model.responseCode import responseCode
# 生成新闻
def generate_news(file, picture, title, author, type, tag):
    timestamp = str(int(time.time()))
    docxpath = "/var/www/html/news/documents/" + timestamp + ".docx"
    picturepath = "http://123.60.94.12/news/picture/" + timestamp + ".jpg"

    # 将两个文件写入本地服务器
    with open(docxpath, "wb") as f:
        f.write(file)
    with open("/var/www/html/news/picture/"+ timestamp + ".jpg", "wb") as f:
        f.write(picture)
    
    # get time
    now = int(round(time.time()*1000))
    time_now = time.strftime('%Y-%m-%d %H:%M',time.localtime(now/1000))
    url = news.generate_news(title, author, str(timestamp), time_now)
    if(url):
        # 保存数据库
        issuccess = newsDao.saveNews(title, author, time_now, url, picturepath, type, tag)
        if(not issuccess):
            return responseCode(400, None, "数据库操作错误")
        #返回链接
        return responseCode(200,url,"success")
    return responseCode(400, None, "数据读写错误，请检查后重试")


# 根据返回列表
def getnewsList(offset:int):
    data, issuccess = newsDao.getnewsList(offset)
    if(issuccess):
        result = []
        for i in range(len(data)):
            temp = {
                "news_id" : int(data[i][4].split("/")[-2]),
                "title" : data[i][1],
                "author" : data[i][2],
                "time" : data[i][3],
                "url" : data[i][4],
                "picture" : data[i][5],
                "type" : data[i][6],
                "tag":data[i][7]
            }
            result.append(temp)
        return responseCode(200, result, "success")
    elif (data == None):
        return responseCode(400, None, "没有更多了")
    else:
        return responseCode(400, None, "数据库操作错误")