# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
import os
# email 用于构建邮件内容
from email.header import Header
import lxml

import lxml.etree


# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
with open(os.path.abspath(os.path.pardir) + '\\send_mail\\file\\%s'% '申请jumpserver服务器','r',encoding='utf-8') as newfile:
    content = newfile.read()
    print(content)
    msg = MIMEText(content, 'html', 'utf-8')


def showEmailType():
    filenames = []
    for filename in os.listdir(r'%s\\file'% os.path.abspath(os.path.curdir)):
        if filename !=  '__init__.py':
            yield (filename)

def readEmailTypChose(typename):
    typesfield = {}
    with open(os.path.abspath(os.path.pardir) + '\\send_mail\\file\\%s'% typename,'r',encoding='utf-8') as newfile:
        html = lxml.etree.HTML(newfile.read())
        types = html.xpath('//tr[1]/td')
        for i in types:
            typesfield[i.text.strip()] =  ''
            ## typesfield.append(i.text.strip())
    return typesfield

def fullcontext(typename,**kwargs):
    field = readEmailTypChose(typename)
    for key  in kwargs:
        print(key)
        field[key] = kwargs[key]
    print(field)

def sendMail(content,from_addr= 'xxx@qq.com',to_addr= 'denis.mao@xxx.com',title='python test',smtp_server='smtp.qq.com'):
    # 用于构建邮件头
    print(from_addr)
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header(title)
    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = '2278562@qq.com'
    password = 'gjkiwcwsunkecbdg'
    # 发信服务器
    #smtp_server =
    # 收信方邮箱
    to_addr = 'denis.mao@yunlsp.com'
    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL()
    server.connect(smtp_server, 465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, content.as_string())
    # 关闭服务器
    server.quit()


if __name__ == '__main__':
    # 邮件头信息

    for i in showEmailType():
        print(i)
    #sendMail(content = msg)
    readEmailTypChose('申请jumpserver服务器')
    fullcontext('申请jumpserver服务器',服务器 = 'xxx',原因 =  '嘻嘻嘻', 权限='xxx', 申请人员=' ')