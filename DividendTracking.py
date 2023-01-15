import yfinance as yf

print("Dividend Tracking Stocks:")
print(" ")
stock_symbol = ["PSEC","O","MAIN","MULN"]
stock_number = [3338.057, 1001.078, 100.003, 307100]
total_dividends = 0

for i in stock_symbol:
    try:
        
        stock_info = yf.Ticker(i)
        dividends_history = stock_info.dividends
        print(i) #Monthly Dividend
        #print(dividends_history[-1])
        index = stock_symbol.index(i)
        print(stock_number[index] * dividends_history[-1])
        print(" ")
        total_dividends += stock_number[index] * dividends_history[-1]
    except:
        print(0.00)
        pass

print(" ")
print("Total Dividends:")
print(total_dividends)
