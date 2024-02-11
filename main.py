import datetime as dt
import pandas as pd
from random import choice
import smtplib

class Mailer:
        def __init__(self):
                self.your_mail = 'your mail'
                self.password = 'your pass'
                self.templates = ['template1.txt', 'template2.txt', 'template3.txt']
                self.data = pd.read_csv('birthdays.csv', index_col=False)
                self.now = dt.datetime.now()
                self.todays_birthdays = self.data[(self.data['month'] == self.now.month) & (self.data['day'] == self.now.day)]
                
                
        def send_mail(self):
                if not self.todays_birthdays.empty:

                        today_name = self.todays_birthdays['name'].values[0]
                        address = self.todays_birthdays['email'].values[0]
                        r_choice = choice(self.templates)


                        with open(f'./templates/{r_choice}', 'r') as f:
                                txt_tmp = f.readlines()

                        for i in range(len(txt_tmp)):
                                if '[Name]' in txt_tmp[i]:
                                        txt_tmp[i] = today_name
                                elif '[Your Name]' in txt_tmp[i]:
                                        txt_tmp[i] = 'Kostas'
                        msg = ''.join(txt_tmp)



                        with smtplib.SMTP('smtp.gmail.com') as connection:
                                connection.starttls()
                                connection.login(user=self.your_mail, password=self.password)
                                connection.sendmail(
                                        from_addr=self.your_mail, 
                                        to_addrs=address, 
                                        msg=f'Subject:Happy Birthday!\n\n{msg}'
                                )
                else:
                        print('No birthdays today!')


mail = Mailer()
mail.send_mail()                     