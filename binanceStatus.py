#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota
# andre.scota@gmail.com
# MIT license

import os, sys
from binancePrint import printMarginOrder, printDetailsAssets, printTradeFee, printHelp, printTradeAllHist, printTradeHistory, printMarginAssets, printOrder, printAccount
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceWithdrawException, BinanceRequestException

def printAccountInfos(client):
	try:
		acc = client.get_account()
	except:
		print('Erro at client.get_account()')
		return

	totAccBalance = len(acc['balances'])

	try:
		accStatus = client.get_account_status()
	except:
		print('Erro at client.get_account_status()')
		return

	print('Can trade: ' + str(acc['canTrade']) + ' | Can withdraw: ' + str(acc['canWithdraw']) + ' | Can deposit: ' + str(acc['canDeposit']) + ' | Account type: ' + str(acc['accountType']))
	print('(Account status detail: ' + accStatus['msg'] + ' | Success: ' + str(accStatus['success']) + ')')

	if len(acc['balances']) != 0:
		[printAccount(n) for n in acc['balances'] if float(n['free']) != 0.0 or float(n['locked']) != 0.0]

	# Orders
	try:
		openOrders = client.get_open_orders()
	except:
		print('Erro at client.get_open_orders()')
		return

	totOpenOrder = len(openOrders)

	if totOpenOrder != 0:
		if totOpenOrder == 1:
			print('Open order:')
		elif totOpenOrder < 1:
			print(f'Open orders ({totOpenOrder}):')

		[printOrder(n, i, totOpenOrder) for i,n in enumerate(openOrders, 1)]
	else:
		print('No open orders')

	# MARGIN

	marginInfo = client.get_margin_account()
	if marginInfo['borrowEnabled'] == False:
		return

	print("* MARGIN *")

	print(f"Margin level..........: [{marginInfo['marginLevel']}]")
	print(f"Total asset of BTC....: [{marginInfo['totalAssetOfBtc']}]")
	print(f"Total liability of BTC: [{marginInfo['totalLiabilityOfBtc']}]")
	print(f"Total Net asset of BTC: [{marginInfo['totalNetAssetOfBtc']}]")
	print(f"Trade enabled.........? [{marginInfo['tradeEnabled']}]")

	print('Borrowed assets:')
	[printMarginAssets(n, i) for i,n in enumerate(marginInfo['userAssets'], 1) if float(n['netAsset']) != 0.0]

	# Margin Orders
	try:
		openMarginOrders = client.get_open_margin_orders()
	except:
		print('Erro at client.get_open_margin_orders()')
		return

	totOpenMarginOrder = len(openMarginOrders)

	if totOpenMarginOrder != 0:
		if totOpenMarginOrder == 1:
			print('Open margin order:')
		elif totOpenMarginOrder < 1:
			print(f'Open margin orders ({totOpenOrder}):')

		[printMarginOrder(n, i, totOpenMarginOrder) for i,n in enumerate(openMarginOrders, 1)]
	else:
		print('No open margin orders')

# ---------------------------------------------------

def printAccountHistory(client, symb):
	try:
		tradeHist = client.get_my_trades(symbol=symb)
	except:
		print(f'Erro at client.get_my_trades(symbol={symb})')
		return

	tradeHistTot = len(tradeHist)

	print(f'Trade history {symb}:')

	[printTradeHistory(n, i, tradeHistTot) for i,n in enumerate(tradeHist, 1)]

	print('=8 get_dust_log() =============================================================================================================')
	print(client.get_dust_log())
	print('==============================================================================================================')

	try:
		tradeAllHist = client.get_all_orders(symbol=symb)
	except:
		print(f'Erro at client.get_all_orders(symbol={symb})')
		return

	tradeAllHistTot = len(tradeAllHist)

	print(f'Trade history {symb}:')

	[printTradeAllHist(n, i, tradeAllHistTot) for i,n in enumerate(tradeAllHist, 1)]

# ---------------------------------------------------

def printAccountDetails(client):
	try:
		assDet = client.get_asset_details()
		tradFee = client.get_trade_fee()
	except BinanceWithdrawException as e:
		print('Erro BinanceWithdrawException')

	print('Details on Assets')
	[printDetailsAssets(n, assDet['assetDetail'][n], i, len(assDet['assetDetail'])) for i,n in enumerate(assDet['assetDetail'].keys(), 1)]

	print('Trade Fee:')
	[printTradeFee(n, i, len(tradFee['tradeFee'])) for i,n in enumerate(tradFee['tradeFee'], 1)]

# ---------------------------------------------------

def sellMarketOrder(client, symb, qtd):
	print(f'Market order for symbol {symb} with quantity {qtd}')

	try:
		order = client.order_market_sell(symbol=symb, quantity=qtd) 
	except BinanceRequestException as e:
		print('Erro BinanceRequestException')
	except BinanceAPIException as e:
		print('Erro BinanceAPIException')
	except BinanceOrderException as e:
		print('Erro BinanceOrderException')
	except BinanceOrderMinAmountException as e:
		print('Erro BinanceOrderMinAmountException')
	except BinanceOrderMinPriceException as e:
		print('Erro BinanceOrderMinPriceException')
	except BinanceOrderMinTotalException as e:
		print('Erro BinanceOrderMinTotalException')
	except BinanceOrderUnknownSymbolException as e:
		print('Erro BinanceOrderUnknownSymbolException')
	except BinanceOrderInactiveSymbolException as e:
		print('Erro BinanceOrderInactiveSymbolException')
	else:
		print(order)

# ---------------------------------------------------

def sellLimitOrder(client, symb, qtd, prc):
	print(f'Limit order for {symb} with quantity {qtd} at price {prc}')

	try:
		order = client.order_limit_sell(symbol=symb, quantity=qtd, price=prc)
	except BinanceRequestException as e:
		print('Erro BinanceRequestException')
	except BinanceAPIException as e:
		print('Erro BinanceAPIException')
	except BinanceOrderException as e:
		print('Erro BinanceOrderException')
	except BinanceOrderMinAmountException as e:
		print('Erro BinanceOrderMinAmountException')
	except BinanceOrderMinPriceException as e:
		print('Erro BinanceOrderMinPriceException')
	except BinanceOrderMinTotalException as e:
		print('Erro BinanceOrderMinTotalException')
	except BinanceOrderUnknownSymbolException as e:
		print('Erro BinanceOrderUnknownSymbolException')
	except BinanceOrderInactiveSymbolException as e:
		print('Erro BinanceOrderInactiveSymbolException')
	else:
		print(order)

# ---------------------------------------------------

def buyLimitOrder(client, symb, qtd, prc):
	print(f'Limit order for {symb} with quantity {qtd} at price {prc}')

	try:
		order = client.order_limit_buy(symbol=symb, quantity=qtd, price=prc)
	except BinanceRequestException as e:
		print('Erro BinanceRequestException')
	except BinanceAPIException as e:
		print('Erro BinanceAPIException')
	except BinanceOrderException as e:
		print('Erro BinanceOrderException')
	except BinanceOrderMinAmountException as e:
		print('Erro BinanceOrderMinAmountException')
	except BinanceOrderMinPriceException as e:
		print('Erro BinanceOrderMinPriceException')
	except BinanceOrderMinTotalException as e:
		print('Erro BinanceOrderMinTotalException')
	except BinanceOrderUnknownSymbolException as e:
		print('Erro BinanceOrderUnknownSymbolException')
	except BinanceOrderInactiveSymbolException as e:
		print('Erro BinanceOrderInactiveSymbolException')
	else:
		print(order)

# ---------------------------------------------------

def buyMarketOrder(client, symb, qtd):
	print(f'Market order for symbol {symb} with quantity {qtd}')

	try:
		order = client.order_market_buy(symbol=symb, quantity=qtd) 
	except BinanceRequestException as e:
		print('Erro BinanceRequestException')
	except BinanceAPIException as e:
		print('Erro BinanceAPIException')
	except BinanceOrderException as e:
		print('Erro BinanceOrderException')
	except BinanceOrderMinAmountException as e:
		print('Erro BinanceOrderMinAmountException')
	except BinanceOrderMinPriceException as e:
		print('Erro BinanceOrderMinPriceException')
	except BinanceOrderMinTotalException as e:
		print('Erro BinanceOrderMinTotalException')
	except BinanceOrderUnknownSymbolException as e:
		print('Erro BinanceOrderUnknownSymbolException')
	except BinanceOrderInactiveSymbolException as e:
		print('Erro BinanceOrderInactiveSymbolException')
	else:
		print(order)

# ---------------------------------------------------

if __name__ == '__main__':

	if len(sys.argv) <= 1:
		printHelp(sys.argv[0])
		sys.exit(0)

	binanceAPIKey = os.getenv('BINANCE_APIKEY', 'NOTDEF_APIKEY')
	if binanceAPIKey == 'NOTDEF_APIKEY':
		print('Environment variable BINANCE_APIKEY not defined!')
		sys.exit(0)

	binanceSEKKey = os.getenv('BINANCE_SEKKEY', 'NOTDEF_APIKEY')
	if binanceSEKKey == 'NOTDEF_APIKEY':
		print('Environment variable BINANCE_SEKKEY not defined!')
		sys.exit(0)

	try:
		client = Client(binanceAPIKey, binanceSEKKey, {"verify": True, "timeout": 20})

	except BinanceAPIException as e:
		print(f'Binance API exception: {e.status_code} - {e.message}')

	except BinanceRequestException as e:
		print(f'Binance request exception: {e.status_code} - {e.message}')

	except BinanceWithdrawException as e:
		print(f'Binance withdraw exception: {e.status_code} - {e.message}')

	# Exchange status
	try:
		if client.get_system_status()['status'] != 0:
			print('Binance out of service')
			sys.exit(0)
	except:
		print('Erro at client.get_system_status()')
		sys.exit(0)
	

	# Wallet/Account information
	if sys.argv[1] == '-i' and len(sys.argv) == 2:
		printAccountInfos(client)

	# Account history (trades, dusts, etc)
	elif sys.argv[1] == '-h' and len(sys.argv) == 3:
		printAccountHistory(client, sys.argv[2])

	# Account details (fees)
	elif sys.argv[1] == '-d' and len(sys.argv) == 2:
		printAccountDetails(client)

	# Buy order
	elif sys.argv[1] == '-b' and len(sys.argv) > 2:

		# Market order
		if sys.argv[2] == 'MARKET' and len(sys.argv) == 5:
			buyMarketOrder(client, sys.argv[3], sys.argv[4])

		# Limit order
		elif sys.argv[2] == 'LIMIT' and len(sys.argv) == 6:
			buyLimitOrder(client, sys.argv[3], sys.argv[4], sys.argv[5])

		else:
			print('Parameters error for buy order')

	# Sell order
	elif sys.argv[1] == '-s' and len(sys.argv) > 2:

		# Market order
		if sys.argv[2] == 'MARKET' and len(sys.argv) == 5:
			sellMarketOrder(client, sys.argv[3], sys.argv[4])

		# Limit order
		elif sys.argv[2] == 'LIMIT' and len(sys.argv) == 6:
			sellLimitOrder(client, sys.argv[3], sys.argv[4], sys.argv[5])

		else:
			print('Parameters error for sell order')

	else:
		print('Parameters error.')
		printHelp(sys.argv[0])
		sys.exit(0)
