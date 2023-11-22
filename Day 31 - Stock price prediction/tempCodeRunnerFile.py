data=response.json()["Time Series (Daily)"]
# data_list=[val for (key,val) in data.items()]
# yesterday_data=data_list[0]
# yesterday_closing_price=yesterday_data["4. close"]
# print(yesterday_closing_price)

# day_before_yesterday=data_list[1]
# day_before_yesterday_closing_price=day_before_yesterday["4. close"]
# print(day_before_yesterday_closing_price)


# difference_price=abs(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))
# print(difference_price)

# difference_percentage=(difference_price/float(yesterday_closing_price))*100
# print(difference_percentage)

# if difference_percentage > 1 :
#     news_param={
#         "apiKey":NEWS_API,
#         "qInTitle":COMPANY_NAME,
        
#     }
#     news_response=requests.get(NEWS_ENDPOINT,params=news_param)
#     articles=news_response.json()["articles"]
#     print(articles)
# #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


#     ## STEP 3: Use twilio.com/docs/sms/quickstart/python
#     #to send a separate message with each article's title and description to your phone number. 

# #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# #TODO 9. - Send each article as a separate message via Twilio. 



# #Optional TODO: Format the message like this: 
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """

