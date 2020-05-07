#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota
# andre.scota@gmail.com
# MIT license

import binanceUtil as BU

def printHelp(execName):
	print("[asset] = BTC, BNB, ETH ... | [symbol] = BTCUSDT, BNBBTC, ...")
	print("------------------------------------------------------------------------")
	print("1.1) Account")
	print(f"{execName} -D\n\tAccount details (fees, assets, etc)\n")
	print(f"{execName} -h [symbol]\n\tAccount history (trades, dusts, etc)\n")
#print(f"{execName} -hm [symbol]\n\tAccount history (trades, dusts, etc)\n")
	print(f"{execName} -i\n\tWallet/Account SPOT and MARGIN information (details, open orders, etc)\n")

	print("1.2) Deposit/Withdraw")
	print(f"{execName} -d [Asset]\n\tDeposit address (Asset = 'BTC')\n")
	print(f"{execName} -dh [Asset]\n\tDeposit history (Asset can be null)\n")
	print(f"{execName} -w [Asset] [Address] [Amount]\n\tSubmit a withdraw request\n")
	print(f"{execName} -wh [Asset]\n\tWithdraw history (Asset can be null)\n")

	print("------------------------------------------------------------------------")
	print("2) Trade:")
	print("2.1) SPOT")
	print(f'{execName} -s\n\tPlace a SPOT sell order')
	print(f'\t\t{execName} -s MARKET [symbol] [qtd]')
	print(f'\t\t{execName} -s LIMIT [symbol] [qtd] [price]')
	print(f'\t\t{execName} -s STOP [symbol] [qtd] [price] [stopPrice]\n')

	print(f'{execName} -b\n\tPlace a SPOT buy order')
	print(f'\t\t{execName} -b MARKET [symbol] [qtd] [--TEST]')
	print(f'\t\t{execName} -b LIMIT [symbol] [qtd] [price] [--TEST]')
	print(f'\t\t{execName} -b STOP [symbol] [qtd] [price] [stopPrice]\n')

	print(f'{execName} -c [symbol] [order_id]\n\tCancel a SPOT order\n')

	print("2.2) MARGIN")
	print(f'{execName} -sm\n\tPlace a MARGIN sell order')
	print(f'\t\t{execName} -sm MARKET [symbol] [qtd] [--TEST]')
	print(f'\t\t{execName} -sm LIMIT [symbol] [qtd] [price] [--TEST]')
	print(f'\t\t{execName} -sm STOP [symbol] [qtd] [price] [stopPrice]\n')

	print(f'{execName} -bm\n\tPlace a MARGIN buy order')
	print(f'\t\t{execName} -bm MARKET [symbol] [qtd]')
	print(f'\t\t{execName} -bm LIMIT [symbol] [qtd] [price]')
	print(f'\t\t{execName} -bm STOP [symbol] [qtd] [price] [stopPrice]\n')

	print(f'{execName} -cm [symbol] [order_id]\n\tCancel a MARGIN order\n')

	print(f'{execName} -ma [asset]\n\tQuery max transfer-out amount\n')

	print("------------------------------------------------------------------------")
	print("3) Binance market:")
	print(f'{execName} -p \n\t24 hour price change statistics\n')

	print(f'{execName} -l\n\tList of symbols and rate/limits\n')

	print(f'{execName} -v [symbol] [interval] [qtd candles]\n\tInformation (prices) about a symbol.\n\t[interval] is one of \'1m\', \'3m\', \'5m\', \'15m\', \'30m\', \'2h\', \'4h\', \'6h\', \'8h\', \'12h\', \'1h\', \'1d\', \'3d\', \'1w\', \'1M\'\n')

	print(f'{execName} -V [symbol]\n\tInformation (details) about a symbol\n')

	print(f'{execName} -B\n\tBinance Informations (server time, server status, products)\n')

	print("------------------------------------------------------------------------")
	print("4) Miscellaneous:")
	print(f'{execName} [...] --xls >> output.xls\n\tOutput with TAB separator\n')
	print(f'{execName} [...] -Y\n\tForce ALL CONFIRMATIONS = YES\n')

# ----------------------------------------------------------------------------

def printWithdrawResponseXLSHEADER():
	print("Message\tSuccess\tId")

def printWithdrawResponseXLS(withdrawReq):
	print(f"{withdrawReq['msg']}\t{withdrawReq['success']}\t{withdrawReq['id']}")

def printWithdrawResponse(withdrawReq):
	print(f"Message: [{withdrawReq['msg']}]")
	print(f"Success: [{withdrawReq['success']}]")
	print(f"Id.....: [{withdrawReq['id']}]")

# ----------------------------------------------------------------------------

def printWithdrawHistoryXLSHEADER():
	print("Amount\tAsset\tAddress\tApply Time\tStatus")

def printWithdrawHistoryXLS(withdraw):
	print(f"{withdraw['amount']}\t{withdraw['asset']}\t{withdraw['address']}\t{BU.completeMilliTime(withdraw['insertTime'])}\t{withdraw['status']}")

def printWithdrawHistory(withdraw):
	print(f"Asset: [{withdraw['asset']}]")
	print(f"\tAmount.....: [{withdraw['amount']}]")
	print(f"\tAddress....: [{withdraw['address']}]")
	print(f"\tApply Time.: [{BU.completeMilliTime(withdraw['applyTime'])}]")
	print(f"\tStatus.....: [{withdraw['status']}]")

# ----------------------------------------------------------------------------

def printDepositHistoryXLSHEADER():
	print("Amount\tAsset\tInsert Time\tStatus")

def printDepositHistoryXLS(deposits):
	print(f"{deposits['amount']}\t{deposits['asset']}\t{BU.completeMilliTime(deposits['insertTime'])}\t{deposits['status']}")

def printDepositHistory(deposits):
	print(f"Asset: [{deposits['asset']}]")
	print(f"\tAmount.....: [{deposits['amount']}]")
	print(f"\tInsert Time: [{BU.completeMilliTime(deposits['insertTime'])}]")
	print(f"\tStatus.....: [{deposits['status']}]")

# ----------------------------------------------------------------------------

def printDepositAddress(depAdd):
	print(f"Asset......: [{depAdd['asset']}]")
	print(f"Address....: [{depAdd['address']}]")
	print(f"Success....: [{depAdd['success']}]")
	print(f"Address Tag: [{depAdd['addressTag']}]")

def printDepositAddressXLSHEADER():
	print("Asset\tAddress\tSuccess\tAddress Tag")

def printDepositAddressXLS(depAdd):
	print(f"{depAdd['asset']}\t{depAdd['address']}\t{depAdd['success']}\t{depAdd['addressTag']}")

# ----------------------------------------------------------------------------

def printMarginOrder(order, seq = 0, tot = 0):
	printOrder(order, seq, tot)

def printMarginOrderXLSHEADER():
	printOrderXLSHEADER()

def printMarginOrderXLS(order):
	printOrderXLS(order)

# ----------------------------------------------------------------------------

def printInfoSymbolValues(symbPrc, seq = 0, tot = 0):
	print(f"{seq}/{tot}) Candle:")
	print(f"Open time...................: [{BU.completeMilliTime(symbPrc[0])}]")
	print(f"Close time..................: [{BU.completeMilliTime(symbPrc[6])}]")
	print(f"High........................: [{symbPrc[2]}]")
	print(f"Open........................: [{symbPrc[1]}]")
	print(f"Close.......................: [{symbPrc[4]}]")
	print(f"Low.........................: [{symbPrc[3]}]")
	print(f"Volume......................: [{symbPrc[5]}]")
	print(f"Quote asset volume..........: [{symbPrc[7]}]")
	print(f"Number of trades............: [{symbPrc[8]}]")
	print(f"Taker buy base asset volume.: [{symbPrc[9]}]")
	print(f"Taker buy quote asset volume: [{symbPrc[10]}]\n")

def printInfoSymbolValuesXLSHEADER():
	print("Open time\t"
	      "Close time\t"
	      "High\t"
	      "Open\t"
	      "Close\t"
	      "Low\t"
	      "Volume\t"
	      "Quote asset volume\t"
	      "Number of trades\t"
	      "Taker buy base asset volume\t"
	      "Taker buy quote asset volume")

def printInfoSymbolValuesXLS(symbPrc):
	print(f"{BU.completeMilliTime(symbPrc[0])}\t"
	      f"{BU.completeMilliTime(symbPrc[6])}\t"
	      f"{symbPrc[2]}\t"
	      f"{symbPrc[1]}\t"
	      f"{symbPrc[4]}\t"
	      f"{symbPrc[3]}\t"
	      f"{symbPrc[5]}\t"
	      f"{symbPrc[7]}\t"
	      f"{symbPrc[8]}\t"
	      f"{symbPrc[9]}\t"
	      f"{symbPrc[10]}")

# ----------------------------------------------------------------------------

def print24hPrcChangSts(priceSts, seq = 0, tot = 0):
	print(f"{seq}/{tot}) Symbol: [{priceSts['symbol']}]")
	print(f"\tPrice Change..........: [{priceSts['priceChange']}]")
	print(f"\tPrice Change Percent..: [{priceSts['priceChangePercent']}]")
	print(f"\tWeighted Avarege Price: [{priceSts['weightedAvgPrice']}]")
	print(f"\tPrevious Close Price..: [{priceSts['prevClosePrice']}]")
	print(f"\tLast Price............: [{priceSts['lastPrice']}]")
	print(f"\tLast Qty..............: [{priceSts['lastQty']}]")
	print(f"\tBid Price.............: [{priceSts['bidPrice']}]")
	print(f"\tBid Qty...............: [{priceSts['bidQty']}]")
	print(f"\tAsk Price.............: [{priceSts['askPrice']}]")
	print(f"\tAsk Qty...............: [{priceSts['askQty']}]")
	print(f"\tOpen Price............: [{priceSts['openPrice']}]")
	print(f"\tHigh Price............: [{priceSts['highPrice']}]")
	print(f"\tLow Price.............: [{priceSts['lowPrice']}]")
	print(f"\tVolume................: [{priceSts['volume']}]")
	print(f"\tQuote Volume..........: [{priceSts['quoteVolume']}]")
	print(f"\tOpen Time.............: [{BU.completeMilliTime(priceSts['openTime'])}]")
	print(f"\tClose Time............: [{BU.completeMilliTime(priceSts['closeTime'])}]")
	print(f"\tFirst Id..............: [{priceSts['firstId']}]")
	print(f"\tLast Id...............: [{priceSts['lastId']}]")
	print(f"\tCount.................: [{priceSts['count']}]\n")

def print24hPrcChangStsXLSHEADER():
	print("Symbol\t"
	      "Price Change\t"
	      "Price Change Percent\t"
	      "Weighted Avarege Price\t"
	      "Previous Close Price\t"
	      "Last Price\t"
	      "Last Qty\t"
	      "Bid Price\t"
	      "Bid Qty\t"
	      "Ask Price\t"
	      "Ask Qty\t"
	      "Open Price\t"
	      "High Price\t"
	      "Low Price\t"
	      "Volume\t"
	      "Quote Volume\t"
	      "Open Time\t"
	      "Close Time\t"
	      "First Id\t"
	      "Last Id\t"
	      "Count")

def print24hPrcChangStsXLS(priceSts):
	print(f"{priceSts['symbol']}\t"
	      f"{priceSts['priceChange']}\t"
	      f"{priceSts['priceChangePercent']}\t"
	      f"{priceSts['weightedAvgPrice']}\t"
	      f"{priceSts['prevClosePrice']}\t"
	      f"{priceSts['lastPrice']}\t"
	      f"{priceSts['lastQty']}\t"
	      f"{priceSts['bidPrice']}\t"
	      f"{priceSts['bidQty']}\t"
	      f"{priceSts['askPrice']}\t"
	      f"{priceSts['askQty']}\t"
	      f"{priceSts['openPrice']}\t"
	      f"{priceSts['highPrice']}\t"
	      f"{priceSts['lowPrice']}\t"
	      f"{priceSts['volume']}\t"
	      f"{priceSts['quoteVolume']}\t"
	      f"{BU.completeMilliTime(priceSts['openTime'])}\t"
	      f"{BU.completeMilliTime(priceSts['closeTime'])}\t"
	      f"{priceSts['firstId']}\t"
	      f"{priceSts['lastId']}\t"
	      f"{priceSts['count']}")

# ----------------------------------------------------------------------------

def printDustTrade(order, seq = 0, tot = 0):
	print(f"{seq}/{tot}) Total transfered BNB amount for this exchange: [{order['transfered_total']}]")
	print(f"\tTotal service charge amount for this exchange: [{order['service_charge_total']}]")
	print(f"\tTransaction Id...............................: [{order['tran_id']}]")
	print(f"\tOperate time.................................: [{order['operate_time']}]")
	print("\tLogs:")
	for logs in order['logs']:
		print(f"\t\tFrom Asset...........: [{logs['fromAsset']}]")
		print(f"\t\tAmount...............: [{logs['amount']}]")
		print(f"\t\tService Charge Amount: [{logs['serviceChargeAmount']}]")
		print(f"\t\tTransfered Amount....: [{logs['transferedAmount']}]")
		print(f"\t\tUId..................: [{logs['uid']}]\n")

# ----------------------------------------------------------------------------

def printDetailsAssets(ass, detAss, seq = 0, tot = 0):
	print(f"{seq}/{tot}) Asset: [{ass}]");
	print(f"\tMin. withdraw amount: [{detAss['minWithdrawAmount']}]");
	print(f"\tDeposit status......: [{detAss['depositStatus']}]");
	dt = detAss.get('depositTip', '')
	if dt != '':
		print(f"\tDeposit tip.........: [{dt}]");
	print(f"\tWithdraw fee........: [{detAss['withdrawFee']}]");
	print(f"\tWithdraw status.....: [{detAss['withdrawStatus']}]\n");

def printDetailsAssetsXLSHEADER():
	print("Asset\tMin. withdraw amount\tDeposit status\tDeposit tip\tWithdraw fee\tWithdraw status")

def printDetailsAssetsXLS(ass, detAss):
	print(f"{ass}\t{detAss['minWithdrawAmount']}\t{detAss['depositStatus']}\t{detAss.get('depositTip', '')}\t{detAss['withdrawFee']}\t{detAss['withdrawStatus']}");

# ----------------------------------------------------------------------------

def printTradeFee(tf, seq = 0, tot = 0):
	print(f"{seq}/{tot}) Symbol: [{tf['symbol']}]\tMaker: [{tf['maker']}]\tTaker: [{tf['taker']}]");

def printTradeFeeXLSHEADER():
	print("Symbol\t"
	      "Maker\t"
	      "Taker");

def printTradeFeeXLS(tf):
	print(f"{tf['symbol']}\t"
	      f"{tf['maker']}\t"
	      f"{tf['taker']}");

# ----------------------------------------------------------------------------

def printTradeAllHist(tradeAllHist, seq = 0, tot = 0):
	print(f"{seq}/{tot}) Symbol: [{tradeAllHist['symbol']}]")
	print(f"\tTime.................: [{BU.completeMilliTime(tradeAllHist['time'])}]")
	print(f"\tUpdate time..........: [{BU.completeMilliTime(tradeAllHist['updateTime'])}]")
	print(f"\tOrder Id.............: [{tradeAllHist['orderId']}]")
#	print(f"\tOrder list Id........: [{tradeAllHist['orderListId']}]")
	print(f"\tClient Order Id......: [{tradeAllHist['clientOrderId']}]")
	print(f"\tPrice................: [{tradeAllHist['price']}]")
	print(f"\tOrig Qtd.............: [{tradeAllHist['origQty']}]")
	print(f"\tExecuted Qtd.........: [{tradeAllHist['executedQty']}]")
	print(f"\tCummulative Quote Qtd: [{tradeAllHist['cummulativeQuoteQty']}]")
	print(f"\tStatus...............: [{tradeAllHist['status']}]")
	print(f"\tTime in Force........: [{tradeAllHist['timeInForce']}]")
	print(f"\tSide.................: [{tradeAllHist['side']}]")
	print(f"\tType.................: [{tradeAllHist['type']}]")
	print(f"\tStop Price...........: [{tradeAllHist['stopPrice']}]")
	print(f"\tIs working...........: [{tradeAllHist['isWorking']}]\n")

def printTradeAllHistXLSHEADER():
	print(f"Symbol\t"
	       "Time\t"
	       "Update time\t"
	       "Order Id\t"
	       "Client Order Id\t"
	       "Price\t"
	       "Orig Qtd\t"
	       "Executed Qtd\t"
	       "Cummulative Quote Qtd\t"
	       "Status\t"
	       "Time in Force\t"
	       "Side\t"
	       "Type\t"
	       "Stop Price\t"
	       "Is working")

def printTradeAllHistXLS(tradeAllHist):
	print(f"{tradeAllHist['symbol']}\t"
	      f"{BU.completeMilliTime(tradeAllHist['time'])}\t"
	      f"{BU.completeMilliTime(tradeAllHist['updateTime'])}\t"
	      f"{tradeAllHist['orderId']}\t"
	      f"{tradeAllHist['clientOrderId']}\t"
	      f"{tradeAllHist['price']}\t"
	      f"{tradeAllHist['origQty']}\t"
	      f"{tradeAllHist['executedQty']}\t"
	      f"{tradeAllHist['cummulativeQuoteQty']}\t"
	      f"{tradeAllHist['status']}\t"
	      f"{tradeAllHist['timeInForce']}\t"
	      f"{tradeAllHist['side']}\t"
	      f"{tradeAllHist['type']}\t"
	      f"{tradeAllHist['stopPrice']}\t"
	      f"{tradeAllHist['isWorking']}")

# ----------------------------------------------------------------------------

def printTradeHistory(tradeHist, seq = 0, tot = 0):
	print(f"{seq}/{tot}) Symbol: [{tradeHist['symbol']}]")
	print(f"\tTime............: [{BU.completeMilliTime(tradeHist['time'])}]")
	print(f"\tOrder Id........: [{tradeHist['orderId']}]")
	print(f"\tId..............: [{tradeHist['id']}]")
	print(f"\tPrice...........: [{tradeHist['price']}]")
	print(f"\tQtd.............: [{tradeHist['qty']}]")
	print(f"\tQuote Qtd.......: [{tradeHist['quoteQty']}]")
	print(f"\tCommission......: [{tradeHist['commission']}]")
	print(f"\tCommission asset: [{tradeHist['commissionAsset']}]")
	print(f"\tBuyer...........: [{tradeHist['isBuyer']}]")
	print(f"\tMaker...........: [{tradeHist['isMaker']}]")
	print(f"\tTrade History...: [{tradeHist['isBestMatch']}]\n")

def printTradeHistoryXLSHEADER():
	print("Symbol\t"
	      "Time\t"
	      "Order Id\t"
	      "Id\t"
	      "Price\t"
	      "Qtd\t"
	      "Quote Qtd\t"
	      "Commission\t"
	      "Commission asset\t"
	      "Buyer\t"
	      "Maker\t"
	      "TradeHist")

def printTradeHistoryXLS(tradeHist):
	print(f"{tradeHist['symbol']}\t"
	      f"{BU.completeMilliTime(tradeHist['time'])}\t"
	      f"{tradeHist['orderId']}\t"
	      f"{tradeHist['id']}\t"
	      f"{tradeHist['price']}\t"
	      f"{tradeHist['qty']}\t"
	      f"{tradeHist['quoteQty']}\t"
	      f"{tradeHist['commission']}\t"
	      f"{tradeHist['commissionAsset']}\t"
	      f"{tradeHist['isBuyer']}\t"
	      f"{tradeHist['isMaker']}\t"
	      f"{tradeHist['isBestMatch']}")

# ----------------------------------------------------------------------------

def printMarginAssets(asset, seq = 0):
	print(f"{seq}) Asset: [{asset['asset']}]");
	print(f"\tBorrowed.: [{asset['borrowed']}]");
	print(f"\tFree.....: [{asset['free']}]");
	print(f"\tLocked...: [{asset['locked']}]");
	print(f"\tNet asset: [{asset['netAsset']}]\n");

def printMarginAssetsXLSHEADER():
	print("Asset\t"
	      "Borrowed\t"
	      "Free\t"
	      "Locked\t"
	      "Net asset")

def printMarginAssetsXLS(asset):
	print(f"{asset['asset']}\t"
	      f"{asset['borrowed']}\t"
	      f"{asset['free']}\t"
	      f"{asset['locked']}\t"
	      f"{asset['netAsset']}")

# ----------------------------------------------------------------------------

def printOrder(order, seq = 0, tot = 0):
	print(f"{seq}/{tot}) Order id [{order['orderId']}]:")
	print(f"\tSymbol......: [{order['symbol']}]")
	print(f"\tPrice.......: [{order['price']}]")
	print(f"\tQtd.........: [{order['origQty']}]")
	print(f"\tQtd executed: [{order['executedQty']}]")
	print(f"\tSide........: [{order['side']}]")
	print(f"\tType........: [{order['type']}]")
	print(f"\tStop price..: [{order['stopPrice']}]")
	print(f"\tIs working..: [{order['isWorking']}]\n")

def printOrderXLSHEADER():
	print("Order id\t"
	      "Symbol\t"
	      "Price\t"
	      "Qtd\t"
	      "Qtd executed\t"
	      "Side\t"
	      "Type\t"
	      "Stop price\t"
	      "Is working")

def printOrderXLS(order):
	print(f"{order['orderId']}\t"
	      f"{order['symbol']}\t"
	      f"{order['price']}\t"
	      f"{order['origQty']}\t"
	      f"{order['executedQty']}\t"
	      f"{order['side']}\t"
	      f"{order['type']}\t"
	      f"{order['stopPrice']}\t"
	      f"{order['isWorking']}")

# ----------------------------------------------------------------------------

def printAccount(accBalance):
	print(f"Asset balance [{accBalance['asset']}] | Free [{accBalance['free']}] | Locked [{accBalance['locked']}]")

def printAccountXLSHEADER():
	print("Asset balance\tFree\tLocked")

def printAccountXLS(accBalance):
	print(f"{accBalance['asset']}\t{accBalance['free']}\t{accBalance['locked']}")

# ----------------------------------------------------------------------------

def printSystemStatusXLS(sst):
	print(f"{sst['msg']}\t{'normal' if sst['status'] == 0 else 'system maintenance'}")

def printSystemStatus(sst):
	print(f"Message: [{sst['msg']}]")
	print(f"Status.: [{'normal' if sst['status'] == 0 else 'system maintenance'}]")

# ----------------------------------------------------------------------------

def printServerTimeXLS(st):
	print(f"{BU.completeMilliTime(st['serverTime'])}")

def printServerTime(st):
	print(f"Server Time: [{BU.completeMilliTime(st['serverTime'])}]")

# ----------------------------------------------------------------------------

def printProductsXLSHEADER():
	print("Symbol\tQuote Asset Name\tTraded Money\tBase Asset Unit\tBase Asset Name\tBase Asset\tTick Size\tPrev Close\tActive Buy\tHigh\tLow\tMatching Unit Type\tClose\tQuote Asset\tProduct Type\tOpen\tStatus\tActive\tMin Trade\tMin Qty\tActive Sell\tLast Aggregate Trade Id\tWithdraw Fee\tMarket\tVolume\tMarket Name\tDecimal Places\tParent Market\tParent Market Name\tQuote Asset Unit") 

def printProductsXLS(product):
	print(f"{product['symbol']}\t{product['quoteAssetName']}\t{product['tradedMoney']}\t{product['baseAssetUnit']}\t{product['baseAssetName']}\t{product['baseAsset']}\t{product['tickSize']}\t{product['prevClose']}\t{product['activeBuy']}\t{product['high']}\t{product['low']}\t{product['matchingUnitType']}\t{product['close']}\t{product['quoteAsset']}\t{product['productType']}\t{product['open']}\t{product['status']}\t{product['active']}\t{product['minTrade']}\t{product['minQty']}\t{product['activeSell']}\t{product['lastAggTradeId']}\t{product['withdrawFee']}\t{product['market']}\t{product['volume']}\t{product['marketName']}\t{product['decimalPlaces']}\t{product['parentMarket']}\t{product['parentMarketName']}\t{product['quoteAssetUnit']}")

def printProducts(product, seq, tot):
	print(f"{seq}/{tot}) Symbol: [{product['symbol']}]")
	print(f"\tQuote Asset Name.......: [{product['quoteAssetName']}]")
	print(f"\tTraded Money...........: [{product['tradedMoney']}]")
	print(f"\tBase Asset Unit........: [{product['baseAssetUnit']}]")
	print(f"\tBase Asset Name........: [{product['baseAssetName']}]")
	print(f"\tBase Asset.............: [{product['baseAsset']}]")
	print(f"\tTick Size..............: [{product['tickSize']}]")
	print(f"\tPrev Close.............: [{product['prevClose']}]")
	print(f"\tActive Buy.............: [{product['activeBuy']}]")
	print(f"\tHigh...................: [{product['high']}]")
	print(f"\tLow....................: [{product['low']}]")
	print(f"\tMatching Unit Type.....: [{product['matchingUnitType']}]")
	print(f"\tClose..................: [{product['close']}]")
	print(f"\tQuote Asset............: [{product['quoteAsset']}]")
	print(f"\tProduct Type...........: [{product['productType']}]")
	print(f"\tOpen...................: [{product['open']}]")
	print(f"\tStatus.................: [{product['status']}]")
	print(f"\tActive.................: [{product['active']}]")
	print(f"\tMin Trade..............: [{product['minTrade']}]")
	print(f"\tMin Qty................: [{product['minQty']}]")
	print(f"\tActive Sell............: [{product['activeSell']}]")
	print(f"\tLast Aggregate Trade Id: [{product['lastAggTradeId']}]")
	print(f"\tWithdraw Fee...........: [{product['withdrawFee']}]")
	print(f"\tMarket.................: [{product['market']}]")
	print(f"\tVolume.................: [{product['volume']}]")
	print(f"\tMarket Name............: [{product['marketName']}]")
	print(f"\tDecimal Places.........: [{product['decimalPlaces']}]")
	print(f"\tParent Market..........: [{product['parentMarket']}]")
	print(f"\tParent Market Name.....: [{product['parentMarketName']}]")
	print(f"\tQuote Asset Unit.......: [{product['quoteAssetUnit']}]")

# ----------------------------------------------------------------------------

def printListRateLimit(limits, seq = 0, tot = 0):
	print(f"{seq}/{tot}) Type: [{limits['rateLimitType']}]");
	print(f"Interval.......: [{limits['interval']}]");
	print(f"IntervalNum....: [{limits['intervalNum']}]");
	print(f"Limit..........: [{limits['limit']}]\n");

def printListSymbols(symbs, seq = 0, tot = 0):
	print(f"{seq}/{tot}) Symbol: [{symbs['symbol']}]");
	print(f"\tStatus........................: [{symbs['status']}]");
	print(f"\tBase Asset....................: [{symbs['baseAsset']}]");
	print(f"\tBase Asset Precision..........: [{symbs['baseAssetPrecision']}]");
	print(f"\tQuote Asset...................: [{symbs['quoteAsset']}]");
	print(f"\tQuote Precision...............: [{symbs['quotePrecision']}]");
	print(f"\tQuote Asset Precision.........: [{symbs['quoteAssetPrecision']}]");
	print(f"\tBase Commission Precision.....: [{symbs['baseCommissionPrecision']}]");
	print(f"\tQuote Commission Precision....: [{symbs['quoteCommissionPrecision']}]");
	print(f"\tIceberg Allowed...............: [{symbs['icebergAllowed']}]");
	print(f"\tOco Allowed...................: [{symbs['ocoAllowed']}]");
	print(f"\tQuote Order Qty Market Allowed: [{symbs['quoteOrderQtyMarketAllowed']}]");
	print(f"\tIs Spot Trading Allowed.......: [{symbs['isSpotTradingAllowed']}]");
	print(f"\tIs Margin Trading Allowed.....: [{symbs['isMarginTradingAllowed']}]");
	print(f"\tOrder Types...................: [{', '.join(symbs['orderTypes'])}]");
	print(f"\tPermissions...................: [{', '.join(symbs['permissions'])}]");

	print("\tFilters:");
	for n in symbs['filters']:
		print(f"\t\tType: [{n['filterType']}]");

		sf = n.get('minPrice', '')
		if sf != '': print(f"\t\t\tMin Price.........: [{sf}]");

		sf = n.get('maxPrice', '')
		if sf != '': print(f"\t\t\tMax Price..........: [{sf}]");

		sf = n.get('tickSize', '')
		if sf != '': print(f"\t\t\tTick Size..........: [{sf}]");

		sf = n.get('multiplierUp', '')
		if sf != '': print(f"\t\t\tMultiplier Up......: [{sf}]");

		sf = n.get('multiplierDown', '')
		if sf != '': print(f"\t\t\tMultiplier Down....: [{sf}]");

		sf = n.get('avgPriceMins', '')
		if sf != '': print(f"\t\t\tAvg Price Mins.....: [{sf}]");

		sf = n.get('minQty', '')
		if sf != '': print(f"\t\t\tMin Qty............: [{sf}]");

		sf = n.get('maxQty', '')
		if sf != '': print(f"\t\t\tMax Qty............: [{sf}]");

		sf = n.get('stepSize', '')
		if sf != '': print(f"\t\t\tStep Size..........: [{sf}]");

		sf = n.get('minNotional', '')
		if sf != '': print(f"\t\t\tMin Notional.......: [{sf}]");

		sf = n.get('applyToMarket', '')
		if sf != '': print(f"\t\t\tApply To Market....: [{sf}]");

		sf = n.get('avgPriceMins', '')
		if sf != '': print(f"\t\t\tAvg Price Mins.....: [{sf}]");

		sf = n.get('maxNumAlgoOrders', '')
		if sf != '': print(f"\t\t\tMax Num Algo Orders: [{sf}]");

def printListRateLimitXLSHEADER():
	print("Type\tInterval\tIntervalNum\tLimit")

def printListRateLimitXLS(limits):
	print(f"{limits['rateLimitType']}\t{limits['interval']}\t{limits['intervalNum']}\t{limits['limit']}");

def printListSymbolsXLSHEADER():
	print("Symbol\tStatus\tBase Asset\tBase Asset Precision\tQuote Asset\tQuote Precision\tQuote Asset Precision\tBase Commission Precision\tQuote Commission Precision\tIceberg Allowed\tOco Allowed\tQuote Order Qty Market Allowed\tIs Spot Trading Allowed\tIs Margin Trading Allowed\tOrder Types\tPermissions")

def printListSymbolsXLS(symb):
	print(f"{symb['symbol']}\t{symb['status']}\t{symb['baseAsset']}\t{symb['baseAssetPrecision']}\t{symb['quoteAsset']}\t{symb['quotePrecision']}\t{symb['quoteAssetPrecision']}\t{symb['baseCommissionPrecision']}\t{symb['quoteCommissionPrecision']}\t{symb['icebergAllowed']}\t{symb['ocoAllowed']}\t{symb['quoteOrderQtyMarketAllowed']}\t{symb['isSpotTradingAllowed']}\t{symb['isMarginTradingAllowed']}\t{', '.join(symb['orderTypes'])}\t{', '.join(symb['permissions'])}")

	print("\tFilters\tType\tMin Price\tMax Price\tTick Size\tMultiplier Up\tMultiplier Down\tAvg Price Mins\tMin Qty\tMax Qty\tStep Size\tMin Notional\tApply To Market\tAvg Price Mins\tMax Num Algo Orders")
	for n in symb['filters']:
		print(f"\t\t{n['filterType']}\t{n.get('minPrice', '')}\t{n.get('maxPrice', '')}\t{n.get('tickSize', '')}\t{n.get('multiplierUp', '')}\t{n.get('multiplierDown', '')}\t{n.get('avgPriceMins', '')}\t{n.get('minQty', '')}\t{n.get('maxQty', '')}\t{n.get('stepSize', '')}\t{n.get('minNotional', '')}\t{n.get('applyToMarket', '')}\t{n.get('avgPriceMins', '')}\t{n.get('maxNumAlgoOrders', '')}")

# ----------------------------------------------------------------------------

def print_OM_Sell_PlacedOrder(order):
	printPlacedOrder(order)

def print_OCO_Sell_PlacedOrder(order):
	printPlacedOrder(order)

def print_LO_Sell_PlacedOrder(order):
	printPlacedOrder(order)

def print_OCO_Buy_PlacedOrder(order):
	printPlacedOrder(order)

def print_OL_Buy_PlacedOrder(order):
	printPlacedOrder(order)

def print_OM_Buy_PlacedOrder(order):
	printPlacedOrder(order)

def print_Margin_PlacedOrder(order):
	printPlacedOrder(order)

def printPlacedOrder(order):
	print(f"Symbol: [{order['symbol']}")
	print(f"\tSide.................: [{order['side']}")
	print(f"\tType.................: [{order['type']}")
	print(f"\tTransaction Time.....: [{order['transactTime']}")
	print(f"\tPrice................: [{order['price']}")
	print(f"\tOrig Qtd.............: [{order['origQty']}")
	print(f"\tExecuted Qtd.........: [{order['executedQty']}")
	print(f"\tCummulative Quote Qtd: [{order['cummulativeQuoteQty']}")
	print(f"\tStatus...............: [{order['status']}")
	print(f"\tTime In Force........: [{order['timeInForce']}")
	print(f"\tOrder Id.............: [{order['orderId']}")
	print(f"\tClient Order Id......: [{order['clientOrderId']}")

	if 'fills' not in order:
		return

	for f in order['fills']:
		print(f"\t\tPrice...........: [{f['price']}")
		print(f"\t\tQty.............: [{f['qty']}")
		print(f"\t\tCommission......: [{f['commission']}")
		print(f"\t\tCommission Asset: [{f['commissionAsset']}")
