# Tyrus Malmstrom
# May 16th,2016
# Rasberry Pi Project

import sys
import smtplib #The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.
# Import the email modules we'll need
import time
from datetime import datetime
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def main():
    print "Hello World!"
