#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota
# andre.scota@gmail.com
# MIT license

import os, sys
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceWithdrawException, BinanceRequestException

def printOrder(order, seq, tot):
	print(f'{seq}/{tot}) Order id [' + str(order['orderId']) + '] data:\n' 
		+ '\tPrice.......: [' + order['price']          + ']\n'
		+ '\tQtd.........: [' + order['origQty']        + ']\n'
		+ '\tQtd executed: [' + order['executedQty']    + ']\n'
		+ '\tSide........: [' + order['side']           + ']\n'
		+ '\tType........: [' + order['type']           + ']\n'
		+ '\tStop price..: [' + order['stopPrice']      + ']\n'
		+ '\tIs working..: [' + str(order['isWorking']) + ']')

#def printAccount(accBalance, seq, tot):
def printAccount(accBalance):
	print('Asset balance [' + accBalance['asset'] + '] | Free [' + accBalance['free'] + '] | Locked [' + accBalance['locked'] + ']')

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
		print('No open order')

def printHelp(execName):
	print(f'{execName} -h <ASSET>\n\tAccount history (trades, dusts, etc)\n')
	print(f'{execName} -i\n\tWallet/Account information\n')
	print(f'{execName} -d\n\tAccount details (fees)\n')
	print(f'{execName} -s\n\tPlace a sell order\n')
	print(f'{execName} -b\n\tPlace a buy order\n')
	print(f'{execName} -c \n\tCancel a order\n')

def printTradeAllHist(tradeAllHist, seq, tot):
	print(f'{seq}/{tot}) Symbol: [' + tradeAllHist['symbol'] + ']\n'
		+ '\tTime: [' + str(tradeAllHist['time']) + ' | Update time: [' + str(tradeAllHist['updateTime']) + ']\n'
		+ '\tOrder Id: [' + str(tradeAllHist['orderId']) + '| Order list Id: [' + str(tradeAllHist['orderListId']) + '] | Client Order Id: [' + tradeAllHist['clientOrderId'] + ']\n'
		+ '\tPrice: [' + tradeAllHist['price'] + ' | Orig Qtd: [' + tradeAllHist['origQty'] + ' | Executed Qtd: [' + tradeAllHist['executedQty'] + 'Cummulative Quote Qtd: [' + tradeAllHist['cummulativeQuoteQty'] + ']\n'
		+ '\tStatus: [' + tradeAllHist['status'] + '] | Time in Force: [' + tradeAllHist['timeInForce'] + ']\n'
		+ '\tSide: [' + tradeAllHist['side'] + ']\n'
		+ '\tType: [' + tradeAllHist['type'] + ']\n'
		+ '\tStop Price: [' + tradeAllHist['stopPrice'] + ']\n'
		+ '\tIs working: [' + str(tradeAllHist['isWorking']) + ']')

def printTradeHistory(tradeHist, seq, tot):
	print(f'{seq}/{tot}) Symbol: [' + tradeHist['symbol'] + ']\n'
		+ '\tTime: [' + str(tradeHist['time']) + ']\n'
		+ '\tOrder Id: [' + str(tradeHist['orderId']) + ' | Id: [' + str(tradeHist['id']) + ' Order List Id: [' + str(tradeHist['orderListId']) + ']\n'
		+ '\tPrice: [' + tradeHist['price'] + '] | Qtd: [' + tradeHist['qty'] + '] | Quote Qtd: [' + tradeHist['quoteQty'] + ']\n'
		+ '\tCommission: [' + tradeHist['commission'] + 'Commission asset: [' + tradeHist['commissionAsset'] + ']\n'
		+ '\tBuyer: [' + str(tradeHist['isBuyer']) + '] | Maker: [' + str(tradeHist['isMaker']) + '] | TradeHist: [' + str(tradeHist['isBestMatch']) + ']')

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

def printAccountDetails(client):
	print('=5 get_asset_details() =============================================================================================================')
	print(client.get_asset_details())
	print('=6 get_trade_fee() =============================================================================================================')
	print(client.get_trade_fee())

def sellMarketOrder(client, symb, qtd):
	print(f'Market order for symbol {symb} with quantity {qtd}')

def sellLimitOrder(client, symb, qtd, prc):
	print(f'Limit order for {symb} with quantity {qtd} at price {prc}')

# ---------------------------------------------------------------------------

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

	# Sell order
	elif sys.argv[1] == '-s' and len(sys.argv) > 2:

		# Market order
		if sys.argv[2] == 'MARKET' and len(sys.argv) == 5:
			sellMarketOrder(client, sys.argv[3], sys.argv[4])

		# Limit order
		elif sys.argv[2] == 'LIMIT' and len(sys.argv) == 6:
			sellLimitOrder(client, sys.argv[3], sys.argv[4], sys.argv[5])

	else:
		print('Parameters error.')
		printHelp(sys.argv[0])
		sys.exit(0)
