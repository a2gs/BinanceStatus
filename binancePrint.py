#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota
# andre.scota@gmail.com
# MIT license

import time

def printHelp(execName):
	print("1) Account:")
	print(f'{execName} -h [symbol]\n\tAccount history (trades, dusts, etc)\n')
	print(f'{execName} -i\n\tWallet/Account information (open orders)\n')
	print(f'{execName} -d\n\tAccount details (fees)\n')

	print("2) Trade:")
	print(f'{execName} -s\n\tPlace a sell order')
	print(f'\t\t{execName} -s MARKET [symbol] [qtd]')
	print(f'\t\t{execName} -s LIMIT [symbol] [qtd] [price]')
	print(f'\t\t{execName} -s STOP [symbol] [qtd] [price] [stopPrice]\n')

	print(f'{execName} -b\n\tPlace a buy order')
	print(f'\t\t{execName} -b MARKET [symbol] [qtd]')
	print(f'\t\t{execName} -b LIMIT [symbol] [qtd] [price]')
	print(f'\t\t{execName} -b STOP [symbol] [qtd] [price] [stopPrice]\n')

	print(f'{execName} -c \n\tCancel a order\n')

	print("3) Market:")
	print(f'{execName} -p \n\t24 hour price change statistics\n')

	print(f'{execName} -l\n\tList of symbols and rate\n')

	print(f'{execName} -v [symbol] [interval] [qtd candles]\n\tInformation (prices) about a symbol.\n\t[interval] is one of \'1m\', \'3m\', \'5m\', \'15m\', \'30m\', \'2h\', \'4h\', \'6h\', \'8h\', \'12h\', \'1h\', \'1d\', \'3d\', \'1w\', \'1M\'\n')

	print(f'{execName} -V [symbol]\n\tInformation (details) about a symbol\n')

	print(f'{execName} [...] --xls >> output.xls\n\tOutput with TAB separator\n')

# ----------------------------------------------------------------------------

def printMarginOrder(order, seq, tot):
	printOrder(order, seq, tot)

def printMarginOrderXLSHEADER():
	printOrderXLSHEADER()

def printMarginOrderXLS(order):
	printOrderXLS(order)

# ----------------------------------------------------------------------------

def printInfoSymbolValues(symbPrc, seq, tot):
	print(f"{seq}/{tot}) Candle:")
	print(f"Open time...................: [{time.ctime(symbPrc[0]/1000)}]")
	print(f"Close time..................: [{time.ctime(symbPrc[6]/1000)}]")
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
	print(f"{time.ctime(symbPrc[0]/1000)}\t"
	      f"{time.ctime(symbPrc[6]/1000)}\t"
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

def print24hPrcChangSts(priceSts, seq, tot):
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
	print(f"\tOpen Time.............: [{time.ctime(priceSts['openTime']/1000)}]")
	print(f"\tClose Time............: [{time.ctime(priceSts['closeTime']/1000)}]")
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
	      f"{time.ctime(priceSts['openTime']/1000)}\t"
	      f"{time.ctime(priceSts['closeTime']/1000)}\t"
	      f"{priceSts['firstId']}\t"
	      f"{priceSts['lastId']}\t"
	      f"{priceSts['count']}")

# ----------------------------------------------------------------------------

def printDustTrade(order, seq, tot):
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

def printDetailsAssets(ass, detAss, seq, tot):
	print(f"{seq}/{tot}) Asset: [{ass}]");
	print(f"\tMin. withdraw amount: [{detAss['minWithdrawAmount']}]");
	print(f"\tDeposit status......: [{detAss['depositStatus']}]");
	dt = detAss.get('depositTip', '')
	if dt != '':
		print(f"\tDeposit tip.........: [{dt}]");
	print(f"\tWithdraw fee........: [{detAss['withdrawFee']}]");
	print(f"\tWithdraw status.....: [{detAss['withdrawStatus']}]\n");

# ----------------------------------------------------------------------------

def printTradeFee(tf, seq, tot):
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

def printTradeAllHist(tradeAllHist, seq, tot):
	print(f"{seq}/{tot}) Symbol: [{tradeAllHist['symbol']}]")
	print(f"\tTime.................: [{time.ctime(tradeAllHist['time']/1000)}]")
	print(f"\tUpdate time..........: [{time.ctime(tradeAllHist['updateTime']/1000)}]")
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
	      f"{time.ctime(tradeAllHist['time']/1000)}\t"
	      f"{time.ctime(tradeAllHist['updateTime']/1000)}\t"
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

def printTradeHistory(tradeHist, seq, tot):
	print(f"{seq}/{tot}) Symbol: [{tradeHist['symbol']}]")
	print(f"\tTime............: [{time.ctime(tradeHist['time']/1000)}]")
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
	      f"{time.ctime(tradeHist['time']/1000)}\t"
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

def printMarginAssets(asset, seq):
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

def printOrder(order, seq, tot):
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
