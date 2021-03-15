import tweepy
from playsound import playsound
from binance.client import Client
import datetime
import time

class MyStreamListener(tweepy.StreamListener):

    client = Client("binance_key", "binance_secret")

    btc_within_1_hour = False
    btc_within_1_hour_ts = ""
    btc_time_between_price_check = 5
    btc_time_between_price_check_last_ts = ""

    eth_within_1_hour = False
    eth_within_1_hour_ts = ""
    eth_time_between_price_check = 5
    eth_time_between_price_check_last_ts = ""

    ada_within_1_hour = False
    ada_within_1_hour_ts = ""
    ada_time_between_price_check = 5
    ada_time_between_price_check_last_ts = ""

    doge_within_1_hour = False
    doge_within_1_hour_ts = ""
    doge_time_between_price_check = 5
    doge_time_between_price_check_last_ts = ""

    def on_status(self, status):
        if status.user.id_str != '44196397':
            return
        print(status.text)
        playsound('beep.wav')

        if("btc" in status.text or "bitcoin" in status.text):
            btc_within_1_hour = True
            btc_within_1_hour_ts = time.time()
            btc_time_between_price_check_last_ts = time.time()
            print(client.get_avg_price(symbol='BTCUSDT'))
        
        if("eth" in status.text):
            eth_within_1_hour = True
            eth_within_1_hour_ts = time.time()
            eth_time_between_price_check_last_ts = time.time()
            print(client.get_avg_price(symbol='ETHUSDT'))
        
        if("ada" in status.text or "cardano" in status.text):
            ada_within_1_hour = True
            ada_within_1_hour_ts = time.time()
            ada_time_between_price_check_last_ts = time.time()
            print(client.get_avg_price(symbol='ADAUSDT'))
        
        if("doge" in status.text):
            doge_within_1_hour = True
            doge_within_1_hour_ts = time.time()
            doge_time_between_price_check_last_ts = time.time()
            print(client.get_avg_price(symbol='DOGEUSDT'))

        ct = datetime.datetime.now() 
        print("current time:-", ct) 


    def on_error(self, status_code):
        if status_code == 420:
            return False

    def on_data(self, raw_data):

        if(btc_within_1_hour == True):
            if(btc_within_1_hour_ts + 3600 > time.time()):
                if(time.time() > btc_time_between_price_check_last_ts + (btc_time_between_price_check * 60)):
                    print(client.get_avg_price(symbol='BTCUSDT'))
                    btc_time_between_price_check_last_ts = time.time()
                else:
                    return
            else:
                btc_within_1_hour = False

        if(eth_within_1_hour == True):
            if(eth_within_1_hour_ts + 3600 > time.time()):
                if(time.time() > eth_time_between_price_check_last_ts + (eth_time_between_price_check * 60)):
                    print(client.get_avg_price(symbol='ETHUSDT'))
                    eth_time_between_price_check_last_ts = time.time()
                else:
                    return
            else:
                eth_within_1_hour = False

        if(ada_within_1_hour == True):
            if(ada_within_1_hour_ts + 3600 > time.time()):
                if(time.time() > ada_time_between_price_check_last_ts + (ada_time_between_price_check * 60)):
                    print(client.get_avg_price(symbol='ADAUSDT'))
                    ada_time_between_price_check_last_ts = time.time()
                else:
                    return
            else:
                ada_within_1_hour = False

        if(doge_within_1_hour == True):
            if(doge_within_1_hour_ts + 3600 > time.time()):
                if(time.time() > doge_time_between_price_check_last_ts + (doge_time_between_price_check * 60)):
                    print(client.get_avg_price(symbol='DOGEUSDT'))
                    doge_time_between_price_check_last_ts = time.time()
                else:
                    return
            else:
                doge_within_1_hour = False


auth = tweepy.OAuthHandler("twitter_api_key", "twitter_api_secret")
auth.set_access_token("twitter_auth_key", "twitter_auth_secret")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['btc','bitcoin','eth','ethereum','ada','cardano','doge','dogecoin','buy','sell','crypto','stock','bonds','market','$','ticker'], is_async=True)
print("Starting.....")

