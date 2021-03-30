import smtplib
from smtplib import *

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("spotr.iiita@gmail.com","spotr1234")
server.sendmail("spotr.iiita@gmail.com","piyushgurjar4064@gmail.com","Testing success :)")
server.quit()
