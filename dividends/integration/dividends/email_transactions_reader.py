'''
Created on 17 May 2022

@author: mpayen
'''
import imaplib
import os
import json
import email
import traceback
from django.core.exceptions import ImproperlyConfigured
import MyInvest.settings as settings

class Email_New_Transactions_Reader(object):
    '''
    This class will be used to read an email summarizing all the transactions that occurred the day N-1 on Trading 212 (Basically the morning before the stock market opens)
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def read_email_from_gmail(self):
        print("Read email")
        try:
            mail = imaplib.IMAP4_SSL(settings.EMAILS.get('SMTP_SERVER'))
            mail.login(settings.EMAILS.get('FROM_EMAIL'),settings.EMAILS.get('FROM_PWD'))
            mail.select('inbox')
            
            print(settings.EMAILS.get('FROM_EMAIL'))
            print(settings.EMAILS.get('FROM_PWD'))
            
            new_transactions = []
            data = mail.search(None, 'ALL')
            mail_ids = data[1]
            id_list = mail_ids[0].split()   
            first_email_id = int(id_list[0])
            latest_email_id = int(id_list[-1])
            
            print(data)
    
            for i in range(latest_email_id,first_email_id, -1):
                data = mail.fetch(str(i), '(RFC822)' )
                for response_part in data:
                    arr = response_part[0]
                    if isinstance(arr, tuple):
                        msg = email.message_from_string(str(arr[1],'utf-8'))
                        email_subject = msg['subject']
                        email_from = msg['from']
                        print('From : ' + email_from + '\n')
                        print('Subject : ' + email_subject + '\n')
    
        except Exception as e:
            traceback.print_exc() 
            print(str(e))
    
    with open(os.path.join(settings.BASE_DIR, 'parameters.json')) as parameters_file:
        parameters = json.load(parameters_file)

    def get_email_subject(self, setting, parameters=parameters):
        """Get secret setting or fail with ImproperlyConfigured"""
        try:
            return parameters[setting]
        except KeyError:
            raise ImproperlyConfigured("Set the {} setting".format(setting))    
    