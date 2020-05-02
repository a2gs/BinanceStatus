# BinanceStatus
Get status (balance, orders, symbols, history, etc), place orders (spot and margin accounts. Types: market, limit, stop/OCO) to Binance account through command line.<br>
<br>
Dependence:<br>
1) Python >= 3.5<br>
2) Binance Python API >= 0.2.0 from https://pypi.org/project/python-binance/ (Can be installed with pip comamand: <i>pip install python-binance</i>)<br>
3) <i>virtualenv</i> is not mandatory, but a good python practice<br>
<br>
Setup:<br>
1) Create Binance API from their site.<br>
2) Insert Binance API Key and Securiry Key into follow variables into <b>walletId.sh</b> file:<br>
<i>export BINANCE_APIKEY='<b>AAABBBCCCDDDEEE</b>'<br>
export BINANCE_SEKKEY='<b>AAABBBCCCDDDEEE</b>'</i><br>
<br>
Usage:<br>
# <i>source ./walletId.sh</i><br>
# <i>./binanceStatus.py</i><br>
