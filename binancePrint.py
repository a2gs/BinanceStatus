#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota
# andre.scota@gmail.com
# MIT license

import binanceUtil as BU

def printHelp(execName):
	print("")
	print("0) Reference")
	print("[ASSET] = BTC, USDT, BNB, ETH ...")
	print("[SYMBOL] = BTCUSDT, BNBBTC, ... (you can see them all with \'-l\' option)")
	print("")
	print("1) BINANCE INFORMATION AND MARKET")
	print("-B\n\tBinance Informations (server time and server status).\n")
	print("-p\n\t24 hour price change statistics.\n")
	print("-pa [SYMBOL]\n\tCurrent average price for a symbol.\n")
	print("-l\n\tList of symbols and rate/limits.\n")
	print("-v [SYMBOL] [INTERVAL] [QTD CANDLES]\n\tInformation (prices) about a symbol.\n\t[interval] is one of \'1m\', \'3m\', \'5m\', \'15m\', \'30m\', \'2h\', \'4h\', \'6h\', \'8h\', \'12h\', \'1h\', \'1d\', \'3d\', \'1w\', \'1M\'.\n")
	print("-V [SYMBOL]\n\tInformation (details) about a symbol.")
	print("")
	print("2) ACCOUNT INFORMATION")
	print("-i\n\tSpot and Margin account information.\n")
	print("-D\n\tAccount details (trade fees, assets details, etc).\n")
	print("-sal\n\tList sub-accounts.")
	print("-sah [EMAIL]\n\tSub-accounts transfer history.")
	print("-saa [EMAIL] [SYMBOL]\n\tSub-accounts assets (symbol is optional).")
	print("")
	print("2.1) SPOT")
	print("-os [SYMBOL]\n\tSpot open orders.\n")
	print("-ba [ASSET]\n\tAccount balance by asset. Query max borrow and transfer-out margin amount for an asset.\n")
	print("-h [SYMBOL]\n\tAccount history (trades, dusts, etc).\n")
	print("-ht [SYMBOL]\n\tLast 500 older trades.")
	print("")
	print("2.2) MARGIN")
	print("-om [SYMBOL]\n\tMargin open orders.\n")
	print("-ml [SYMBOL]\n\tMargin symbol info.\n")
	print("-mp [SYMBOL]\n\tMargin price index.\n")
	print("-mh [SYMBOL] [ORDER ID] [LIMIT]\n\tQuery all margin accounts orders (order id and limit can be null).\n")
	print("-mm [ASSET]\n\tQuery margin asset.\n")
	print("-mt [SYMBOL] [FROM ID] [LIMIT]\n\tQuery margin accounts trades (from id and limit can be null).\n")
	print("-ma [ASSET]\n\tQuery max transfer-out amount.\n")
	print("-mi [ASSET] [AMOUNT]\n\tExecute transfer between spot account and margin account.\n")
	print("-mo [ASSET] [AMOUNT]\n\tExecute transfer between margin account and spot account.")
	print("")
	print("3) DEPOSIT/WITHDRAW")
	print("-d [ASSET]\n\tDeposit address.\n")
	print("-dh [ASSET]\n\tDeposit history (Asset can be null).\n")
	print("-w [ASSET] [ADDRESS] [AMOUNT]\n\tSubmit a withdraw request.\n")
	print("-wh [ASSET]\n\tWithdraw history (Asset can be null).")
	print("")
	print("4) TRADE")
	print("-O [ASSET] [ORDER ID]\n\tCheck an order\'s status.")
	print("")
	print("4.1) SPOT")
	print("-s\n\tPlace a SPOT sell order.")
	print("\t\t-s MARKET [SYMBOL] [QTD] [-TEST]")
	print("\t\t-s LIMIT [SYMBOL] [QTD] [PRICE] [-TEST]")
	print("\t\t-s STOP [SYMBOL] [QTD] [PRICE] [STOP PRICE]")
	print("\t\t-s OCO [SYMBOL] [QTD] [PRICE] [STOP PRICE] [LIMIT]")
	print("")
	print("-b\n\tPlace a SPOT buy order.")
	print("\t\t-b MARKET [SYMBOL] [QTD] [-TEST]")
	print("\t\t-b LIMIT [SYMBOL] [QTD] [PRICE] [-TEST]")
	print("\t\t-b STOP [SYMBOL] [QTD] [PRICE] [STOP PRICE]")
	print("\t\t-b OCO [SYMBOL] [QTD] [PRICE] [STOP PRICE] [LIMIT]")
	print("")
	print("-c [SYMBOL] [ORDER ID]\n\tCancel a SPOT order.")
	print("")
	print("4.2) MARGIN")
	print("-sm\n\tPlace a MARGIN sell order.")
	print("\t\t-sm MARKET [SYMBOL] [QTD]")
	print("\t\t-sm LIMIT [SYMBOL] [QTD] [PRICE]")
	print("\t\t-sm STOP [SYMBOL] [QTD] [PRICE] [STOP PRICE]   (Stop take profit limit")
	print("\t\t-sm OCO [SYMBOL] [QTD] [PRICE] [STOP PRICE] [LIMIT]")
	print("")
	print("-bm\n\tPlace a MARGIN buy order.")
	print("\t\t-bm MARKET [SYMBOL] [QTD]")
	print("\t\t-bm LIMIT [SYMBOL] [QTD] [PRICE]")
	print("\t\t-bm STOP [SYMBOL] [QTD] [PRICE] [STOP PRICE]   (Stop take profit limit)")
	print("\t\t-bm OCO [SYMBOL] [QTD] [PRICE] [STOP PRICE] [LIMIT]")
	print("")
	print("-cm [SYMBOL] [ORDER ID]\n\tCancel a MARGIN order.")
	print("")
	print("5) BOOK")
	print("-bp [SYMBOL] [LIMIT]\n\tGet the Order Book for the market.\n")
	print("-bt [SYMBOL]\n\tLatest ticker/price for a symbol.")
	print("")
	print("6) MISCELLANEOUS")
	print("[...] -xls > output.xls\n\tOutput with TAB separator.")
	print("[...] -Y\n\tForce ALL CONFIRMATIONS = YES")
	print("[...] -TS\n\tPrint Binance timestamp, does not convert to human datetime.")

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

def printOrderBook(line):
	print(f"{line[0][1]}\t{line[0][0]}\t|\t{line[1][0]}\t{line[1][1]}")

def printOrderBookXLSHEADER():
	print("BIDS\t\t\tASKS")
	print("Qtd\tPrice\t\tPrice\tQtd")

def printOrderBookXLS(line):
	print(f"{line[0][1]}\t{line[0][0]}\t\t{line[1][0]}\t{line[1][1]}")

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
	print(f"\tDeposit status......? [{detAss['depositStatus']}]");
	dt = detAss.get('depositTip', '')
	if dt != '':
		print(f"\tDeposit tip.........: [{dt}]");
	print(f"\tWithdraw fee........: [{detAss['withdrawFee']}]");
	print(f"\tWithdraw status.....? [{detAss['withdrawStatus']}]\n");

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
	print(f"\tIs working...........? [{tradeAllHist['isWorking']}]\n")

def printTradeAllHistXLSHEADER():
	print("Symbol\t"
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

def printMarginTrades(mt, seq = 0, tot = 0):
	print(f"{seq}/{tot}) Symbol: [{mt['symbol']}]")
	print(f"\tId..............: [{mt['id']}]")
	print(f"\tOrder Id........: [{mt['orderId']}]")
	print(f"\tPrice...........: [{mt['price']}]")
	print(f"\tQtd.............: [{mt['qty']}]")
	print(f"\tCommission......: [{mt['commission']}]")
	print(f"\tAsset commission: [{mt['commissionAsset']}]")
	print(f"\tIs Best Match...: [{mt['isBestMatch']}]")
	print(f"\tIs Buyer........: [{mt['isBuyer']}]")
	print(f"\tIs Maker........: [{mt['isMaker']}]")
	print(f"\tTime............: [{BU.completeMilliTime(mt['time'])}]")

def printMarginTradesXLSHEADER():
	print("Symbol\tId\tOrder Id\tPrice\tQty\tTime\tCommission\tCommissionAsset\tIs Best Match\tIs Buyer\tIs Maker")

def printMarginTradesXLS(mt):
	print(f"{mt['symbol']}\t"
	      f"{mt['id']}\t"
	      f"{mt['orderId']}\t"
	      f"{mt['price']}\t"
	      f"{mt['qty']}\t"
	      f"{mt['time']}\t"
	      f"{mt['commission']}\t"
	      f"{mt['commissionAsset']}\t"
	      f"{mt['isBestMatch']}\t"
	      f"{mt['isBuyer']}\t"
	      f"{BU.completeMilliTime(mt['time'])}")

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
	print(f"{seq}/{tot}) Order id: [{order['orderId']}]")
	print(f"\tSymbol......: [{order['symbol']}]")
	print(f"\tPrice.......: [{order['price']}]")
	print(f"\tQtd.........: [{order['origQty']}]")
	print(f"\tQtd executed: [{order['executedQty']}]")
	print(f"\tSide........: [{order['side']}]")
	print(f"\tType........: [{order['type']}]")
	print(f"\tStop price..: [{order['stopPrice']}]")
	print(f"\tIs working..? [{order['isWorking']}]\n")

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

def printHistoricalTradesXLSHEADER():
	print("Id\tPrice\tQtyt\tQuote Qty\tTime\tIs Buyer Maker\tIs Best Match")

def printHistoricalTradesXLS(trade):
	print(f"{trade['id']}\t{trade['price']}\t{trade['qty']}\t{trade['quoteQty']}\t{BU.completeMilliTime(trade['time'])}\t{trade['isBuyerMaker']}\t{trade['isBestMatch']}")

def printHistoricalTrades(trade, seq = 0, tot = 0):
	print(f"{seq}/{tot}) Id: [{trade['id']}]")
	print(f"Price.........: [{trade['price']}]")
	print(f"Qtd...........: [{trade['qty']}]")
	print(f"Quote Qtd.....: [{trade['quoteQty']}]")
	print(f"Time..........: [{BU.completeMilliTime(trade['time'])}]")
	print(f"Is Buyer Maker? [{trade['isBuyerMaker']}]")
	print(f"Is Best Match.? [{trade['isBestMatch']}]\n")

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
	print(f"\tActive.................? [{product['active']}]")
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
	print(f"\tIceberg Allowed...............? [{symbs['icebergAllowed']}]");
	print(f"\tOco Allowed...................? [{symbs['ocoAllowed']}]");
	print(f"\tQuote Order Qty Market Allowed? [{symbs['quoteOrderQtyMarketAllowed']}]");
	print(f"\tIs Spot Trading Allowed.......? [{symbs['isSpotTradingAllowed']}]");
	print(f"\tIs Margin Trading Allowed.....? [{symbs['isMarginTradingAllowed']}]");
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
		if sf != '': print(f"\t\t\tApply To Market....? [{sf}]");

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

def printsubAccountsListXLSHEADER():
	print("Email\tStatus\tActivated\tMobile\tAuth\tCreate Time")

def printsubAccountsListXLS(n):
	print(f"{n['email']}\t{n['status']}\t{n['activated']}\t{n['mobile']}\t{n['gAuth']}\t{n['createTime']}")

def printsubAccountsList(n, i, totSal):
	print(f"{i}/{totSal}) Email: [{n['email']}]")
	print(f"Status.....: [{n['status']}]")
	print(f"Activated..: [{n['activated']}]")
	print(f"Mobile.....: [{n['mobile']}]")
	print(f"Auth.......: [{n['gAuth']}]")
	print(f"Create Time: [{BU.completeMilliTime(n['createTime'])}]")

def printsubAccountTransferHistoryXLSHEADER():
	print("From\tTo\tAsset\tQty\tTime")

def printsubAccountTransferHistoryXLS(n):
	print(f"{n['from']}\t{n['to']}\t{n['asset']}\t{n['qty']}\t{BU.completeMilliTime(n['time'])}")

def printsubAccountTransferHistory(n, i, totSath):
	print(f"{i}/{totSath}) From: [{n['from']}]")
	print(f"To...: [{n['to']}]")
	print(f"Asset: [{n['asset']}]")
	print(f"Qty..: [{n['qty']}]")
	print(f"Time.: [{BU.completeMilliTime(n['time'])}]")

def printsubAccountsAssetsXLSHEADER():
	print("Asset\tFree\tLocked")

def printsubAccountsAssetsXLS(n):
	print(f"{n['asset']}\t{n['free']}\t{n['locked']}")

def printsubAccountsAssets(n, i, totSaa):
	print(f"{i}/{totSaa}) Asset: [{n['asset']}]")
	print(f"Free..: [{n['free']}]")
	print(f"Locked: [{n['locked']}]")

# ----------------------------------------------------------------------------

def printPlacedOrder(order):
	print(f"Symbol: [{order['symbol']}]")
	print(f"\tSide.................: [{order['side']}]")
	print(f"\tType.................: [{order['type']}]")
	print(f"\tTransaction Time.....: [{order['transactTime']}]")
	print(f"\tPrice................: [{order['price']}]")
	print(f"\tOrig Qtd.............: [{order['origQty']}]")
	print(f"\tExecuted Qtd.........: [{order['executedQty']}]")
	print(f"\tCummulative Quote Qtd: [{order['cummulativeQuoteQty']}]")
	print(f"\tStatus...............: [{order['status']}]")
	print(f"\tTime In Force........: [{order['timeInForce']}]")
	print(f"\tOrder Id.............: [{order['orderId']}]")
	print(f"\tClient Order Id......: [{order['clientOrderId']}]")

	if 'fills' not in order:
		return

	for f in order['fills']:
		print(f"\t\tPrice...........: [{f['price']}]")
		print(f"\t\tQty.............: [{f['qty']}]")
		print(f"\t\tCommission......: [{f['commission']}]")
		print(f"\t\tCommission Asset: [{f['commissionAsset']}]")
