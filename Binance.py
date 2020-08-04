#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota
# andre.scota@gmail.com
# MIT license

import os, sys

import binancePrint as BP
import binanceUtil  as BU
import binanceOrder as BO

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceWithdrawException, BinanceRequestException

# ---------------------------------------------------

def binanceInfo(client) -> bool:

	try:
		sst = client.get_system_status()
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_system_status() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False

	try:
		st = client.get_server_time()
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_server_time() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_server_time() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_server_time(): {e}")
		return False

	if BU.getExportXLS() == True:
		BU.errPrint("Server Status")
		BP.printSystemStatusXLS(sst)

		BU.errPrint("\nTime")
		BP.printServerTimeXLS(st)

	else:
		BU.errPrint("Server Status:")
		BP.printSystemStatus(sst)

		BU.errPrint("")
		BP.printServerTime(st)

	return True

def accountInformation(client) -> bool:

	BU.errPrint("Spot accoutn information:")
	try:
		acc = client.get_account(recvWindow = BU.getRecvWindow())
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_account() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_account() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_account(): {e}")
		return False

	try:
		accStatus = client.get_account_status(recvWindow = BU.getRecvWindow())
	except BinanceWithdrawException as e:
		BU.errPrint(f"Erro at client.get_account_status() BinanceWithdrawException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_account_status(): {e}")
		return False

	if BU.getExportXLS() == True:
		BU.errPrint(f"Can trade\t{acc['canTrade']}\nCan withdraw\t{acc['canWithdraw']}\nCan deposit\t{acc['canDeposit']}\nAccount type\t{acc['accountType']}\nCommissions Maker\t{acc['makerCommission']}\nCommissions Taker\t{acc['takerCommission']}\nCommissions Buyer\t{acc['buyerCommission']}\nCommissions Seller\t{acc['sellerCommission']}\n")
		BU.errPrint(f"Account status detail\t{accStatus['msg']}\nSuccess\t{accStatus['success']}\n")
	else:
		BU.errPrint(f"Can trade............? [{acc['canTrade']}]")
		BU.errPrint(f"Can withdraw.........? [{acc['canWithdraw']}]")
		BU.errPrint(f"Can deposit..........? [{acc['canDeposit']}]")
		BU.errPrint(f"Account type.........: [{acc['accountType']}]")
		BU.errPrint(f"Account status detail: [{accStatus['msg']}] Success: [{accStatus['success']}]")
		BU.errPrint(f"Commissions..........: Maker: [{acc['makerCommission']}] | Taker: [{acc['takerCommission']}] | Buyer: [{acc['buyerCommission']}] | Seller: [{acc['sellerCommission']}]")

	if len(acc['balances']) != 0:
		if BU.getExportXLS() == True:
			BP.printAccountXLSHEADER()
			[BP.printAccountXLS(n) for n in acc['balances'] if float(n['free']) != 0.0 or float(n['locked']) != 0.0]
		else:
			[BP.printAccount(n) for n in acc['balances'] if float(n['free']) != 0.0 or float(n['locked']) != 0.0]

	BU.errPrint("\nMargin accoutn information:")
	try:
		marginInfo = client.get_margin_account(recvWindow = BU.getRecvWindow())
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_margin_account() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_margin_account() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_margin_account(): {e}")
		return False

	cleanedMarginAssets = [n for n in marginInfo['userAssets'] if float(n['netAsset']) != 0.0]

	if BU.getExportXLS() == True:
		BU.errPrint("Margin level\tTotal asset of BTC\tTotal liability of BTC\tTotal Net asset of BTC\tTrade enabled")
		BU.errPrint(f"{marginInfo['marginLevel']}\t{marginInfo['totalAssetOfBtc']}\t{marginInfo['totalLiabilityOfBtc']}\t{marginInfo['totalNetAssetOfBtc']}\t{marginInfo['tradeEnabled']}\n")

		BU.errPrint('Borrowed assets:')
		BP.printMarginAssetsXLSHEADER()
		[BP.printMarginAssetsXLS(n) for n in cleanedMarginAssets]
	else:
		BU.errPrint(f"Borrow Enabled........? [{marginInfo['borrowEnabled']}]")
		BU.errPrint(f"Trade enabled.........? [{marginInfo['tradeEnabled']}]")
		BU.errPrint(f"Level.................: [{marginInfo['marginLevel']}]")
		BU.errPrint(f"Total asset of BTC....: [{marginInfo['totalAssetOfBtc']}]")
		BU.errPrint(f"Total liability of BTC: [{marginInfo['totalLiabilityOfBtc']}]")
		BU.errPrint(f"Total Net asset of BTC: [{marginInfo['totalNetAssetOfBtc']}]\n")

		BU.errPrint('Borrowed assets:')
		[BP.printMarginAssets(n, i) for i, n in enumerate(cleanedMarginAssets, 1)]

	return True

def spotOpenOrders(client) -> bool:

	try:
		openOrders = client.get_open_orders(recvWindow = BU.getRecvWindow())
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_open_orders() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_open_orders() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_open_orders(): {e}")
		return False

	totOpenOrder = len(openOrders)

	if totOpenOrder != 0:

		if BU.getExportXLS() == True:

			BP.printOrderXLSHEADER()
			[BP.printOrderXLS(n) for n in openOrders]

		else:

			if   totOpenOrder == 1: BU.errPrint("Open spot order:")
			elif totOpenOrder <  1: BU.errPrint(f"Open spot orders ({totOpenOrder}):")

			[BP.printOrder(n, i, totOpenOrder) for i, n in enumerate(openOrders, 1)]
	else:
		BU.errPrint("No spot open orders")

	return True

# ---------------------------------------------------

def marginOpenOrders(client) -> bool:

	try:
		openMarginOrders = client.get_open_margin_orders(recvWindow = BU.getRecvWindow())
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_open_margin_orders() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_open_margin_orders() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_open_margin_orders(): {e}")
		return False

	totOpenMarginOrder = len(openMarginOrders)

	if totOpenMarginOrder != 0:

		if BU.getExportXLS() == True:

			BP.printMarginOrderXLSHEADER()
			[BP.printMarginOrderXLS(n) for n in openMarginOrders]

		else:

			if   totOpenMarginOrder == 1: BU.errPrint("Margin open order:")
			elif totOpenMarginOrder <  1: BU.errPrint(f"Margin open orders ({totOpenMarginOrder}):")

			[BP.printMarginOrder(n, i, totOpenMarginOrder) for i, n in enumerate(openMarginOrders, 1)]
	else:
		BU.errPrint('No margin open orders')

	return True

# ---------------------------------------------------

def marginSymbPriceIndex(client, symb = '') -> bool:

	try:
		mp = client.get_margin_price_index(symbol = symb, recvWindow = BU.getRecvWindow())

	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_margin_price_index() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_margin_price_index() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_margin_price_index(): {e}")
		return False

	if BU.getExportXLS() == True:
		BU.errPrint("Symbol\tPrice\tTime")
		BU.errPrint(f"{mp['symbol']}\t{mp['price']}\t{BU.completeMilliTime(mp['calcTime'])}")

	else:
		BU.errPrint(f"Margin symbol price index [{symb}]\n")

		BU.errPrint(f"Price: [{mp['price']}]")
		BU.errPrint(f"Time.: [{BU.completeMilliTime(mp['calcTime'])}]")

	return True

# ---------------------------------------------------

def marginSymbInfo(client, symb = '') -> bool:

	try:
		mi = client.get_margin_symbol(symbol = symb, recvWindow = BU.getRecvWindow())

	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_margin_symbol() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_margin_symbol() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_margin_symbol(): {e}")
		return False

	if BU.getExportXLS() == True:
		BU.errPrint("Symbol\tQuote\tBase\tId\tIs Buy Allowed\tIs Margin Trade\tIs Sell Allowed")
		BU.errPrint(f"{mi['symbol']}\t{mi['quote']}\t{mi['base']}\t{mi['id']}\t{mi['isBuyAllowed']}\t{mi['isMarginTrade']}\t{mi['isSellAllowed']}")

	else:
		BU.errPrint(f"Margin symbol info [{symb}]\n")

		BU.errPrint(f"Symbol.........: [{mi['symbol']}]")
		BU.errPrint(f"Quote..........: [{mi['quote']}]")
		BU.errPrint(f"Base...........: [{mi['base']}]")
		BU.errPrint(f"Id.............: [{mi['id']}]")
		BU.errPrint(f"Is Buy Allowed.: [{mi['isBuyAllowed']}]")
		BU.errPrint(f"Is Margin Trade: [{mi['isMarginTrade']}]")
		BU.errPrint(f"Is Sell Allowed: [{mi['isSellAllowed']}]")

	return True

# ---------------------------------------------------

def marginAsset(client, ass = '') -> bool:

	try:
		mo = client.get_margin_asset(asset = ass, recvWindow = BU.getRecvWindow())

	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_margin_asset() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_margin_asset() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_margin_asset(): {e}")
		return False

	if BU.getExportXLS() == True:
		BU.errPrint("Full Name\tName\tIs Borrowable\tIs Mortgageable\tUser Minimum Borrow\tUser Minimum Repay")
		BU.errPrint(f"{mo['assetFullName']}\t{mo['assetName']}\t{mo['isBorrowable']}\t{mo['isMortgageable']}\t{mo['userMinBorrow']}\t{mo['userMinRepay']}")
	else:
		BU.errPrint(f"Query margin asset [{ass}]")

		BU.errPrint(f"Name...............: [{mo['assetName']}]")
		BU.errPrint(f"Full name..........: [{mo['assetFullName']}]")
		BU.errPrint(f"Is borrowable......? [{mo['isBorrowable']}]")
		BU.errPrint(f"Is mortageable.....? [{mo['isMortgageable']}]")
		BU.errPrint(f"User minimum borrow: [{mo['userMinBorrow']}]")
		BU.errPrint(f"User monimum repay.: [{mo['userMinRepay']}]")

	return True

# ---------------------------------------------------

def marginTrades(client, symb = '', fromordid = '', lim = '1000') -> bool:

	try:
		mt = client.get_margin_trades(symbol = symb, fromId = fromordid, limit = lim, recvWindow = BU.getRecvWindow())

	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_margin_trades() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_margin_trades() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_margin_trades(): {e}")
		return False

	mttot = len(mt)

	if BU.getExportXLS() == True:
		BP.printMarginTradesXLSHEADER()
		[BP.printMarginTradesXLS(n) for n in mt]
	else:
		if fromordid == '':
			BU.errPrint(f"Margin accounts trades [{symb}] (limit: [{lim}]).")
		else:
			BU.errPrint(f"Margin accounts trades from order id [{fromordid}] for symbol [{symb}] (limit: [{lim}]).")

		[BP.printMarginTrades(n, i, mttot) for i, n in enumerate(mt, 1)]

	return True

# ---------------------------------------------------

def allMarginOrders(client, symb = '', ordid = '', lim = '1000') -> bool:

	try:
		mo = client.get_all_margin_orders(symbol = symb, orderId = ordid, limit = lim, recvWindow = BU.getRecvWindow())

	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_all_margin_orders() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_all_margin_orders() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_all_margin_orders(): {e}")
		return False

	motot = len(mo)

	if BU.getExportXLS() == True:
		BP.printTradeAllHistXLSHEADER()
		[BP.printTradeAllHistXLS(n) for n in mo]
	else:
		if ordid == '':
			BU.errPrint(f"All margin accounts orders for symbol [{symb}] (limit: [{lim}]).")
		else:
			BU.errPrint(f"Margin accounts order [{ordid}] for symbol [{symb}] (limit: [{lim}]).")

		[BP.printTradeAllHist(n, i, motot) for i, n in enumerate(mo, 1)]

	return True

# ---------------------------------------------------

def withdrawRequest(client, ass = '', addr = '', amnt = 0) -> bool:

	if BU.getExportXLS() == True:
		BU.errPrint("Asset\tAddress\tAmount")
		BU.errPrint(f"{ass}\t{addr}\t{amnt}")
	else:
		BU.errPrint("Withdraw Request")

		BU.errPrint(f"Asset..: [{ass}]")
		BU.errPrint(f"Address: [{addr}]")
		BU.errPrint(f"Amount.: [{amnt}]")

	if BU.askConfirmation() == False:
		return False

	try:
		withdrawReq = client.withdraw(asset = ass, address = addr, amount = amnt)

	except BinanceRequestException as e:
		BU.errPrint(f"Erro at withdraw BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at withdraw BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceWithdrawException as e:
		BU.errPrint(f"Erro at withdraw BinanceWithdrawException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at withdraw: {e}")
		return False

	if BU.getExportXLS() == True:
		BP.printWithdrawResponseXLSHEADER()
		BP.printWithdrawResponseXLS(withdrawReq)
	else:
		BP.printWithdrawResponse(withdrawReq)

	return True

def withdrawHistory(client, ass = '') -> bool:

	try:
		withdraw = client.get_withdraw_history(asset = ass, recvWindow = BU.getRecvWindow())

	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_withdraw_history() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_withdraw_history() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_withdraw_history(): {e}")
		return False

	if BU.getExportXLS() == True:

		BP.printWithdrawHistoryXLSHEADER()
		[BP.printWithdrawHistoryXLS(n) for n in withdraw['withdrawList']]

	else:

		BU.errPrint("Withdraw History")
		[BP.printWithdrawHistory(n) for n in withdraw['withdrawList']]

	return True

# ---------------------------------------------------

def depositHistory(client, ass = '') -> bool:

	try:
		deposits = client.get_deposit_history(asset = ass, recvWindow = BU.getRecvWindow())

	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_deposit_history() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_deposit_history() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_deposit_history(): {e}")
		return False

	if BU.getExportXLS() == True:

		BP.printDepositHistoryXLSHEADER()
		[BP.printDepositHistoryXLS(n) for n in deposits['depositList']]

	else:

		BU.errPrint(f"Deposit History for [{ass}]")
		[BP.printDepositHistory(n) for n in deposits['depositList']]

	return True

def depositAddress(client, ass) -> bool:

	try:
		depAdd = client.get_deposit_address(asset = ass, recvWindow = BU.getRecvWindow())

	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_deposit_address() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_deposit_address() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_deposit_address(): {e}")
		return False

	if BU.getExportXLS() == True:

		BP.printDepositAddressXLSHEADER()
		BP.printDepositAddressXLS(depAdd)

	else:
		BU.errPrint(f"Deposit Address for [{ass}]")
		BP.printDepositAddress(depAdd)

	return True

# ---------------------------------------------------

def orderStatus(client, symb, ordrId) -> bool:

	try:
		ogs = client.get_order(symbol = symb, orderId = ordrId, recvWindow = BU.getRecvWindow())

	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_order() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_order() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_order(): {e}")
		return False

	if BU.getExportXLS() == True:
		BU.errPrint("Symbol\tOrder Id\tOrder List Id\tClient Order Id\tPrice\tOrig Qty\tExecuted Qty\tCummulative Quote Qty\tStatus\tTime In Force\tType\tSide\tStop Price\tIceberg Qty\tTime\tUpdate Time\tIs Working\tOrig Quote Order Qty")
		BU.errPrint(f"{ogs['symbol']}\t{ogs['orderId']}\t{ogs['orderListId']}\t{ogs['clientOrderId']}\t{ogs['price']}\t{ogs['origQty']}\t{ogs['executedQty']}\t{ogs['cummulativeQuoteQty']}\t{ogs['status']}\t{ogs['timeInForce']}\t{ogs['type']}\t{ogs['side']}\t{ogs['stopPrice']}\t{ogs['icebergQty']}\t{BU.completeMilliTime(ogs['time'])}\t{BU.completeMilliTime(ogs['updateTime'])}\t{ogs['isWorking']}\t{ogs['origQuoteOrderQty']}")

	else:
		BU.errPrint(f"Check an order's id [{ordrId}] and symbol [{symb}] status")

		BU.errPrint(f"Symbol...............: [{ogs['symbol']}]")
		BU.errPrint(f"Order Id.............: [{ogs['orderId']}]")
		BU.errPrint(f"Order List Id........: [{ogs['orderListId']}]")
		BU.errPrint(f"Client Order Id......: [{ogs['clientOrderId']}]")
		BU.errPrint(f"Price................: [{ogs['price']}]")
		BU.errPrint(f"Orig Qty.............: [{ogs['origQty']}]")
		BU.errPrint(f"Executed Qty.........: [{ogs['executedQty']}]")
		BU.errPrint(f"Cummulative Quote Qty: [{ogs['cummulativeQuoteQty']}]")
		BU.errPrint(f"Status...............: [{ogs['status']}]")
		BU.errPrint(f"Time In Force........: [{ogs['timeInForce']}]")
		BU.errPrint(f"Type.................: [{ogs['type']}]")
		BU.errPrint(f"Side.................: [{ogs['side']}]")
		BU.errPrint(f"Stop Price...........: [{ogs['stopPrice']}]")
		BU.errPrint(f"Iceberg Qty..........: [{ogs['icebergQty']}]")
		BU.errPrint(f"Time.................: [{BU.completeMilliTime(ogs['time'])}]")
		BU.errPrint(f"Update Time..........: [{BU.completeMilliTime(ogs['updateTime'])}]")
		BU.errPrint(f"Is Working...........: [{ogs['isWorking']}]")
		BU.errPrint(f"Orig Quote Order Qty.: [{ogs['origQuoteOrderQty']}]")

	return True

# ---------------------------------------------------

def olderTrades(client, ass = '') -> bool:

	try:
		th = client.get_historical_trades(symbol = ass, limit = 500, recvWindow = BU.getRecvWindow())

	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_historical_trades() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_historical_trades() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_historical_trades(): {e}")
		return False

	if BU.getExportXLS() == True:
		BP.printHistoricalTradesXLSHEADER()
		[BP.printHistoricalTradesXLS(n) for n in th]
	else:
		BU.errPrint("500 older trades for [{ass}]")

		thTot = len(th)
		[BP.printHistoricalTrades(n, i, thTot) for i, n in enumerate(th, 1)]

	return True

# ---------------------------------------------------

def subAccountsList(client) -> bool:

	try:
		sal = client.get_sub_account_list(recvWindow = BU.getRecvWindow())
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_sub_account_list() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_sub_account_list() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_sub_account_list(): {e}")
		return False

	totSal = len(sal['subAccounts'])

	if sal['success'] == True and totSal > 0:

		if BU.getExportXLS() == True:
			BP.printsubAccountsListXLSHEADER()
			[BP.printsubAccountsListXLS(n) for n in sal['subAccounts']]
		else:
			BU.errPrint("Sub account(s):")
			[BP.printsubAccountsList(n, i, totSal) for i, n in enumerate(sal['subAccounts'], 1)]
	else:
		BU.errPrint("There are no sub accounts.")

	return True

def subAccountTransferHistory(client, em: str = "") -> bool:

	try:
		sath = client.get_sub_account_transfer_history(email = em, recvWindow = BU.getRecvWindow())
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_sub_account_transfer_history() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_sub_account_transfer_history() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_sub_account_transfer_history(): {e}")
		return False

	if sath['success'] == True:

		if BU.getExportXLS() == True:
			BP.printsubAccountTransferHistoryXLSHEADER()
			[BP.printsubAccountTransferHistoryXLS(n) for n in sath['transfers']]
		else:
			totSath = len(sath['transfers'])
			BU.errPrint("Sub account(s) transfer history:")
			[BP.printsubAccountTransferHistory(n, i, totSath) for i, n in enumerate(sath['transfers'], 1)]
	else:
		BU.errPrint(f"Sub accounts transfer history returned: [{sath['msg']}]")

	return True

def subAccountsAssets(client, em: str = "", symb: str = "") -> bool:

	try:
		saa = client.get_sub_account_assets(email = em, symbol = symb, recvWindow = BU.getRecvWindow())
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_sub_account_assets() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_sub_account_assets() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_sub_account_assets(): {e}")
		return False

	if saa['success'] == True:

		if BU.getExportXLS() == True:
			BP.printsubAccountsAssetsXLSHEADER()
			[BP.printsubAccountsAssetsXLS(n) for n in saa['balances']]
		else:
			BU.errPrint("Sub account(s):")
			totSaa = len(saa['balances'])
			[BP.printsubAccountsAssets(n, i, totSaa) for i, n in enumerate(saa['balances'], 1)]
	else:
		BU.errPrint(f"Sub accounts assets returned: [{saa['msg']}]")

	return True

# ---------------------------------------------------

def accountHistory(client, symb) -> bool:

	try:
		tradeHist = client.get_my_trades(symbol=symb, recvWindow = BU.getRecvWindow())
	except Exception as e:
		BU.errPrint(f"Erro at client.get_my_trades(symbol={symb}): {e}")
		return False

	tradeHistTot = len(tradeHist)

	if BU.getExportXLS() == True:
		BP.printTradeHistoryXLSHEADER()
		[BP.printTradeHistoryXLS(n) for n in tradeHist]
	else:
		BU.errPrint(f"Trade history {symb}:")
		[BP.printTradeHistory(n, i, tradeHistTot) for i, n in enumerate(tradeHist, 1)]

	BU.errPrint(f"All trade history {symb}:")

	try:
		tradeAllHist = client.get_all_orders(symbol=symb, recvWindow = BU.getRecvWindow())
	except Exception as e:
		BU.errPrint(f"Erro at client.get_all_orders(symbol={symb}): {e}")
		return False

	tradeAllHistTot = len(tradeAllHist)

	if BU.getExportXLS() == True:
		BP.printTradeAllHistXLSHEADER()
		[BP.printTradeAllHistXLS(n) for n in tradeAllHist]
	else:
		BU.errPrint(f"Trade history [{symb}]:")
		[BP.printTradeAllHist(n, i, tradeAllHistTot) for i, n in enumerate(tradeAllHist, 1)]

	try:
		allDust = client.get_dust_log(recvWindow = BU.getRecvWindow())
	except BinanceWithdrawException as e:
		BU.errPrint(f"Erro at client.get_dust_log() BinanceWithdrawException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_dust_log(): {e}")
		return False

	allDustTot = len(allDust['results']['rows'])

	if BU.getExportXLS() == True:
		BU.errPrint("============== UNDERCONSTRUCTION ==========================")
	else:
		BU.errPrint("Log of small amounts exchanged for BNB:")
		[BP.printDustTrade(n, i, allDustTot) for i, n in enumerate(allDust['results']['rows'], 1)]

	return True

# ---------------------------------------------------

def accountDetails(client) -> bool:

	try:
		assDet = client.get_asset_details(recvWindow = BU.getRecvWindow())
		tradFee = client.get_trade_fee(recvWindow = BU.getRecvWindow())
	except BinanceWithdrawException as e:
		BU.errPrint(f"Erro get_asset_details and get_trade_fee BinanceWithdrawException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro get_asset_details and get_trade_fee: {e}")
		return False

	if BU.getExportXLS() == True:
		BU.errPrint('Details on Assets')
		BP.printDetailsAssetsXLSHEADER()
		[BP.printDetailsAssetsXLS(n, assDet['assetDetail'][n]) for n in assDet['assetDetail'].keys()]

		BU.errPrint('\nTrade Fee')
		BP.printTradeFeeXLSHEADER()
		[BP.printTradeFeeXLS(n) for n in tradFee['tradeFee']]

	else:
		BU.errPrint('Details on Assets:')
		adTot = len(assDet['assetDetail'])
		[BP.printDetailsAssets(n, assDet['assetDetail'][n], i, adTot) for i, n in enumerate(assDet['assetDetail'].keys(), 1)]

		BU.errPrint('Trade Fee:')
		adTot = len(tradFee['tradeFee'])
		[BP.printTradeFee(n, i, adTot) for i, n in enumerate(tradFee['tradeFee'], 1)]

	return True

# ---------------------------------------------------

def infoSymbol(client, symb, interv, candlesTot) -> bool:

	try:
		sumbPrc = client.get_klines(symbol = symb, interval = BU.binanceInterval(interv), limit = candlesTot, recvWindow = BU.getRecvWindow())
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_klines() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_klines() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_klines(): {e}")
		return False

	if sumbPrc is None:
		return False

	if BU.getExportXLS() == True:
		BP.printInfoSymbolValuesXLSHEADER()
		[BP.printInfoSymbolValuesXLS(n) for n in sumbPrc]
	else:
		BU.errPrint(f"Symbol [{symb}] in interval [{interv}]");
		totsumbPrc = len(sumbPrc)
		[BP.printInfoSymbolValues(n, i, totsumbPrc) for i, n in enumerate(sumbPrc, 1)]

	return True

# ---------------------------------------------------

def listSymbolsRateLimits(client) -> bool:

	try:
		ei = client.get_exchange_info()
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_exchange_info() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_exchange_info() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_exchange_info(): {e}")
		return False

	if BU.getExportXLS() == True:
		BU.errPrint("Rate Limits")
		BP.printListRateLimitXLSHEADER()
		[BP.printListRateLimitXLS(n) for n in ei['rateLimits']]

		BU.errPrint("\nSymbols")
		BP.printListSymbolsXLSHEADER()
		[BP.printListSymbolsXLS(n) for n in ei['symbols']]

	else:
		BU.errPrint("Rate Limits:")
		totei = len(ei['rateLimits'])
		[BP.printListRateLimit(n, i, totei) for i, n in enumerate(ei['rateLimits'], 1)]

		BU.errPrint("Symbols:")
		totei = len(ei['symbols'])
		[BP.printListSymbols(n, i, totei) for i, n in enumerate(ei['symbols'], 1)]

	return True

# ---------------------------------------------------

def transfSpotToMargin(client, ass = '', ap = '0.0') -> bool:
	BU.errPrint(f"Tranfering [{ap}] of [{ass}] from Spot to Margin account")

	try:
		transfer = client.transfer_spot_to_margin(asset = ass, amount = ap)	
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.transfer_spot_to_margin() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.transfer_spot_to_margin() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.transfer_spot_to_margin(): {e}")
		return False

	BU.errPrint("Return Ok. Spot to Margin transaction Id: [{transfer['tranId']}] ")

	return True

def transfMarginToSpot(client, ass = '', ap = '0.0') -> bool:
	BU.errPrint(f"Tranfering [{ap}] of [{ass}] from Margin to Spot account")

	try:
		transfer = client.transfer_margin_to_spot(asset = ass, amount = ap)	
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.transfer_margin_to_spot() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.transfer_margin_to_spot() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.transfer_margin_to_spot(): {e}")
		return False

	BU.errPrint("Return Ok. Margin to Spot transaction Id: [{transfer['tranId']}] ")

	return True

# ---------------------------------------------------

def bookTicker(client, symb = '') -> bool:

	try:
		bt = client.get_orderbook_ticker(symbol = symb, recvWindow = BU.getRecvWindow())
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_orderbook_ticker() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_orderbook_ticker() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_orderbook_ticker(): {e}")
		return False

	if BU.getExportXLS() == True:
		BU.errPrint("Symbol\tBid Price\tBid Qty\tAsk Price\tAsk Qty")
		BU.errPrint(f"{bt['symbol']}\t{bt['bidPrice']}\t{bt['bidQty']}\t{bt['askPrice']}\t{bt['askQty']}")

	else:
		BU.errPrint(f"Latest ticker/price for [{symb}] symbol\n")

		BU.errPrint(f"Symbol...: [{bt['symbol']}]")
		BU.errPrint(f"Bid Price: [{bt['bidPrice']}]")
		BU.errPrint(f"Bid Qtd..: [{bt['bidQty']}]")
		BU.errPrint(f"Ask Price: [{bt['askPrice']}]")
		BU.errPrint(f"Ask Qtd..: [{bt['askQty']}]")

	return True

# ---------------------------------------------------

def balanceAccAsset(client, ass = '') -> bool:

	try:
		ba = client.get_asset_balance(asset = ass, recvWindow = BU.getRecvWindow())
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_asset_balance() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_asset_balance() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_asset_balance(): {e}")
		return False

	if BU.getExportXLS() == True:
		BU.errPrint("Asset\tFree\tLocked")
		BU.errPrint(f"{ba['asset']}\t{ba['free']}\t{ba['locked']}")
	else:
		BU.errPrint(f"Account balance for asset [{ass}]")
		BU.errPrint(f"Asset.: [{ba['asset']}]")
		BU.errPrint(f"Free..: [{ba['free']}]")
		BU.errPrint(f"Locked: [{ba['locked']}]")

	try:
		bl = client.get_max_margin_loan(asset = ass, recvWindow = BU.getRecvWindow())
		bt = client.get_max_margin_transfer(asset = ass, recvWindow = BU.getRecvWindow())
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_max_margin_loan()/get_max_margin_transfer() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_max_margin_loan()/get_max_margin_transfer() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_max_margin_loan()/get_max_margin_transfer(): {e}")
		return False

	if BU.getExportXLS() == True:
		BU.errPrint(f"Margin max borrow amount for {ass}\tMargin max transfer-out amount for {ass}")
		BU.errPrint(f"{bl['amount']}\t{bt['amount']}")
	else:
		BU.errPrint(f"Margin max borrow amount for [{ass}]......: [{bl['amount']}]")
		BU.errPrint(f"Margin max transfer-out amount for [{ass}]: [{bt['amount']}]")

	return True

# ---------------------------------------------------

def orderBook(client, symb = '', lim = 1000) -> bool:

	try:
		ob = client.get_order_book(symbol = symb, limit = lim, recvWindow = BU.getRecvWindow())
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_order_book() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_order_book() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_order_book(): {e}")
		return False

	if BU.getExportXLS() == True:
		BU.errPrint(f"Update id\t{ob['lastUpdateId']}")
		BP.printOrderBookXLSHEADER()
		[BP.printOrderBookXLS(n) for n in zip(ob['bids'], ob['asks'])]

	else:
		BU.errPrint(f"Order Book: [{symb}]\n")
		BU.errPrint(f"(Update id: [{ob['lastUpdateId']}])")
		BU.errPrint("\tBids\t\t\t|\t\tAsks")
		BU.errPrint("Qtd\t\tPrice\t\t|\tPrice\t\tQtd")
		[BP.printOrderBook(n) for n in zip(ob['bids'], ob['asks'])]

	return True

# ---------------------------------------------------

def infoDetailsSymbol(client, symb) -> bool:

	try:
		si = client.get_symbol_info(symb)
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_symbol_info() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_symbol_info() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_symbol_info(): {e}")
		return False

	if si is None:
		return False

	if BU.getExportXLS() == True:
		BP.printListSymbolsXLSHEADER()
		BP.printListSymbolsXLS(si)

	else:
		BU.errPrint("Symbol: [{symb}]")
		BP.printListSymbols(si)

	return True

# ---------------------------------------------------

def averagePrice(client, symb = '') -> bool:

	try:
		pa = client.get_avg_price(symbol = symb)
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_avg_price() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_avg_price() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_avg_price(): {e}")
		return False

	if BU.getExportXLS() == True:
		BU.errPrint("Symbol\tPrice\tMins")
		BU.errPrint(f"{symb}\t{pa['price']}\t{pa['mins']}")
	else:
		BU.errPrint("Current average price for a symbol")

		BU.errPrint(f"Symbol...: [{symb}]")
		BU.errPrint(f"Price....: [{pa['price']}]")
		BU.errPrint(f"Mins.....: [{pa['mins']}]")

	return True

def h24PriceChangeStats(client) -> bool:

	try:
		ga = client.get_ticker()
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_ticker() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_ticker() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_ticker(): {e}")
		return False

	totGa = len(ga)

	if BU.getExportXLS() == True:
		BP.print24hPrcChangStsXLSHEADER()
		[BP.print24hPrcChangStsXLS(n) for n in ga]
	else:
		BU.errPrint("24 hour price change statistics:")
		[BP.print24hPrcChangSts(n, i, totGa) for i, n in enumerate(ga, 1)]

# ---------------------------------------------------

if __name__ == '__main__':

	if len(sys.argv) <= 1:
		BP.printHelp(sys.argv[0])
		BU.nmExit()

	binanceAPIKey = os.getenv("BINANCE_APIKEY", "NOTDEF_APIKEY")
	if binanceAPIKey == "NOTDEF_APIKEY":
		BU.errPrint("Environment variable BINANCE_APIKEY not defined!")
		BU.nmExitErro()

	binanceSEKKey = os.getenv("BINANCE_SEKKEY", "NOTDEF_APIKEY")
	if binanceSEKKey == "NOTDEF_APIKEY":
		BU.errPrint("Environment variable BINANCE_SEKKEY not defined!")
		BU.nmExitErro()

	BU.setRecvWindow(os.getenv("BINANCE_RECVWINDOW", 5000))

	try:
		client = Client(binanceAPIKey, binanceSEKKey, {"verify": True, "timeout": 20})

	except BinanceAPIException as e:
		BU.errPrint(f"Binance API exception: [{e.status_code} - {e.message}]")
		BU.nmExitErro()

	except BinanceRequestException as e:
		BU.errPrint(f"Binance request exception: [{e.status_code} - {e.message}]")
		BU.nmExitErro()

	except BinanceWithdrawException as e:
		BU.errPrint(f"Binance withdraw exception: [{e.status_code} - {e.message}]")
		BU.nmExitErro()

	except Exception as e:
		BU.errPrint(f"Binance connection error: {e}")
		BU.nmExitErro()

	# Exchange status
	try:
		if client.get_system_status()['status'] != 0:
			BU.errPrint("Binance out of service")
			BU.nmExitErro()
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_system_status() BinanceAPIException: [{e.status_code} - {e.message}]")
		BU.nmExitErro()
	except Exception as e:
		BU.errPrint(f"Erro at client.get_system_status(): {e}")
		BU.nmExitErro()

	# Miscellaneous
	if "-xls" in sys.argv:
		BU.setExportXLS(True)
		sys.argv.remove("-xls")
	else:
		BU.setExportXLS(False)
	
	if "-Y" in sys.argv:
		BU.setConfirmationYES(True)
		sys.argv.remove("-Y")
	else:
		BU.setConfirmationYES(False)

	if "-TS" in sys.argv:
		BU.setTimestamp(True)
		sys.argv.remove("-TS")
	else:
		BU.setTimestamp(False)

	if "-TEST" in sys.argv:
		BO.setTestOrder(True)
		sys.argv.remove("-TEST")
	else:
		BO.setTestOrder(False)

	# Binance Info
	if sys.argv[1] == "-B" and len(sys.argv) == 2:
		if binanceInfo(client) == True:
			BU.nmExitOk()

	# Asset balance
	elif sys.argv[1] == "-ba" and len(sys.argv) == 3:
		if balanceAccAsset(client, sys.argv[2]) == True:
			BU.nmExitOk()

	# Wallet/Account information
	elif sys.argv[1] == "-i" and len(sys.argv) == 2:
		if accountInformation(client) == True:
			BU.nmExitOk()

	# Spot open orders
	elif sys.argv[1] == "-os" and len(sys.argv) == 2:
		if spotOpenOrders(client) == True:
			BU.nmExitOk()

	# Margim open orders
	elif sys.argv[1] == "-om" and len(sys.argv) == 2:
		if marginOpenOrders(client) == True:
			BU.nmExitOk()

	# Account history (trades, dusts, etc)
	elif sys.argv[1] == "-h" and len(sys.argv) == 3:
		if accountHistory(client, sys.argv[2]) == True:
			BU.nmExitOk()

	# List sub-accounts
	elif sys.argv[1] == "-sal" and len(sys.argv) == 2:
		if subAccountsList(client) == True:
			BU.nmExitOk()

	# Sub-accounts transfer history
	elif sys.argv[1] == "-sah" and len(sys.argv) == 3:
		if subAccountTransferHistory(client, em = sys.argv[2]) == True:
			BU.nmExitOk()

	# Sub-accounts assets
	elif sys.argv[1] == "-saa":
		if	len(sys.argv) == 3:
			if subAccountsAssets(client, em = sys.argv[2]) == True:
				BU.nmExitOk()
		elif len(sys.argv) == 4:
			if subAccountsAssets(client, em = sys.argv[2], symb = sys.argv[3]) == True:
				BU.nmExitOk()
		else: BU.errPrint("-saa parameters error")

	# Query all margin accounts orders
	elif sys.argv[1] == "-mh":
		if   len(sys.argv) == 3:
			if allMarginOrders(client, sys.argv[2]) == True:
				BU.nmExitOk()
		elif len(sys.argv) == 4:
			if allMarginOrders(client, sys.argv[2], sys.argv[3]) == True:
				BU.nmExitOk()
		elif len(sys.argv) == 5:
			if allMarginOrders(client, sys.argv[2], sys.argv[3], sys.argv[4]) == True:
				BU.nmExitOk()
		else: BU.errPrint("-mh parameters error")

	# Query margin accounts trades
	elif sys.argv[1] == "-mt":
		if   len(sys.argv) == 3:
			if marginTrades(client, sys.argv[2]) == True:
				BU.nmExitOk()
		elif len(sys.argv) == 4:
			if marginTrades(client, sys.argv[2], sys.argv[3]) == True:
				BU.nmExitOk()
		elif len(sys.argv) == 5:
			if marginTrades(client, sys.argv[2], sys.argv[3], sys.argv[4]) == True:
				BU.nmExitOk()
		else: BU.errPrint("-mt parameters error")

	# Query margin asset
	elif sys.argv[1] == "-mm" and len(sys.argv) == 3:
		if marginAsset(client, sys.argv[2]) == True:
			BU.nmExitOk()

	# 500 older trades
	elif sys.argv[1] == "-ht" and len(sys.argv) == 3:
		if olderTrades(client, sys.argv[2]) == True:
			BU.nmExitOk()

	# Account details (fees)
	elif sys.argv[1] == "-D" and len(sys.argv) == 2:
		if accountDetails(client) == True:
			BU.nmExitOk()

	# Rate limits and list of symbols
	elif sys.argv[1] == "-l" and len(sys.argv) == 2:
		if listSymbolsRateLimits(client) == True:
			BU.nmExitOk()

	# Information (prices) about a symbol
	elif sys.argv[1] == "-v" and len(sys.argv) == 5:
		if infoSymbol(client, sys.argv[2], sys.argv[3], int(sys.argv[4])) == True:
			BU.nmExitOk()

	# Information (details) about a symbol
	elif sys.argv[1] == "-V" and len(sys.argv) == 3:
		if infoDetailsSymbol(client, sys.argv[2]) == True:
			BU.nmExitOk()

	# Information (details) about a symbol
	elif sys.argv[1] == "-bp":
		if len(sys.argv) == 3:
			if orderBook(client, symb = sys.argv[2]) == True:
				BU.nmExitOk()
		elif len(sys.argv) == 4:
			if orderBook(client, symb = sys.argv[2], lim = int(sys.argv[3])) == True:
				BU.nmExitOk()
		else: BU.errPrint("-bp parameters error")

	# 24 hour price change statistics
	elif sys.argv[1] == "-p" and len(sys.argv) == 2:
		if h24PriceChangeStats(client) == True:
			BU.nmExitOk()

	# Current average price for a symbol
	elif sys.argv[1] == "-pa" and len(sys.argv) == 3:
		if averagePrice(client, sys.argv[2]) == True:
			BU.nmExitOk()

	# Deposit address for a symbol
	elif sys.argv[1] == "-d" and len(sys.argv) == 3:
		if depositAddress(client, sys.argv[2]) == True:
			BU.nmExitOk()

	# Margin symbol info
	elif sys.argv[1] == "-ml" and len(sys.argv) == 3:
		if marginSymbInfo(client, sys.argv[2]) == True:
			BU.nmExitOk()

	# Margin symbol price index
	elif sys.argv[1] == "-mp" and len(sys.argv) == 3:
		if marginSymbPriceIndex(client, sys.argv[2]) == True:
			BU.nmExitOk()

	# Latest tricker/price for a symbol
	elif sys.argv[1] == "-bt" and len(sys.argv) == 3:
		if bookTicker(client, sys.argv[2]) == True:
			BU.nmExitOk()

	# Check an order's status
	elif sys.argv[1] == "-O" and len(sys.argv) == 4:
		if orderStatus(client, sys.argv[2], sys.argv[3]) == True:
			BU.nmExitOk()

	# Deposit history
	elif sys.argv[1] == "-dh" and (len(sys.argv) == 3 or len(sys.argv) == 2):
		if len(sys.argv) == 3:
			if depositHistory(client, sys.argv[2]) == True:
				BU.nmExitOk()
		else:
			if depositHistory(client) == True:
				BU.nmExitOk()

	# Withdraw
	elif sys.argv[1] == "-w" and len(sys.argv) == 5:
		if withdrawRequest(client, ass = sys.argv[2], addr = sys.argv[3], amnt = sys.argv[4]) == True:
			BU.nmExitOk()

	# Withdraw history
	elif sys.argv[1] == "-wh" and (len(sys.argv) == 3 or len(sys.argv) == 2):
		if len(sys.argv) == 3:
			if withdrawHistory(client, sys.argv[2]) == True:
				BU.nmExitOk()
		else:
			if withdrawHistory(client) == True:
				BU.nmExitOk()

	# Transfer between spot account to margin account
	elif sys.argv[1] == "-mi" and len(sys.argv) == 4:
		if transfSpotToMargin(client, ass = sys.argv[2], ap = sys.argv[3]) == True:
			BU.nmExitOk()

	# Transfer between margin account to spot account
	elif sys.argv[1] == "-mo" and len(sys.argv) == 4:
		if transfMarginToSpot(client, ass = sys.argv[2], ap = sys.argv[3]) == True:
			BU.nmExitOk()

	# SPOT Buy order
	elif sys.argv[1] == "-b" and len(sys.argv) > 2:

		# Market order
		if sys.argv[2] == "MARKET" and len(sys.argv) == 5:
			#if BO.buyMarketOrder(client, sys.argv[3], sys.argv[4]) == True:
			if BO.orderSpot(client,
			                symbOrd = sys.argv[3],
			                qtdOrd  = sys.argv[4],
			                sideOrd = Client.SIDE_BUY,
			                typeOrd = Client.ORDER_TYPE_MARKET) == True:
				BU.nmExitOk()

		# Limit order
		elif sys.argv[2] == "LIMIT" and len(sys.argv) == 6:
			#if BO.buyLimitOrder(client, sys.argv[3], sys.argv[4], sys.argv[5]) == True:
			if BO.orderSpot(client,
			                symbOrd = sys.argv[3],
			                qtdOrd  = sys.argv[4],
			                prcOrd  = sys.argv[5],
			                sideOrd = Client.SIDE_BUY,
			                typeOrd = Client.ORDER_TYPE_LIMIT) == True:
				BU.nmExitOk()

		# Stop Limit
		elif sys.argv[2] == "STOP" and len(sys.argv) == 7:
			#if BO.buyStopOrder(client, sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]) == True:
			if BO.orderSpotLimit(client,
			                     symbOrd         = sys.argv[3],
			                     qtdOrd          = sys.argv[4],
			                     prcStopOrd      = sys.argv[5],
			                     prcStopLimitOrd = sys.argv[6],
			                     sideOrd         = Client.SIDE_BUY) == True:
				BU.nmExitOk()

		# OCO
		elif sys.argv[2] == "OCO" and len(sys.argv) == 8:
			if BO.buyOCOOrder(client, sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]) == True:
				BU.nmExitOk()

		else:
			BU.errPrint("Parameters error for SPOT buy order.")
			#BU.nmExitErro()

	# SPOT Sell order
	elif sys.argv[1] == "-s" and len(sys.argv) > 2:

		# Market order
		if sys.argv[2] == "MARKET" and len(sys.argv) == 5:
			#if BO.sellMarketOrder(client, sys.argv[3], sys.argv[4]) == True:
			if BO.orderSpot(client,
			                symbOrd = sys.argv[3],
			                qtdOrd  = sys.argv[4],
			                sideOrd = Client.SIDE_SELL,
			                typeOrd = Client.ORDER_TYPE_MARKET) == True:
				BU.nmExitOk()

		# Limit order
		elif sys.argv[2] == "LIMIT" and len(sys.argv) == 6:
			#if BO.sellLimitOrder(client, sys.argv[3], sys.argv[4], sys.argv[5]) == True:
			if BO.orderSpot(client,
			                symbOrd = sys.argv[3],
			                qtdOrd  = sys.argv[4],
			                prcOrd  = sys.argv[5],
			                sideOrd = Client.SIDE_SELL,
			                typeOrd = Client.ORDER_TYPE_LIMIT) == True:
				BU.nmExitOk()

		# Stop Limit
		elif sys.argv[2] == "STOP" and len(sys.argv) == 7:
			#if BO.sellStopOrder(client, sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]) == True:
			if BO.orderSpotLimit(client,
			                     symbOrd         = sys.argv[3],
			                     qtdOrd          = sys.argv[4],
			                     prcStopOrd      = sys.argv[5],
			                     prcStopLimitOrd = sys.argv[6],
			                     sideOrd         = Client.SIDE_SELL) == True:
				BU.nmExitOk()

		# OCO
		elif sys.argv[2] == "OCO" and len(sys.argv) == 8:
			if BO.sellOCOOrder(client, sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]) == True:
				BU.nmExitOk()

		else:
			BU.errPrint("Parameters error for SPOT sell order.")
			#BU.nmExitErro()

	elif sys.argv[1] == "-c" and len(sys.argv) == 4:
		ret, msgRet = BO.cancel_a_spot_order(client, sys.argv[2], sys.argv[3])
		if ret == False:
			BU.nmExitErro(m = msgRet)

		BU.nmExitOk(m = msgRet)

	# MARGIN Buy order
	elif sys.argv[1] == "-bm" and len(sys.argv) > 2:

		# Market order
		if sys.argv[2] == "MARKET" and len(sys.argv) == 5:
			if BO.orderMargin(client,
				               symbOrd = sys.argv[3], sideOrd = "BUY",
			                  typeOrd = "MARKET",    qtdOrd  = sys.argv[4],
			                  prcOrd  = 0.0,         prcStop = 0.0) == True:
				BU.nmExitOk()

		# Limit order
		elif sys.argv[2] == "LIMIT" and len(sys.argv) == 6:
			if BO.orderMargin(client,
				               symbOrd = sys.argv[3], sideOrd = "BUY",
			                  typeOrd = "LIMIT",     qtdOrd  = sys.argv[4],
			                  prcOrd  = sys.argv[5], prcStop = 0.0) == True:
				BU.nmExitOk()

		# Stop limit
		elif sys.argv[2] == "STOP" and len(sys.argv) == 7:
			if BO.orderMargin(client,
				               symbOrd = sys.argv[3],         sideOrd = "BUY",
			                  typeOrd = "TAKE_PROFIT_LIMIT", qtdOrd  = sys.argv[4],
			                  prcOrd  = sys.argv[5],         prcStop = sys.argv[6]) == True:
				BU.nmExitOk()

		# OCO
		elif sys.argv[2] == "OCO" and len(sys.argv) == 8:
			if BO.orderMargin(client,
				               symbOrd = sys.argv[3],         sideOrd = "BUY",
			                  typeOrd = "TAKE_PROFIT_LIMIT", qtdOrd  = sys.argv[4],
			                  prcOrd  = sys.argv[5],         prcStop = sys.argv[6],
			                  limit   = argv[7] ) == True:
				BU.nmExitOk()

		else:
			BU.errPrint("Parameters error for MARGIN buy order.")
			#BU.nmExitErro()

	# MARGIN Sell order
	elif sys.argv[1] == "-sm" and len(sys.argv) > 2:

		# Market order
		if sys.argv[2] == "MARKET" and len(sys.argv) == 5:
			if BO.orderMargin(client,
				               symbOrd = sys.argv[3], sideOrd = "SELL",
			                  typeOrd = "MARKET",    qtdOrd  = sys.argv[4],
			                  prcOrd  = 0.0,         prcStop = 0.0) == True:
				BU.nmExitOk()

		# Limit order
		elif sys.argv[2] == "LIMIT" and len(sys.argv) == 6:
			if BO.orderMargin(client,
				               symbOrd = sys.argv[3], sideOrd = "SELL",
			                  typeOrd = "LIMIT",     qtdOrd  = sys.argv[4],
			                  prcOrd  = sys.argv[5], prcStop = 0.0) == True:
				BU.nmExitOk()

		# Stop limit
		elif sys.argv[2] == "STOP" and len(sys.argv) == 7:
			if BO.orderMargin(client,
				               symbOrd = sys.argv[3],         sideOrd = "SELL",
			                  typeOrd = "TAKE_PROFIT_LIMIT", qtdOrd  = sys.argv[4],
			                  prcOrd  = sys.argv[5],         prcStop = sys.argv[6]) == True:
				BU.nmExitOk()

		# OCO
		elif sys.argv[2] == "OCO" and len(sys.argv) == 8:
			if BO.orderMargin(client,
				               symbOrd = sys.argv[3],         sideOrd = "SELL",
			                  typeOrd = "TAKE_PROFIT_LIMIT", qtdOrd  = sys.argv[4],
			                  prcOrd  = sys.argv[5],         prcStop = sys.argv[6],
			                  limit   = argv[7] ) == True:
				BU.nmExitOk()

		else:
			BU.errPrint("Parameters error for MARGIN sell order.")
			#BU.nmExitErro()

	elif sys.argv[1] == "-cm" and len(sys.argv) == 4:
		ret, msgRet = BO.cancel_a_margin_order(client, sys.argv[2], sys.argv[3])
		if ret == False:
			BU.nmExitErro(m = msgRet)

		BU.nmExitOk(m = msgRet)

	else:
		BU.errPrint("Parameters error.")
		BP.printHelp(sys.argv[0])

	BU.nmExitErro()
