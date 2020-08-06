#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota
# andre.scota@gmail.com
# MIT license

import binanceUtil  as BU
import binancePrint as BP

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceWithdrawException, BinanceRequestException, BinanceOrderException, BinanceOrderMinAmountException, BinanceOrderMinPriceException, BinanceOrderMinTotalException, BinanceOrderUnknownSymbolException, BinanceOrderInactiveSymbolException

testOrder = False
#LOCK = True
LOCK = False

def setTestOrder(o: bool):
	global testOrder
	testOrder = o

def getTestOrder() -> bool:
	global testOrder
	return testOrder

# ---------------------------------------------------

def cancel_a_spot_order(client, symbOrd = '', ordrid = 0) -> [bool, str]:
	print(f"Cancel SPOT Order Id [{ordrid}] with Symbol [{symbOrd}]")

	if BU.askConfirmation() == False:
		return True, "Canceled by confirmation!"

	# TESTING
	global LOCK
	if LOCK == True:
		return False, "Programmed flag order lock ON!"

	try:
		cancOrd = client.cancel_order(symbol = symbOrd, orderId = ordrid)
	except BinanceRequestException as e:
		return False, f"Erro BinanceRequestException: [{e.status_code} - {e.message}]"
	except BinanceAPIException as e:
		return False, f"Erro at client.cancel_order() BinanceAPIException: [{e.status_code} - {e.message}]"
	except Exception as e:
		return False, f"Erro at client.cancel_order(): {e}"

	#print("Cancellation return")
	if BU.getExportXLS() == True:
		BU.errPrint("Symbol\tOriginal Client Order Id\tOrder Id\tOrder List Id (OCO info)\tClient Order Id\tPrice\tOriginal Qtd\tExecuted Qty\tCummulative Quote Qty\tStatus\tTime In Force\tType\tSide")
		BU.errPrint(f"{cancOrd['symbol']}\t{cancOrd['origClientOrderId']}\t{cancOrd['orderId']}\t{cancOrd['orderListId']}\t{cancOrd['clientOrderId']}\t{cancOrd['price']}\t{cancOrd['origQty']}\t{cancOrd['executedQty']}\t{cancOrd['cummulativeQuoteQty']}\t{cancOrd['status']}\t{cancOrd['timeInForce']}\t{cancOrd['timeInForce']}\t{cancOrd['type']}\t{cancOrd['side']}")

	else:
		print(f"Symbol..................: [{cancOrd['symbol']}]")
		print(f"Original Client Order Id: [{cancOrd['origClientOrderId']}]")
		print(f"Order Id................: [{cancOrd['orderId']}]")
		print(f"Order List Id (OCO info): [{cancOrd['orderListId']}]")
		print(f"Client Order Id.........: [{cancOrd['clientOrderId']}]")
		print(f"Price...................: [{cancOrd['price']}]")
		print(f"Original Qtd............: [{cancOrd['origQty']}]")
		print(f"Executed Qty............: [{cancOrd['executedQty']}]")
		print(f"Cummulative Quote Qty...: [{cancOrd['cummulativeQuoteQty']}]")
		print(f"Status..................: [{cancOrd['status']}]")
		print(f"Time In Force...........: [{cancOrd['timeInForce']}]")
		print(f"Type....................: [{cancOrd['type']}]")
		print(f"Side....................: [{cancOrd['side']}]")

	return True, "Ok"

def cancel_a_margin_order(client, symbOrd = '', ordrid = 0) -> [bool, str]:
	print(f"Cancel Margin Order Id [{ordrid}] with Symbol [{symbOrd}]")

	if BU.askConfirmation() == False:
		return True, "Cancelled by Confirmation!"

	# TESTING
	global LOCK
	if LOCK == True:
		return False, "Programmed flag order lock ON!"

	try:
		cancOrd = client.cancel_margin_order(symbol = symbOrd, orderId = ordrid)
	except BinanceRequestException as e:
		return False, f"Erro at client.cancel_margin_order() BinanceRequestException: [{e.status_code} - {e.message}]"

	except BinanceAPIException as e:
		return False, f"Erro at client.cancel_margin_order() BinanceAPIException: [{e.status_code} - {e.message}]"

	except Exception as e:
		return False, f"Erro at client.cancel_margin_order(): {e}"

	if BU.getExportXLS() == True:
		BU.errPrint("Symbol\tOriginal Client Order Id\tOrder Id\tClient Order Id\tPrice\tOriginal Qtd\tExecuted Qty\tCummulative Quote Qty\tStatus\tTime In Force\tType\tSide")
		BU.errPrint(f"{cancOrd['symbol']}\t{cancOrd['origClientOrderId']}\t{cancOrd['orderId']}\t{cancOrd['clientOrderId']}\t{cancOrd['price']}\t{cancOrd['origQty']}\t{cancOrd['executedQty']}\t{cancOrd['cummulativeQuoteQty']}\t{cancOrd['status']}\t{cancOrd['timeInForce']}\t{cancOrd['timeInForce']}\t{cancOrd['type']}\t{cancOrd['side']}")

	else:
		print(f"Symbol..................: [{cancOrd['symbol']}]")
		print(f"Original Client Order Id: [{cancOrd['origClientOrderId']}]")
		print(f"OrderId.................: [{cancOrd['orderId']}]")
		print(f"Client Order Id.........: [{cancOrd['clientOrderId']}]")
		print(f"Price...................: [{cancOrd['price']}]")
		print(f"Original Qtd............: [{cancOrd['origQty']}]")
		print(f"Executed Qty............: [{cancOrd['executedQty']}]")
		print(f"Cummulative Quote Qty...: [{cancOrd['cummulativeQuoteQty']}]")
		print(f"Status..................: [{cancOrd['status']}]")
		print(f"Time In Force...........: [{cancOrd['timeInForce']}]")
		print(f"Type....................: [{cancOrd['type']}]")
		print(f"Side....................: [{cancOrd['side']}]")

	return True, 'Ok'

# ---------------------------------------------------

def orderSpotLimit(client, symbOrd = '', qtdOrd = 0, prcOrd = 0.0, prcStopOrd = 0.0, prcStopLimitOrd = 0.0, sideOrd = 0) -> [bool, str]:

	if BU.getExportXLS() == True:
		BU.errPrint("Symbol\tSide\tQuantity\tPrice\tStop Price\tLimit OCO")
		BU.errPrint(f"{symbOrd}\t{sideOrd}\t{qtdOrd}\t{prcOrd}\t{prcStopOrd}\t{prcStopLimitOrd}")
	else:
		print(f"Symbol....: [{symbOrd}]")
		print(f"Side......: [{sideOrd}]")
		print(f"Quantity..: [{qtdOrd}]")
		print(f"Price.....: [{prcOrd}]")
		print(f"Stop Price: [{prcStopOrd}]")
		print(f"Limit OCO.: [{prcStopLimitOrd}]")

	if BU.askConfirmation() == False:
		return True, "Cancelled by Confirmation!"

	# TESTING
	global LOCK
	if LOCK == True:
		return False, "Programmed flag order lock ON!"

	try:
		order = client.create_oco_order(symbol               = symbOrd,
		                                side                 = sideOrd,
		                                quantity             = qtdOrd,
		                                price                = prcOrd,
		                                stopPrice            = prcStopOrd,
												  stopLimitPrice       = prcStopLimitOrd,
		                                stopLimitTimeInForce = Client.TIME_IN_FORCE_GTC,
		                                newOrderRespType     = Client.ORDER_RESP_TYPE_FULL)

	except BinanceRequestException as e:
		return False, f"Erro create_oco_order BinanceRequestException: [{e.status_code} - {e.message}]"
	except BinanceAPIException as e:
		return False, f"Erro create_oco_order BinanceAPIException: [{e.status_code} - {e.message}]"
	except BinanceOrderException as e:
		return False, f"Erro create_oco_order BinanceOrderException: [{e.status_code} - {e.message}]"
	except BinanceOrderMinAmountException as e:
		return False, f"Erro create_oco_order BinanceOrderMinAmountException: [{e.status_code} - {e.message}]"
	except BinanceOrderMinPriceException as e:
		return False, f"Erro create_oco_order BinanceOrderMinPriceException: [{e.status_code} - {e.message}]"
	except BinanceOrderMinTotalException as e:
		return False, f"Erro create_oco_order BinanceOrderMinTotalException: [{e.status_code} - {e.message}]"
	except BinanceOrderUnknownSymbolException as e:
		return False, f"Erro create_oco_order BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]"
	except BinanceOrderInactiveSymbolException as e:
		return False, f"Erro create_oco_order BinanceOrderInactiveSymbolException: [{e.status_code} - {e.message}]"
	except Expcetion as e:
		return False, f"Erro create_oco_order generic exception: {e}"

	printPlacedOrder(order)

	return True, "Ok"

def orderSpot(client, symbOrd = '', qtdOrd = 0, prcOrd = 0.0, sideOrd = 0, typeOrd = 0) ->[bool, str]:

	if BU.getExportXLS() == True:
		BU.errPrint("Symbol\tSide\tQuantity\tPrice\tStop Price\tLimit OCO\tType")
		BU.errPrint(f"{symbOrd}\t{sideOrd}\t{qtdOrd}\t{prcOrd}\t{typeOrd}")
	else:
		print(f"Symbol....: [{symbOrd}]")
		print(f"Side......: [{sideOrd}]")
		print(f"Quantity..: [{qtdOrd}]")
		print(f"Price.....: [{prcOrd}]")
		print(f"Type......: [{typeOrd}]")

	if BU.askConfirmation() == False:
		return True, "Cancelled by Confirmation!"

	# TESTING
	global LOCK
	if LOCK == True:
		return False, "Programmed flag order lock ON!"

	try:

		if getTestOrder() == True:
			print("TESTING ORDER")
			order = client.create_test_order(symbol      = symbOrd,
			                                 side        = sideOrd,
			                                 type        = typeOrd,
			                                 timeInForce = Client.TIME_IN_FORCE_GTC,
			                                 quantity    = qtdOrd,
			                                 price       = prcOrd)
		else:
			order = client.create_order(symbol           = symbOrd,
			                            quantity         = qtdOrd,
			                            price            = prcOrd,
			                            side             = sideOrd,
			                            type             = typeOrd,
			                            timeInForce      = Client.TIME_IN_FORCE_GTC,
			                            newOrderRespType = Client.ORDER_RESP_TYPE_FULL)

	except BinanceRequestException as e:
		return False, f"Erro order_limit_buy BinanceRequestException: [{e.status_code} - {e.message}]"
	except BinanceAPIException as e:
		return False, f"Erro order_limit_buy BinanceAPIException: [{e.status_code} - {e.message}]"
	except BinanceOrderException as e:
		return False, f"Erro order_limit_buy BinanceOrderException: [{e.status_code} - {e.message}]"
	except BinanceOrderMinAmountException as e:
		return False, f"Erro order_limit_buy BinanceOrderMinAmountException: [{e.status_code} - {e.message}]"
	except BinanceOrderMinPriceException as e:
		return False, f"Erro order_limit_buy BinanceOrderMinPriceException: [{e.status_code} - {e.message}]"
	except BinanceOrderMinTotalException as e:
		return False, f"Erro order_limit_buy BinanceOrderMinTotalException: [{e.status_code} - {e.message}]"
	except BinanceOrderUnknownSymbolException as e:
		return False, f"Erro order_limit_buy BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]"
	except BinanceOrderInactiveSymbolException as e:
		return False, f"Erro order_limit_buy BinanceOrderInactiveSymbolException: [{e.status_code} - {e.message}]"
	except Exception as e:
		return False, f"Erro order_limit_buy generic exception: {e}"

	printPlacedOrder(order)

	return True, "Ok"

# ---------------------------------------------------

def buyOCOOrder(client, symb = '', qtd = 0, prc = 0.0, stopprice = 0.0, limit = 0.0) -> bool:
	print("NOT IMPLEMENTED")

def sellOCOOrder(client, symb = '', qtd = 0, prc = 0.0, stopprice = 0.0, limit = 0.0) -> bool:
	print("NOT IMPLEMENTED")

# ---------------------------------------------------

def orderMargin(client, symbOrd = '', sideOrd = 0, typeOrd = 0, qtdOrd = 0, prcOrd = 0.0, prcStop = 0.0, limit = 0.0) ->[bool, str]:
	print(f"MARGIN Order {typeOrd}")

	if BU.getExportXLS() == True:
		BU.errPrint("Symbol\tSide\tQuantity\tPrice\tStop Price\tLimit OCO\tType")
		BU.errPrint(f"{symbOrd}\t{sideOrd}\t{qtdOrd}\t{prcOrd}\t{prcStop}\t{limit}\t{typeOrd}")
	else:
		print(f"Symbol....: [{symbOrd}]")
		print(f"Side......: [{sideOrd}]")
		print(f"Quantity..: [{qtdOrd}]")
		print(f"Price.....: [{prcOrd}]")
		print(f"Stop Price: [{prcStop}]")
		print(f"Limit OCO.: [{limit}]")
		print(f"Type......: [{typeOrd}]")

	if BU.askConfirmation() == False:
		return True, "Cancelled by Confirmation!"

	# TESTING
	global LOCK
	if LOCK == True:
		return False, "Programmed flag order lock ON!"

	try:
		if typeOrd == 'LIMIT':
			order = client.create_margin_order(symbol           = symbOrd,
		                                      side             = BU.binanceSide(sideOrd),
		                                      type             = Client.ORDER_TYPE_LIMIT,
		                                      timeInForce      = Client.TIME_IN_FORCE_GTC,
		                                      quantity         = qtdOrd,
		                                      price            = prcOrd,
		                                      newOrderRespType = Client.ORDER_RESP_TYPE_FULL)
		else:
			order = client.create_margin_order(symbol           = symbOrd,
		                                      side             = BU.binanceSide(sideOrd),
		                                      type             = BU.binanceOrderType(typeOrd),
		                                      timeInForce      = Client.TIME_IN_FORCE_GTC,
		                                      quantity         = qtdOrd,
		                                      price            = prcOrd,
		                                      stopPrice        = prcStop,
		                                      newOrderRespType = Client.ORDER_RESP_TYPE_FULL)

	except BinanceRequestException as e:
		return False, f"Erro create_margin_order BinanceRequestException: [{e.status_code} - {e.message}]"
	except BinanceAPIException as e:
		return False, f"Erro create_margin_order BinanceAPIException: [{e.status_code} - {e.message}]"
	except BinanceOrderException as e:
		return False, f"Erro create_margin_order BinanceOrderException: [{e.status_code} - {e.message}]"
	except BinanceOrderMinAmountException as e:
		return False, f"Erro create_margin_order BinanceOrderMinAmountException: [{e.status_code} - {e.message}]"
	except BinanceOrderMinPriceException as e:
		return False, f"Erro create_margin_order BinanceOrderMinPriceException: [{e.status_code} - {e.message}]"
	except BinanceOrderMinTotalException as e:
		return False, f"Erro create_margin_order BinanceOrderMinTotalException: [{e.status_code} - {e.message}]"
	except BinanceOrderUnknownSymbolException as e:
		return False, f"Erro create_margin_order BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]"
	except BinanceOrderInactiveSymbolException as e:
		return False, f"Erro create_margin_order BinanceOrderInactiveSymbolException: [{e.status_code} - {e.message}]"
	except Exception as e:
		return False, f"Erro create_margin_order generic exception: {e}"

	BP.printMarginOrder(order)

	return True, "Ok"
