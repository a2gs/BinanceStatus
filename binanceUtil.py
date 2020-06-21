#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota
# andre.scota@gmail.com
# MIT license

from time import strftime, gmtime
from sys import exit, stderr
from binance.client import Client

# ---------------------------------------------------

confirmationYES = False
exportToXls = False
recvWindow = int(0)
binanceTimestamp = False

def nmExit(n: int = 0, m: str = ""):
	print(m)
	exit(n)

def nmExitOk(n : int = 0, m : str = "Ok."):
	nmExit(n, m)

def nmExitErro(n : int = 1, m : str = "Erro."):
	nmExit(n, m)

def getRecvWindow() -> int:
	global recvWindow
	return recvWindow

def setRecvWindow(rw: int):
	global recvWindow
	recvWindow = rw

def getConfirmationYES() -> bool:
	global confirmationYES
	return confirmationYES

def setConfirmationYES(y: bool):
	global confirmationYES
	confirmationYES = y

def getExportXLS() -> bool:
	global exportToXls
	return exportToXls

def setExportXLS(x: bool):
	global exportToXls
	exportToXls = x

def setTimestamp(f: bool = False):
	global binanceTimestamp
	binanceTimestamp = f

# ---------------------------------------------------

def completeMilliTime(tm) -> str:
	global binanceTimestamp

	if binanceTimestamp == True:
		return(tm)
	else:
		return(strftime(f"%d/%b/%Y %a %H:%M:%S.{tm % 1000}", gmtime(tm / 1000)))

def errPrint(*args, **kwargs):
	print(*args, file = stderr, **kwargs)

def askConfirmation() -> bool:
	if getConfirmationYES() == False:
		conf = input("Confirm operation? (N/y) \n")

		if conf != 'Y' and conf != 'y':
			print("CANCELED!")
			return False

	return True

# ---------------------------------------------------

def binanceInterval(i: str):
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

	return ''

def binanceOrderType(t: str):
	if   t == 'LIMIT':             return Client.ORDER_TYPE_LIMIT
	elif t == 'LIMIT_MAKER':       return Client.ORDER_TYPE_LIMIT_MAKER
	elif t == 'MARKET':            return Client.ORDER_TYPE_MARKET 
	elif t == 'STOP_LOSS':         return Client.ORDER_TYPE_STOP_LOSS 
	elif t == 'STOP_LOSS_LIMIT':   return Client.ORDER_TYPE_STOP_LOSS_LIMIT 
	elif t == 'TAKE_PROFIT':       return Client.ORDER_TYPE_TAKE_PROFIT 
	elif t == 'TAKE_PROFIT_LIMIT': return Client.ORDER_TYPE_TAKE_PROFIT_LIMIT 

	return ''

def binanceSide(s: str):
	if   s == 'BUY':  return Client.SIDE_BUY
	elif s == 'SELL': return Client.SIDE_SELL

	return ''
