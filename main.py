import ccxt
exchange = ccxt.binance()
data = exchange.fetchTicker(symbol='BTC/USDT')

print(data['high'],data['bid'])
