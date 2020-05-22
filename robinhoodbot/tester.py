
import robin_stocks as r
import pandas as pd
import numpy as np
import ta as ta
from pandas.plotting import register_matplotlib_converters
from ta import *
from misc import *
from tradingstats import *

#!!! Fill out username and password
username = 'NickolausS7966'
password = 'Vvert#1313#1313'
#!!!

print("\n----- Logging in under user: " + str(username) + " -----\n")
#Log in to Robinhood
login = r.login(username,password)

data = r.get_historicals('WFTLF',span='year',bounds='regular')
print(data)
if not data:
    print("oh")

def get_watchlist_names():
    """
    Returns: the name of each watchlist as a list of strings
    """
    my_list_names = []
    symbols = []
    for name in r.get_all_watchlists(info='name'):
        my_list_names.append(name)
    for name in my_list_names:
        list = r.get_watchlist_by_name(name)
        for item in list:
            instrument_data = r.get_instrument_by_url(item.get('instrument'))
            symbol = instrument_data['symbol']
            symbols.append(symbol)
    return my_list_names

def get_portfolio_symbols():
    """
    Returns: the symbol for each stock in your portfolio as a list of strings
    """
    symbols = []
    holdings_data = r.get_current_positions()
    for item in holdings_data:
        if not item:
            continue
        instrument_data = r.get_instrument_by_url(item.get('instrument'))
        symbol = instrument_data['symbol']
        symbols.append(symbol)
    return symbols

def get_watchlist_symbols():
    """
    Returns: the symbol for each stock in your watchlist as a list of strings
    """
    my_list_names = []
    symbols = []
    for name in r.get_all_watchlists(info='name'):
        my_list_names.append(name)
    for name in my_list_names:
        list = r.get_watchlist_by_name(name)
        for item in list:
            instrument_data = r.get_instrument_by_url(item.get('instrument'))
            symbol = instrument_data['symbol']
            symbols.append(symbol)
    return symbols

# # watchlist = r.get_watchlist_by_name(name='new', info=None)
# all_watchlists = r.account.get_all_watchlists('name')
# watchlist_symbols = get_watchlist_symbols()
# watchlist_names = get_watchlist_names()
# portfolio_symbols = get_portfolio_symbols()
# print(watchlist_symbols)
# print(watchlist_names)
# print(all_watchlists)
# print(portfolio_symbols)

# my_list = ['AAPL', 'ADSK']
# print(my_list)

print("----- Logging out -----\n")
#Log in to Robinhood
logout = r.logout()