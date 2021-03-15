import tweepy
from playsound import playsound
from binance.client import Client
import datetime
import time


class MyStreamListener(tweepy.StreamListener):

    client = Client("Rbf6XBLon1tZyettwIGAl4HndRox4vBrJkOVIb3s4pj9Z5bYBeDmNfLGmylWFdnz",
                    "3Pwpw8v9qEFXecOtVjwL9B72LMUbxWVsoM7fJfOLE4778NMiYLjvYHozSsJjUysZ")

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

    def __init__(self):
        self.client = Client("binance_key",
                             "binance_secret")

        self.btc_within_1_hour = False
        self.btc_within_1_hour_ts = ""
        self.btc_time_between_price_check = 5
        self.btc_time_between_price_check_last_ts = ""

        self.eth_within_1_hour = False
        self.eth_within_1_hour_ts = ""
        self.eth_time_between_price_check = 5
        self.eth_time_between_price_check_last_ts = ""

        self.ada_within_1_hour = False
        self.ada_within_1_hour_ts = ""
        self.ada_time_between_price_check = 5
        self.ada_time_between_price_check_last_ts = ""

        self.doge_within_1_hour = False
        self.doge_within_1_hour_ts = ""
        self.doge_time_between_price_check = 5
        self.doge_time_between_price_check_last_ts = ""

    def on_status(self, status):
        if status.user.id_str != '44196397':
            return
        print(status.text)
        playsound('beep.wav')

        if("btc" in status.text or "bitcoin" in status.text):
            self.btc_within_1_hour = True
            self.btc_within_1_hour_ts = time.time()
            self.btc_time_between_price_check_last_ts = time.time()
            print(self.client.get_avg_price(symbol='BTCUSDT'))

        if("eth" in status.text):
            self.eth_within_1_hour = True
            self.eth_within_1_hour_ts = time.time()
            self.eth_time_between_price_check_last_ts = time.time()
            print(self.client.get_avg_price(symbol='ETHUSDT'))

        if("ada" in status.text or "cardano" in status.text):
            self.ada_within_1_hour = True
            self.ada_within_1_hour_ts = time.time()
            self.ada_time_between_price_check_last_ts = time.time()
            print(self.client.get_avg_price(symbol='ADAUSDT'))

        if("doge" in status.text):
            self.doge_within_1_hour = True
            self.doge_within_1_hour_ts = time.time()
            self.doge_time_between_price_check_last_ts = time.time()
            print(self.client.get_avg_price(symbol='DOGEUSDT'))

        ct = datetime.datetime.now()
        print("current time:-", ct)

    def on_error(self, status_code):
        if status_code == 420:
            return False

    def on_data(self, raw_data):

        if(self.btc_within_1_hour == True):
            if(self.btc_within_1_hour_ts + 3600 > time.time()):
                if(time.time() > self.btc_time_between_price_check_last_ts + (self.btc_time_between_price_check * 60)):
                    print(self.client.get_avg_price(symbol='BTCUSDT'))
                    self.btc_time_between_price_check_last_ts = time.time()
                else:
                    return
            else:
                self.btc_within_1_hour = False

        if(self.eth_within_1_hour == True):
            if(self.eth_within_1_hour_ts + 3600 > time.time()):
                if(time.time() > self.eth_time_between_price_check_last_ts + (self.eth_time_between_price_check * 60)):
                    print(self.client.get_avg_price(symbol='ETHUSDT'))
                    self.eth_time_between_price_check_last_ts = time.time()
                else:
                    return
            else:
                self.eth_within_1_hour = False

        if(self.ada_within_1_hour == True):
            if(self.ada_within_1_hour_ts + 3600 > time.time()):
                if(time.time() > self.ada_time_between_price_check_last_ts + (self.ada_time_between_price_check * 60)):
                    print(self.client.get_avg_price(symbol='ADAUSDT'))
                    self.ada_time_between_price_check_last_ts = time.time()
                else:
                    return
            else:
                self.ada_within_1_hour = False

        if(self.doge_within_1_hour == True):
            if(self.doge_within_1_hour_ts + 3600 > time.time()):
                if(time.time() > self.doge_time_between_price_check_last_ts + (self.doge_time_between_price_check * 60)):
                    print(self.client.get_avg_price(symbol='DOGEUSDT'))
                    self.doge_time_between_price_check_last_ts = time.time()
                else:
                    return
            else:
                self.doge_within_1_hour = False


auth = tweepy.OAuthHandler("twitter_api_key", "twitter_api_secret")
auth.set_access_token("twitter_auth_key", "twitter_auth_secret")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['btc','bitcoin','eth','ethereum','ada','cardano','doge','dogecoin','buy','sell','crypto','stock','bonds','market','$','ticker'], is_async=True)
print("Starting.....")

