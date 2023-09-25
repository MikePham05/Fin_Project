import yfinance as yf
import pandas as pd

def main():
    stocks = ["amzn", "tsla", "goog", "meta", "nflx"]
    stocks = list(map(str.upper, stocks))
    interested_info = ["Open", "High", "Close", "Low"]
    # Fetch data
    df = yf.download(stocks, period="1wk")
    for index, row in df.iterrows():
        for name in stocks:
            print(index, row["Open", name], row["High", name], row["Close", name], row["Low", name])

    return

if __name__ == "__main__":
    main()
