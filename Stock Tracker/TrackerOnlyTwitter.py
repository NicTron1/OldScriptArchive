from datetime import date
import datetime
from datetime import datetime, timedelta
import pandas as pd
import time
from pytrends.request import TrendReq
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
import requests
import random
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import yfinance as yf
from pandas_datareader import data as pdr
import os
import json
import pytz
from pyrfc3339 import generate, parse

data_agg = int(input("Please enter the data aggregation period: "))
raw_get_twit = input("Would you like twitter data included? (Yes or No): ")
if raw_get_twit == 'Yes' or 'yes':
    get_twit = True
elif raw_get_twit == 'No' or 'no':
    get_twit = False

dub_data_agg = data_agg*2

def auth():
    return 'AAAAAAAAAAAAAAAAAAAAAC2oGwEAAAAANe6sIQ%2Bpy%2F34oVdXB5DA8I4xcG4%3DvojzwDscZh0Wu7ds214h99nHBQqyDHxZMed7KKlyVrJrO3pxbe'


def create_url():
    
    results = 100

    d = datetime.utcnow() - timedelta(hours=data_agg)
    start = d.isoformat("T") + "Z"


    url = "https://api.twitter.com/2/tweets/search/recent?query={}&max_results={}&start_time={}".format(
        query, results, start
    )
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()



yf.pdr_override()




date = datetime.now()
yesterday = datetime.now() - timedelta(7)
current_year=date.year
current_month=date.month
current_day=date.day
yester_month=yesterday.month
yester_year=yesterday.year
yester_day=yesterday.day

proxies = ['https://192.101.217.112:6174', 'https://192.101.216.246:6116','https://192.101.216.218:5633', 'https://192.101.222.111:5856', 'https://192.101.222.70:6310', 'https://192.101.217.117:6062', 'https://192.101.221.108:5136', 'https://192.101.217.4:5432', 'https://192.101.222.198:6430', 'https://192.101.219.206:5594']

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value]

user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
user_agents = user_agent_rotator.get_user_agents()
user_agent = user_agent_rotator.get_random_user_agent()

headers = { 'User-Agent': user_agent }

nas_list = pd.read_excel('./NL.xlsx')
#/home/computerfanatic21/script/NL.xlsx

pytrend = TrendReq(hl='en-US', proxies=proxies, tz=300, requests_args={'headers':headers})


strt = 0
trends_data_set = [['Test', 0]]
gains_list = ["!"]
data_set = [['Test', 0, 0]]
count=0
amount= 3641 
down = 0

while count < amount:
    tik = nas_list.at[count, 'Symbol']
    tik1 = nas_list.at[count+1, 'Symbol'] 
    tik2 = nas_list.at[count+2, 'Symbol'] 
    tik3 = nas_list.at[count+3, 'Symbol']
    tik4 = nas_list.at[count+4, 'Symbol'] 
    ftik = [str(tik)+" stock", (tik1)+" stock", str(tik2)+" stock", str(tik3)+" stock", str(tik4)+" stock"]
    raw_tik = [tik, tik1, tik2, tik3, tik4]
    
    df=pytrend.get_historical_interest(ftik, year_start=yester_year, month_start=yester_month, day_start=yester_day, hour_start=0, year_end=current_year, month_end=current_month, day_end=current_day, hour_end=0, geo='US', cat='1163')
    
    if df.empty == False:
        old_df = df[::-1]
        new_df = old_df.iloc[0:dub_data_agg]
        ite = 0
        while ite < 5:
            raw_list=['!']
            yes_raw_list=['!']
            pos=0
            not_found = False
            rows = new_df.index
            while pos < len(rows) and pos < data_agg:
                cnt = new_df.iat[pos, ite]
                raw_list.append(cnt)
                if len(rows) > data_agg:
                    yes_cnt = new_df.iat[pos+data_agg, ite]
                    yes_raw_list.append(yes_cnt)
                else:
                    not_found = True
                
                pos+=1
            
            
            yes_raw_list.reverse()
            yes_raw_list.pop()
            raw_list.reverse()
            raw_list.pop()
            if len(yes_raw_list) > 0 and not_found == False:  
                yes = sum(yes_raw_list)/len(yes_raw_list)
            elif len(yes_raw_list) == 0 or not_found == True:
                yes = 0
            if len(raw_list) > 0 and not_found == False:
                avg = sum(raw_list)/len(raw_list)
            elif len(raw_list) == 0 or not_found == True:
                avg = 0
            
            change = avg-yes
            if yes != 0:
                dec = change/yes
                perc = round(dec*100,2)
            elif change == 0:
                perc = 0.0
            elif yes == 0 and change > 0:
                perc = round(change*100,2)
            
            yes_mens = nas_list.at[count+ite, 'Mentions Yesterday']

            trends_data_set.append([raw_tik[ite], perc, yes_mens])


            
            ite += 1

    time.sleep(.1)
    down += 5
    if down == 300:
        time.sleep(10)
        down = 0
    count += 5
    print(count)

trends_data_df_raw = pd.DataFrame(trends_data_set, columns = ['Ticker', 'Gain', 'Mentions'])

trends_data_df = trends_data_df_raw.sort_values(by='Gain', ascending=False)

twit_count = 0
twit_amount = 450
twit_data_set = [['Test', 0]]

while twit_count < twit_amount and get_twit == True:

    raw_query = trends_data_df.at[twit_count, 'Ticker']
    query = str(trends_data_df.at[twit_count, 'Ticker']) + " stock"
    

    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    
    twit_list = []
    twit_data = json_response
    
    if 'data' in twit_data:
        for i in twit_data['data']:
            twit_list.append(i)

        print(len(twit_list))

        twit_cnt = len(twit_list)
    else:
        twit_cnt = 0
    
    twit_data_set.append([raw_query, twit_cnt])

    twit_count += 1

calc_data_set = [['Test', 0]]

if get_twit == True:
    twit_data_df = pd.DataFrame(twit_data_set, columns = ['Ticker', 'Gain'])

    calc_count = 0
    calc_amount = 450

    while calc_count < calc_amount:
        calc_trends = trends_data_df.at[calc_count, 'Gain']
        calc_twit = twit_data_df.at[calc_count, 'Gain']
        calc_tik = twit_data_df.at[calc_count, 'Ticker']

        final_calc = calc_twit
        
        calc_data_set.append([calc_tik, final_calc])
        calc_count += 1

elif get_twit == False:
    calc_data_set = trends_data_set


calc_data_df = pd.DataFrame(calc_data_set, columns = ['Ticker', 'Gain'])
tik_count = 0
tik_amount = len(calc_data_df.index)
final_data_set = [['Test', 0, 0, 'Test']]

while tik_count < tik_amount:

    current_tik = calc_data_df.at[tik_count, 'Ticker']
    current_calc = calc_data_df.at[tik_count, 'Gain']
    data = pdr.get_data_yahoo(current_tik, period = "1d", prepost = True)


    if data.empty:
        print('Could not fetch data')
        market_perc='No Data'
    else:
        market_close = data.iat[0, 4]
        market_open = data.iat[0, 1]
        market_change = market_open-market_close
        market_dec = market_change/market_open
        market_perc = round(market_dec*100,2)

    finviz_link = 'https://www.finviz.com/quote.ashx?t='+current_tik
    final_data_set.append([current_tik, current_calc, market_perc, finviz_link])
    tik_count += 1


final_data_df = pd.DataFrame(final_data_set, columns = ['Ticker', 'Hype Gain', 'Percentage Gain', 'Link'])

final_data_df.to_excel('./Gains.xlsx', index=False)
#/home/computerfanatic21/script/Gains.xlsx


#Email Stuff

email_user = 'troncosopythonemail@gmail.com'
email_password = 'dinont01'
email_send = 'nicolasltroncoso@gmail.com'

subject = 'Hype'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = "Hi there, here are today's top stock hype gains"
msg.attach(MIMEText(body,'plain'))

filename='./Gains.xlsx'
#/home/computerfanatic21/script/Gains.xlsx
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()

print('Mail Sent')
