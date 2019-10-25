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

try:
	client = Client(os.getenv('BINANCE_APIKEY', 'NOTDEF_APIKEY'), os.getenv('BINANCE_SEKKEY', 'NOTDEF_APIKEY'), {"verify": True, "timeout": 20})

	# Exchange status
	if client.get_system_status()['status'] != 0:
		print('Binance out of service')
		sys.exit(0)

	# Orders
	openOrders = client.get_open_orders()
	totOpenOrder = len(openOrders)

	if totOpenOrder != 0:
		if totOpenOrder == 1:
			print('Open order:')
		elif totOpenOrder < 1:
			print(f'Open orders ({totOpenOrder}):')

		[printOrder(n, i, len(openOrders)) for i,n in enumerate(openOrders, 1)]
	else:
		print('No open order')

except BinanceAPIException as e:
	logging.info(f'Binance API exception: {e.status_code} - {e.message}')

except BinanceRequestException as e:
	logging.info(f'Binance request exception: {e.status_code} - {e.message}')

except BinanceWithdrawException as e:
	logging.info(f'Binance withdraw exception: {e.status_code} - {e.message}')
