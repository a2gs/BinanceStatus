#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota
# andre.scota@gmail.com
# MIT license

def printMarginOrder(order, seq, tot):
	printOrder(order, seq, tot)

def printDetailsAssets(ass, detAss, seq, tot):
	print(f"{seq}/{tot}) Asset: [{ass}]");
	print(f"\tMin. withdraw amount: [{detAss['minWithdrawAmount']}]");
	print(f"\tDeposit status......: [{detAss['depositStatus']}]");
	print(f"\tWithdraw fee........: [{detAss['withdrawFee']}]");
	print(f"\tWithdraw status.....: [{detAss['withdrawStatus']}]");
	dt = detAss.get('depositTip', '')
	if dt != '':
		print(f"\tDeposit tip.........: [{dt}]");

def printTradeFee(tf, seq, tot):
	print(f"{seq}/{tot}) Symbol: [{tf['symbol']}]\tMaker: [{tf['maker']}]\tTaker: [{tf['taker']}]");

def printHelp(execName):
	print(f'{execName} -h <ASSET>\n\tAccount history (trades, dusts, etc)\n')
	print(f'{execName} -i\n\tWallet/Account information\n')
	print(f'{execName} -d\n\tAccount details (fees)\n')

	print(f'{execName} -s\n\tPlace a sell order')
	print(f'\t\t{execName} -s MARKET [symbol] [qtd]')
	print(f'\t\t{execName} -s LIMIT [symbol] [qtd] [price] (TODO: STOP PARAMETERS)\n')

	print(f'{execName} -b\n\tPlace a buy order\n')
	print(f'\t\t{execName} -b MARKET [symbol] [qtd]')
	print(f'\t\t{execName} -b LIMIT [symbol] [qtd] [price] (TODO: STOP PARAMETERS)\n')

	print(f'{execName} -c \n\tCancel a order\n')

def printTradeAllHist(tradeAllHist, seq, tot):
	print(f"{seq}/{tot}) Symbol: [{tradeAllHist['symbol']}]")
	print(f"\tTime: [{tradeAllHist['time']}] Update time: [{tradeAllHist['updateTime']}]")
	print(f"\tOrder Id: [{tradeAllHist['orderId']}] | Order list Id: [{tradeAllHist['orderListId']}] | Client Order Id: [{tradeAllHist['clientOrderId']}]")
	print(f"\tPrice: [{tradeAllHist['price']} | Orig Qtd: [{tradeAllHist['origQty']} | Executed Qtd: [{tradeAllHist['executedQty']} | Cummulative Quote Qtd: [{tradeAllHist['cummulativeQuoteQty']}]")
	print(f"\tStatus: [{tradeAllHist['status']} | Time in Force: [{tradeAllHist['timeInForce']}]")
	print(f"\tSide: [{tradeAllHist['side']}]")
	print(f"\tType: [{tradeAllHist['type']}]")
	print(f"\tStop Price: [{tradeAllHist['stopPrice']}]")
	print(f"\tIs working: [{tradeAllHist['isWorking']}]")

def printTradeHistory(tradeHist, seq, tot):
	print(f'{seq}/{tot}) Symbol: [' + tradeHist['symbol'] + ']\n'
		+ '\tTime: [' + str(tradeHist['time']) + ']\n'
		+ '\tOrder Id: [' + str(tradeHist['orderId']) + ' | Id: [' + str(tradeHist['id']) + ' Order List Id: [' + str(tradeHist['orderListId']) + ']\n'
		+ '\tPrice: [' + tradeHist['price'] + '] | Qtd: [' + tradeHist['qty'] + '] | Quote Qtd: [' + tradeHist['quoteQty'] + ']\n'
		+ '\tCommission: [' + tradeHist['commission'] + 'Commission asset: [' + tradeHist['commissionAsset'] + ']\n'
		+ '\tBuyer: [' + str(tradeHist['isBuyer']) + '] | Maker: [' + str(tradeHist['isMaker']) + '] | TradeHist: [' + str(tradeHist['isBestMatch']) + ']')

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
	print('Asset balance [' + accBalance['asset'] + '] | Free [' + accBalance['free'] + '] | Locked [' + accBalance['locked'] + ']')
