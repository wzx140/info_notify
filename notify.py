import smtplib
import log
from email.mime.text import MIMEText
from email.utils import formataddr
import time
from os import path
 
my_sender = 'xxx'    # 发件人邮箱账号
my_pass = 'xxx'              # 发件人邮箱密码
my_user = 'xxx'      # 收件人邮箱账号，我这边发送给自己
 
def send(sub,meg):
    if meg:
        try:
           msg = MIMEText(meg,'html','UTF-8')
           msg['From'] = formataddr(["南航更新了",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
           msg['To'] = formataddr(["wzx",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
           msg['Subject'] = sub                # 邮件的主题，也可以说是标题
           server = smtplib.SMTP_SSL("smtp.qq.com",465)  # 发件人邮箱中的SMTP服务器，端口是25
           server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
           server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
           server.quit()  # 关闭连接
           log.log_info('notify:发送"'+sub+'"')
        except:
            log.log_exception('notify:发送邮件出现问题')
    else:
        log.log_error('notify:更新内容为空')

# if __name__ == '__main__':
#     send('请9.25日来面试')

