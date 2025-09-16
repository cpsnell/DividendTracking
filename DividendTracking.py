import yfinance as yf

print("Dividend Tracking Stocks:\n")

stock_symbols = ["KO", "MTN", "GOOGL", "MSFT"]
stock_numbers = [10.0, 10, 4, 2]

total_dividends = 0.0

# Iterate with both symbol and number together
for symbol, number in zip(stock_symbols, stock_numbers):
    try:
        stock_info = yf.Ticker(symbol)
        dividends_history = stock_info.dividends

        if not dividends_history.empty:
            last_dividend = dividends_history.iloc[-1]  # label position access
            dividend_value = number * last_dividend
            print(f"{symbol}: {dividend_value:.2f}")
            total_dividends += dividend_value
        else:
            print(f"{symbol}: 0.00 (no dividend data)")
    except Exception as e:
        print(f"{symbol}: 0.00 (error: {e})")
        continue

print("\nTotal Dividends:")
print(f"{total_dividends:.2f}")
