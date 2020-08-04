#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota
# andre.scota@gmail.com
# MIT license

import binanceUtil as BU

def printHelp(execName):
	BU.errPrint("")
	BU.errPrint("0) Reference")
	BU.errPrint("[ASSET] = BTC, USDT, BNB, ETH ...")
	BU.errPrint("[SYMBOL] = BTCUSDT, BNBBTC, ... (you can see them all with \'-l\' option)")
	BU.errPrint("")
	BU.errPrint("1) BINANCE INFORMATION AND MARKET")
	BU.errPrint("-B\n\tBinance Informations (server time and server status).\n")
	BU.errPrint("-p\n\t24 hour price change statistics.\n")
	BU.errPrint("-pa [SYMBOL]\n\tCurrent average price for a symbol.\n")
	BU.errPrint("-l\n\tList of symbols and rate/limits.\n")
	BU.errPrint("-v [SYMBOL] [INTERVAL] [QTD CANDLES]\n\tInformation (prices) about a symbol.\n\t[interval] is one of \'1m\', \'3m\', \'5m\', \'15m\', \'30m\', \'2h\', \'4h\', \'6h\', \'8h\', \'12h\', \'1h\', \'1d\', \'3d\', \'1w\', \'1M\'.\n")
	BU.errPrint("-V [SYMBOL]\n\tInformation (details) about a symbol.")
	BU.errPrint("")
	BU.errPrint("2) ACCOUNT INFORMATION")
	BU.errPrint("-i\n\tSpot and Margin account information.\n")
	BU.errPrint("-D\n\tAccount details (trade fees, assets details, etc).\n")
	BU.errPrint("-sal\n\tList sub-accounts.")
	BU.errPrint("-sah [EMAIL]\n\tSub-accounts transfer history.")
	BU.errPrint("-saa [EMAIL] [SYMBOL]\n\tSub-accounts assets (symbol is optional).")
	BU.errPrint("")
	BU.errPrint("2.1) SPOT")
	BU.errPrint("-os [SYMBOL]\n\tSpot open orders.\n")
	BU.errPrint("-ba [ASSET]\n\tAccount balance by asset. Query max borrow and transfer-out margin amount for an asset.\n")
	BU.errPrint("-h [SYMBOL]\n\tAccount history (trades, dusts, etc).\n")
	BU.errPrint("-ht [SYMBOL]\n\tLast 500 older trades.")
	BU.errPrint("")
	BU.errPrint("2.2) MARGIN")
	BU.errPrint("-om [SYMBOL]\n\tMargin open orders.\n")
	BU.errPrint("-ml [SYMBOL]\n\tMargin symbol info.\n")
	BU.errPrint("-mp [SYMBOL]\n\tMargin price index.\n")
	BU.errPrint("-mh [SYMBOL] [ORDER ID] [LIMIT]\n\tQuery all margin accounts orders (order id and limit can be null).\n")
	BU.errPrint("-mm [ASSET]\n\tQuery margin asset.\n")
	BU.errPrint("-mt [SYMBOL] [FROM ID] [LIMIT]\n\tQuery margin accounts trades (from id and limit can be null).\n")
	BU.errPrint("-ma [ASSET]\n\tQuery max transfer-out amount.\n")
	BU.errPrint("-mi [ASSET] [AMOUNT]\n\tExecute transfer between spot account and margin account.\n")
	BU.errPrint("-mo [ASSET] [AMOUNT]\n\tExecute transfer between margin account and spot account.")
	BU.errPrint("")
	BU.errPrint("3) DEPOSIT/WITHDRAW")
	BU.errPrint("-d [ASSET]\n\tDeposit address.\n")
	BU.errPrint("-dh [ASSET]\n\tDeposit history (Asset can be null).\n")
	BU.errPrint("-w [ASSET] [ADDRESS] [AMOUNT]\n\tSubmit a withdraw request.\n")
	BU.errPrint("-wh [ASSET]\n\tWithdraw history (Asset can be null).")
	BU.errPrint("")
	BU.errPrint("4) TRADE")
	BU.errPrint("-O [ASSET] [ORDER ID]\n\tCheck an order\'s status.")
	BU.errPrint("")
	BU.errPrint("4.1) SPOT")
	BU.errPrint("-s\n\tPlace a SPOT sell order.")
	BU.errPrint("\t\t-s MARKET [SYMBOL] [QTD] [-TEST]")
	BU.errPrint("\t\t-s LIMIT [SYMBOL] [QTD] [PRICE] [-TEST]")
	BU.errPrint("\t\t-s STOP [SYMBOL] [QTD] [PRICE] [STOP PRICE]")
	BU.errPrint("\t\t-s OCO [SYMBOL] [QTD] [PRICE] [STOP PRICE] [LIMIT]")
	BU.errPrint("")
	BU.errPrint("-b\n\tPlace a SPOT buy order.")
	BU.errPrint("\t\t-b MARKET [SYMBOL] [QTD] [-TEST]")
	BU.errPrint("\t\t-b LIMIT [SYMBOL] [QTD] [PRICE] [-TEST]")
	BU.errPrint("\t\t-b STOP [SYMBOL] [QTD] [PRICE] [STOP PRICE]")
	BU.errPrint("\t\t-b OCO [SYMBOL] [QTD] [PRICE] [STOP PRICE] [LIMIT]")
	BU.errPrint("")
	BU.errPrint("-c [SYMBOL] [ORDER ID]\n\tCancel a SPOT order.")
	BU.errPrint("")
	BU.errPrint("4.2) MARGIN")
	BU.errPrint("-sm\n\tPlace a MARGIN sell order.")
	BU.errPrint("\t\t-sm MARKET [SYMBOL] [QTD]")
	BU.errPrint("\t\t-sm LIMIT [SYMBOL] [QTD] [PRICE]")
	BU.errPrint("\t\t-sm STOP [SYMBOL] [QTD] [PRICE] [STOP PRICE]   (Stop take profit limit")
	BU.errPrint("\t\t-sm OCO [SYMBOL] [QTD] [PRICE] [STOP PRICE] [LIMIT]")
	BU.errPrint("")
	BU.errPrint("-bm\n\tPlace a MARGIN buy order.")
	BU.errPrint("\t\t-bm MARKET [SYMBOL] [QTD]")
	BU.errPrint("\t\t-bm LIMIT [SYMBOL] [QTD] [PRICE]")
	BU.errPrint("\t\t-bm STOP [SYMBOL] [QTD] [PRICE] [STOP PRICE]   (Stop take profit limit)")
	BU.errPrint("\t\t-bm OCO [SYMBOL] [QTD] [PRICE] [STOP PRICE] [LIMIT]")
	BU.errPrint("")
	BU.errPrint("-cm [SYMBOL] [ORDER ID]\n\tCancel a MARGIN order.")
	BU.errPrint("")
	BU.errPrint("5) BOOK")
	BU.errPrint("-bp [SYMBOL] [LIMIT]\n\tGet the Order Book for the market.\n")
	BU.errPrint("-bt [SYMBOL]\n\tLatest ticker/price for a symbol.")
	BU.errPrint("")
	BU.errPrint("6) MISCELLANEOUS")
	BU.errPrint("[...] -xls 2> output.xls\n\tOutput with TAB separator.")
	BU.errPrint("[...] -Y\n\tForce ALL CONFIRMATIONS = YES")
	BU.errPrint("[...] -TS\n\tPrint Binance timestamp, does not convert to human datetime.")

# ----------------------------------------------------------------------------

def printWithdrawResponseXLSHEADER():
	BU.errPrint("Message\tSuccess\tId")

def printWithdrawResponseXLS(withdrawReq):
	BU.errPrint(f"{withdrawReq['msg']}\t{withdrawReq['success']}\t{withdrawReq['id']}")

def printWithdrawResponse(withdrawReq):
	BU.errPrint(f"Message: [{withdrawReq['msg']}]")
	BU.errPrint(f"Success: [{withdrawReq['success']}]")
	BU.errPrint(f"Id.....: [{withdrawReq['id']}]")

# ----------------------------------------------------------------------------

def printWithdrawHistoryXLSHEADER():
	BU.errPrint("Amount\tAsset\tAddress\tApply Time\tStatus")

def printWithdrawHistoryXLS(withdraw):
	BU.errPrint(f"{withdraw['amount']}\t{withdraw['asset']}\t{withdraw['address']}\t{BU.completeMilliTime(withdraw['insertTime'])}\t{withdraw['status']}")

def printWithdrawHistory(withdraw):
	BU.errPrint(f"Asset: [{withdraw['asset']}]")
	BU.errPrint(f"\tAmount.....: [{withdraw['amount']}]")
	BU.errPrint(f"\tAddress....: [{withdraw['address']}]")
	BU.errPrint(f"\tApply Time.: [{BU.completeMilliTime(withdraw['applyTime'])}]")
	BU.errPrint(f"\tStatus.....: [{withdraw['status']}]")

# ----------------------------------------------------------------------------

def printDepositHistoryXLSHEADER():
	BU.errPrint("Amount\tAsset\tInsert Time\tStatus")

def printDepositHistoryXLS(deposits):
	BU.errPrint(f"{deposits['amount']}\t{deposits['asset']}\t{BU.completeMilliTime(deposits['insertTime'])}\t{deposits['status']}")

def printDepositHistory(deposits):
	BU.errPrint(f"Asset: [{deposits['asset']}]")
	BU.errPrint(f"\tAmount.....: [{deposits['amount']}]")
	BU.errPrint(f"\tInsert Time: [{BU.completeMilliTime(deposits['insertTime'])}]")
	BU.errPrint(f"\tStatus.....: [{deposits['status']}]")

# ----------------------------------------------------------------------------

def printDepositAddress(depAdd):
	BU.errPrint(f"Asset......: [{depAdd['asset']}]")
	BU.errPrint(f"Address....: [{depAdd['address']}]")
	BU.errPrint(f"Success....: [{depAdd['success']}]")
	BU.errPrint(f"Address Tag: [{depAdd['addressTag']}]")

def printDepositAddressXLSHEADER():
	BU.errPrint("Asset\tAddress\tSuccess\tAddress Tag")

def printDepositAddressXLS(depAdd):
	BU.errPrint(f"{depAdd['asset']}\t{depAdd['address']}\t{depAdd['success']}\t{depAdd['addressTag']}")

# ----------------------------------------------------------------------------

def printMarginOrder(order, seq = 0, tot = 0):
	printOrder(order, seq, tot)

def printMarginOrderXLSHEADER():
	printOrderXLSHEADER()

def printMarginOrderXLS(order):
	printOrderXLS(order)

# ----------------------------------------------------------------------------

def printInfoSymbolValues(symbPrc, seq = 0, tot = 0):
	BU.errPrint(f"{seq}/{tot}) Candle:")
	BU.errPrint(f"Open time...................: [{BU.completeMilliTime(symbPrc[0])}]")
	BU.errPrint(f"Close time..................: [{BU.completeMilliTime(symbPrc[6])}]")
	BU.errPrint(f"High........................: [{symbPrc[2]}]")
	BU.errPrint(f"Open........................: [{symbPrc[1]}]")
	BU.errPrint(f"Close.......................: [{symbPrc[4]}]")
	BU.errPrint(f"Low.........................: [{symbPrc[3]}]")
	BU.errPrint(f"Volume......................: [{symbPrc[5]}]")
	BU.errPrint(f"Quote asset volume..........: [{symbPrc[7]}]")
	BU.errPrint(f"Number of trades............: [{symbPrc[8]}]")
	BU.errPrint(f"Taker buy base asset volume.: [{symbPrc[9]}]")
	BU.errPrint(f"Taker buy quote asset volume: [{symbPrc[10]}]\n")

def printInfoSymbolValuesXLSHEADER():
	BU.errPrint("Open time\t"
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
	BU.errPrint(f"{BU.completeMilliTime(symbPrc[0])}\t"
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
	BU.errPrint(f"{line[0][1]}\t{line[0][0]}\t|\t{line[1][0]}\t{line[1][1]}")

def printOrderBookXLSHEADER():
	BU.errPrint("BIDS\t\t\tASKS")
	BU.errPrint("Qtd\tPrice\t\tPrice\tQtd")

def printOrderBookXLS(line):
	BU.errPrint(f"{line[0][1]}\t{line[0][0]}\t\t{line[1][0]}\t{line[1][1]}")

# ----------------------------------------------------------------------------

def print24hPrcChangSts(priceSts, seq = 0, tot = 0):
	BU.errPrint(f"{seq}/{tot}) Symbol: [{priceSts['symbol']}]")
	BU.errPrint(f"\tPrice Change..........: [{priceSts['priceChange']}]")
	BU.errPrint(f"\tPrice Change Percent..: [{priceSts['priceChangePercent']}]")
	BU.errPrint(f"\tWeighted Avarege Price: [{priceSts['weightedAvgPrice']}]")
	BU.errPrint(f"\tPrevious Close Price..: [{priceSts['prevClosePrice']}]")
	BU.errPrint(f"\tLast Price............: [{priceSts['lastPrice']}]")
	BU.errPrint(f"\tLast Qty..............: [{priceSts['lastQty']}]")
	BU.errPrint(f"\tBid Price.............: [{priceSts['bidPrice']}]")
	BU.errPrint(f"\tBid Qty...............: [{priceSts['bidQty']}]")
	BU.errPrint(f"\tAsk Price.............: [{priceSts['askPrice']}]")
	BU.errPrint(f"\tAsk Qty...............: [{priceSts['askQty']}]")
	BU.errPrint(f"\tOpen Price............: [{priceSts['openPrice']}]")
	BU.errPrint(f"\tHigh Price............: [{priceSts['highPrice']}]")
	BU.errPrint(f"\tLow Price.............: [{priceSts['lowPrice']}]")
	BU.errPrint(f"\tVolume................: [{priceSts['volume']}]")
	BU.errPrint(f"\tQuote Volume..........: [{priceSts['quoteVolume']}]")
	BU.errPrint(f"\tOpen Time.............: [{BU.completeMilliTime(priceSts['openTime'])}]")
	BU.errPrint(f"\tClose Time............: [{BU.completeMilliTime(priceSts['closeTime'])}]")
	BU.errPrint(f"\tFirst Id..............: [{priceSts['firstId']}]")
	BU.errPrint(f"\tLast Id...............: [{priceSts['lastId']}]")
	BU.errPrint(f"\tCount.................: [{priceSts['count']}]\n")

def print24hPrcChangStsXLSHEADER():
	BU.errPrint("Symbol\t"
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
	BU.errPrint(f"{priceSts['symbol']}\t"
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
	BU.errPrint(f"{seq}/{tot}) Total transfered BNB amount for this exchange: [{order['transfered_total']}]")
	BU.errPrint(f"\tTotal service charge amount for this exchange: [{order['service_charge_total']}]")
	BU.errPrint(f"\tTransaction Id...............................: [{order['tran_id']}]")
	BU.errPrint(f"\tOperate time.................................: [{order['operate_time']}]")
	BU.errPrint("\tLogs:")
	for logs in order['logs']:
		BU.errPrint(f"\t\tFrom Asset...........: [{logs['fromAsset']}]")
		BU.errPrint(f"\t\tAmount...............: [{logs['amount']}]")
		BU.errPrint(f"\t\tService Charge Amount: [{logs['serviceChargeAmount']}]")
		BU.errPrint(f"\t\tTransfered Amount....: [{logs['transferedAmount']}]")
		BU.errPrint(f"\t\tUId..................: [{logs['uid']}]\n")

# ----------------------------------------------------------------------------

def printDetailsAssets(ass, detAss, seq = 0, tot = 0):
	BU.errPrint(f"{seq}/{tot}) Asset: [{ass}]");
	BU.errPrint(f"\tMin. withdraw amount: [{detAss['minWithdrawAmount']}]");
	BU.errPrint(f"\tDeposit status......? [{detAss['depositStatus']}]");
	dt = detAss.get('depositTip', '')
	if dt != '':
		BU.errPrint(f"\tDeposit tip.........: [{dt}]");
	BU.errPrint(f"\tWithdraw fee........: [{detAss['withdrawFee']}]");
	BU.errPrint(f"\tWithdraw status.....? [{detAss['withdrawStatus']}]\n");

def printDetailsAssetsXLSHEADER():
	BU.errPrint("Asset\tMin. withdraw amount\tDeposit status\tDeposit tip\tWithdraw fee\tWithdraw status")

def printDetailsAssetsXLS(ass, detAss):
	BU.errPrint(f"{ass}\t{detAss['minWithdrawAmount']}\t{detAss['depositStatus']}\t{detAss.get('depositTip', '')}\t{detAss['withdrawFee']}\t{detAss['withdrawStatus']}");

# ----------------------------------------------------------------------------

def printTradeFee(tf, seq = 0, tot = 0):
	BU.errPrint(f"{seq}/{tot}) Symbol: [{tf['symbol']}]\tMaker: [{tf['maker']}]\tTaker: [{tf['taker']}]");

def printTradeFeeXLSHEADER():
	BU.errPrint("Symbol\t"
	      "Maker\t"
	      "Taker");

def printTradeFeeXLS(tf):
	BU.errPrint(f"{tf['symbol']}\t"
	      f"{tf['maker']}\t"
	      f"{tf['taker']}");

# ----------------------------------------------------------------------------

def printTradeAllHist(tradeAllHist, seq = 0, tot = 0):
	BU.errPrint(f"{seq}/{tot}) Symbol: [{tradeAllHist['symbol']}]")
	BU.errPrint(f"\tTime.................: [{BU.completeMilliTime(tradeAllHist['time'])}]")
	BU.errPrint(f"\tUpdate time..........: [{BU.completeMilliTime(tradeAllHist['updateTime'])}]")
	BU.errPrint(f"\tOrder Id.............: [{tradeAllHist['orderId']}]")
#	BU.errPrint(f"\tOrder list Id........: [{tradeAllHist['orderListId']}]")
	BU.errPrint(f"\tClient Order Id......: [{tradeAllHist['clientOrderId']}]")
	BU.errPrint(f"\tPrice................: [{tradeAllHist['price']}]")
	BU.errPrint(f"\tOrig Qtd.............: [{tradeAllHist['origQty']}]")
	BU.errPrint(f"\tExecuted Qtd.........: [{tradeAllHist['executedQty']}]")
	BU.errPrint(f"\tCummulative Quote Qtd: [{tradeAllHist['cummulativeQuoteQty']}]")
	BU.errPrint(f"\tStatus...............: [{tradeAllHist['status']}]")
	BU.errPrint(f"\tTime in Force........: [{tradeAllHist['timeInForce']}]")
	BU.errPrint(f"\tSide.................: [{tradeAllHist['side']}]")
	BU.errPrint(f"\tType.................: [{tradeAllHist['type']}]")
	BU.errPrint(f"\tStop Price...........: [{tradeAllHist['stopPrice']}]")
	BU.errPrint(f"\tIs working...........? [{tradeAllHist['isWorking']}]\n")

def printTradeAllHistXLSHEADER():
	BU.errPrint("Symbol\t"
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
	BU.errPrint(f"{tradeAllHist['symbol']}\t"
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
	BU.errPrint(f"{seq}/{tot}) Symbol: [{mt['symbol']}]")
	BU.errPrint(f"\tId..............: [{mt['id']}]")
	BU.errPrint(f"\tOrder Id........: [{mt['orderId']}]")
	BU.errPrint(f"\tPrice...........: [{mt['price']}]")
	BU.errPrint(f"\tQtd.............: [{mt['qty']}]")
	BU.errPrint(f"\tCommission......: [{mt['commission']}]")
	BU.errPrint(f"\tAsset commission: [{mt['commissionAsset']}]")
	BU.errPrint(f"\tIs Best Match...: [{mt['isBestMatch']}]")
	BU.errPrint(f"\tIs Buyer........: [{mt['isBuyer']}]")
	BU.errPrint(f"\tIs Maker........: [{mt['isMaker']}]")
	BU.errPrint(f"\tTime............: [{BU.completeMilliTime(mt['time'])}]")

def printMarginTradesXLSHEADER():
	BU.errPrint("Symbol\tId\tOrder Id\tPrice\tQty\tTime\tCommission\tCommissionAsset\tIs Best Match\tIs Buyer\tIs Maker")

def printMarginTradesXLS(mt):
	BU.errPrint(f"{mt['symbol']}\t"
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
	BU.errPrint(f"{seq}/{tot}) Symbol: [{tradeHist['symbol']}]")
	BU.errPrint(f"\tTime............: [{BU.completeMilliTime(tradeHist['time'])}]")
	BU.errPrint(f"\tOrder Id........: [{tradeHist['orderId']}]")
	BU.errPrint(f"\tId..............: [{tradeHist['id']}]")
	BU.errPrint(f"\tPrice...........: [{tradeHist['price']}]")
	BU.errPrint(f"\tQtd.............: [{tradeHist['qty']}]")
	BU.errPrint(f"\tQuote Qtd.......: [{tradeHist['quoteQty']}]")
	BU.errPrint(f"\tCommission......: [{tradeHist['commission']}]")
	BU.errPrint(f"\tCommission asset: [{tradeHist['commissionAsset']}]")
	BU.errPrint(f"\tBuyer...........: [{tradeHist['isBuyer']}]")
	BU.errPrint(f"\tMaker...........: [{tradeHist['isMaker']}]")
	BU.errPrint(f"\tTrade History...: [{tradeHist['isBestMatch']}]\n")

def printTradeHistoryXLSHEADER():
	BU.errPrint("Symbol\t"
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
	BU.errPrint(f"{tradeHist['symbol']}\t"
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
	BU.errPrint(f"{seq}) Asset: [{asset['asset']}]");
	BU.errPrint(f"\tBorrowed.: [{asset['borrowed']}]");
	BU.errPrint(f"\tFree.....: [{asset['free']}]");
	BU.errPrint(f"\tLocked...: [{asset['locked']}]");
	BU.errPrint(f"\tNet asset: [{asset['netAsset']}]\n");

def printMarginAssetsXLSHEADER():
	BU.errPrint("Asset\t"
	      "Borrowed\t"
	      "Free\t"
	      "Locked\t"
	      "Net asset")

def printMarginAssetsXLS(asset):
	BU.errPrint(f"{asset['asset']}\t"
	      f"{asset['borrowed']}\t"
	      f"{asset['free']}\t"
	      f"{asset['locked']}\t"
	      f"{asset['netAsset']}")

# ----------------------------------------------------------------------------

def printOrder(order, seq = 0, tot = 0):
	BU.errPrint(f"{seq}/{tot}) Order id: [{order['orderId']}]")
	BU.errPrint(f"\tSymbol......: [{order['symbol']}]")
	BU.errPrint(f"\tPrice.......: [{order['price']}]")
	BU.errPrint(f"\tQtd.........: [{order['origQty']}]")
	BU.errPrint(f"\tQtd executed: [{order['executedQty']}]")
	BU.errPrint(f"\tSide........: [{order['side']}]")
	BU.errPrint(f"\tType........: [{order['type']}]")
	BU.errPrint(f"\tStop price..: [{order['stopPrice']}]")
	BU.errPrint(f"\tIs working..? [{order['isWorking']}]")

def printOrderXLSHEADER():
	BU.errPrint("Order id\t"
	      "Symbol\t"
	      "Price\t"
	      "Qtd\t"
	      "Qtd executed\t"
	      "Side\t"
	      "Type\t"
	      "Stop price\t"
	      "Is working")

def printOrderXLS(order):
	BU.errPrint(f"{order['orderId']}\t"
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
	BU.errPrint(f"Asset balance [{accBalance['asset']}] | Free [{accBalance['free']}] | Locked [{accBalance['locked']}]")

def printAccountXLSHEADER():
	BU.errPrint("Asset balance\tFree\tLocked")

def printAccountXLS(accBalance):
	BU.errPrint(f"{accBalance['asset']}\t{accBalance['free']}\t{accBalance['locked']}")

# ----------------------------------------------------------------------------

def printSystemStatusXLS(sst):
	BU.errPrint(f"{sst['msg']}\t{'normal' if sst['status'] == 0 else 'system maintenance'}")

def printSystemStatus(sst):
	BU.errPrint(f"Message: [{sst['msg']}]")
	BU.errPrint(f"Status.: [{'normal' if sst['status'] == 0 else 'system maintenance'}]")

# ----------------------------------------------------------------------------

def printHistoricalTradesXLSHEADER():
	BU.errPrint("Id\tPrice\tQtyt\tQuote Qty\tTime\tIs Buyer Maker\tIs Best Match")

def printHistoricalTradesXLS(trade):
	BU.errPrint(f"{trade['id']}\t{trade['price']}\t{trade['qty']}\t{trade['quoteQty']}\t{BU.completeMilliTime(trade['time'])}\t{trade['isBuyerMaker']}\t{trade['isBestMatch']}")

def printHistoricalTrades(trade, seq = 0, tot = 0):
	BU.errPrint(f"{seq}/{tot}) Id: [{trade['id']}]")
	BU.errPrint(f"Price.........: [{trade['price']}]")
	BU.errPrint(f"Qtd...........: [{trade['qty']}]")
	BU.errPrint(f"Quote Qtd.....: [{trade['quoteQty']}]")
	BU.errPrint(f"Time..........: [{BU.completeMilliTime(trade['time'])}]")
	BU.errPrint(f"Is Buyer Maker? [{trade['isBuyerMaker']}]")
	BU.errPrint(f"Is Best Match.? [{trade['isBestMatch']}]\n")

# ----------------------------------------------------------------------------

def printServerTimeXLS(st):
	BU.errPrint(f"{BU.completeMilliTime(st['serverTime'])}")

def printServerTime(st):
	BU.errPrint(f"Server Time: [{BU.completeMilliTime(st['serverTime'])}]")

# ----------------------------------------------------------------------------

def printProductsXLSHEADER():
	BU.errPrint("Symbol\tQuote Asset Name\tTraded Money\tBase Asset Unit\tBase Asset Name\tBase Asset\tTick Size\tPrev Close\tActive Buy\tHigh\tLow\tMatching Unit Type\tClose\tQuote Asset\tProduct Type\tOpen\tStatus\tActive\tMin Trade\tMin Qty\tActive Sell\tLast Aggregate Trade Id\tWithdraw Fee\tMarket\tVolume\tMarket Name\tDecimal Places\tParent Market\tParent Market Name\tQuote Asset Unit") 

def printProductsXLS(product):
	BU.errPrint(f"{product['symbol']}\t{product['quoteAssetName']}\t{product['tradedMoney']}\t{product['baseAssetUnit']}\t{product['baseAssetName']}\t{product['baseAsset']}\t{product['tickSize']}\t{product['prevClose']}\t{product['activeBuy']}\t{product['high']}\t{product['low']}\t{product['matchingUnitType']}\t{product['close']}\t{product['quoteAsset']}\t{product['productType']}\t{product['open']}\t{product['status']}\t{product['active']}\t{product['minTrade']}\t{product['minQty']}\t{product['activeSell']}\t{product['lastAggTradeId']}\t{product['withdrawFee']}\t{product['market']}\t{product['volume']}\t{product['marketName']}\t{product['decimalPlaces']}\t{product['parentMarket']}\t{product['parentMarketName']}\t{product['quoteAssetUnit']}")

def printProducts(product, seq, tot):
	BU.errPrint(f"{seq}/{tot}) Symbol: [{product['symbol']}]")
	BU.errPrint(f"\tQuote Asset Name.......: [{product['quoteAssetName']}]")
	BU.errPrint(f"\tTraded Money...........: [{product['tradedMoney']}]")
	BU.errPrint(f"\tBase Asset Unit........: [{product['baseAssetUnit']}]")
	BU.errPrint(f"\tBase Asset Name........: [{product['baseAssetName']}]")
	BU.errPrint(f"\tBase Asset.............: [{product['baseAsset']}]")
	BU.errPrint(f"\tTick Size..............: [{product['tickSize']}]")
	BU.errPrint(f"\tPrev Close.............: [{product['prevClose']}]")
	BU.errPrint(f"\tActive Buy.............: [{product['activeBuy']}]")
	BU.errPrint(f"\tHigh...................: [{product['high']}]")
	BU.errPrint(f"\tLow....................: [{product['low']}]")
	BU.errPrint(f"\tMatching Unit Type.....: [{product['matchingUnitType']}]")
	BU.errPrint(f"\tClose..................: [{product['close']}]")
	BU.errPrint(f"\tQuote Asset............: [{product['quoteAsset']}]")
	BU.errPrint(f"\tProduct Type...........: [{product['productType']}]")
	BU.errPrint(f"\tOpen...................: [{product['open']}]")
	BU.errPrint(f"\tStatus.................: [{product['status']}]")
	BU.errPrint(f"\tActive.................? [{product['active']}]")
	BU.errPrint(f"\tMin Trade..............: [{product['minTrade']}]")
	BU.errPrint(f"\tMin Qty................: [{product['minQty']}]")
	BU.errPrint(f"\tActive Sell............: [{product['activeSell']}]")
	BU.errPrint(f"\tLast Aggregate Trade Id: [{product['lastAggTradeId']}]")
	BU.errPrint(f"\tWithdraw Fee...........: [{product['withdrawFee']}]")
	BU.errPrint(f"\tMarket.................: [{product['market']}]")
	BU.errPrint(f"\tVolume.................: [{product['volume']}]")
	BU.errPrint(f"\tMarket Name............: [{product['marketName']}]")
	BU.errPrint(f"\tDecimal Places.........: [{product['decimalPlaces']}]")
	BU.errPrint(f"\tParent Market..........: [{product['parentMarket']}]")
	BU.errPrint(f"\tParent Market Name.....: [{product['parentMarketName']}]")
	BU.errPrint(f"\tQuote Asset Unit.......: [{product['quoteAssetUnit']}]")

# ----------------------------------------------------------------------------

def printListRateLimit(limits, seq = 0, tot = 0):
	BU.errPrint(f"{seq}/{tot}) Type: [{limits['rateLimitType']}]");
	BU.errPrint(f"Interval.......: [{limits['interval']}]");
	BU.errPrint(f"IntervalNum....: [{limits['intervalNum']}]");
	BU.errPrint(f"Limit..........: [{limits['limit']}]\n");

def printListSymbols(symbs, seq = 0, tot = 0):
	BU.errPrint(f"{seq}/{tot}) Symbol: [{symbs['symbol']}]");
	BU.errPrint(f"\tStatus........................: [{symbs['status']}]");
	BU.errPrint(f"\tBase Asset....................: [{symbs['baseAsset']}]");
	BU.errPrint(f"\tBase Asset Precision..........: [{symbs['baseAssetPrecision']}]");
	BU.errPrint(f"\tQuote Asset...................: [{symbs['quoteAsset']}]");
	BU.errPrint(f"\tQuote Precision...............: [{symbs['quotePrecision']}]");
	BU.errPrint(f"\tQuote Asset Precision.........: [{symbs['quoteAssetPrecision']}]");
	BU.errPrint(f"\tBase Commission Precision.....: [{symbs['baseCommissionPrecision']}]");
	BU.errPrint(f"\tQuote Commission Precision....: [{symbs['quoteCommissionPrecision']}]");
	BU.errPrint(f"\tIceberg Allowed...............? [{symbs['icebergAllowed']}]");
	BU.errPrint(f"\tOco Allowed...................? [{symbs['ocoAllowed']}]");
	BU.errPrint(f"\tQuote Order Qty Market Allowed? [{symbs['quoteOrderQtyMarketAllowed']}]");
	BU.errPrint(f"\tIs Spot Trading Allowed.......? [{symbs['isSpotTradingAllowed']}]");
	BU.errPrint(f"\tIs Margin Trading Allowed.....? [{symbs['isMarginTradingAllowed']}]");
	BU.errPrint(f"\tOrder Types...................: [{', '.join(symbs['orderTypes'])}]");
	BU.errPrint(f"\tPermissions...................: [{', '.join(symbs['permissions'])}]");

	BU.errPrint("\tFilters:");
	for n in symbs['filters']:
		BU.errPrint(f"\t\tType: [{n['filterType']}]");

		sf = n.get('minPrice', '')
		if sf != '': BU.errPrint(f"\t\t\tMin Price..........: [{sf}]");

		sf = n.get('maxPrice', '')
		if sf != '': BU.errPrint(f"\t\t\tMax Price..........: [{sf}]");

		sf = n.get('tickSize', '')
		if sf != '': BU.errPrint(f"\t\t\tTick Size..........: [{sf}]");

		sf = n.get('multiplierUp', '')
		if sf != '': BU.errPrint(f"\t\t\tMultiplier Up......: [{sf}]");

		sf = n.get('multiplierDown', '')
		if sf != '': BU.errPrint(f"\t\t\tMultiplier Down....: [{sf}]");

		sf = n.get('avgPriceMins', '')
		if sf != '': BU.errPrint(f"\t\t\tAvg Price Mins.....: [{sf}]");

		sf = n.get('minQty', '')
		if sf != '': BU.errPrint(f"\t\t\tMin Qty............: [{sf}]");

		sf = n.get('maxQty', '')
		if sf != '': BU.errPrint(f"\t\t\tMax Qty............: [{sf}]");

		sf = n.get('stepSize', '')
		if sf != '': BU.errPrint(f"\t\t\tStep Size..........: [{sf}]");

		sf = n.get('minNotional', '')
		if sf != '': BU.errPrint(f"\t\t\tMin Notional.......: [{sf}]");

		sf = n.get('applyToMarket', '')
		if sf != '': BU.errPrint(f"\t\t\tApply To Market....? [{sf}]");

		sf = n.get('avgPriceMins', '')
		if sf != '': BU.errPrint(f"\t\t\tAvg Price Mins.....: [{sf}]");

		sf = n.get('maxNumAlgoOrders', '')
		if sf != '': BU.errPrint(f"\t\t\tMax Num Algo Orders: [{sf}]");

def printListRateLimitXLSHEADER():
	BU.errPrint("Type\tInterval\tIntervalNum\tLimit")

def printListRateLimitXLS(limits):
	BU.errPrint(f"{limits['rateLimitType']}\t{limits['interval']}\t{limits['intervalNum']}\t{limits['limit']}");

def printListSymbolsXLSHEADER():
	BU.errPrint("Symbol\tStatus\tBase Asset\tBase Asset Precision\tQuote Asset\tQuote Precision\tQuote Asset Precision\tBase Commission Precision\tQuote Commission Precision\tIceberg Allowed\tOco Allowed\tQuote Order Qty Market Allowed\tIs Spot Trading Allowed\tIs Margin Trading Allowed\tOrder Types\tPermissions")

def printListSymbolsXLS(symb):
	BU.errPrint(f"{symb['symbol']}\t{symb['status']}\t{symb['baseAsset']}\t{symb['baseAssetPrecision']}\t{symb['quoteAsset']}\t{symb['quotePrecision']}\t{symb['quoteAssetPrecision']}\t{symb['baseCommissionPrecision']}\t{symb['quoteCommissionPrecision']}\t{symb['icebergAllowed']}\t{symb['ocoAllowed']}\t{symb['quoteOrderQtyMarketAllowed']}\t{symb['isSpotTradingAllowed']}\t{symb['isMarginTradingAllowed']}\t{', '.join(symb['orderTypes'])}\t{', '.join(symb['permissions'])}")

	BU.errPrint("\tFilters\tType\tMin Price\tMax Price\tTick Size\tMultiplier Up\tMultiplier Down\tAvg Price Mins\tMin Qty\tMax Qty\tStep Size\tMin Notional\tApply To Market\tAvg Price Mins\tMax Num Algo Orders")
	for n in symb['filters']:
		BU.errPrint(f"\t\t{n['filterType']}\t{n.get('minPrice', '')}\t{n.get('maxPrice', '')}\t{n.get('tickSize', '')}\t{n.get('multiplierUp', '')}\t{n.get('multiplierDown', '')}\t{n.get('avgPriceMins', '')}\t{n.get('minQty', '')}\t{n.get('maxQty', '')}\t{n.get('stepSize', '')}\t{n.get('minNotional', '')}\t{n.get('applyToMarket', '')}\t{n.get('avgPriceMins', '')}\t{n.get('maxNumAlgoOrders', '')}")

# ----------------------------------------------------------------------------

def printsubAccountsListXLSHEADER():
	BU.errPrint("Email\tStatus\tActivated\tMobile\tAuth\tCreate Time")

def printsubAccountsListXLS(n):
	BU.errPrint(f"{n['email']}\t{n['status']}\t{n['activated']}\t{n['mobile']}\t{n['gAuth']}\t{n['createTime']}")

def printsubAccountsList(n, i, totSal):
	BU.errPrint(f"{i}/{totSal}) Email: [{n['email']}]")
	BU.errPrint(f"Status.....: [{n['status']}]")
	BU.errPrint(f"Activated..: [{n['activated']}]")
	BU.errPrint(f"Mobile.....: [{n['mobile']}]")
	BU.errPrint(f"Auth.......: [{n['gAuth']}]")
	BU.errPrint(f"Create Time: [{BU.completeMilliTime(n['createTime'])}]")

def printsubAccountTransferHistoryXLSHEADER():
	BU.errPrint("From\tTo\tAsset\tQty\tTime")

def printsubAccountTransferHistoryXLS(n):
	BU.errPrint(f"{n['from']}\t{n['to']}\t{n['asset']}\t{n['qty']}\t{BU.completeMilliTime(n['time'])}")

def printsubAccountTransferHistory(n, i, totSath):
	BU.errPrint(f"{i}/{totSath}) From: [{n['from']}]")
	BU.errPrint(f"To...: [{n['to']}]")
	BU.errPrint(f"Asset: [{n['asset']}]")
	BU.errPrint(f"Qty..: [{n['qty']}]")
	BU.errPrint(f"Time.: [{BU.completeMilliTime(n['time'])}]")

def printsubAccountsAssetsXLSHEADER():
	BU.errPrint("Asset\tFree\tLocked")

def printsubAccountsAssetsXLS(n):
	BU.errPrint(f"{n['asset']}\t{n['free']}\t{n['locked']}")

def printsubAccountsAssets(n, i, totSaa):
	BU.errPrint(f"{i}/{totSaa}) Asset: [{n['asset']}]")
	BU.errPrint(f"Free..: [{n['free']}]")
	BU.errPrint(f"Locked: [{n['locked']}]")

# ----------------------------------------------------------------------------

def printPlacedOrder(order):
	BU.errPrint(f"Symbol: [{order['symbol']}]")
	BU.errPrint(f"\tSide.................: [{order['side']}]")
	BU.errPrint(f"\tType.................: [{order['type']}]")
	BU.errPrint(f"\tTransaction Time.....: [{order['transactTime']}]")
	BU.errPrint(f"\tPrice................: [{order['price']}]")
	BU.errPrint(f"\tOrig Qtd.............: [{order['origQty']}]")
	BU.errPrint(f"\tExecuted Qtd.........: [{order['executedQty']}]")
	BU.errPrint(f"\tCummulative Quote Qtd: [{order['cummulativeQuoteQty']}]")
	BU.errPrint(f"\tStatus...............: [{order['status']}]")
	BU.errPrint(f"\tTime In Force........: [{order['timeInForce']}]")
	BU.errPrint(f"\tOrder Id.............: [{order['orderId']}]")
	BU.errPrint(f"\tClient Order Id......: [{order['clientOrderId']}]")

	if 'fills' not in order:
		return

	for f in order['fills']:
		BU.errPrint(f"\t\tPrice...........: [{f['price']}]")
		BU.errPrint(f"\t\tQty.............: [{f['qty']}]")
		BU.errPrint(f"\t\tCommission......: [{f['commission']}]")
		BU.errPrint(f"\t\tCommission Asset: [{f['commissionAsset']}]")
