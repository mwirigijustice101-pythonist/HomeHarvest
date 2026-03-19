#step1:install yfinance pandas numpy matplotlib

#step2:
import yfinance as yf #for stock data
import pandas as pd #for data manupulation
import numpy as np #for numerical operations
import matplotlib.pyplot as plt #for visualizations

#step3:fetch historical stock data
#we need historical price data to analyze and backtest our trading strategy
#Define the stock ticker (e.g., AAPL for Apple).
#setting the start and end dates for our analysis.
#use yfinance to fetch the data
#Define parameters
ticker = "AAPL" #Apple stock
start_date = "2024-02-17"
end_date = "2025-02-19"

#fetch historical data
data = yf.download("AAPL", start="2024-02-17", end="2026-02-19")

#CHECK IF DATA IS EMPTY
if data.empty:
    print("No data downloaded.check ticker or connection.")
else:
    # fix multiIndex access
    data["SMA50"] = data["Close"].rolling(window=20).mean()
    print(data.tail())


#Display first few rows
print(data.head())

#yf.download(ticker,start=start_date,end=end_date)downloads historical stock data for the given ticker and date range.
#this is done to backtest trading strategies using historical data.to analyze price trends,volatility and other market characteristics

#step4:calculate techinical indicators
#indicators help indentify trends and generate trading signals.moving averages smooth out the price data over a set number of days,making it easier to indentify trends and filter out short-term noise.
#Simple Moving Averages(SMA):
#1SMA50(short-term trend)
#SMA200(long-term trend)
#2.use rolling().mean()to compute the averages over a specified window.
##calculate simple moving averages
short_window = 50 #short-term SMA
long_window =200 #long-term SMA

#data["SMA50"] = data["close"].rolling(window=short_window).mean()
#Assuming you are only fetchimg one ticker (AAPL)
data["SMA50"] = data["Close"]["AAPL"].rolling(window=short_window).mean()
data["SMA200"] = data["Close"].rolling(window=long_window).mean()

#step5:Define Buy/sell signals
#why are signals are used:
#.helps in making trading decisions based on historical trends
#.A clear visual guide for when to enter or exit the market based on crossovers

#.Trading signals are created based on SMA crossover:
#..Buy signal(1):when SMA50>SMA200.
#...sells ignal(-1):when SMA50<SMA200
#Define signals
data["Signal"] = 0 #Initialize signal column with 0
data.loc[data["SMA50"] > data["SMA200"], "Signal"] = 1 #Buy
data.loc[data["SMA50"] < data["SMA200"], "Signal"] = -1 #Sell

#explantion:Signal column is updated with 1 for buy and -1 for sale based on the conditions

#step6:Simulate trades
#Simulate the strategy by calculating daily and cumulative returns.
#create positions (shift signals to avoid look-ahead bias)
data["Position"] = data["Signal"].shift(1)

#Calculate daily percentage change in stock prices
data["Daily Return"] = data["Close"].pct_change()

#calculate returns based on the strategy
data["Strategy Return"] = data["Position"] * data["Daily Return"].cumprod()
#data["Cumulative Strategy Return"] = (1 + data[Strategy Return"]).cumprod()

#calculate cumulative returns
data["Cumulative Market Return"] = (1 + data["Daily Return"]).cumprod()
data["Cumulative Strategy Return"] = (1 + data["Strategy Return"]).cumprod()
#Explanation:
#Position:reflects the previous day's signal
#Daily Returns:the percentage in stock price from the previous day.
#Strategy Returns:returns achieved using the trading strategy.
#Cumulative returns:tracks the growth of $1 invested.

#step7:Visualize data
#visualize the stock price,SMA and returns to better understand the strategy.
#(a)Plot Stock Price and SMAs:
plt.rcParams["figure.figsize"] = (14, 7)
#plt.figure(figsiz=(14,7))
plt.plot(data["Close"],label="Close price",alpha=0.5)
plt.plot(data["SMA50"],label="SMA50",alpha=0.75)
plt.plot(data["SMA200"],label="SMA200",alpha=0.75)
plt.title(f"{ticker} Price and Moving Avarages")
plt.legend()
plt.show()

#(b)Plot Cumulative Returns:
plt.figure(figsiz=(14,7))
plt.plot(data["Cumulative Market Return"],label="Market Return",alpha=0.75)
plt.plot(data["Cumulative Strategy Return"],label="Strategy Return",alpha=0.75)
plt.title("Cumulative Returns")
plt.legend()
plt.show()
#Explanation:
#visualizing SMAS:helps in indentifying buy/sell zones when SMA50 crosses above or below SMA200
#Cumulative Returns Plot:Compares how the strategy performs against holding the stock without any active trading strategy.

#step8:Evaluate Performance
#compare the cumulative returns of the strategy vs.holding the market
total_strategy_return = data["Strategy Return"].iloc[-1] -1
total_market_return = data["Cumulative Market Return"].iloc[-1] -1

print(f"Total Strategy Return: {total_strategy_return:.2%}")
print(f"Total Market Return: {total_market_return:.2%}")
#why is this step is important:
#:measures the profitability of the trading strategy against a buy-and-hold approach.
#helps evaluate how well the strategy performs on historical data provides a risk-adjusted returns.
