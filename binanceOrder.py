#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota
# andre.scota@gmail.com
# MIT license

import binanceUtil as BU
import binancePrint as BP

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceWithdrawException, BinanceRequestException

testOrder = False
LOCK = True

def setTestOrder(o: bool):
	global testOrder
	testOrder = o

def getTestOrder() -> bool:
	global testOrder
	return testOrder

# ---------------------------------------------------

def binancePlaceSPOTOCOOrder(symbOrd = '', qtdOrd = 0, prcOrd = 0.0, prcStopOrd = 0.0, prcStopLimitOrd = 0.0, sideOrd = 0):

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
		                                stopLimitTimeInForce = TIME_IN_FORCE_GTC,
		                                newOrderRespType     = Client.ORDER_RESP_TYPE_FULL)

	except BinanceRequestException as e:
		BU.errPrint(f"Erro create_oco_order BinanceRequestException: [{e.status_code} - {e.message}]")
	except BinanceAPIException as e:
		BU.errPrint(f"Erro create_oco_order BinanceAPIException: [{e.status_code} - {e.message}]")
	except BinanceOrderException as e:
		BU.errPrint(f"Erro create_oco_order BinanceOrderException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinAmountException as e:
		BU.errPrint(f"Erro create_oco_order BinanceOrderMinAmountException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinPriceException as e:
		BU.errPrint(f"Erro create_oco_order BinanceOrderMinPriceException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinTotalException as e:
		BU.errPrint(f"Erro create_oco_order BinanceOrderMinTotalException: [{e.status_code} - {e.message}]")
	except BinanceOrderUnknownSymbolException as e:
		BU.errPrint(f"Erro create_oco_order BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]")
	except BinanceOrderInactiveSymbolException as e:
		BU.errPrint(f"Erro create_oco_order BinanceRequestException: [{e.status_code} - {e.message}]")
	else:
		return order
	finally:
		raise

def binancePlaceSPOTOrder(symbOrd = '', qtdOrd = 0, prcOrd = 0.0, sideOrd = 0, typeOrd = 0):

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
			order = create_test_order(symbol      = symbOrd,
			                          side        = sideOrd,
			                          type        = typeOrd,
			                          timeInForce = Client.TIME_IN_FORCE_GTC,
			                          quantity    = qtdOrd,
			                          price       = prcOrd)
		else:
			order = create_order(symbol           = symbOrd,
			                     quantity         = qtdOrd,
			                     price            = prcOrd,
			                     side             = sideOrd,
			                     type             = typeOrd,
			                     timeInForce      = Client.TIME_IN_FORCE_GTC,
			                     newOrderRespType = Client.ORDER_RESP_TYPE_FULL)

	except BinanceRequestException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceRequestException: [{e.status_code} - {e.message}]")
	except BinanceAPIException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceAPIException: [{e.status_code} - {e.message}]")
	except BinanceOrderException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceOrderException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinAmountException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceOrderMinAmountException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinPriceException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceOrderMinPriceException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinTotalException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceOrderMinTotalException: [{e.status_code} - {e.message}]")
	except BinanceOrderUnknownSymbolException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]")
	except BinanceOrderInactiveSymbolException as e:
		BU.errPrint(f"Erro order_limit_buy BinanceOrderInactiveSymbolException: [{e.status_code} - {e.message}]")
	else:
		return order
	finally:
		raise

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
		order = binancePlaceSPOTOrder(symb, qtd, 0.0, Client.SIDE_SELL, Client.ORDER_TYPE_MARKET)
	except:
		return False

	if order is not None:
		BP.print_OM_Sell_PlacedOrder(order)

	return True

def buyMarketOrder(client, symb = '', qtd = 0) -> bool:
	print("SPOT Buy order")

	if BU.getExportXLS() == True:
		print("Symbol\tQuantity")
		print(f"{symb}\t{qtd}")
	else:
		print(f"Symbol..: [{symb}]")
		print(f"Quantity: [{qtd}]")

	try:
		order = binancePlaceSPOTOrder(symb, qtd, 0.0, Client.SIDE_BUY, Client.ORDER_TYPE_MARKET)
	except:
		return False

	if order is not None:
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
		order = binancePlaceSPOTOrder(symb, qtd, prc, Client.SIDE_SELL, Client.ORDER_TYPE_LIMIT)
	except:
		return False

	if order is not None:
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
		order = binancePlaceSPOTOrder(symb, qtd, prc, Client.SIDE_BUY, Client.ORDER_TYPE_LIMIT)
	except:
		return False

	if order is not None:
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
		order = binancePlaceSPOTOCOOrder(symbOrd         = symb,
		                                 qtdOrd          = qtd,
		                                 prcOrd          = prc,
		                                 prcStopOrd      = stopprice,
		                                 prcStopLimitOrd = 0.0,
		                                 sideOrd         = Client.SIDE_SELL)

	except:
		return False

	if order is not None:
		BP.print_OCO_Sell_PlacedOrder(order)

	return True

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
		order = binancePlaceSPOTOCOOrder(symbOrd         = symb,
		                                 qtdOrd          = qtd,
		                                 prcOrd          = prc,
		                                 prcStopOrd      = stopprice,
		                                 prcStopLimitOrd = 0.0,
		                                 sideOrd         = Client.SIDE_BUY)

	except:
		return False

	if order is not None:
		BP.print_OCO_Buy_PlacedOrder(order)

	return True

# ---------------------------------------------------

def orderMargin(symbOrd = '', sideOrd = 0, typeOrd = 0, qtdOrd = 0, prcOrd = 0.0):
	print("MARGIN Order")

	if BU.getExportXLS() == True:
		print("Symbol\tSide\tQuantity\tPrice\tType")
		print(f"{symbOrd}\t{sideOrd}\t{qtdOrd}\t{priceOrd}\t{typeOrd}]")
	else:
		print(f"Symbol..: [{symbOrd}]")
		print(f"Side....: [{sideOrd}]")
		print(f"Quantity: [{qtdOrd}]")
		print(f"Price...: [{priceOrd}]")
		print(f"Type....: [{typeOrd}]")

	if BU.askConfirmation() == False:
		return None

	# TESTING
	global LOCK
	if LOCK == True:
		print("PROGRAM LOCKED BY SECURITY!")
		return None

	try:
		order = client.create_margin_order(symbol      = symbOrd,
		                                   side        = BU.binanceSide(sideOrd),
		                                   type        = BU.binanceOrderType(typeOrd),
		                                   timeInForce = TIME_IN_FORCE_GTC,
		                                   quantity    = qtdOrd,
		                                   price       = prcOrd)

	except BinanceRequestException as e:
		BU.errPrint(f"Erro create_margin_order BinanceRequestException: [{e.status_code} - {e.message}]")
	except BinanceAPIException as e:
		BU.errPrint(f"Erro create_margin_order BinanceAPIException: [{e.status_code} - {e.message}]")
	except BinanceOrderException as e:
		BU.errPrint(f"Erro create_margin_order BinanceOrderException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinAmountException as e:
		BU.errPrint(f"Erro create_margin_order BinanceOrderMinAmountException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinPriceException as e:
		BU.errPrint(f"Erro create_margin_order BinanceOrderMinPriceException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinTotalException as e:
		BU.errPrint(f"Erro create_margin_order BinanceOrderMinTotalException: [{e.status_code} - {e.message}]")
	except BinanceOrderUnknownSymbolException as e:
		BU.errPrint(f"Erro create_margin_order BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]")
	except BinanceOrderInactiveSymbolException as e:
		BU.errPrint(f"Erro create_margin_order BinanceOrderInactiveSymbolException: [{e.status_code} - {e.message}]")
	else:
		BP.print_Margin_Order(order)