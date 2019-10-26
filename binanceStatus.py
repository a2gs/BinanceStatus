#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota
# andre.scota@gmail.com
# MIT license

import os
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

def printAccount(accBalance, seq, tot):
	print(f'{seq}/{tot}) Asset balance [' + accBalance['asset'] + '] | Free [' + accBalance['free'] + '] | Locked [' + accBalance['locked'] + ']')

try:
	client = Client(os.getenv('BINANCE_APIKEY', 'NOTDEF_APIKEY'), os.getenv('BINANCE_SEKKEY', 'NOTDEF_APIKEY'), {"verify": True, "timeout": 20})

	# Exchange status
	if client.get_system_status()['status'] != 0:
		print('Binance out of service')
		sys.exit(0)

	print('=1=============================================================================================================')
	acc = client.get_account()
	print('Can trade: ' + str(acc['canTrade']) + ' | Can withdraw: ' + str(acc['canWithdraw']) + ' | Can deposit: ' + str(acc['canDeposit']) + ' | Account type: ' + str(acc['accountType']))

	totAccBalance = len(acc['balances'])

	if totAccBalance != 0:
		[printAccount(n, i, totAccBalance) for i,n in enumerate(acc['balances'], 1) if float(n['free']) != 0.0 or float(n['locked']) != 0.0]

	print('=2=============================================================================================================')
	print(client.get_asset_balance(asset='BTC'))
	print('=3=============================================================================================================')
	print(client.get_account_status())
	print('=4=============================================================================================================')
	print(client.get_my_trades(symbol='BNBBTC'))
	print('=5=============================================================================================================')
	print(client.get_asset_details())
	print('=6=============================================================================================================')
	print(client.get_trade_fee())
	print('=7=============================================================================================================')
	print(client.get_dust_log())
	print('=8=============================================================================================================')

	# Orders
	openOrders = client.get_open_orders()
	totOpenOrder = len(openOrders)

	if totOpenOrder != 0:
		if totOpenOrder == 1:
			print('Open order:')
		elif totOpenOrder < 1:
			print(f'Open orders ({totOpenOrder}):')

		[printOrder(n, i, totOpenOrder) for i,n in enumerate(openOrders, 1)]
	else:
		print('No open order')

except BinanceAPIException as e:
	print(f'Binance API exception: {e.status_code} - {e.message}')

except BinanceRequestException as e:
	print(f'Binance request exception: {e.status_code} - {e.message}')

except BinanceWithdrawException as e:
	print(f'Binance withdraw exception: {e.status_code} - {e.message}')
