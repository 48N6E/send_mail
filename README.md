# send_mail
按照模板发送邮件



1). python一键生成依赖包：（requirements.txt用来记录项目所有的依赖包和版本号）
    > pip freeze >requirements.txt
2).python一键安装依赖包：（一次性安装requirements.txt里面所有的依赖包）
  pip install -r requirements.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple


  python pip安装smtplib库的方法
  要安装smtplib 首先可以执行一下这个命令：pip search smtplib
  一般用PyEmail,所以直接pip install PyEmail 就行 ，然后再import smtplib就不会有问题了