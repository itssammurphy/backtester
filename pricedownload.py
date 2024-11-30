import yfinance as yf

ticker = yf.Ticker("GYG.AX")
hourly_data = ticker.history(
    period="5d", interval="1m")
hourly_data.to_csv("hourly_data.csv")
