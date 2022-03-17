from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import getinfobcks
from info_intro_html import info_intro_html
import getenv

def send_mail(routes, mail, subject):
    
    data_info_bck = []
    env = getenv.Getenv()

    for route in routes: 
        data_info_bck += getinfobcks.info_backup(route)

    html_template= info_intro_html(data_info_bck)
    html = MIMEText(html_template, 'html')

    server = smtplib.SMTP(host='smtp.office365.com', port=587)
    server.starttls()
    server.login(env.env('USER'), env.env('PASS'))

    message = MIMEMultipart('Backups')
    message['From'] = env.env('USER')
    message['To'] = ','.join(mail)
    message['Subject'] = subject
    message.attach(html)

    server.sendmail(message['From'], mail, message.as_string())
    server.quit()
