import os
from pydocx import PyDocX
import zipfile
import re
from const import *
# 服务器存放路径
htmlpath = news_save_path

def extract_jpg(filename):
    # 文件地址
    doc_path = os.path.join(htmlpath, "documents", filename + ".docx")
    # 图片存放地址
    os.makedirs(os.path.join(htmlpath, filename, "index", "word", "media"))
    image_path = os.path.join(htmlpath, filename, "index")
    # 解析压缩包
    doc = zipfile.ZipFile(doc_path)     
    # 提取文档图片
    for info in doc.infolist():
        if (info.filename.endswith((".jpeg",".png",".gif"))):
            doc.extract(info,image_path)
    doc.close()


def convert_to_html(filename):
    # 建立新闻文件夹
    dirpath = os.path.join(htmlpath, filename)
    os.mkdir(dirpath)
    # Doc转换成Html文件
    html = PyDocX.to_html(os.path.join(htmlpath, "documents", filename + ".docx"))
    path = os.path.join(htmlpath, filename, "index.html")
    f = open(path, 'w', encoding="utf-8")
    f.write(html)
    f.close()

def xml_convert(title, institution, time, filename):
    # 打开文件
    path = os.path.join(htmlpath, filename, "index.html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.readline()

    # 替换head
    head_str = re.findall("<head>.*?</head>", html)[0]
    head_str_new = """
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="initial-scale=1.0, user-scalable=0, minimum-scale=1.0, maximum-scale=1.0">
        <link href="https://s2.pstatp.com/inapp/TTDefaultCSS.css" rel="stylesheet" type="text/css">
        <title>{title}</title>
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
        <author>{institution}</author>
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
    img_path = os.path.join(htmlpath, filename, "index", "word", "media")
    img_name = os.listdir(img_path)
    img_name.sort()
    for i in range(len(img_datalist)):
        each_img_data = img_datalist[i]
        img_src = 'src={img_src} style="display: block;"'.format(img_src = "http://" + host + "/news/" + filename  + "/index/word/media/" + img_name[i])
        html = html.replace(each_img_data, img_src)

    # 添加css style
    html = add_style(html)

    # 重新写入文件
    path = os.path.join(htmlpath, filename, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

def add_style(html:str):
    # body
    html = html.replace("<body", "<body style = \"font-family: helvetica;font-size: 18px;overflow-x: hidden;-webkit-text-size-adjust: none;margin: 0;padding: 0\"")
    # h1
    html = html.replace("<h1", "<h1 style = \"display: block;font-size: 22px;font-weight: bolder;padding-bottom: 15px;line-height: 1.3;margin: 0;color: #000\"")
    # subtitle
    html = html.replace("<subtitle", "<subtitle style = \"position: relative;font-size: 11px;line-height: 1;color: #505050\"")
    # time
    html = html.replace("<time", "<time style = \"display: inline-block; margin-left:8px; font-size: 13px;color: inherit;height: auto;line-height: 1\"")
    # article
    html = html.replace("<article", "<article style = \"overflow: hidden;font-size: 17px;word-wrap: break-word;text-align: justify;margin: 0 15px 10px;color: #505050;line-height: 1.647\"")
    # img
    html = html.replace("<img", "<img style = \"display: block;max-width: 100%;background: #efefef;border-radius: 0;margin: 8px auto\"")
    # p
    html = html.replace("<p", "<img style = \"word-wrap: break-word;text-align: justify;margin: 0 0 20px;color: #505050;line-height: 1.647;padding: 0\"")
    # header
    html = html.replace("<header", "<header style = \"padding-left: 6px;display: block;margin: 24px 15px;padding: 0\"")
    # author
    html = html.replace("<author", "<author style = \"display: inline-block;font-size: 13px;color: inherit;height: auto;line-height: 1\"")
    return html

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
    return "http://" + host + "/news/" + filename + '/index.html'