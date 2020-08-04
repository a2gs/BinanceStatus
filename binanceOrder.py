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

def cancel_a_spot_order(client, symbOrd = '', ordrid = 0) -> bool:
	BU.errPrint(f"Cancel SPOT Order Id [{ordrid}] with Symbol [{symbOrd}]")

	if BU.askConfirmation() == False:
		return True

	# TESTING
	global LOCK
	if LOCK == True:
		BU.errPrint("PROGRAM LOCKED BY SECURITY!")
		return False

	try:
		cancOrd = client.cancel_order(symbol = symbOrd, orderId = ordrid)
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.cancel_order() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.cancel_order() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.cancel_order(): {e}")
		return False

	BU.errPrint("Cancellation return")
	if BU.getExportXLS() == True:
		BU.errPrint("Symbol\tOriginal Client Order Id\tOrder Id\tOrder List Id (OCO info)\tClient Order Id\tPrice\tOriginal Qtd\tExecuted Qty\tCummulative Quote Qty\tStatus\tTime In Force\tType\tSide")
		BU.errPrint(f"{cancOrd['symbol']}\t{cancOrd['origClientOrderId']}\t{cancOrd['orderId']}\t{cancOrd['orderListId']}\t{cancOrd['clientOrderId']}\t{cancOrd['price']}\t{cancOrd['origQty']}\t{cancOrd['executedQty']}\t{cancOrd['cummulativeQuoteQty']}\t{cancOrd['status']}\t{cancOrd['timeInForce']}\t{cancOrd['timeInForce']}\t{cancOrd['type']}\t{cancOrd['side']}")

	else:
		BU.errPrint(f"Symbol..................: [{cancOrd['symbol']}]")
		BU.errPrint(f"Original Client Order Id: [{cancOrd['origClientOrderId']}]")
		BU.errPrint(f"Order Id................: [{cancOrd['orderId']}]")
		BU.errPrint(f"Order List Id (OCO info): [{cancOrd['orderListId']}]")
		BU.errPrint(f"Client Order Id.........: [{cancOrd['clientOrderId']}]")
		BU.errPrint(f"Price...................: [{cancOrd['price']}]")
		BU.errPrint(f"Original Qtd............: [{cancOrd['origQty']}]")
		BU.errPrint(f"Executed Qty............: [{cancOrd['executedQty']}]")
		BU.errPrint(f"Cummulative Quote Qty...: [{cancOrd['cummulativeQuoteQty']}]")
		BU.errPrint(f"Status..................: [{cancOrd['status']}]")
		BU.errPrint(f"Time In Force...........: [{cancOrd['timeInForce']}]")
		BU.errPrint(f"Type....................: [{cancOrd['type']}]")
		BU.errPrint(f"Side....................: [{cancOrd['side']}]")

	return True	

def cancel_a_margin_order(client, symbOrd = '', ordrid = 0) -> bool:
	BU.errPrint(f"Cancel Margin Order Id [{ordrid}] with Symbol [{symbOrd}]")

	if BU.askConfirmation() == False:
		return True

	# TESTING
	global LOCK
	if LOCK == True:
		BU.errPrint("PROGRAM LOCKED BY SECURITY!")
		return False

	try:
		cancOrd = client.cancel_margin_order(symbol = symbOrd, orderId = ordrid)
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.cancel_margin_order() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.cancel_margin_order() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.cancel_margin_order(): {e}")
		return False

	BU.errPrint("Cancellation return")

	if BU.getExportXLS() == True:
		BU.errPrint("Symbol\tOriginal Client Order Id\tOrder Id\tClient Order Id\tPrice\tOriginal Qtd\tExecuted Qty\tCummulative Quote Qty\tStatus\tTime In Force\tType\tSide")
		BU.errPrint(f"{cancOrd['symbol']}\t{cancOrd['origClientOrderId']}\t{cancOrd['orderId']}\t{cancOrd['clientOrderId']}\t{cancOrd['price']}\t{cancOrd['origQty']}\t{cancOrd['executedQty']}\t{cancOrd['cummulativeQuoteQty']}\t{cancOrd['status']}\t{cancOrd['timeInForce']}\t{cancOrd['timeInForce']}\t{cancOrd['type']}\t{cancOrd['side']}")

	else:
		BU.errPrint(f"Symbol..................: [{cancOrd['symbol']}]")
		BU.errPrint(f"Original Client Order Id: [{cancOrd['origClientOrderId']}]")
		BU.errPrint(f"OrderId.................: [{cancOrd['orderId']}]")
		BU.errPrint(f"Client Order Id.........: [{cancOrd['clientOrderId']}]")
		BU.errPrint(f"Price...................: [{cancOrd['price']}]")
		BU.errPrint(f"Original Qtd............: [{cancOrd['origQty']}]")
		BU.errPrint(f"Executed Qty............: [{cancOrd['executedQty']}]")
		BU.errPrint(f"Cummulative Quote Qty...: [{cancOrd['cummulativeQuoteQty']}]")
		BU.errPrint(f"Status..................: [{cancOrd['status']}]")
		BU.errPrint(f"Time In Force...........: [{cancOrd['timeInForce']}]")
		BU.errPrint(f"Type....................: [{cancOrd['type']}]")
		BU.errPrint(f"Side....................: [{cancOrd['side']}]")

	return True	

# ---------------------------------------------------

def orderSpotLimit(client, symbOrd = '', qtdOrd = 0, prcOrd = 0.0, prcStopOrd = 0.0, prcStopLimitOrd = 0.0, sideOrd = 0) -> bool:

	if BU.askConfirmation() == False:
		return False

	# TESTING
	global LOCK
	if LOCK == True:
		BU.errPrint("PROGRAM LOCKED BY SECURITY!")
		return False

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
		BU.errPrint(f"Erro create_oco_order BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except BinanceAPIException as e:
		BU.errPrint(f"Erro create_oco_order BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceOrderException as e:
		BU.errPrint(f"Erro create_oco_order BinanceOrderException: [{e.status_code} - {e.message}]")
		return False
	except BinanceOrderMinAmountException as e:
		BU.errPrint(f"Erro create_oco_order BinanceOrderMinAmountException: [{e.status_code} - {e.message}]")
		return False
	except BinanceOrderMinPriceException as e:
		BU.errPrint(f"Erro create_oco_order BinanceOrderMinPriceException: [{e.status_code} - {e.message}]")
		return False
	except BinanceOrderMinTotalException as e:
		BU.errPrint(f"Erro create_oco_order BinanceOrderMinTotalException: [{e.status_code} - {e.message}]")
		return False
	except BinanceOrderUnknownSymbolException as e:
		BU.errPrint(f"Erro create_oco_order BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]")
		return False
	except BinanceOrderInactiveSymbolException as e:
		BU.errPrint(f"Erro create_oco_order BinanceOrderInactiveSymbolException: [{e.status_code} - {e.message}]")
		return False
	except Expcetion as e:
		BU.errPrint(f"Erro create_oco_order generic exception: {e}")
		return False

	printPlacedOrder(order)

	return True

def orderSpot(client, symbOrd = '', qtdOrd = 0, prcOrd = 0.0, sideOrd = 0, typeOrd = 0) -> bool:

	if BU.askConfirmation() == False:
		return False

	# TESTING
	global LOCK
	if LOCK == True:
		BU.errPrint("PROGRAM LOCKED BY SECURITY!")
		return False

	try:

		if getTestOrder() == True:
			BU.errPrint("TESTING ORDER")
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
		BU.errPrint(f"Erro order_limit_buy BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except BinanceAPIException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceOrderException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceOrderException: [{e.status_code} - {e.message}]")
		return False
	except BinanceOrderMinAmountException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceOrderMinAmountException: [{e.status_code} - {e.message}]")
		return False
	except BinanceOrderMinPriceException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceOrderMinPriceException: [{e.status_code} - {e.message}]")
		return False
	except BinanceOrderMinTotalException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceOrderMinTotalException: [{e.status_code} - {e.message}]")
		return False
	except BinanceOrderUnknownSymbolException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]")
		return False
	except BinanceOrderInactiveSymbolException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceOrderInactiveSymbolException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro order_limit_buy generic exception: {e}")
		return False

	printPlacedOrder(order)

	return True

# ---------------------------------------------------

def buyOCOOrder(client, symb = '', qtd = 0, prc = 0.0, stopprice = 0.0, limit = 0.0) -> bool:
	BU.errPrint("NOT IMPLEMENTED")

def sellOCOOrder(client, symb = '', qtd = 0, prc = 0.0, stopprice = 0.0, limit = 0.0) -> bool:
	BU.errPrint("NOT IMPLEMENTED")

# ---------------------------------------------------

def orderMargin(client, symbOrd = '', sideOrd = 0, typeOrd = 0, qtdOrd = 0, prcOrd = 0.0, prcStop = 0.0, limit = 0.0) -> bool:
	BU.errPrint(f"MARGIN Order {typeOrd}")

	if BU.getExportXLS() == True:
		BU.errPrint("Symbol\tSide\tQuantity\tPrice\tStop Price\tLimit OCO\tType")
		BU.errPrint(f"{symbOrd}\t{sideOrd}\t{qtdOrd}\t{prcOrd}\t{prcStop}\t{limit}\t{typeOrd}\t]")
	else:
		BU.errPrint(f"Symbol....: [{symbOrd}]")
		BU.errPrint(f"Side......: [{sideOrd}]")
		BU.errPrint(f"Quantity..: [{qtdOrd}]")
		BU.errPrint(f"Price.....: [{prcOrd}]")
		BU.errPrint(f"Stop Price: [{prcStop}]")
		BU.errPrint(f"Limit OCO.: [{limit}]")
		BU.errPrint(f"Type......: [{typeOrd}]")

	if BU.askConfirmation() == False:
		return False

	# TESTING
	global LOCK
	if LOCK == True:
		BU.errPrint("PROGRAM LOCKED BY SECURITY!")
		return False

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
		BU.errPrint(f"Erro create_margin_order BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except BinanceAPIException as e:
		BU.errPrint(f"Erro create_margin_order BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceOrderException as e:
		BU.errPrint(f"Erro create_margin_order BinanceOrderException: [{e.status_code} - {e.message}]")
		return False
	except BinanceOrderMinAmountException as e:
		BU.errPrint(f"Erro create_margin_order BinanceOrderMinAmountException: [{e.status_code} - {e.message}]")
		return False
	except BinanceOrderMinPriceException as e:
		BU.errPrint(f"Erro create_margin_order BinanceOrderMinPriceException: [{e.status_code} - {e.message}]")
		return False
	except BinanceOrderMinTotalException as e:
		BU.errPrint(f"Erro create_margin_order BinanceOrderMinTotalException: [{e.status_code} - {e.message}]")
		return False
	except BinanceOrderUnknownSymbolException as e:
		BU.errPrint(f"Erro create_margin_order BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]")
		return False
	except BinanceOrderInactiveSymbolException as e:
		BU.errPrint(f"Erro create_margin_order BinanceOrderInactiveSymbolException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro create_margin_order generic exception: {e}")
		return False

	BP.printMarginOrder(order)
	return True
