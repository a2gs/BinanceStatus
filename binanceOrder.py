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
	print(f"Cancel SPOT Order Id [{ordrid}] with Symbol [{symbOrd}]")

	if BU.askConfirmation() == False:
		return True

	# TESTING
	global LOCK
	if LOCK == True:
		print("PROGRAM LOCKED BY SECURITY!")
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

	print("Cancellation return")
	if BU.getExportXLS() == True:
		print("Symbol\tOriginal Client Order Id\tOrder Id\tOrder List Id (OCO info)\tClient Order Id\tPrice\tOriginal Qtd\tExecuted Qty\tCummulative Quote Qty\tStatus\tTime In Force\tType\tSide")
		print(f"{cancOrd['symbol']}\t{cancOrd['origClientOrderId']}\t{cancOrd['orderId']}\t{cancOrd['orderListId']}\t{cancOrd['clientOrderId']}\t{cancOrd['price']}\t{cancOrd['origQty']}\t{cancOrd['executedQty']}\t{cancOrd['cummulativeQuoteQty']}\t{cancOrd['status']}\t{cancOrd['timeInForce']}\t{cancOrd['timeInForce']}\t{cancOrd['type']}\t{cancOrd['side']}")

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

	return True	

def cancel_a_margin_order(client, symbOrd = '', ordrid = 0) -> bool:
	print(f"Cancel Margin Order Id [{ordrid}] with Symbol [{symbOrd}]")

	if BU.askConfirmation() == False:
		return True

	# TESTING
	global LOCK
	if LOCK == True:
		print("PROGRAM LOCKED BY SECURITY!")
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

	print("Cancellation return")

	if BU.getExportXLS() == True:
		print("Symbol\tOriginal Client Order Id\tOrder Id\tClient Order Id\tPrice\tOriginal Qtd\tExecuted Qty\tCummulative Quote Qty\tStatus\tTime In Force\tType\tSide")
		print(f"{cancOrd['symbol']}\t{cancOrd['origClientOrderId']}\t{cancOrd['orderId']}\t{cancOrd['clientOrderId']}\t{cancOrd['price']}\t{cancOrd['origQty']}\t{cancOrd['executedQty']}\t{cancOrd['cummulativeQuoteQty']}\t{cancOrd['status']}\t{cancOrd['timeInForce']}\t{cancOrd['timeInForce']}\t{cancOrd['type']}\t{cancOrd['side']}")

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

	return True	

# ---------------------------------------------------

def binancePlaceSPOTOCOOrder(client, symbOrd = '', qtdOrd = 0, prcOrd = 0.0, prcStopOrd = 0.0, prcStopLimitOrd = 0.0, sideOrd = 0):

	if BU.askConfirmation() == False:
		return None

	# TESTING
	global LOCK
	if LOCK == True:
		print("PROGRAM LOCKED BY SECURITY!")
		return None

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
		return None
	except BinanceAPIException as e:
		BU.errPrint(f"Erro create_oco_order BinanceAPIException: [{e.status_code} - {e.message}]")
		return None
	except BinanceOrderException as e:
		BU.errPrint(f"Erro create_oco_order BinanceOrderException: [{e.status_code} - {e.message}]")
		return None
	except BinanceOrderMinAmountException as e:
		BU.errPrint(f"Erro create_oco_order BinanceOrderMinAmountException: [{e.status_code} - {e.message}]")
		return None
	except BinanceOrderMinPriceException as e:
		BU.errPrint(f"Erro create_oco_order BinanceOrderMinPriceException: [{e.status_code} - {e.message}]")
		return None
	except BinanceOrderMinTotalException as e:
		BU.errPrint(f"Erro create_oco_order BinanceOrderMinTotalException: [{e.status_code} - {e.message}]")
		return None
	except BinanceOrderUnknownSymbolException as e:
		BU.errPrint(f"Erro create_oco_order BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]")
		return None
	except BinanceOrderInactiveSymbolException as e:
		BU.errPrint(f"Erro create_oco_order BinanceOrderInactiveSymbolException: [{e.status_code} - {e.message}]")
		return None
	except Expcetion as e:
		BU.errPrint(f"Erro create_oco_order generic exception: {e}")
		return None

	return order

def binancePlaceSPOTOrder(client, symbOrd = '', qtdOrd = 0, prcOrd = 0.0, sideOrd = 0, typeOrd = 0):

	if BU.askConfirmation() == False:
		return None

	# TESTING
	global LOCK
	if LOCK == True:
		print("PROGRAM LOCKED BY SECURITY!")
		return None

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
		BU.errPrint(f"Erro order_limit_buy BinanceRequestException: [{e.status_code} - {e.message}]")
		return None
	except BinanceAPIException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceAPIException: [{e.status_code} - {e.message}]")
		return None
	except BinanceOrderException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceOrderException: [{e.status_code} - {e.message}]")
		return None
	except BinanceOrderMinAmountException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceOrderMinAmountException: [{e.status_code} - {e.message}]")
		return None
	except BinanceOrderMinPriceException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceOrderMinPriceException: [{e.status_code} - {e.message}]")
		return None
	except BinanceOrderMinTotalException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceOrderMinTotalException: [{e.status_code} - {e.message}]")
		return None
	except BinanceOrderUnknownSymbolException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]")
		return None
	except BinanceOrderInactiveSymbolException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceOrderInactiveSymbolException: [{e.status_code} - {e.message}]")
		return None
	except Exception as e:
		BU.errPrint(f"Erro order_limit_buy generic exception: {e}")
		return None

	return order

# ---------------------------------------------------

def sellMarketOrder(client, symb = '', qtd = 0) -> bool:
	print("SPOT Sell Market order")

	if BU.getExportXLS() == True:
		print("Symbol\tQuantity")
		print(f"{symb}\t{qtd}")
	else:
		print(f"Symbol..: [{symb}]")
		print(f"Quantity: [{qtd}]")

	try:
		order = binancePlaceSPOTOrder(client, symb, qtd, 0.0, Client.SIDE_SELL, Client.ORDER_TYPE_MARKET)
	except Exception as e:
		BU.errPrint(f"Erro binancePlaceSPOTOrder SELL MARKET(): {e}")
		return False

	if order is None:
		return False

	BP.print_OM_Sell_PlacedOrder(order)

	return True

def buyMarketOrder(client, symb = '', qtd = 0) -> bool:
	print("SPOT Buy Market order")

	if BU.getExportXLS() == True:
		print("Symbol\tQuantity")
		print(f"{symb}\t{qtd}")
	else:
		print(f"Symbol..: [{symb}]")
		print(f"Quantity: [{qtd}]")

	try:
		order = binancePlaceSPOTOrder(client, symb, qtd, 0.0, Client.SIDE_BUY, Client.ORDER_TYPE_MARKET)
	except Exception as e:
		BU.errPrint(f"Erro binancePlaceSPOTOrder BUY MARKET(): {e}")
		return False

	if order is None:
		return False

	BP.print_OM_Buy_PlacedOrder(order)

	return True

# ---------------------------------------------------

def sellLimitOrder(client, symb = '', qtd = 0, prc = 0.0) -> bool:
	print("SPOT Sell Limit order")

	if BU.getExportXLS() == True:
		print("Symbol\tQuantity\tPrice")
		print(f"{symb}\t{qtd}\t{prc}")
	else:
		print(f"Symbol..: [{symb}]")
		print(f"Quantity: [{qtd}]")
		print(f"Price...: [{prc}]")

	try:
		order = binancePlaceSPOTOrder(client, symb, qtd, prc, Client.SIDE_SELL, Client.ORDER_TYPE_LIMIT)
	except Exception as e:
		BU.errPrint(f"Erro binancePlaceSPOTOrder SELL LIMIT(): {e}")
		return False

	if order is None:
		return False

	BP.print_LO_Sell_PlacedOrder(order)

	return True

def buyLimitOrder(client, symb = '', qtd = 0, prc = 0.0) -> bool:
	print("SPOT Buy Limit Order")

	if BU.getExportXLS() == True:
		print("Symbol\tQuantity\tPrice")
		print(f"{symb}\t{qtd}\t{prc}")
	else:
		print(f"Symbol..: [{symb}]")
		print(f"Quantity: [{qtd}]")
		print(f"Price...: [{prc}]")

	try:
		order = binancePlaceSPOTOrder(client, symb, qtd, prc, Client.SIDE_BUY, Client.ORDER_TYPE_LIMIT)
	except Exception as e:
		BU.errPrint(f"Erro binancePlaceSPOTOrder BUY LIMIT(): {e}")
		return False

	if order is None:
		return False

	BP.print_OL_Buy_PlacedOrder(order)

	return True

# ---------------------------------------------------

def sellStopOrder(client, symb = '', qtd = 0, prc = 0.0, stopprice = 0.0) -> bool:
	print("SPOT Stop (OCO) Sell order")

	if BU.getExportXLS() == True:
		print("Symbol\tQuantity\tPrice\tStop Price")
		print(f"{symb}\t{qtd}\t{prc}\t{stopprice}]")
	else:
		print(f"Symbol....: [{symb}]")
		print(f"Quantity..: [{qtd}]")
		print(f"Price.....: [{prc}]")
		print(f"Stop Price: [{stopprice}]")

	try:
		order = binancePlaceSPOTOCOOrder(client,
		                                 symbOrd         = symb,
		                                 qtdOrd          = qtd,
		                                 prcOrd          = prc,
		                                 prcStopOrd      = stopprice,
		                                 prcStopLimitOrd = 0.0,
		                                 sideOrd         = Client.SIDE_SELL)

	except Exception as e:
		BU.errPrint(f"Erro binancePlaceSPOTOCOOrder SELL(): {e}")
		return False

	if order is None:
		return False

	BP.print_OCO_Sell_PlacedOrder(order)

	return True

def buyOCOOrder(client, symb = '', qtd = 0, prc = 0.0, stopprice = 0.0, limit = 0.0) -> bool:
	print("NOT IMPLEMENTED")

def sellOCOOrder(client, symb = '', qtd = 0, prc = 0.0, stopprice = 0.0, limit = 0.0) -> bool:
	print("NOT IMPLEMENTED")

def buyStopOrder(client, symb = '', qtd = 0, prc = 0.0, stopprice = 0.0) -> bool:
	print("SPOT Stop (OCO) Buy order")

	if BU.getExportXLS() == True:
		print("Symbol\tQuantity\tPrice\tStop Price")
		print(f"{symb}\t{qtd}\t{prc}\t{stopprice}")
	else:
		print(f"Symbol....: [{symb}]")
		print(f"Quantity..: [{qtd}]")
		print(f"Price.....: [{prc}]")
		print(f"Stop Price: [{stopprice}]")

	try:
		order = binancePlaceSPOTOCOOrder(client,
		                                 symbOrd         = symb,
		                                 qtdOrd          = qtd,
		                                 prcOrd          = prc,
		                                 prcStopOrd      = stopprice,
		                                 prcStopLimitOrd = 0.0,
		                                 sideOrd         = Client.SIDE_BUY)

	except Exception as e:
		BU.errPrint(f"Erro binancePlaceSPOTOCOOrder BUY(): {e}")
		return False

	if order is None:
		return False

	BP.print_OCO_Buy_PlacedOrder(order)

	return True

# ---------------------------------------------------

def orderMargin(client, symbOrd = '', sideOrd = 0, typeOrd = 0, qtdOrd = 0, prcOrd = 0.0, prcStop = 0.0, limit = 0.0) -> bool:
	print(f"MARGIN Order {typeOrd}")

	if BU.getExportXLS() == True:
		print("Symbol\tSide\tQuantity\tPrice\tStop Price\tType")
		print(f"{symbOrd}\t{sideOrd}\t{qtdOrd}\t{prcOrd}\t{prcStop}{typeOrd}\t]")
	else:
		print(f"Symbol....: [{symbOrd}]")
		print(f"Side......: [{sideOrd}]")
		print(f"Quantity..: [{qtdOrd}]")
		print(f"Price.....: [{prcOrd}]")
		print(f"Stop Price: [{prcStop}]")
		print(f"Type......: [{typeOrd}]")

	if BU.askConfirmation() == False:
		return False

	# TESTING
	global LOCK
	if LOCK == True:
		print("PROGRAM LOCKED BY SECURITY!")
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

	BP.print_Margin_Order(order)
	return True
