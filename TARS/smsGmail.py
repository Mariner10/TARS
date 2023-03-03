import smtplib


from constants import gmail_SENDING_appPass,gmail_user

CARRIERS = {
"att": "@mms.att.net",
"tmobile": "@tmomail.net",
"verizon": "@vtext.com",
"sprint": "@messaging.sprintpcs.com"
}

EMAIL = gmail_user
PASSWORD = gmail_SENDING_appPass

def send_message(phone_number, carrier, message):
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
    server.sendmail(auth[0], recipient, message)
