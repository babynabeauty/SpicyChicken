from model import news
import time
from dao import newsDao
from model.responseCode import responseCode
def genarate_news(file, picture, title, author, type, tag):
    timestamp = int(time.time())
    docxpath = "/var/www/html/news/documents/" + timestamp + ".docx"
    picturepath = "http://123.60.94.12/news/picture/" + timestamp + ".jpg"

    # 将两个文件写入本地服务器
    with open(docxpath, "w") as f:
        f.write(file)
    with open(picturepath, "w") as f:
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