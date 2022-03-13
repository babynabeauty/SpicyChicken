import os
from pydocx import PyDocX
import zipfile
import re
import time
# 服务器存放路径
htmlpath = "/var/www/html/news/"
def extract_jpg(filename):
    # 文件地址
    doc_path = htmlpath +  "documents/"+ filename + ".docx"
    # 图片存放地址
    os.makedirs(htmlpath + filename + "/" + "index/word/media")
    image_path = htmlpath + filename + "/index/"
    # 解析压缩包
    doc = zipfile.ZipFile(doc_path)     
    # 提取文档图片
    for info in doc.infolist():
        if (info.filename.endswith((".jpeg",".png",".gif"))):
            doc.extract(info,image_path)
    doc.close()


def convert_to_html(filename):
    # 建立新闻文件夹
    dirpath = htmlpath + filename + "/"
    os.mkdir(dirpath)
    # Doc转换成Html文件
    html = PyDocX.to_html(htmlpath +  "documents/"+ filename + ".docx")
    f = open(htmlpath + filename + "/index.html", 'w', encoding="utf-8")
    f.write(html)
    f.close()

def xml_convert(title, institution, time, filename):
    # 打开文件
    with open(htmlpath + filename + "/index.html", "r", encoding="utf-8") as f:
        html = f.readline()

    # 替换head
    head_str = re.findall("<head>.*?</head>", html)[0]
    head_str_new = """
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="initial-scale=1.0, user-scalable=0, minimum-scale=1.0, maximum-scale=1.0">
        <title>{title}</title>
        <link href="https://s2.pstatp.com/inapp/TTDefaultCSS.css" rel="stylesheet" type="text/css">
        </head>
    """.format(title = title)
    html = html.replace(head_str, head_str_new)

    # 替换body前半部分
    body_str = "<body>"
    body_str_new = """
        <body style="max-width: 100%; margin: 0px auto; background-color: rgb(255, 255, 255);">
        <header tt-ignored-node="1">
        <h1>{title}</h1>
        <div class="subtitle">
        <span id="source">{institution}</span>
        <time>{time}</time>
        </div>
        </header>
        <article tt-ignored-node="1">
    """.format(title = title, institution = institution, time = time)
    html = html.replace(body_str, body_str_new)

    # 替换body后半部分
    body_str = "</body>"
    body_str_new = """
        </article>
        </body>
    """
    html = html.replace(body_str, body_str_new)

    # 处理图片信息
    img_datalist = re.findall("<img (.*?)>", html)
    img_path = htmlpath + filename  + "/index/word/media/"
    img_name = os.listdir(img_path)
    img_name.sort()
    for i in range(len(img_datalist)):
        each_img_data = img_datalist[i]
        img_src = 'src={img_src} style="display: block;"'.format(img_src = "http://123.60.94.12/news/" + filename  + "/index/word/media/" + img_name[i])
        html = html.replace(each_img_data, img_src)
    
    # 重新写入文件
    with open(htmlpath + filename + "/index.html", "w", encoding="utf-8") as f:
        f.write(html)
        
def generate_news(title, institution, filename, time_now):
    try:
        # make docx to html
        convert_to_html(filename)
        # extract jpg from docx
        extract_jpg(filename)
        # make html better
        xml_convert(title, institution, time_now, filename)
    except:
        return None
    return "http://123.60.94.12/news/" + filename + '/index.html'