import pandas 
import datetime
import random
import smtplib

MY_EMAIL = "sasi.pydev@gmail.com"
MY_PASSWORD = "ukie meud xcgr syvx"

today_details=datetime.datetime.now()
this_month=today_details.month
day=today_details.day
today=(this_month,day)



data=pandas.read_csv("birthdays.csv")
birthdays_dict={(data_row["month"], data_row["day"]):data_row for (index, data_row) in data.iterrows()}



random_letter_number=random.randint(1,3)
if today in birthdays_dict:
    birthday_person=birthdays_dict[today]
    filepath=f"letter_templates\\letter_{random_letter_number}.txt"
    with open (filepath) as l:
        letter=l.read()
        letter=letter.replace("[NAME]",birthday_person["name"])


    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!!\n\n{letter}")