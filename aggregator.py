#!/usr/bin/python3

import robin_stocks as r
import robin_stocks.helper as helper
import robin_stocks.urls as urls
import math
import io
import sys
import os
import fnmatch
import datetime
import time
import json


class Aggregator:

  def __init__(self):
    self.stocks = {} # dictionary of stock data sorted by symbol
    self.watchlist = [] 
    self.holdings = []
    self.tickers = []
    self.prices = []
    self.lastPrices = []
    self.stockData = [] 
    self.dOpen = []
    self.dHigh = []
    self.dLow = []
    self.high52 = []
    self.low52 = []
    self.dVolume = []
    self.avgVolume = []
    self.volume2 = []

    # Login to Robin Hood Account
    username = 'bryanduarte@me.com'
    password = 'Masterman1$'
    login = r.login(username,password)


#adds a new stock ticker symbol to the list
  def addTicker(self, symbol, myList=False):
    if myList == True:
      self.holdings.append(symbol)
      self.watchlist.append(symbol)
      self.holdings.sort()
      self.watchlist.sort()
    else:
      self.watchlist.append(symbol)
      self.watchlist.sort()


# removes a stock ticker symbol from the list
  def removeTicker(self, symbol, myList = False):
    if myList == True:
      self.holdings.remove(symbol)
    else:
      self.watchlist.remove(symbol)



  def buildStockData(self):
    # stockData = r.get_historicals(self.watchlist,span='day',bounds='regular')

# pulling stock data into lists
    for ticker in self.watchlist:
      self.tickers.append(r.get_name_by_symbol(ticker))
      self.prices.append(r.get_latest_price(ticker))
      self.stockData.append(r.get_fundamentals(ticker))

# extracts specified data from fundamentals list and appends it to individual lists
    for stk in self.stockData:
      data = stk[0]
      self.dOpen.append(data['open'])
      self.dHigh.append(data['high'])
      self.dLow.append(data['low'])
      self.high52.append(data['high_52_weeks'])
      self.low52.append(data['low_52_weeks'])
      self.dVolume.append(data['volume'])
      self.avgVolume.append(data['average_volume'])
      self.volume2.append(data['average_volume_2_weeks'])

# builds a dictionary of stocks and their respective data
    self.stocks = {
      'stock ticker': self.tickers,
      'current price': self.prices,
      'days open': self.dOpen,
      'days high': self.dHigh,
      'days low': self.dLow,
      '52 week high': self.high52,
      '52 week low': self.low52,
      'days volume': self.dVolume,
      'average volume': self.avgVolume,
      '2 week volume': self.volume2}


# writes stock data to JSON file
  def writeToJSON(self):
    p = ''
    today = datetime.datetime.today()
    filename = ('data-{:%a-%b-%d,%Y-%H-%M}.json'.format(today))
    pathToFile = p.join(('stockData/',filename))
    with open(pathToFile, 'w') as f:
      json.dump(self.stocks, f)
      f.close()


# format stock data into human readable text
  def formatData(self):
    p = ''
    for file in os.listdir('./stockData'):
      if fnmatch.fnmatch(file, '*.json'):
        path = p.join(("./stockData/",file))
        f = open(path, 'r')
        fin = json.load(f)
        f.close()

    # Breaking data points into separate lines
        line1 = zip(fin.get('stock ticker'), fin.get('current price'),fin.get('days open'))
        line2 = zip(fin.get('days high'), fin.get('days low'), fin.get('days volume'))
        line3 = zip(fin.get('52 week high'), fin.get('52 week low'), fin.get('average volume'), fin.get('2 week volume'))

    # Writing column headings and data points for each section
        pp = ''
        today = datetime.datetime.today()
        filename = ('data-{:%a-%b-%d,%Y-%H-%M}'.format(today))
        pathToFile = pp.join(('stockData/',filename))
        fout = open(pathToFile, "w+")

    # section 1 data
        fout.write('stock ticker \t| current price \t| days open\n')
        for data1 in line1:
          fout.write(str(data1) + "\n")

    # section 2 data
        fout.write('days high \t| days low \t| days volume\n')
        for data2 in line2:
          fout.write(str(data2) + "\n")

    # section 3 data
        fout.write('52 week high \t| 52 week low \t| average volume \t| 2 week volume\n')
        for data3 in line3:
          fout.write(str(data3) + "\n")
        fout.close()

