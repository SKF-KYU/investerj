from binance.client import Client
import streamlit as st
import pandas as pd
import numpy as np
from numpy import linspace
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

limit = 10000

class BinanceAPI:

    def __init__(self):
        API_KEY = 'sIwCMV8ymxh2xsQSycuR5Stp66GKnH0A6gDx3jlwNtCIIWBQmGTIVgjN9SSGQ7hq'
        API_SECRET = 'rZBsX7m8jJs9pwLgRgr1woHfOu8SGDyiEQAXIxLVobUs6JsQQ7PcaCHuBpyb0Vb6'

        self.client = Client(API_KEY, API_SECRET)

    def get_ticker(self, pair):
        try:
            value = self.client.get_ticker(symbol=pair)
            return value
        except Exception as e:
            print('Exception Messege : {}'.format(e))
            return None

    def get_order_book(self, pair):
        try:
            value = self.client.get_order_book(symbol=pair,limit=limit)
            return value
        except Exception as e:
            print('Exception Messege : {}'.format(e))
            return None

    def get_asset(self, symbol):
        try:
            value = self.client.get_asset_balance(asset=symbol)
            return value
        except Exception as e:
            print('Exception Messege : {}'.format(e))
            return None

def main():
    binance_set = BinanceAPI()

    orderbook = binance_set.get_order_book('JASMYUSDT')

    df_bids = pd.DataFrame(orderbook['bids'])
    df_asks = pd.DataFrame(orderbook['asks'])

    df_bids.columns=['kakaku','maisu']
    df_asks.columns=['kakaku','maisu']

    df_bids['kakaku']=df_bids['kakaku'].astype(float)
    df_bids['maisu']=df_bids['maisu'].astype(float)
    df_asks['kakaku']=df_asks['kakaku'].astype(float)
    df_asks['maisu']=df_asks['maisu'].astype(float)

    pd.set_option('display.max_rows', None)

    # df_bids

    st.write(df_bids.style.bar(subset=['maisu'], color='#10aa10'))
    st.write(df_asks.style.bar(subset=['maisu'], color='#ff3333'))

    # print(df_bids.style.bar(subset=['maisu'], color='#d65f5f'))

    # df_bids.style.bar(subset=['maisu'], color='#d65f5f')

    # st.write(orderbook)
    # print(pd.read_json(orderbook))
    # print(orderbook)

    # st.write(orderbook)

    # print(ticker['lastPrice'])
    # print(ticker['volume'])

    # asset_dict = prv_set.get_asset('BTC')
    # print(asset_dict['free'])

# if __name__ == '__main__':
#     main()


main()
