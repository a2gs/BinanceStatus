#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota
# andre.scota@gmail.com
# MIT license

import os, sys
from time import ctime
import binancePrint as BP
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceWithdrawException, BinanceRequestException

exportToXls = False

def errPrint(*args, **kwargs):
	print(*args, file = sys.stderr, **kwargs)

def accountInfos(client):
	try:
		acc = client.get_account()
	except BinanceAPIException as e:
		errPrint(f"Erro at client.get_account() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except BinanceRequestException as e:
		errPrint(f"Erro at client.get_account() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except:
		errPrint("Erro at client.get_account()")
		return

	try:
		accStatus = client.get_account_status()
	except BinanceWithdrawException as e:
		errPrint(f"Erro at client.get_account_status() BinanceWithdrawException: [{e.status_code} - {e.message}]")
		return
	except:
		errPrint("Erro at client.get_account_status()")
		return

	if exportToXls == True:
		print(f"Can trade\t{acc['canTrade']}\nCan withdraw\t{acc['canWithdraw']}\nCan deposit\t{acc['canDeposit']}\nAccount type\t{acc['accountType']}")
		print(f"Account status detail\t{accStatus['msg']}\nSuccess\t{accStatus['success']}\n")
	else:
		print(f"Can trade: [{acc['canTrade']}] Can withdraw: [{acc['canWithdraw']}] Can deposit: [{acc['canDeposit']}] Account type: [{acc['accountType']}]")
		print(f"(Account status detail: [{accStatus['msg']}] Success: [{accStatus['success']}]\n")

	if len(acc['balances']) != 0:
		if exportToXls == True:
			BP.printAccountXLSHEADER()
			[BP.printAccountXLS(n) for n in acc['balances'] if float(n['free']) != 0.0 or float(n['locked']) != 0.0]
		else:
			[BP.printAccount(n) for n in acc['balances'] if float(n['free']) != 0.0 or float(n['locked']) != 0.0]

	# Orders
	try:
		openOrders = client.get_open_orders()
	except BinanceRequestException as e:
		errPrint(f"Erro at client.get_open_orders() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except BinanceAPIException as e:
		errPrint(f"Erro at client.get_open_orders() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except:
		errPrint("Erro at client.get_open_orders()")
		return

	totOpenOrder = len(openOrders)

	if totOpenOrder != 0:
		if totOpenOrder == 1:
			print("\n* SPOT *")
		elif totOpenOrder < 1:
			print(f"Open orders ({totOpenOrder}):")

		if exportToXls == True:
			BP.printOrderXLSHEADER()
			[BP.printOrderXLS(n) for n in openOrders]
		else:
			[BP.printOrder(n, i, totOpenOrder) for i, n in enumerate(openOrders, 1)]
	else:
		print("No open orders")

	# MARGIN

	marginInfo = client.get_margin_account()
	if marginInfo['borrowEnabled'] == False:
		return

	print("\n* MARGIN *")

	if exportToXls == True:
		print("Margin level\tTotal asset of BTC\tTotal liability of BTC\tTotal Net asset of BTC\tTrade enabled")
		print(f"{marginInfo['marginLevel']}\t{marginInfo['totalAssetOfBtc']}\t{marginInfo['totalLiabilityOfBtc']}\t{marginInfo['totalNetAssetOfBtc']}\t{marginInfo['tradeEnabled']}\n")

		print('Borrowed assets:')
		BP.printMarginAssetsXLSHEADER()
		[BP.printMarginAssetsXLS(n) for n in marginInfo['userAssets'] if float(n['netAsset']) != 0.0]
	else:
		print(f"Margin level..........: [{marginInfo['marginLevel']}]")
		print(f"Total asset of BTC....: [{marginInfo['totalAssetOfBtc']}]")
		print(f"Total liability of BTC: [{marginInfo['totalLiabilityOfBtc']}]")
		print(f"Total Net asset of BTC: [{marginInfo['totalNetAssetOfBtc']}]")
		print(f"Trade enabled.........? [{marginInfo['tradeEnabled']}]\n")

		print('Borrowed assets:')
		[BP.printMarginAssets(n, i) for i, n in enumerate(marginInfo['userAssets'], 1) if float(n['netAsset']) != 0.0]

	# Margin Orders
	try:
		openMarginOrders = client.get_open_margin_orders()
	except BinanceRequestException as e:
		errPrint(f"Erro at client.get_open_margin_orders() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except BinanceAPIException as e:
		errPrint(f"Erro at client.get_open_margin_orders() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except:
		errPrint("Erro at client.get_open_margin_orders()")
		return

	totOpenMarginOrder = len(openMarginOrders)

	if totOpenMarginOrder != 0:
		print("");
		if   totOpenMarginOrder == 1: print("Open margin order:")
		elif totOpenMarginOrder <  1: print(f"Open margin orders ({totOpenOrder}):")

		if exportToXls == True:
			BP.printMarginOrderXLSHEADER()
			[BP.printMarginOrderXLS(n) for n in openMarginOrders]
		else:
			[BP.printMarginOrder(n, i, totOpenMarginOrder) for i, n in enumerate(openMarginOrders, 1)]
	else:
		print('No open margin orders')

# ---------------------------------------------------

def accountHistory(client, symb):
	try:
		tradeHist = client.get_my_trades(symbol=symb)
	except:
		errPrint(f"Erro at client.get_my_trades(symbol={symb})")
		return

	tradeHistTot = len(tradeHist)

	if exportToXls == True:
		BP.printTradeHistoryXLSHEADER()
		[BP.printTradeHistoryXLS(n) for n in tradeHist]
	else:
		print(f"Trade history {symb}:")
		[BP.printTradeHistory(n, i, tradeHistTot) for i, n in enumerate(tradeHist, 1)]

	print(f"All trade history {symb}:")

	try:
		tradeAllHist = client.get_all_orders(symbol=symb)
	except:
		errPrint(f"Erro at client.get_all_orders(symbol={symb})")
		return

	tradeAllHistTot = len(tradeAllHist)

	if exportToXls == True:
		BP.printTradeAllHistXLSHEADER()
		[BP.printTradeAllHistXLS(n) for n in tradeAllHist]
	else:
		print(f"Trade history {symb}:")
		[BP.printTradeAllHist(n, i, tradeAllHistTot) for i, n in enumerate(tradeAllHist, 1)]

	try:
		allDust = client.get_dust_log()
	except BinanceWithdrawException as e:
		errPrint(f"Erro at client.get_dust_log() BinanceWithdrawException: [{e.status_code} - {e.message}]")
		return
	except:
		errPrint("Erro at client.get_dust_log()")
		return

	allDustTot = len(allDust['results']['rows'])

	if exportToXls == True:
		pass
	else:
		print("Log of small amounts exchanged for BNB:")
		[BP.printDustTrade(n, i, allDustTot) for i, n in enumerate(allDust['results']['rows'], 1)]

# ---------------------------------------------------

def accountDetails(client):
	try:
		assDet = client.get_asset_details()
		tradFee = client.get_trade_fee()
	except BinanceWithdrawException as e:
		errPrint(f"Erro BinanceWithdrawException: [{e.status_code} - {e.message}]")
		return

	if exportToXls == True:
		print('Details on Assets')
		BP.printDetailsAssetsXLSHEADER()
		[BP.printDetailsAssetsXLS(n, assDet['assetDetail'][n]) for n in assDet['assetDetail'].keys()]

		print('\nTrade Fee')
		BP.printTradeFeeXLSHEADER()
		[BP.printTradeFeeXLS(n) for n in tradFee['tradeFee']]

	else:
		print('Details on Assets:')
		adTot = len(assDet['assetDetail'])
		[BP.printDetailsAssets(n, assDet['assetDetail'][n], i, adTot) for i, n in enumerate(assDet['assetDetail'].keys(), 1)]

		print('Trade Fee:')
		adTot = len(tradFee['tradeFee'])
		[BP.printTradeFee(n, i, adTot) for i, n in enumerate(tradFee['tradeFee'], 1)]

# ---------------------------------------------------

def sellMarketOrder(client, symb, qtd):
	print(f"Market order for symbol {symb} with quantity {qtd}")

	try:
		order = client.order_market_sell(symbol = symb, quantity = qtd) 
	except BinanceRequestException as e:
		errPrint(f"Erro order_market_sell() BinanceRequestException: [{e.status_code} - {e.message}]")
	except BinanceAPIException as e:
		errPrint(f"Erro order_market_sell() BinanceAPIException: [{e.status_code} - {e.message}]")
	except BinanceOrderException as e:
		errPrint(f"Erro order_market_sell() BinanceOrderException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinAmountException as e:
		errPrint(f"Erro order_market_sell() BinanceOrderMinAmountException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinPriceException as e:
		errPrint(f"Erro order_market_sell() BinanceOrderMinPriceException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinTotalException as e:
		errPrint(f"Erro order_market_sell() BinanceOrderMinTotalException: [{e.status_code} - {e.message}]")
	except BinanceOrderUnknownSymbolException as e:
		errPrint(f"Erro order_market_sell() BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]")
	except BinanceOrderInactiveSymbolException as e:
		errPrint(f"Erro order_market_sell() BinanceOrderInactiveSymbolException: [{e.status_code} - {e.message}]")
	else:
		print(order)

# ---------------------------------------------------

def sellStopOrder(client, symb, qtd, prc, stopprice):
	print(f"Stop sell order for {symb} with quantity {qtd} at price {prc} and stop price {stopprice}")

	try:
		order = client.create_oco_order(symbol = {symb}, side = SIDE_SELL, stopLimitTimeInForce = TIME_IN_FORCE_GTC,
		                                quantity = {qtd}, stopPrice = {stopprice}, price = {prc})

	except BinanceRequestException as e:
		errPrint(f"Erro create_oco_order() BinanceRequestException: [{e.status_code} - {e.message}]")
	except BinanceAPIException as e:
		errPrint(f"Erro create_oco_order() BinanceAPIException: [{e.status_code} - {e.message}]")
	except BinanceOrderException as e:
		errPrint(f"Erro create_oco_order() BinanceOrderException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinAmountException as e:
		errPrint(f"Erro create_oco_order() BinanceOrderMinAmountException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinPriceException as e:
		errPrint(f"Erro create_oco_order() BinanceOrderMinPriceException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinTotalException as e:
		errPrint(f"Erro create_oco_order() BinanceOrderMinTotalException: [{e.status_code} - {e.message}]")
	except BinanceOrderUnknownSymbolException as e:
		errPrint(f"Erro create_oco_order() BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]")
	except BinanceOrderInactiveSymbolException as e:
		errPrint(f"Erro create_oco_order() BinanceRequestException: [{e.status_code} - {e.message}]")
	else:
		print(order)

# ---------------------------------------------------

def sellLimitOrder(client, symb, qtd, prc):
	print(f"Limit order for {symb} with quantity {qtd} at price {prc}")

	try:
		order = client.order_limit_sell(symbol = symb, quantity = qtd, price = prc)
	except BinanceRequestException as e:
		errPrint(f"Erro order_limit_sell() BinanceRequestException: [{e.status_code} - {e.message}]")
	except BinanceAPIException as e:
		errPrint(f"Erro order_limit_sell() BinanceAPIException: [{e.status_code} - {e.message}]")
	except BinanceOrderException as e:
		errPrint(f"Erro order_limit_sell() BinanceOrderException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinAmountException as e:
		errPrint(f"Erro order_limit_sell() BinanceOrderMinAmountException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinPriceException as e:
		errPrint(f"Erro order_limit_sell() BinanceOrderMinPriceException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinTotalException as e:
		errPrint(f"Erro order_limit_sell() BinanceOrderMinTotalException: [{e.status_code} - {e.message}]")
	except BinanceOrderUnknownSymbolException as e:
		errPrint(f"Erro order_limit_sell() BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]")
	except BinanceOrderInactiveSymbolException as e:
		errPrint(f"Erro order_limit_sell() BinanceOrderInactiveSymbolException: [{e.status_code} - {e.message}]")
	else:
		print(order)

# ---------------------------------------------------

def buyStopOrder(client, symb, qtd, prc):
	print(f"Stop buy order for {symb} with quantity {qtd} at price {prc} and stop price {stopprice}")

	try:
		order = client.create_oco_order(symbol = {symb}, side = SIDE_BUY, stopLimitTimeInForce = TIME_IN_FORCE_GTC,
		                                quantity = {qtd}, stopPrice = {stopprice}, price = {prc})

	except BinanceRequestException as e:
		errPrint(f"Erro create_oco_order() BinanceRequestException: [{e.status_code} - {e.message}]")
	except BinanceAPIException as e:
		errPrint(f"Erro create_oco_order() BinanceAPIException: [{e.status_code} - {e.message}]")
	except BinanceOrderException as e:
		errPrint(f"Erro create_oco_order() BinanceOrderException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinAmountException as e:
		errPrint(f"Erro create_oco_order() BinanceOrderMinAmountException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinPriceException as e:
		errPrint(f"Erro create_oco_order() BinanceOrderMinPriceException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinTotalException as e:
		errPrint(f"Erro create_oco_order() BinanceOrderMinTotalException: [{e.status_code} - {e.message}]")
	except BinanceOrderUnknownSymbolException as e:
		errPrint(f"Erro create_oco_order() BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]")
	except BinanceOrderInactiveSymbolException as e:
		errPrint(f"Erro create_oco_order() BinanceRequestException: [{e.status_code} - {e.message}]")
	else:
		print(order)

# ---------------------------------------------------

def buyLimitOrder(client, symb, qtd, prc):
	print(f'Limit order for {symb} with quantity {qtd} at price {prc}')

	try:
		order = client.order_limit_buy(symbol=symb, quantity=qtd, price=prc)
	except BinanceRequestException as e:
		errPrint(f"Erro BinanceRequestException: [{e.status_code} - {e.message}]")
	except BinanceAPIException as e:
		errPrint(f"Erro BinanceAPIException: [{e.status_code} - {e.message}]")
	except BinanceOrderException as e:
		errPrint(f"Erro BinanceOrderException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinAmountException as e:
		errPrint(f"Erro BinanceOrderMinAmountException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinPriceException as e:
		errPrint(f"Erro BinanceOrderMinPriceException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinTotalException as e:
		errPrint(f"Erro BinanceOrderMinTotalException: [{e.status_code} - {e.message}]")
	except BinanceOrderUnknownSymbolException as e:
		errPrint(f"Erro BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]")
	except BinanceOrderInactiveSymbolException as e:
		errPrint(f"Erro BinanceOrderInactiveSymbolException: [{e.status_code} - {e.message}]")
	else:
		print(order)

# ---------------------------------------------------

def buyMarketOrder(client, symb, qtd):
	print(f"Market order for symbol {symb} with quantity {qtd}")

	try:
		order = client.order_market_buy(symbol=symb, quantity=qtd) 
	except BinanceRequestException as e:
		errPrint(f"Erro BinanceRequestException: [{e.status_code} - {e.message}]")
	except BinanceAPIException as e:
		errPrint(f"Erro BinanceAPIException: [{e.status_code} - {e.message}]")
	except BinanceOrderException as e:
		errPrint(f"Erro BinanceOrderException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinAmountException as e:
		errPrint(f"Erro BinanceOrderMinAmountException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinPriceException as e:
		errPrint(f"Erro BinanceOrderMinPriceException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinTotalException as e:
		errPrint(f"Erro BinanceOrderMinTotalException: [{e.status_code} - {e.message}]")
	except BinanceOrderUnknownSymbolException as e:
		errPrint(f"Erro BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]")
	except BinanceOrderInactiveSymbolException as e:
		errPrint(f"Erro BinanceOrderInactiveSymbolException: [{e.status_code} - {e.message}]")
	else:
		print(order)

# ---------------------------------------------------

def binanceInterval(i):
	if   i == '12h': return Client.KLINE_INTERVAL_12HOUR
	elif i == '15m': return Client.KLINE_INTERVAL_15MINUTE
	elif i == '1d':  return Client.KLINE_INTERVAL_1DAY
	elif i == '1h':  return Client.KLINE_INTERVAL_1HOUR
	elif i == '1m':  return Client.KLINE_INTERVAL_1MINUTE
	elif i == '1M':  return Client.KLINE_INTERVAL_1MONTH
	elif i == '1w':  return Client.KLINE_INTERVAL_1WEEK
	elif i == '2h':  return Client.KLINE_INTERVAL_2HOUR
	elif i == '30m': return Client.KLINE_INTERVAL_30MINUTE
	elif i == '3d':  return Client.KLINE_INTERVAL_3DAY
	elif i == '3m':  return Client.KLINE_INTERVAL_3MINUTE
	elif i == '4h':  return Client.KLINE_INTERVAL_4HOUR
	elif i == '5m':  return Client.KLINE_INTERVAL_5MINUTE
	elif i == '6h':  return Client.KLINE_INTERVAL_6HOUR
	elif i == '8h':  return Client.KLINE_INTERVAL_8HOUR
	else:            return ""

# ---------------------------------------------------

def infoSymbol(client, symb, interv, candlesTot):

	try:
		sumbPrc = client.get_klines(symbol=symb, interval = binanceInterval(interv), limit = candlesTot)
	except BinanceAPIException as e:
		errPrint(f"Erro at client.get_klines() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except BinanceRequestException as e:
		errPrint(f"Erro at client.get_klines() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except:
		errPrint("Erro at client.get_klines()")
		return

	if exportToXls == True:
		BP.printInfoSymbolValuesXLSHEADER()
		[BP.printInfoSymbolValuesXLS(n) for n in sumbPrc]
	else:
		print(f"Symbol [{symb}] in interval [{interv}]");
		totsumbPrc = len(sumbPrc)
		[BP.printInfoSymbolValues(n, i, totsumbPrc) for i, n in enumerate(sumbPrc, 1)]

# ---------------------------------------------------

def listSymbolsRateLimits(client):
	try:
		ei = client.get_exchange_info()
	except BinanceAPIException as e:
		errPrint(f"Erro at client.get_exchange_info() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except BinanceRequestException as e:
		errPrint(f"Erro at client.get_exchange_info() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except:
		errPrint("Erro at client.get_exchange_info()")
		return

	if exportToXls == True:
		print("Rate Limits")
		BP.printListRateLimitXLSHEADER()
		[BP.printListRateLimitXLS(n) for n in ei['rateLimits']]

		print("\nSymbols")
		BP.printListSymbolsXLSHEADER()
		[BP.printListSymbolsXLS(n) for n in ei['symbols']]

	else:
		print("Rate Limits:")
		totei = len(ei['rateLimits'])
		[BP.printListRateLimit(n, i, totei) for i, n in enumerate(ei['rateLimits'], 1)]

		print("Symbols:")
		totei = len(ei['symbols'])
		[BP.printListSymbols(n, i, totei) for i, n in enumerate(ei['symbols'], 1)]

# ---------------------------------------------------

def infoDetailsSymbol(client, symb):
	try:
		si = client.get_symbol_info(symb)
	except BinanceAPIException as e:
		errPrint(f"Erro at client.get_symbol_info() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except BinanceRequestException as e:
		errPrint(f"Erro at client.get_symbol_info() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except:
		errPrint("Erro at client.get_symbol_info()")
		return

	if exportToXls == True:
		BP.printListSymbolsXLSHEADER()
		BP.printListSymbolsXLS(si)

	else:
		print("Symbol: [{symb}]")
		BP.printListSymbols(si)

# ---------------------------------------------------

def h24PriceChangeStats(client):

	try:
		ga = client.get_ticker()
	except BinanceAPIException as e:
		errPrint(f"Erro at client.get_ticker() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except BinanceRequestException as e:
		errPrint(f"Erro at client.get_ticker() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except:
		errPrint("Erro at client.get_ticker()")
		return

	totGa = len(ga)

	if exportToXls == True:
		BP.print24hPrcChangStsXLSHEADER()
		[BP.print24hPrcChangStsXLS(n) for n in ga]
	else:
		print("24 hour price change statistics:")
		[BP.print24hPrcChangSts(n, i, totGa) for i, n in enumerate(ga, 1)]

# ---------------------------------------------------

if __name__ == '__main__':

	if len(sys.argv) <= 1:
		printHelp(sys.argv[0])
		sys.exit(0)

	binanceAPIKey = os.getenv("BINANCE_APIKEY", "NOTDEF_APIKEY")
	if binanceAPIKey == "NOTDEF_APIKEY":
		print("Environment variable BINANCE_APIKEY not defined!")
		sys.exit(0)

	binanceSEKKey = os.getenv("BINANCE_SEKKEY", "NOTDEF_APIKEY")
	if binanceSEKKey == "NOTDEF_APIKEY":
		print("Environment variable BINANCE_SEKKEY not defined!")
		sys.exit(0)

	try:
		client = Client(binanceAPIKey, binanceSEKKey, {"verify": True, "timeout": 20})

	except BinanceAPIException as e:
		print(f"Binance API exception: [{e.status_code} - {e.message}]")
		sys.exit(0)

	except BinanceRequestException as e:
		print(f"Binance request exception: [{e.status_code} - {e.message}]")
		sys.exit(0)

	except BinanceWithdrawException as e:
		print(f"Binance withdraw exception: [{e.status_code} - {e.message}]")
		sys.exit(0)

	except:
		print("Binance connection error")
		sys.exit(0)

	# Exchange status
	try:
		if client.get_system_status()['status'] != 0:
			errPrint("Binance out of service")
			sys.exit(0)
	except BinanceAPIException as e:
		errPrint(f"Erro at client.get_system_status() BinanceAPIException: [{e.status_code} - {e.message}]")
		sys.exit(0)
	except:
		errPrint("Erro at client.get_system_status()")
		sys.exit(0)
	
	if "--xls" in sys.argv:
		exportToXls = True
		sys.argv.remove("--xls")
	else:
		exportToXls = False

	# Wallet/Account information
	if sys.argv[1] == "-i" and len(sys.argv) == 2:
		accountInfos(client)

	# Account history (trades, dusts, etc)
	elif sys.argv[1] == "-h" and len(sys.argv) == 3:
		accountHistory(client, sys.argv[2])

	# Account details (fees)
	elif sys.argv[1] == "-d" and len(sys.argv) == 2:
		accountDetails(client)

	# Rate limits and list of symbols
	elif sys.argv[1] == "-l" and len(sys.argv) == 2:
		listSymbolsRateLimits(client)

	# Information (prices) about a symbol
	elif sys.argv[1] == "-v" and len(sys.argv) == 5:
		infoSymbol(client, sys.argv[2], sys.argv[3], int(sys.argv[4]))

	# Information (details) about a symbol
	elif sys.argv[1] == "-V" and len(sys.argv) == 3:
		infoDetailsSymbol(client, sys.argv[2])

	# 24 hour price change statistics
	elif sys.argv[1] == "-p" and len(sys.argv) == 2:
		h24PriceChangeStats(client)

	# Buy order
	elif sys.argv[1] == "-b" and len(sys.argv) > 2:

		# Market order
		if sys.argv[2] == "MARKET" and len(sys.argv) == 5:
			buyMarketOrder(client, sys.argv[3], sys.argv[4])

		# Limit order
		elif sys.argv[2] == "LIMIT" and len(sys.argv) == 6:
			buyLimitOrder(client, sys.argv[3], sys.argv[4], sys.argv[5])

		# OCO
		elif sys.argv[2] == "STOP" and len(sys.argv) == 7:
			buyStopOrder(client, sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])

		else:
			print("Parameters error for buy order")

	# Sell order
	elif sys.argv[1] == "-s" and len(sys.argv) > 2:

		# Market order
		if sys.argv[2] == "MARKET" and len(sys.argv) == 5:
			sellMarketOrder(client, sys.argv[3], sys.argv[4])

		# Limit order
		elif sys.argv[2] == "LIMIT" and len(sys.argv) == 6:
			sellLimitOrder(client, sys.argv[3], sys.argv[4], sys.argv[5])

		# OCO
		elif sys.argv[2] == "STOP" and len(sys.argv) == 7:
			sellStopOrder(client, sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])

		else:
			print("Parameters error for sell order")

	else:
		print("Parameters error.")
		printHelp(sys.argv[0])
		sys.exit(0)
