#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

import time
from os import getenv
from sys import exit, argv

import PySimpleGUI as sg
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceWithdrawException, BinanceRequestException

import binanceOrder as BO
import binanceUtil as BU

#from gui.orderListButton import getOrderList, orderListFixed

def BS_MarginStopLimit(client, bgcolor = '', windowTitle = '', clientSide = 0)-> bool:
	layoutMSL = [
		[sg.Text('Symbol: ', background_color = bgcolor), sg.InputText(key = '-SYMBOL-')],
		[sg.Text('Qtd: ', background_color = bgcolor), sg.InputText(key = '-QTD-')],
		[sg.Text('Stop Price: ', background_color = bgcolor), sg.InputText(key = '-STOP PRICE-')],
		[sg.Text('Limit Price: ', background_color = bgcolor), sg.InputText(key = '-LIMIT PRICE-')],
		[sg.Button('SEND!'), sg.Button('CANCEL')],
	]

	windowMSL = sg.Window(windowTitle, layoutMSL, background_color = bgcolor).Finalize()

	while True:
		eventMSL, valuesMSL = windowMSL.read()

		if eventMSL == 'SEND!':
			BU.errPrint(f"{windowTitle} - Order Symbol: [{valuesMSL['-SYMBOL-']}] Qtd: [{valuesMSL['-QTD-']}] Stop Prc: [{valuesMSL['-STOP PRICE-']}] Limit Prc: [{valuesMSL['-LIMIT PRICE-']}]")

			if sg.popup_yes_no('CONFIRM?', text_color='yellow', background_color='red') == 'No':
				BU.errPrint(f'{windowTitle} - CANCELLED!')
				break;

			if BO.orderMargin(client,
			                  symbOrd = valuesMSL['-SYMBOL-'],
			                  qtdOrd = valuesMSL['-QTD-'],
			                  prcOrd = valuesMSL['-STOP PRICE-'],
			                  prcStop = valuesMSL['-LIMIT PRICE-'],
			                  sideOrd = clientSide,
			                  typeOrd = "TAKE_PROFIT_LIMIT",
			                  limit = 0.0 ) == False:
				sg.popup('ERRO! Order didnt post!')
				break;

			BU.errPrint(f'{windowTitle} - CONFIRMED!')

		elif eventMSL == sg.WIN_CLOSED or eventMSL == 'CANCEL':
			BU.errPrint(f'{windowTitle} - CANCELLED!')
			break

	windowMSL.close()
	del windowMSL
	del layoutMSL

	return True

def BS_MarginMarket(client, bgcolor = '', windowTitle = '', clientSide = 0)-> bool:
	layoutMM = [
		[sg.Text('Symbol: ', background_color = bgcolor), sg.InputText(key = '-SYMBOL-')],
		[sg.Text('Qtd: ', background_color = bgcolor), sg.InputText(key = '-QTD-')],
		[sg.Button('SEND!'), sg.Button('CANCEL')],
	]

	windowMM = sg.Window(windowTitle, layoutMM, background_color = bgcolor).Finalize()

	while True:
		eventMM, valuesMM = windowMM.read()

		if eventMM == 'SEND!':
			BU.errPrint(f"{windowTitle} - Order Symbol: [{valuesMM['-SYMBOL-']}] Qtd: [{valuesMM['-QTD-']}]")

			if sg.popup_yes_no('CONFIRM?', text_color='yellow', background_color='red') == 'No':
				BU.errPrint(f'{windowTitle} - CANCELLED!')
				break;

			if BO.orderMargin(client,
			                  symbOrd = valuesMM['-SYMBOL-'],
			                  qtdOrd  = valuesMM['-QTD-'],
			                  sideOrd = clientSide,
			                  typeOrd = Client.ORDER_TYPE_MARKET) == False:
				sg.popup('ERRO! Order didnt post!')
				break;

			BU.errPrint(f'{windowTitle} - CONFIRMED!')

		elif eventMM == sg.WIN_CLOSED or eventMM == 'CANCEL':
			BU.errPrint(f'{windowTitle} - CANCELLED!')
			break

	windowMM.close()

	del windowMM
	del layoutMM

	return True

def BS_MarginLimit(client, bgcolor = '', windowTitle = '', clientSide = 0)-> bool:
	layoutML = [
		[sg.Text('Symbol: ', background_color = bgcolor), sg.InputText(key = '-SYMBOL-')],
		[sg.Text('Qtd: ', background_color = bgcolor), sg.InputText(key = '-QTD-')],
		[sg.Text('Price: ', background_color = bgcolor), sg.InputText(key = '-PRICE-')],
		[sg.Button('SEND!'), sg.Button('CANCEL')],
	]

	windowML = sg.Window(windowTitle, layoutML, background_color = bgcolor).Finalize()

	while True:
		eventML, valuesML = windowML.read()

		if eventML == 'SEND!':
			BU.errPrint(f"{windowTitle} - Order Symbol: [{valuesML['-SYMBOL-']}] Qtd: [{valuesML['-QTD-']}] Price: [{valuesML['-PRICE-']}]")

			if sg.popup_yes_no('CONFIRM?', text_color='yellow', background_color='red') == 'No':
				BU.errPrint(f'{windowTitle} - CANCELLED!')
				break;

			if BO.orderMargin(client,
			                  symbOrd = valuesML['-SYMBOL-'],
			                  qtdOrd  = valuesML['-QTD-'],
			                  prcOrd  = valuesML['-PRICE-'],
			                  sideOrd = clientSide,
			                  typeOrd = Client.ORDER_TYPE_LIMIT) == False:
				sg.popup('ERRO! Order didnt post!')
				break;

			BU.errPrint(f'{windowTitle} - CONFIRMED!')

		elif eventML == sg.WIN_CLOSED or eventML == 'CANCEL':
			BU.errPrint(f'{windowTitle} - CANCELLED!')
			break

	windowML.close()
	del windowML
	del layoutML

	return True

def BS_SpotStopLimit(client, bgcolor = '', windowTitle = '', clientSide = 0)-> bool:
	layoutSSL = [
		[sg.Text('Symbol: ', background_color = bgcolor), sg.InputText(key = '-SYMBOL-')],
		[sg.Text('Qtd: ', background_color = bgcolor), sg.InputText(key = '-QTD-')],
		[sg.Text('Stop Price: ', background_color = bgcolor), sg.InputText(key = '-STOP PRICE-')],
		[sg.Text('Limit Price: ', background_color = bgcolor), sg.InputText(key = '-LIMIT PRICE-')],
		[sg.Button('SEND!'), sg.Button('CANCEL')],
	]

	windowSSL = sg.Window(windowTitle, layoutSSL, background_color = bgcolor).Finalize()

	while True:
		eventSSL, valuesSSL = windowSSL.read()

		if eventSSL == 'SEND!':
			BU.errPrint(f"{windowTitle} - Order Symbol: [{valuesSSL['-SYMBOL-']}] Qtd: [{valuesSSL['-QTD-']}] Stop Prc: [{valuesSSL['-STOP PRICE-']}] Limit Prc: [{valuesSSL['-LIMIT PRICE-']}]")

			if sg.popup_yes_no('CONFIRM?', text_color='yellow', background_color='red') == 'No':
				BU.errPrint(f'{windowTitle} - CANCELLED!')
				break;

			if BO.orderSpotLimit(client,
			                     symbOrd = valuesSSL['-SYMBOL-'],
			                     qtdOrd = valuesSSL['-QTD-'],
			                     prcStopOrd = valuesSSL['-STOP PRICE-'],
			                     prcStopLimitOrd = valuesSSL['-LIMIT PRICE-'],
			                     sideOrd = clientSide) == False:
				sg.popup('ERRO! Order didnt post!')
				break;

			BU.errPrint(f'{windowTitle} - CONFIRMED!')

		elif eventSSL == sg.WIN_CLOSED or eventSSL == 'CANCEL':
			BU.errPrint(f'{windowTitle} - CANCELLED!')
			break

	windowSSL.close()
	del windowSSL
	del layoutSSL

	return True

def BS_SpotMarket(client, bgcolor = '', windowTitle = '', clientSide = 0)-> bool:
	layoutSM = [
		[sg.Text('Symbol: ', background_color = bgcolor), sg.InputText(key = '-SYMBOL-')],
		[sg.Text('Qtd: ', background_color = bgcolor), sg.InputText(key = '-QTD-')],
		[sg.Button('SEND!'), sg.Button('CANCEL')],
	]

	windowSM = sg.Window(windowTitle, layoutSM, background_color = bgcolor).Finalize()

	while True:
		eventSM, valuesSM = windowSM.read()

		if eventSM == 'SEND!':
			BU.errPrint(f"{windowTitle} - Order Symbol: [{valuesSM['-SYMBOL-']}] Qtd: [{valuesSM['-QTD-']}]")

			if sg.popup_yes_no('CONFIRM?', text_color='yellow', background_color='red') == 'No':
				BU.errPrint(f'{windowTitle} - CANCELLED!')
				break;

			if BO.orderSpot(client,
			                symbOrd = valuesSM['-SYMBOL-'],
			                qtdOrd  = valuesSM['-QTD-'],
			                sideOrd = clientSide,
			                typeOrd = Client.ORDER_TYPE_MARKET) == False:
				sg.popup('ERRO! Order didnt post!')
				break;

			BU.errPrint(f'{windowTitle} - CONFIRMED!')

		elif eventSM == sg.WIN_CLOSED or eventSM == 'CANCEL':
			BU.errPrint(f'{windowTitle} - CANCELLED!')
			break

	windowSM.close()

	del windowSM
	del layoutSM

	return True

def BS_SpotLimit(client, bgcolor = '', windowTitle = '', clientSide = 0)-> bool:
	layoutSL = [
		[sg.Text('Symbol: ', background_color = bgcolor), sg.InputText(key = '-SYMBOL-')],
		[sg.Text('Qtd: ', background_color = bgcolor), sg.InputText(key = '-QTD-')],
		[sg.Text('Price: ', background_color = bgcolor), sg.InputText(key = '-PRICE-')],
		[sg.Button('SEND!'), sg.Button('CANCEL')],
	]

	windowSL = sg.Window(windowTitle, layoutSL, background_color = bgcolor).Finalize()

	while True:
		eventSL, valuesSL = windowSL.read()

		if eventSL == 'SEND!':
			BU.errPrint(f"{windowTitle} - Order Symbol: [{valuesSL['-SYMBOL-']}] Qtd: [{valuesSL['-QTD-']}] Price: [{valuesSL['-PRICE-']}]")

			if sg.popup_yes_no('CONFIRM?', text_color='yellow', background_color='red') == 'No':
				BU.errPrint(f'{windowTitle} - CANCELLED!')
				break;

			if BO.orderSpot(client,
			                symbOrd = valuesSL['-SYMBOL-'],
			                qtdOrd  = valuesSL['-QTD-'],
			                prcOrd  = valuesSL['-PRICE-'],
			                sideOrd = clientSide,
			                typeOrd = Client.ORDER_TYPE_LIMIT) == False:
				sg.popup('ERRO! Order didnt post!')
				break;

			BU.errPrint(f'{windowTitle} - CONFIRMED!')

		elif eventSL == sg.WIN_CLOSED or eventSL == 'CANCEL':
			BU.errPrint(f'{windowTitle} - CANCELLED!')
			break

	windowSL.close()
	del windowSL
	del layoutSL

	return True

def ListOpenOrders(client)->bool:

	def buildOrderList(ordList):
		return [sg.CBox(f"{ordList['orderId']}", key=f"{ordList['orderId']}"),
		        sg.Text(f"{ordList['symbol']}\t\t{ordList['side']}\t\t{ordList['price']}\t\t{ordList['origQty']}\t\t{ordList['type']}", font=("Courier", 10))]

	try:
		openOrders = client.get_open_orders() #recvWindow
		openMarginOrders = client.get_open_margin_orders() #recvWindow
	except BinanceRequestException as e:
		BU.errPrint(f"Erro at client.get_open_orders() BinanceRequestException: [{e.status_code} - {e.message}]")
		return False
	except BinanceAPIException as e:
		BU.errPrint(f"Erro at client.get_open_orders() BinanceAPIException: [{e.status_code} - {e.message}]")
		return False
	except Exception as e:
		BU.errPrint(f"Erro at client.get_open_orders(): {e}")
		return False

	if len(openOrders) == 0:
		layoutFrameSpotOpen = [[sg.Text("0 orders.", font=("Courier", 10))]]
	else:
		layoutFrameSpotOpen = [[sg.Text("Order Id\tSymbol\tSide\tPrice\tQtd\tType", font=("Courier", 10))]]
		[layoutFrameSpotOpen.append(buildOrderList(i)) for i in openOrders]
		layoutFrameSpotOpen.append([sg.Button('Delete Spot Order'), sg.Button('Copy Spot data to clipboard')])

	if len(openMarginOrders) == 0:
		layoutFrameMarginOpen = [[sg.Text("0 orders.", font=("Courier", 10))]]
	else:
		layoutFrameMarginOpen = [[sg.Text("Order Id\tSymbol\tSide\tPrice\tQtd\tType", font=("Courier", 10))]]
		[layoutFrameMarginOpen.append(buildOrderList(i)) for i in openMarginOrders]
		layoutFrameMarginOpen.append([sg.Button('Delete Margin Order'), sg.Button('Copy Margin data to clipboard')])

	layoutListOpenOrders = [
		[sg.Frame('SPOT', layoutFrameSpotOpen, title_color='blue')],
		[sg.Frame('MARGIN', layoutFrameMarginOpen, title_color='blue')],
		[sg.Button('Close')]
	]

	windowListOpenOrder = sg.Window('Open Orders', layoutListOpenOrders);

	while True:
		eventLOO, valuesLOO = windowListOpenOrder.read()

		if eventLOO == sg.WIN_CLOSED or eventLOO == 'Close':
			break

		elif eventLOO == 'Delete Margin Order':
			pass

		elif eventLOO == 'Copy Margin data to clipboard':
			pass

		elif eventLOO == 'Delete Spot Order':
			pass

		elif eventLOO == 'Copy Spot data to clipboard':
			pass

		print(valuesLOO)
		print(eventLOO)

	windowListOpenOrder.close()

	del openOrders
	del openMarginOrders
	del windowListOpenOrder
	del layoutFrameSpotOpen
	del layoutFrameMarginOpen
	del layoutListOpenOrders

def main(argv):

	menu = [
		[ '&Menu', ['Info', 'Config', 'Exit']],
		[ '&Account', ['Infos acc', 'Taxes']],
		[ '&Order', ['BUY',  ['B Spot Market', 'B Spot Limit','B Spot Stop Limit', '!B Spot OCO', '---', 'B Margin Market', 'B Margin Limit', 'B Margin Stop Limit', '!B Margin OCO'],
		             'SELL', ['S Spot Market', 'S Spot Limit','S Spot Stop Limit', '!S Spot OCO', '---', 'S Margin Market', 'S Margin Limit', 'S Margin Stop Limit', '!S Margin OCO'], 'CANCEL', 'LIST or DELETE Open', 'LIST All']],
		[ '&Binance', ['Infos binance', 'Assets', 'Symbols']]
	]

#orderListButton.py
	openOrdersFrame = [
		[sg.CB(''), sg.Text('Order ID ... Symb ... Qtd ... Price', key='cb1')],
		[sg.CB(''), sg.Text('Order ID ... Symb ... Qtd ... Price', key='cb2')],
		[sg.CB(''), sg.Text('Order ID ... Symb ... Qtd ... Price', key='cb3')],
		[sg.CB(''), sg.Text('Order ID ... Symb ... Qtd ... Price', key='cb4')],
		[sg.CB(''), sg.Text('Order ID ... Symb ... Qtd ... Price', key='cb5')],
		[sg.Button('Cancel Order'), sg.Button('Prev page'), sg.Button('Next page')],
	]

	favoriteSymbolsInfo = [
		  [sg.T('empty...')],
	]

	layout = [
		  [sg.Menu(menu)],
#		  [sg.Text('text1', key='-TEXT-')],
#		  [sg.Text('Get symbol info:'), sg.InputText()],
#	  [sg.Frame('Open Orders', openOrdersFrame, font='Any 12', title_color='blue', key = '-OpenOrdersFrame-')],
#	  [sg.Frame('Watching symbols', favoriteSymbolsInfo, font='Any 12', title_color='blue', key = '-WatchingSymbolsFrame-')],
#	  [sg.Button('REFRESH')],
	]

	binanceAPIKey = getenv("BINANCE_APIKEY", "NOTDEF_APIKEY")
	if binanceAPIKey == "NOTDEF_APIKEY":
		BU.errPrint("Environment variable BINANCE_APIKEY not defined!")
		exit(1)

	binanceSEKKey = getenv("BINANCE_SEKKEY", "NOTDEF_APIKEY")
	if binanceSEKKey == "NOTDEF_APIKEY":
		BU.errPrint("Environment variable BINANCE_SEKKEY not defined!")
		exit(1)

	binanceRecvWindow = int(getenv("BINANCE_RECVWINDOW", 5000))

	BU.setConfirmationYES(True)

	# CONNECTING TO BINANCE
	try:
		client = Client(binanceAPIKey, binanceSEKKey, {"verify": True, "timeout": 20})

	except BinanceAPIException as e:
		BU.errPrint(f"Binance API exception: [{e.status_code} - {e.message}]")
		exit(1)

	except BinanceRequestException as e:
		BU.errPrint(f"Binance request exception: [{e.status_code} - {e.message}]")
		exit(1)

	except BinanceWithdrawException as e:
		BU.errPrint(f"Binance withdraw exception: [{e.status_code} - {e.message}]")
		exit(1)

	except Exception as e:
		BU.errPrint(f"Binance connection error: {e}")
		exit(1)

#import pudb
#pudb.set_trace()

	sg.theme('Dark Blue 3')

	#sg.set_options(suppress_raise_key_errors=False, suppress_error_popups=False, suppress_key_guessing=False)

	window = sg.Window('Binance Status GUI', layout, size = (215, 0)).Finalize()

	while True:
		event, values = window.read()  #timeout=1000)

		if event == sg.WIN_CLOSED or event == 'Exit':
			break

		elif event == "Infos":
			sg.popup('INFOS')

		elif event == 'Info':
			pass

		elif event == 'Config':
			pass

		elif event == 'Infos acc':
			pass

		elif event == 'Taxes':
			pass

		elif event == 'B Spot Market':
			window.Hide()
			BS_SpotMarket(client, 'green', 'Buy Spot Market', Client.SIDE_BUY)
			window.UnHide()

		elif event == 'B Spot Limit':
			window.Hide()
			BS_SpotLimit(client, 'green', 'Buy Spot Limit', Client.SIDE_BUY)
			window.UnHide()

		elif event == 'B Spot Stop Limit':
			window.Hide()
			BS_SpotStopLimit(client, 'green', 'Buy Spot Stop Limit', Client.SIDE_BUY)
			window.UnHide()

		elif event == 'B Spot OCO':
			pass

		elif event == 'B Margin Market':
			window.Hide()
			BS_MarginMarket(client, 'red', 'Sell Margin Limit', Client.SIDE_SELL)
			window.UnHide()

		elif event == 'B Margin Limit':
			window.Hide()
			BS_MarginLimit(client, 'green', 'Buy Margin Limit', Client.SIDE_BUY)
			window.UnHide()

		elif event == 'B Margin Stop Limit':
			window.Hide()
			BS_MarginStopLimit(client, 'green', 'Buy Margin Stop Limit', Client.SIDE_BUY)
			window.UnHide()

		elif event == 'B Margin OCO':
			pass

		elif event == 'S Spot Market':
			window.Hide()
			BS_SpotMarket(client, 'red', 'Sell Spot Market', Client.SIDE_SELL)
			window.UnHide()

		elif event == 'S Spot Limit':
			window.Hide()
			BS_SpotLimit(client, 'red', 'Sell Spot Limit', Client.SIDE_SELL)
			window.UnHide()

		elif event == 'S Spot Stop Limit':
			window.Hide()
			BS_SpotStopLimit(client, 'red', 'Sell Spot Stop Limit', Client.SIDE_SELL)
			window.UnHide()

		elif event == 'S Spot OCO':
			pass

		elif event == 'S Margin Market':
			window.Hide()
			BS_MarginMarket(client, 'red', 'Sell Margin Limit', Client.SIDE_SELL)
			window.UnHide()

		elif event == 'S Margin Limit':
			window.Hide()
			BS_MarginLimit(client, 'red', 'Sell Margin Limit', Client.SIDE_SELL)
			window.UnHide()

		elif event == 'S Margin Stop Limit':
			window.Hide()
			BS_MarginStopLimit(client, 'red', 'Sell Margin Stop Limit', Client.SIDE_SELL)
			window.UnHide()

		elif event == 'S Margin OCO':
			pass

		elif event == 'CANCEL':
			pass

		elif event == 'LIST or DELETE Open':
			window.Hide()
			ListOpenOrders(client)
			window.UnHide()

		elif event == 'LIST All':
			pass

		elif event == 'Infos binance':
			pass

		elif event == 'Assets':
			pass

		elif event == 'Symbols':
			pass

	window.close()

if __name__ == '__main__':
	main(argv)
	exit(0)
