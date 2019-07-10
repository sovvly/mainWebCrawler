import requests
from bs4 import BeautifulSoup
import smtplib
import schedule
import time

sender = 'senderEmail@email.ee'
receiver = ['receiverEmail@email.ee']

msg = """From: senderEmail@email.ee
Subject: Text message\n
text continue
"""

def checkAvailability():
    page = requests.get('https://www.urltocheck.sth')

    pageSoup = BeautifulSoup(page.text, 'html.parser')

    element = pageSoup.find(emelentLocators)

    text = element.get("class")

    if conditions in text:
        server = smtplib.SMTP_SSL('mail.server.ee', port)
        server.login(sender, "password")
        server.sendmail(
            sender,
            receiver,
            msg)
        server.quit()


schedule.every(1).minutes.do(checkAvailability)

while True:
    schedule.run_pending()
    time.sleep(1)