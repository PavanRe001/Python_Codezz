
import smtplib
import datetime as dt
import random,pandas
#------smtp-------
my_email="example@gmail.com" #  <--------- Use Sender's Gmail
password="whbxkazjdgdputxx"  #  <--------- To get the password(16) refer to Readme.md for complete process
#------datetime---
now=dt.datetime.now()
today_month=now.month
today_day=now.day
today=(today_month, today_day)

birthdays=pandas.read_csv('birthdays.csv')
PLACEHOLDER = "[NAME]"

birthday_dict={(data_row['month'],data_row['day']):data_row for (index,data_row) in birthdays.iterrows()}
if today in birthday_dict: 
    birthday_person=birthday_dict[today]
    ran = random.randint(1, 3)
    with open(f'letter_templates/letter_{ran}.txt') as starting_letter:
        letter=starting_letter.read()
        new_letters=letter.replace(PLACEHOLDER, birthday_person['name'])

    with smtplib.SMTP('smtp.gmail.com',587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person['email'],
                            msg=f'Happy Birthday to you!: \n\n{new_letters}')


