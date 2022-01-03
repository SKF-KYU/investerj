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

    def get_symbol_ticker(self, pair):
        try:
            value = self.client.get_symbol_ticker(symbol=pair)
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

    value = binance_set.get_symbol_ticker('JASMYUSDT')
    orderbook = binance_set.get_order_book('JASMYUSDT')

    df_bids = pd.DataFrame(orderbook['bids'])
    df_asks = pd.DataFrame(orderbook['asks'])

    df_bids.columns=['価格','枚数']
    df_asks.columns=['価格','枚数']



    df_bids['価格']=df_bids['価格'].astype(float)
    df_bids['枚数']=df_bids['枚数'].astype(float)
    df_asks['価格']=df_asks['価格'].astype(float)
    df_asks['枚数']=df_asks['枚数'].astype(float)

    df_bids = df_bids.set_index('価格')
    df_asks = df_asks.set_index('価格')


    # pd.get.option("display.max_rows")
    # df_bids

    # st.write(df_bids.style.bar(subset=['枚数'], color='#10aa10'))
    # st.write(df_asks.style.bar(subset=['枚数'], color='#ff3333'))

    # a = 1
    # st.write(f'a={a}')
    value = float(value['price'])

    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.write(f'<p class="big-font">BINANCE現在価格：{value}</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.write('ASK')
        st.dataframe(df_asks.style.format(na_rep='MISSING',formatter={('価格'): "{:.4f}", ('枚数'): "{:,.0f}"}).bar(subset=['枚数'], color='#FF0000'), width=500,height=100000)
    with col2:
        st.write('BID')
        st.dataframe(df_bids.style.format(na_rep='MISSING',formatter={('価格'): "{:.4f}", ('枚数'): "{:,.0f}"}).bar(subset=['枚数'], color='#10aa10'), width=500,height=100000)

    # print(df_bids.style.bar(subset=['枚数'], color='#d65f5f'))

    # df_bids.style.bar(subset=['枚数'], color='#d65f5f')

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
