#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

import os, sys
from binancePrint import printMarginOrder, printDetailsAssets, printTradeFee, printHelp, printTradeAllHist
from binancePrint import printTradeHistory, printMarginAssets, printOrder, printAccount, printDustTrade
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceWithdrawException, BinanceRequestException


binanceAPIKey = os.getenv("BINANCE_APIKEY", "NOTDEF_APIKEY")
binanceSEKKey = os.getenv("BINANCE_SEKKEY", "NOTDEF_APIKEY")

client = Client(binanceAPIKey, binanceSEKKey, {"verify": True, "timeout": 20})

print('1---------------------------------------------------------------')
#print(client.get_avg_price(symbol='BTCUSDT'))
print('2---------------------------------------------------------------')
#print(client.get_all_tickers())
print('3---------------------------------------------------------------')
#print(client.get_ticker())
print('4---------------------------------------------------------------')
#print(client.get_symbol_info("BTCUSDT"))
print('5---------------------------------------------------------------')
print(client.get_klines(symbol="BTCUSDT", interval = Client.KLINE_INTERVAL_15MINUTE, limit = 1))
'''
KLINE_INTERVAL_12HOUR = '12h'
KLINE_INTERVAL_15MINUTE = '15m'
KLINE_INTERVAL_1DAY = '1d'
KLINE_INTERVAL_1HOUR = '1h'
KLINE_INTERVAL_1MINUTE = '1m'
KLINE_INTERVAL_1MONTH = '1M'
KLINE_INTERVAL_1WEEK = '1w'
KLINE_INTERVAL_2HOUR = '2h'
KLINE_INTERVAL_30MINUTE = '30m'
KLINE_INTERVAL_3DAY = '3d'
KLINE_INTERVAL_3MINUTE = '3m'
KLINE_INTERVAL_4HOUR = '4h'
KLINE_INTERVAL_5MINUTE = '5m'
KLINE_INTERVAL_6HOUR = '6h'
KLINE_INTERVAL_8HOUR = '8h'
'''
print('6---------------------------------------------------------------')
print('7---------------------------------------------------------------')
print('8---------------------------------------------------------------')
print('9---------------------------------------------------------------')
print('0---------------------------------------------------------------')
