#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota
# andre.scota@gmail.com
# MIT license

import os, sys

import binancePrint as BP
import binanceUtil as BU
import binanceOrder as BO

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceWithdrawException, BinanceRequestException

# ---------------------------------------------------

def binanceInfo(client):
	try:
		sst = client.get_system_status()
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_system_status() BinanceAPIException: [{e.status_code} - {e.message}]")
		return

	try:
		st = client.get_server_time()
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_server_time() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_server_time() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.get_server_time()")
		return

	try:
		prodct = client.get_products()
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_products() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_products() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.get_products()")
		return

	if BU.getExportXLS() == True:
		print("Server Status")
		BP.printSystemStatusXLS(sst)

		print("\nTime")
		BP.printServerTimeXLS(st)

		print("\nProducts")
		BP.printProductsXLSHEADER()
		[BP.printProductsXLS(n) for n in prodct['data']]

	else:
		print("Server Status:")
		BP.printSystemStatus(sst)

		print("\nTime:")
		BP.printServerTime(st)

		print("\nProducts:")
		totProdct = len(prodct['data'])
		[BP.printProducts(n, i, totProdct) for i, n in enumerate(prodct['data'], 1)]

def accountInfos(client):
	try:
		acc = client.get_account()
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_account() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_account() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.get_account()")
		return

	try:
		accStatus = client.get_account_status()
	except BinanceWithdrawException as e:
		BU.errPrint(f"Erro at client.get_account_status() BinanceWithdrawException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.get_account_status()")
		return

	if BU.getExportXLS() == True:
		print(f"Can trade\t{acc['canTrade']}\nCan withdraw\t{acc['canWithdraw']}\nCan deposit\t{acc['canDeposit']}\nAccount type\t{acc['accountType']}")
		print(f"Account status detail\t{accStatus['msg']}\nSuccess\t{accStatus['success']}\n")
	else:
		print(f"Can trade: [{acc['canTrade']}] Can withdraw: [{acc['canWithdraw']}] Can deposit: [{acc['canDeposit']}] Account type: [{acc['accountType']}]")
		print(f"(Account status detail: [{accStatus['msg']}] Success: [{accStatus['success']}]\n")

	if len(acc['balances']) != 0:
		if BU.getExportXLS() == True:
			BP.printAccountXLSHEADER()
			[BP.printAccountXLS(n) for n in acc['balances'] if float(n['free']) != 0.0 or float(n['locked']) != 0.0]
		else:
			[BP.printAccount(n) for n in acc['balances'] if float(n['free']) != 0.0 or float(n['locked']) != 0.0]

	# SPOT

	try:
		openOrders = client.get_open_orders()
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_open_orders() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_open_orders() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.get_open_orders()")
		return

	totOpenOrder = len(openOrders)

	if totOpenOrder != 0:
		if totOpenOrder == 1:
			print("\n* SPOT *")
		elif totOpenOrder < 1:
			print(f"Open orders ({totOpenOrder}):")

		if BU.getExportXLS() == True:
			BP.printOrderXLSHEADER()
			[BP.printOrderXLS(n) for n in openOrders]
		else:
			[BP.printOrder(n, i, totOpenOrder) for i, n in enumerate(openOrders, 1)]
	else:
		print("No open orders")

	# MARGIN

	try:
		marginInfo = client.get_margin_account()
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_margin_account() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_margin_account() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.get_margin_account()")
		return

	print("\n* MARGIN *")

	if BU.getExportXLS() == True:
		print("Margin level\tTotal asset of BTC\tTotal liability of BTC\tTotal Net asset of BTC\tTrade enabled")
		print(f"{marginInfo['marginLevel']}\t{marginInfo['totalAssetOfBtc']}\t{marginInfo['totalLiabilityOfBtc']}\t{marginInfo['totalNetAssetOfBtc']}\t{marginInfo['tradeEnabled']}\n")

		print('Borrowed assets:')
		BP.printMarginAssetsXLSHEADER()
		[BP.printMarginAssetsXLS(n) for n in marginInfo['userAssets'] if float(n['netAsset']) != 0.0]
	else:
		print(f"Borrow Enabled........: [{marginInfo['borrowEnabled']}]")
		print(f"Level.................: [{marginInfo['marginLevel']}]")
		print(f"Total asset of BTC....: [{marginInfo['totalAssetOfBtc']}]")
		print(f"Total liability of BTC: [{marginInfo['totalLiabilityOfBtc']}]")
		print(f"Total Net asset of BTC: [{marginInfo['totalNetAssetOfBtc']}]")
		print(f"Trade enabled.........? [{marginInfo['tradeEnabled']}]\n")

		print('Borrowed assets:')
		[BP.printMarginAssets(n, i) for i, n in enumerate(marginInfo['userAssets'], 1) if float(n['netAsset']) != 0.0]

	try:
		openMarginOrders = client.get_open_margin_orders()
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_open_margin_orders() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_open_margin_orders() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.get_open_margin_orders()")
		return

	totOpenMarginOrder = len(openMarginOrders)

	if totOpenMarginOrder != 0:
		print("");
		if   totOpenMarginOrder == 1: print("Open margin order:")
		elif totOpenMarginOrder <  1: print(f"Open margin orders ({totOpenOrder}):")

		if BU.getExportXLS() == True:
			BP.printMarginOrderXLSHEADER()
			[BP.printMarginOrderXLS(n) for n in openMarginOrders]
		else:
			[BP.printMarginOrder(n, i, totOpenMarginOrder) for i, n in enumerate(openMarginOrders, 1)]
	else:
		print('No open margin orders')

# ---------------------------------------------------

def withdrawRequest(client, ass = '', addr = '', amnt = 0):
	print("Withdraw")

	if BU.getExportXLS() == True:
		print("Asset\tAddress\tAmount")
		print(f"{ass}\t{addr}\t{amnt}")
	else:
		print(f"Asset..: [{ass}]")
		print(f"Address: [{addr}]")
		print(f"Amount.: [{amnt}]")

	if BU.askConfirmation() == False:
		return None

	try:
		withdrawReq = client.withdraw(asset = ass, address = addr, amount = amnt)

	except BinanceRequestException as e:
		BU.errPrint(f"Erro at withdraw BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at withdraw BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except BinanceWithdrawException as e:
		BU.errPrint(f"Erro at withdraw BinanceWithdrawException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint(f"Erro at withdraw")
		return

	if BU.getExportXLS() == True:
		BP.printWithdrawResponseXLSHEADER()
		BP.printWithdrawResponseXLS(withdrawReq)
	else:
		BP.printWithdrawResponse(withdrawReq)

def withdrawHistory(client, ass = ''):
	print("Withdraw History")

	try:
		withdraw = client.get_withdraw_history(asset = ass)

	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_withdraw_history() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_withdraw_history() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.get_withdraw_history()")
		return

	if BU.getExportXLS() == True:
		BP.printWithdrawHistoryXLSHEADER()
		[BP.printWithdrawHistoryXLS(n) for n in withdraw['withdrawList']]
	else:
		[BP.printWithdrawHistory(n) for n in withdraw['withdrawList']]

# ---------------------------------------------------

def depositHistory(client, ass = ''):
	print(f"Deposit History for [{ass}]")

	try:
		deposits = client.get_deposit_history(asset = ass)

	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_deposit_history() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_deposit_history() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.get_deposit_history()")
		return

	if BU.getExportXLS() == True:
		BP.printDepositHistoryXLSHEADER()
		[BP.printDepositHistoryXLS(n) for n in deposits['depositList']]
	else:
		[BP.printDepositHistory(n) for n in deposits['depositList']]

def depositAddress(client, ass):
	print(f"Deposit Address for [{ass}]")

	try:
		depAdd = client.get_deposit_address(asset = ass)

	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_deposit_address() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_deposit_address() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.get_deposit_address()")
		return

	if BU.getExportXLS() == True:
		BP.printDepositAddressXLSHEADER()
		BP.printDepositAddressXLS(depAdd)
	else:
		BP.printDepositAddress(depAdd)

# ---------------------------------------------------

def olderTrades(client, ass = ''):
	print(f"500 older trades")

	try:
		depAdd = client.get_historical_trades(asset = ass)

	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_historical_trades() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_historical_trades() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.get_historical_trades()")
		return

	if BU.getExportXLS() == True:
		BP.printHistoricalTradesXLSHEADER()
		BP.printHistoricalTradesXLS(depAdd)
	else:
		BP.printHistoricalTrades(depAdd)

# ---------------------------------------------------

def accountHistory(client, symb):
	try:
		tradeHist = client.get_my_trades(symbol=symb)
	except:
		BU.errPrint(f"Erro at client.get_my_trades(symbol={symb})")
		return

	tradeHistTot = len(tradeHist)

	if BU.getExportXLS() == True:
		BP.printTradeHistoryXLSHEADER()
		[BP.printTradeHistoryXLS(n) for n in tradeHist]
	else:
		print(f"Trade history {symb}:")
		[BP.printTradeHistory(n, i, tradeHistTot) for i, n in enumerate(tradeHist, 1)]

	print(f"All trade history {symb}:")

	try:
		tradeAllHist = client.get_all_orders(symbol=symb)
	except:
		BU.errPrint(f"Erro at client.get_all_orders(symbol={symb})")
		return

	tradeAllHistTot = len(tradeAllHist)

	if BU.getExportXLS() == True:
		BP.printTradeAllHistXLSHEADER()
		[BP.printTradeAllHistXLS(n) for n in tradeAllHist]
	else:
		print(f"Trade history {symb}:")
		[BP.printTradeAllHist(n, i, tradeAllHistTot) for i, n in enumerate(tradeAllHist, 1)]

	try:
		allDust = client.get_dust_log()
	except BinanceWithdrawException as e:
		BU.errPrint(f"Erro at client.get_dust_log() BinanceWithdrawException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.get_dust_log()")
		return

	allDustTot = len(allDust['results']['rows'])

	if BU.getExportXLS() == True:
		print("============== UNDERCONSTRUCTION ==========================")
	else:
		print("Log of small amounts exchanged for BNB:")
		[BP.printDustTrade(n, i, allDustTot) for i, n in enumerate(allDust['results']['rows'], 1)]

# ---------------------------------------------------

def accountDetails(client):
	try:
		assDet = client.get_asset_details()
		tradFee = client.get_trade_fee()
	except BinanceWithdrawException as e:
		BU.errPrint(f"Erro get_asset_details and get_trade_fee BinanceWithdrawException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint(f"Erro get_asset_details and get_trade_fee")
		return

	if BU.getExportXLS() == True:
		print('Details on Assets')
		BP.printDetailsAssetsXLSHEADER()
		[BP.printDetailsAssetsXLS(n, assDet['assetDetail'][n]) for n in assDet['assetDetail'].keys()]

		print('\nTrade Fee')
		BP.printTradeFeeXLSHEADER()
		[BP.printTradeFeeXLS(n) for n in tradFee['tradeFee']]

	else:
		print('Details on Assets:')
		adTot = len(assDet['assetDetail'])
		[BP.printDetailsAssets(n, assDet['assetDetail'][n], i, adTot) for i, n in enumerate(assDet['assetDetail'].keys(), 1)]

		print('Trade Fee:')
		adTot = len(tradFee['tradeFee'])
		[BP.printTradeFee(n, i, adTot) for i, n in enumerate(tradFee['tradeFee'], 1)]

# ---------------------------------------------------

def infoSymbol(client, symb, interv, candlesTot):

	try:
		sumbPrc = client.get_klines(symbol = symb, interval = BU.binanceInterval(interv), limit = candlesTot)
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_klines() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_klines() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.get_klines()")
		return

	if BU.getExportXLS() == True:
		BP.printInfoSymbolValuesXLSHEADER()
		[BP.printInfoSymbolValuesXLS(n) for n in sumbPrc]
	else:
		print(f"Symbol [{symb}] in interval [{interv}]");
		totsumbPrc = len(sumbPrc)
		[BP.printInfoSymbolValues(n, i, totsumbPrc) for i, n in enumerate(sumbPrc, 1)]

# ---------------------------------------------------

def listSymbolsRateLimits(client):
	try:
		ei = client.get_exchange_info()
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_exchange_info() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_exchange_info() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.get_exchange_info()")
		return

	if BU.getExportXLS() == True:
		print("Rate Limits")
		BP.printListRateLimitXLSHEADER()
		[BP.printListRateLimitXLS(n) for n in ei['rateLimits']]

		print("\nSymbols")
		BP.printListSymbolsXLSHEADER()
		[BP.printListSymbolsXLS(n) for n in ei['symbols']]

	else:
		print("Rate Limits:")
		totei = len(ei['rateLimits'])
		[BP.printListRateLimit(n, i, totei) for i, n in enumerate(ei['rateLimits'], 1)]

		print("Symbols:")
		totei = len(ei['symbols'])
		[BP.printListSymbols(n, i, totei) for i, n in enumerate(ei['symbols'], 1)]

# ---------------------------------------------------

def transfSpotToMargin(client, ass = '', ap = '0.0'):
	print(f"Tranfering [{ap}] of [{ass}] from Spot to Margin account")

	try:
		transfer = client.transfer_spot_to_margin(asset = ass, amount = ap)	
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.transfer_spot_to_margin() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.transfer_spot_to_margin() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.transfer_spot_to_margin()")
		return

	print("Return Ok. Spot to Margin transaction Id: [{transfer['tranId']}] ")

def transfMarginToSpot(client, ass = '', ap = '0.0'):
	print(f"Tranfering [{ap}] of [{ass}] from Margin to Spot account")

	try:
		transfer = client.transfer_margin_to_spot(asset = ass, amount = ap)	
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.transfer_margin_to_spot() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.transfer_margin_to_spot() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.transfer_margin_to_spot()")
		return

	print("Return Ok. Margin to Spot transaction Id: [{transfer['tranId']}] ")

# ---------------------------------------------------

def balanceAccAsset(client, ass = ''):
	print(f"Account balance for asset [{ass}]")

	try:
		ba = client.get_asset_balance(asset = ass)
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_asset_balance() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_asset_balance() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.get_asset_balance()")
		return

	if BU.getExportXLS() == True:
		print("Asset\tFree\tLocked")
		print(f"{ba['asset']}\t{ba['free']}\t{ba['locked']}")
	else:
		print(f"Asset.: [{ba['asset']}]")
		print(f"Free..: [{ba['free']}]")
		print(f"Locked: [{ba['locked']}]")

# ---------------------------------------------------

def infoDetailsSymbol(client, symb):
	try:
		si = client.get_symbol_info(symb)
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_symbol_info() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_symbol_info() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.get_symbol_info()")
		return

	if BU.getExportXLS() == True:
		BP.printListSymbolsXLSHEADER()
		BP.printListSymbolsXLS(si)

	else:
		print("Symbol: [{symb}]")
		BP.printListSymbols(si)

# ---------------------------------------------------
def averagePrice(client, symb = ''):
	print("Current average price for a symbol")

	try:
		pa = client.get_avg_price(symbol = symb)
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_avg_price() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_avg_price() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.get_avg_price()")
		return

	if BU.getExportXLS() == True:
		print("Symbol\tPrice\tMins")
		print(f"{symb}\t{pa['price']}\t{pa['mins']}")
	else:
		print(f"Symbol...: [{symb}]")
		print(f"Price....: [{pa['price']}]")
		print(f"Mins.....: [{pa['mins']}]")

def h24PriceChangeStats(client):

	try:
		ga = client.get_ticker()
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_ticker() BinanceAPIException: [{e.status_code} - {e.message}]")
		return
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_ticker() BinanceRequestException: [{e.status_code} - {e.message}]")
		return
	except:
		BU.errPrint("Erro at client.get_ticker()")
		return

	totGa = len(ga)

	if BU.getExportXLS() == True:
		BP.print24hPrcChangStsXLSHEADER()
		[BP.print24hPrcChangStsXLS(n) for n in ga]
	else:
		print("24 hour price change statistics:")
		[BP.print24hPrcChangSts(n, i, totGa) for i, n in enumerate(ga, 1)]

# ---------------------------------------------------

if __name__ == '__main__':

	if len(sys.argv) <= 1:
		BP.printHelp(sys.argv[0])
		sys.exit(0)

	binanceAPIKey = os.getenv("BINANCE_APIKEY", "NOTDEF_APIKEY")
	if binanceAPIKey == "NOTDEF_APIKEY":
		print("Environment variable BINANCE_APIKEY not defined!")
		sys.exit(0)

	binanceSEKKey = os.getenv("BINANCE_SEKKEY", "NOTDEF_APIKEY")
	if binanceSEKKey == "NOTDEF_APIKEY":
		print("Environment variable BINANCE_SEKKEY not defined!")
		sys.exit(0)

	try:
		client = Client(binanceAPIKey, binanceSEKKey, {"verify": True, "timeout": 20})

	except BinanceAPIException as e:
		print(f"Binance API exception: [{e.status_code} - {e.message}]")
		sys.exit(0)

	except BinanceRequestException as e:
		print(f"Binance request exception: [{e.status_code} - {e.message}]")
		sys.exit(0)

	except BinanceWithdrawException as e:
		print(f"Binance withdraw exception: [{e.status_code} - {e.message}]")
		sys.exit(0)

	except:
		print("Binance connection error")
		sys.exit(0)

	# Exchange status
	try:
		if client.get_system_status()['status'] != 0:
			BU.errPrint("Binance out of service")
			sys.exit(0)
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_system_status() BinanceAPIException: [{e.status_code} - {e.message}]")
		sys.exit(0)
	except:
		BU.errPrint("Erro at client.get_system_status()")
		sys.exit(0)

	# Miscellaneous
	if "--xls" in sys.argv:
		BU.setExportXLS(True)
		sys.argv.remove("--xls")
	else:
		BU.setExportXLS(False)
	
	if "-Y" in sys.argv:
		BU.setConfirmationYES(True)
		sys.argv.remove("-Y")
	else:
		BU.setConfirmationYES(False)

	if "--TEST" in sys.argv:
		BO.setTestOrder(True)
		sys.argv.remove("--TEST")
	else:
		BO.setTestOrder(False)

	# Binance Info
	if sys.argv[1] == "-B" and len(sys.argv) == 2:
		binanceInfo(client)

	# Asset balance
	elif sys.argv[1] == "-ba" and len(sys.argv) == 3:
		balanceAccAsset(client, sys.argv[2])

	# Wallet/Account information
	elif sys.argv[1] == "-i" and len(sys.argv) == 2:
		accountInfos(client)

	# Account history (trades, dusts, etc)
	elif sys.argv[1] == "-h" and len(sys.argv) == 3:
		accountHistory(client, sys.argv[2])

	# 500 older trades
	elif sys.argv[1] == "-ht" and len(sys.argv) == 3:
		olderTrades(client, sys.argv[2])

	# Account details (fees)
	elif sys.argv[1] == "-D" and len(sys.argv) == 2:
		accountDetails(client)

	# Rate limits and list of symbols
	elif sys.argv[1] == "-l" and len(sys.argv) == 2:
		listSymbolsRateLimits(client)

	# Information (prices) about a symbol
	elif sys.argv[1] == "-v" and len(sys.argv) == 5:
		infoSymbol(client, sys.argv[2], sys.argv[3], int(sys.argv[4]))

	# Information (details) about a symbol
	elif sys.argv[1] == "-V" and len(sys.argv) == 3:
		infoDetailsSymbol(client, sys.argv[2])

	# 24 hour price change statistics
	elif sys.argv[1] == "-p" and len(sys.argv) == 2:
		h24PriceChangeStats(client)

	# Current average price for a symbol
	elif sys.argv[1] == "-pa" and len(sys.argv) == 3:
		averagePrice(client, sys.argv[2])

	# Deposit address for a symbol
	elif sys.argv[1] == "-d" and len(sys.argv) == 3:
		depositAddress(client, sys.argv[2])

	# Deposit history
	elif sys.argv[1] == "-dh" and (len(sys.argv) == 3 or len(sys.argv) == 2):
		if len(sys.argv) == 3:
			depositHistory(client, sys.argv[2])
		else:
			depositHistory(client)

	# Withdraw
	elif sys.argv[1] == "-w" and len(sys.argv) == 5:
		withdrawRequest(client, ass = sys.argv[2], addr = sys.argv[3], amnt = sys.argv[4])

	# Withdraw history
	elif sys.argv[1] == "-wh" and (len(sys.argv) == 3 or len(sys.argv) == 2):
		if len(sys.argv) == 3:
			withdrawHistory(client, sys.argv[2])
		else:
			withdrawHistory(client)

	# Transfer between spot account to margin account
	elif sys.argv[1] == "-mi" and len(sys.argv) == 4:
		transfSpotToMargin(client, ass = sys.argv[2], ap = sys.argv[3])

	# Transfer between margin account to spot account
	elif sys.argv[1] == "-mo" and len(sys.argv) == 4:
		transfMarginToSpot(client, ass = sys.argv[2], ap = sys.argv[3])

	# SPOT Buy order
	elif sys.argv[1] == "-b" and len(sys.argv) > 2:

		# Market order
		if sys.argv[2] == "MARKET" and len(sys.argv) == 5:
			BO.buyMarketOrder(client, sys.argv[3], sys.argv[4])

		# Limit order
		elif sys.argv[2] == "LIMIT" and len(sys.argv) == 6:
			BO.buyLimitOrder(client, sys.argv[3], sys.argv[4], sys.argv[5])

		# OCO
		elif sys.argv[2] == "STOP" and len(sys.argv) == 7:
			BO.buyStopOrder(client, sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])

		else:
			print("Parameters error for SPOT buy order")

	# SPOT Sell order
	elif sys.argv[1] == "-s" and len(sys.argv) > 2:

		# Market order
		if sys.argv[2] == "MARKET" and len(sys.argv) == 5:
			BO.sellMarketOrder(client, sys.argv[3], sys.argv[4])

		# Limit order
		elif sys.argv[2] == "LIMIT" and len(sys.argv) == 6:
			BO.sellLimitOrder(client, sys.argv[3], sys.argv[4], sys.argv[5])

		# OCO
		elif sys.argv[2] == "STOP" and len(sys.argv) == 7:
			BO.sellStopOrder(client, sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])

		else:
			print("Parameters error for SPOT sell order")

	elif sys.argv[1] == "-c" and len(sys.argv) == 4:
		BO.cancel_a_spot_order(client, sys.argv[2], sys.argv[3])

	# MARGIN Buy order
	elif sys.argv[1] == "-bm" and len(sys.argv) > 2:

		# Market order
		if sys.argv[2] == "MARKET" and len(sys.argv) == 5:
			orderMargin(symbOrd = sys.argv[3], sideOrd = "BUY",
			            typeOrd = "MARKET",    qtdOrd  = sys.argv[4],
			            prcOrd  = 0.0,         prcStop = 0.0)

		# Limit order
		elif sys.argv[2] == "LIMIT" and len(sys.argv) == 6:
			orderMargin(symbOrd = sys.argv[3], sideOrd = "BUY",
			            typeOrd = "LIMIT",     qtdOrd  = sys.argv[4],
			            prcOrd  = sys.argv[5], prcStop = 0.0)

		# OCO
		elif sys.argv[2] == "STOP" and len(sys.argv) == 7:
			orderMargin(symbOrd = sys.argv[3],   sideOrd = "BUY",
			            typeOrd = "TAKE_PROFIT", qtdOrd  = sys.argv[4],
			            prcOrd  = sys.argv[5],   prcStop = sys.argv[6])

		else:
			print("Parameters error for MARGIN buy order")

	# MARGIN Sell order
	elif sys.argv[1] == "-sm" and len(sys.argv) > 2:

		# Market order
		if sys.argv[2] == "MARKET" and len(sys.argv) == 5:
			orderMargin(symbOrd = sys.argv[3], sideOrd = "SELL",
			            typeOrd = "MARKET",    qtdOrd  = sys.argv[4],
			            prcOrd  = 0.0,         prcStop = 0.0)

		# Limit order
		elif sys.argv[2] == "LIMIT" and len(sys.argv) == 6:
			orderMargin(symbOrd = sys.argv[3], sideOrd = "SELL",
			            typeOrd = "LIMIT",     qtdOrd  = sys.argv[4],
			            prcOrd  = sys.argv[5], prcStop = 0.0)

		# OCO
		elif sys.argv[2] == "STOP" and len(sys.argv) == 7:
			orderMargin(symbOrd = sys.argv[3], sideOrd = "SELL",
			            typeOrd = "STOP_LOSS", qtdOrd  = sys.argv[4],
			            prcOrd  = sys.argv[5], prcStop = sys.argv[6])

		else:
			print("Parameters error for MARGIN sell order")

	elif sys.argv[1] == "-cm" and len(sys.argv) == 4:
		BO.cancel_a_margin_order(client, sys.argv[2], sys.argv[3])

	else:
		print("Parameters error.")
		BP.printHelp(sys.argv[0])
		sys.exit(0)
