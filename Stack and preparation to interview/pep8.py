import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import Autorisation_data as Auth


class EmailApp:
    def __init__(self, user_login, user_password):
        self.connect = {'login': user_login, 'password': user_password}

    def sendmail(self, server_name, port_name, recipients_names, theme_message, text_message):
        try:
            email_message = MIMEMultipart()
            email_message['From'] = self.connect['login']
            email_message['To'] = ', '.join(recipients_names)
            email_message['Subject'] = theme_message
            email_message.attach(MIMEText(text_message))
            sendmail_instance = smtplib.SMTP(server_name, port_name)
            sendmail_instance.ehlo()
            sendmail_instance.starttls()
            sendmail_instance.ehlo()
            sendmail_instance.login(self.connect['login'], self.connect['password'])
            result = sendmail_instance.sendmail(email_message['From'], email_message['To'], email_message.as_string())
            sendmail_instance.quit()
            return result
        except Exception as Error:
            return f'Failed to send email: {Error}'

    def receive_mail(self, server_name, mailbox_name, header=None):
        receive_mail_instance = imaplib.IMAP4_SSL(server_name)
        try:
            receive_mail_instance.login(self.connect['login'], self.connect['password'])
            receive_mail_instance.list()
            receive_mail_instance.select(mailbox_name)
            criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
            result, data = receive_mail_instance.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'
            latest_email_uid = data[0].split()[-1]
            print(latest_email_uid.decode('utf-8'))
            result, data = receive_mail_instance.uid('fetch', latest_email_uid.decode('utf-8'), '(RFC822)')
            raw_email = data[0][1]
            email_result_receive = email.message_from_string(raw_email.decode('utf-8'))
            receive_mail_instance.logout()
            return email_result_receive
        except Exception as Error:
            return f'Failed to receive email:{Error}'


if __name__ == '__main__':
    gmail = EmailApp(Auth.email, Auth.password)
    print(gmail.sendmail(Auth.gmail_smtp, 587, Auth.recipients, Auth.subject, Auth.message))
    print(gmail.receive_mail(Auth.gmail_imap, 'inbox'))