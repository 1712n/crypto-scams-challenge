from bs4 import BeautifulSoup
import requests
import pandas as pd
import telebot
import sys
import os
import datetime
from time import sleep


class Crawl:
    def __init__(self, query, period_days) -> None:
        tok = '5783891518:AAEs5-r1-DeqVLVKpNxF-PIaHdYx59QswiE' 
        self.bot=telebot.TeleBot(tok)
        self.data = []
        self.delta = datetime.timedelta(period_days)
        self.query = query
        self.delta_int = period_days
        self.topic_id = query

    def get_results(self):
        
        
        i = 0
        bad_try = 0
        work = True

        beg_date = datetime.datetime.now()

        start_date = beg_date - self.delta


        while bad_try < 10 or work:

            if start_date == beg_date :
                work = False

            end_date = start_date + datetime.timedelta(1)
            end_str = end_date.strftime('%Y-%m-%d')
            start_str = start_date.strftime('%Y-%m-%d')

            url = f"https://news.google.com/rss/search?q={self.topic_id} before:{end_str} after:{start_str}&hl=en-US&gl=US&ceid=US:en"
            
            print(start_str, end_str, url)
            
            try:
                request_data = requests.get(url) 
                
                if request_data.status_code == 200 :

                    xml_data = request_data.content
                    soup = BeautifulSoup(xml_data, 'xml')
                    all_items = soup.find_all('item')
                    if len(all_items) > 1:
                        for item in all_items:
                            obj = {
                                'title': item.find('title').text,
                                'link': item.find('link').text,
                                'timestamp': item.find('pubDate').text,
                                'description': item.find('description').text
                            }

                            self.data.append(obj)

                        start_date = end_date
                    else:
                        bad_try += 1    
                else:
                    bad_try += 1
            except Exception as e:
                print(e)
                work = False
            
            if start_date == beg_date :
                work = False
        self.save()             
        
    def save(self):
        df = pd.DataFrame(self.data)
        df.head(10)
        df.drop_duplicates(subset='title', inplace=True)
        print(len(df))
        df.to_csv('data.csv')
        self.bot.send_message(chat_id='1671018400', text=f"Файл сохранен.")

    
    



if __name__ == '__main__':
    crawl = Crawl('!bitcoin', 180) # Bitcoin topic id
    try:
        crawl.get_results()
        
        
    except KeyboardInterrupt:
        print('Interrupted')
        crawl.bot.send_message(chat_id='1671018400', text=f"Прервано руками")
        crawl.save()
        
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
        