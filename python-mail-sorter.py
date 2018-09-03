import sys
import imaplib
import getpass
import email
import email.header
import datetime
import re
import base64

EMAIL = "mail@gmail.com"
PASSWD = "password"
MAIL_SERVER = "imap.gmail.com"
MAIL_PORT = 993

def readmail():
    mail = imaplib.IMAP4_SSL(MAIL_SERVER)
    mail.login(EMAIL,PASSWD)
    mail.select('inbox')

    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]

    id_list = mail_ids.split()
    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])

    for i in range(latest_email_id,first_email_id, -1):
            type, data = mail.fetch(i, '(RFC822)' )
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    email_date = msg['date']
                    email_message = msg.get_payload()
                    email_message = ''.join(map(str, email_message))
                    print 'From : ' + email_from + '\n'
                    print 'Subject : ' + email_subject + '\n'
                    print 'Message : ', email_message
                    print 'Date : ' + email_date + '\n'
                    tem_devops(email_message, email_date, email_from, email_subject) # okkkkk
                    tem_devops(email_subject, email_date, email_from, email_subject) # ta ok


def tem_devops(sub_message, email_date, email_from, email_subject ):
    match = re.search(r'.*devops.*', sub_message , re.IGNORECASE)
    if match:
        done = 'yes'
        import MySQLdb
        db = MySQLdb.connect(host="DATABASE IP", user="python", passwd="pythonpass",db="email")
        cur2 = db.cursor()
        cur2.execute("INSERT INTO devops (datamail, origem, assunto) VALUES (%s, %s, %s);", (email_date, email_from, email_subject))
        
    else:
        done = 'no'
       

    return done


readmail()
