import requests
import smtplib
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
MY_EMAIL = "sasi.pydev@gmail.com"
MY_PASSWORD = "ukie meud xcgr syvx"
STOCK_API="TWPBA6LB9YJL88BM"
NEWS_API="335e2ecfdd7248779c4aac554fc918a9"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"



stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API
}
response=requests.get(STOCK_ENDPOINT,params=stock_params)
data=response.json()["Time Series (Daily)"]
data_list=[val for (key,val) in data.items()]
yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday=data_list[1]
day_before_yesterday_closing_price=day_before_yesterday["4. close"]
print(day_before_yesterday_closing_price)


difference_price=float(yesterday_closing_price)-float(day_before_yesterday_closing_price)
up_down=None
if difference_price > 0:
    up_down="🔼"
else:
    up_down="🔽"
difference_percentage=(difference_price/float(yesterday_closing_price))*100
print(difference_percentage)

if abs(difference_percentage) > 2 :
    news_param={
        "apiKey":NEWS_API,
        "qInTitle":COMPANY_NAME,
        
    }
    news_response=requests.get(NEWS_ENDPOINT,params=news_param)
    articles=news_response.json()["articles"]
    top_three=articles[:3]
    

    formatted_articles = [
        f'{STOCK_NAME} : {up_down}{difference_percentage}%\nHeadline:{article["title"]}.\nBrief: {article["description"]}'
        for article in top_three]
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        for article in formatted_articles:
            subject = "Stock Update"
            body = article
    
    
            utf8_subject = f"Subject:{subject}".encode('utf-8')
            utf8_body = body.encode('utf-8')
    
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="mailbox.sasiraj@gmail.com",
                msg=utf8_subject + b'\n\n' + utf8_body
            )