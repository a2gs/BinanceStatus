#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota
# andre.scota@gmail.com
# MIT license

import time

def printHelp(execName):
	print("1) Account:")
	print(f'{execName} -h [symbol]\n\tAccount history (trades, dusts, etc)\n')
	print(f'{execName} -i\n\tWallet/Account information\n')
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

	print(f'{execName} [...] --xls\n\tOutput with TAB separator\n')

def printMarginOrder(order, seq, tot):
	printOrder(order, seq, tot)

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

def printDetailsAssets(ass, detAss, seq, tot):
	print(f"{seq}/{tot}) Asset: [{ass}]");
	print(f"\tMin. withdraw amount: [{detAss['minWithdrawAmount']}]");
	print(f"\tDeposit status......: [{detAss['depositStatus']}]");
	dt = detAss.get('depositTip', '')
	if dt != '':
		print(f"\tDeposit tip.........: [{dt}]");
	print(f"\tWithdraw fee........: [{detAss['withdrawFee']}]");
	print(f"\tWithdraw status.....: [{detAss['withdrawStatus']}]\n");

def printTradeFee(tf, seq, tot):
	print(f"{seq}/{tot}) Symbol: [{tf['symbol']}]\tMaker: [{tf['maker']}]\tTaker: [{tf['taker']}]");

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

def printTradeHistory(tradeHist, seq, tot):
	print(f"{seq}/{tot}) Symbol: [{tradeHist['symbol']}]")
	print(f"\tTime............: [{time.ctime(tradeHist['time']/1000)}]")
	print(f"\tOrder Id........: [{tradeHist['orderId']}]")
	print(f"\tId..............: [{tradeHist['id']}]")
#	print(f"\tOrder List Id...: [{tradeHist['orderListId']}]")
	print(f"\tPrice...........: [{tradeHist['price']}]")
	print(f"\tQtd.............: [{tradeHist['qty']}]")
	print(f"\tQuote Qtd.......: [{tradeHist['quoteQty']}]")
	print(f"\tCommission......: [{tradeHist['commission']}]")
	print(f"\tCommission asset: [{tradeHist['commissionAsset']}]")
	print(f"\tBuyer...........: [{tradeHist['isBuyer']}]")
	print(f"\tMaker...........: [{tradeHist['isMaker']}]")
	print(f"\tTradeHist.......: [{tradeHist['isBestMatch']}]\n")

def printMarginAssets(asset, seq):
	print(f"{seq}) Asset: [{asset['asset']}]");
	print(f"\tBorrowed.: [{asset['borrowed']}]");
	print(f"\tFree.....: [{asset['free']}]");
	print(f"\tLocked...: [{asset['locked']}]");
	print(f"\tNet asset: [{asset['netAsset']}]\n");

def printOrder(order, seq, tot):
	print(f"{seq}/{tot}) Order id [{order['orderId']}] data:")
	print(f"\tSymbol......: [{order['symbol']}]")
	print(f"\tPrice.......: [{order['price']}]")
	print(f"\tQtd.........: [{order['origQty']}]")
	print(f"\tQtd executed: [{order['executedQty']}]")
	print(f"\tSide........: [{order['side']}]")
	print(f"\tType........: [{order['type']}]")
	print(f"\tStop price..: [{order['stopPrice']}]")
	print(f"\tIs working..: [{order['isWorking']}]\n")

def printAccount(accBalance):
	print(f"Asset balance [{accBalance['asset']}] | Free [{accBalance['free']}] | Locked [{accBalance['locked']}]")
