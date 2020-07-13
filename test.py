#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

import os, sys
#from binancePrint import printMarginOrder, printDetailsAssets, printTradeFee, printHelp, printTradeAllHist
#from binancePrint import printTradeHistory, printMarginAssets, printOrder, printAccount, printDustTrade
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceWithdrawException, BinanceRequestException

binanceAPIKey = os.getenv("BINANCE_APIKEY", "NOTDEF_APIKEY")
binanceSEKKey = os.getenv("BINANCE_SEKKEY", "NOTDEF_APIKEY")

client = Client(binanceAPIKey, binanceSEKKey, {"verify": True, "timeout": 20})

print('1---------------------------------------------------------------')
#print("Get compressed, aggregate trades. Trades that fill at the time, from the same order, with the same price will have the quantity aggregated.")
#print(client.get_aggregate_trades())         DEIXA PRA DEPOIS
print('2---------------------------------------------------------------')
print("get_orderbook_ticker")
#print(client.get_orderbook_ticker(symbol=['BTCUSDT','LTCBTC']))
#print(client.get_orderbook_ticker(symbol='BTCUSDT'))
print('--')
#print(client.get_orderbook_tickers(['BTCUSDT','LTCBTC']))


#sys.exit(0)
print('3---------------------------------------------------------------')
#print("Get current asset balance")
#print(client.get_asset_balance('BTC'))
print('4---------------------------------------------------------------')
print("")
#print(client.())
print('5---------------------------------------------------------------')
print("")
#print(client.())
print('6---------------------------------------------------------------')
print("Query loan record          get_margin_loan_details")
#print(client.get_margin_loan_details(asset='USDT', txId = 0, size=100))
#BinanceRequestException, BinanceAPIException
print("Query repay record      get_margin_repay_details")
#print(client.get_margin_repay_details(asset='BTC', txId='', startTime='', size=100))
#BinanceRequestException, BinanceAPIException
print('7---------------------------------------------------------------')
print("")
#print(client.())
print('8---------------------------------------------------------------')
print("")
#print(client.())
print('9---------------------------------------------------------------')
print("")
#print(client.())
print('10---------------------------------------------------------------')
print("get_products")
print(client.get_products())
print('11---------------------------------------------------------------')
print("")
#print(client.())
