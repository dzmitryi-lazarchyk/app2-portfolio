import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "portfolio.app1994@gmail.com"
password = "lcnggayhjbztgzfd"
receiver = "dzmitryi.lazarchyk1994@gmail.com"

context = ssl.create_default_context()

message = f"""\
Subject: Portfolio App
{username} sent you an email!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

