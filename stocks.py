import os
import sys
import yfinance as yf

def getClosingPrice(symbol):
  ticker = yf.Ticker(symbol)
  return ticker.history()['Close'][21]

def t(symbol):
  ticker = yf.Ticker(symbol)
  history = ticker.history(period="max")['Close']
  todayClose = history[-22:][-1]
  thirtyDayClose = history[-22:][0]
  return (todayClose - thirtyDayClose) / thirtyDayClose

print(t("TSLA"))
