#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota
# andre.scota@gmail.com
# MIT license

import binanceUtil as BU
import binancePrint as BP

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceWithdrawException, BinanceRequestException

def sellMarketOrder(client, symb, qtd):
	print("SPOT Sell Market order")
	print(f"Symbol..: [{symb}]")
	print(f"Quantity: [{qtd}]")

	if BU.askConfirmation() == False:
		return

	# TESTING
	return

	try:
		order = client.order_market_sell(symbol = symb, quantity = qtd) 
	except BinanceRequestException as e:
		BU.errPrint(f"Erro order_market_sell BinanceRequestException: [{e.status_code} - {e.message}]")
	except BinanceAPIException as e:
		BU.errPrint(f"Erro order_market_sell BinanceAPIException: [{e.status_code} - {e.message}]")
	except BinanceOrderException as e:
		BU.errPrint(f"Erro order_market_sell BinanceOrderException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinAmountException as e:
		BU.errPrint(f"Erro order_market_sell BinanceOrderMinAmountException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinPriceException as e:
		BU.errPrint(f"Erro order_market_sell BinanceOrderMinPriceException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinTotalException as e:
		BU.errPrint(f"Erro order_market_sell BinanceOrderMinTotalException: [{e.status_code} - {e.message}]")
	except BinanceOrderUnknownSymbolException as e:
		BU.errPrint(f"Erro order_market_sell BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]")
	except BinanceOrderInactiveSymbolException as e:
		BU.errPrint(f"Erro order_market_sell BinanceOrderInactiveSymbolException: [{e.status_code} - {e.message}]")
	else:
		BP.print_OM_Sell_PlacedOrder(order)

def buyMarketOrder(client, symb, qtd):
	print("SPOT Buy order")
	print(f"Symbol..: [{symb}]")
	print(f"Quantity: [{qtd}]")

	if BU.askConfirmation() == False:
		return

	# TESTING
	return

	try:
		order = client.order_market_buy(symbol=symb, quantity=qtd) 
	except BinanceRequestException as e:
		BU.errPrint(f"Erro order_market_buy BinanceRequestException: [{e.status_code} - {e.message}]")
	except BinanceAPIException as e:
		BU.errPrint(f"Erro order_market_buy BinanceAPIException: [{e.status_code} - {e.message}]")
	except BinanceOrderException as e:
		BU.errPrint(f"Erro order_market_buy BinanceOrderException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinAmountException as e:
		BU.errPrint(f"Erro order_market_buy BinanceOrderMinAmountException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinPriceException as e:
		BU.errPrint(f"Erro order_market_buy BinanceOrderMinPriceException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinTotalException as e:
		BU.errPrint(f"Erro order_market_buy BinanceOrderMinTotalException: [{e.status_code} - {e.message}]")
	except BinanceOrderUnknownSymbolException as e:
		BU.errPrint(f"Erro order_market_buy BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]")
	except BinanceOrderInactiveSymbolException as e:
		BU.errPrint(f"Erro order_market_buy BinanceOrderInactiveSymbolException: [{e.status_code} - {e.message}]")
	else:
		BP.print_OM_Buy_PlacedOrder(order)

# ---------------------------------------------------

def sellStopOrder(client, symb, qtd, prc, stopprice):
	print(f"SPOT Stop (OCO) Sell order")
	print(f"Symbol....: [{symb}]")
	print(f"Quantity..: [{qtd}]")
	print(f"Price.....: [{prc}]")
	print(f"Stop Price: [{stopprice}]")

	if BU.askConfirmation() == False:
		return

	# TESTING
	return

	try:
		order = client.create_oco_order(symbol = {symb}, side = SIDE_SELL, stopLimitTimeInForce = TIME_IN_FORCE_GTC,
		                                quantity = {qtd}, stopPrice = {stopprice}, price = {prc})
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
		BP.print_OCO_Sell_PlacedOrder(order)

# ---------------------------------------------------

def sellLimitOrder(client, symb, qtd, prc):
	print("SPOT Sell Limit order")
	print(f"Symbol..: [{symb}]")
	print(f"Quantity: [{qtd}]")
	print(f"Price...: [{prc}]")

	if BU.askConfirmation() == False:
		return

	# TESTING
	return

	try:
		order = client.order_limit_sell(symbol = symb, quantity = qtd, price = prc)
	except BinanceRequestException as e:
		BU.errPrint(f"Erro order_limit_sell BinanceRequestException: [{e.status_code} - {e.message}]")
	except BinanceAPIException as e:
		BU.errPrint(f"Erro order_limit_sell BinanceAPIException: [{e.status_code} - {e.message}]")
	except BinanceOrderException as e:
		BU.errPrint(f"Erro order_limit_sell BinanceOrderException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinAmountException as e:
		BU.errPrint(f"Erro order_limit_sell BinanceOrderMinAmountException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinPriceException as e:
		BU.errPrint(f"Erro order_limit_sell BinanceOrderMinPriceException: [{e.status_code} - {e.message}]")
	except BinanceOrderMinTotalException as e:
		BU.errPrint(f"Erro order_limit_sell BinanceOrderMinTotalException: [{e.status_code} - {e.message}]")
	except BinanceOrderUnknownSymbolException as e:
		BU.errPrint(f"Erro order_limit_sell BinanceOrderUnknownSymbolException: [{e.status_code} - {e.message}]")
	except BinanceOrderInactiveSymbolException as e:
		BU.errPrint(f"Erro order_limit_sell BinanceOrderInactiveSymbolException: [{e.status_code} - {e.message}]")
	else:
		BP.print_LO_Sell_PlacedOrder(order)

# ---------------------------------------------------

def buyStopOrder(client, symb, qtd, prc):
	print(f"SPOT Stop (OCO) Buy order")
	print(f"Symbol....: [{symb}]")
	print(f"Quantity..: [{qtd}]")
	print(f"Price.....: [{prc}]")
	print(f"Stop Price: [{stopprice}]")

	if BU.askConfirmation() == False:
		return

	# TESTING
	return

	try:
		order = client.create_oco_order(symbol = {symb}, side = SIDE_BUY, stopLimitTimeInForce = TIME_IN_FORCE_GTC,
		                                quantity = {qtd}, stopPrice = {stopprice}, price = {prc})
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
		BP.print_OCO_Buy_PlacedOrder(order)

# ---------------------------------------------------

def orderMargin(symbOrd: str, sideOrd, typeOrd, qtdOrd = 0, prcOrd = 0.0):

	print("MARGIN Order")
	print(f"Symbol..: [{symbOrd}]")
	print(f"Side....: [{sideOrd}]")
	print(f"Quantity: [{qtdOrd}]")
	print(f"Price...: [{priceOrd}]")
	print(f"Type....: [{typeOrd}]")

	if BU.askConfirmation() == False:
		return

	# TESTING
	return

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

# ---------------------------------------------------

def buyLimitOrder(client, symb, qtd, prc):
	print("SPOT Buy Limit Order")
	print(f"Symbol..: [{symb}]")
	print(f"Quantity: [{qtd}]")
	print(f"Price...: [{prc}]")

	if BU.askConfirmation() == False:
		return

	# TESTING
	return

	try:
#order = client.order_limit_buy(symbol=symb, quantity=qtd, price=prc)
		order = create_order(symbol = symb,
		                     quantity = qtd,
		                     price = prc,
		                     side = Client.SIDE_BUY,
		                     type = Client.ORDER_TYPE_LIMIT,
		                     timeInForce = Client.TIME_IN_FORCE_GTC,
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
		BP.print_OL_Buy_PlacedOrder(order)
