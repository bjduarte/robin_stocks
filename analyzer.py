#!/usr/bin/python3

import robin_stocks as r
import math
import io
import sys
import os
import fnmatch
import datetime
import time
import json


class Analyzer:

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


# reads in stock data from JSON 
  def readInData(self):
    for file in os.listdir('./stockData'):
      if fnmatch.fnmatch(file, '*.json'):
        with open(file, 'r') as f:
          data = json.load(f)

          self.lastPrices = data.get('current price')
          amtChange = []
          for newAmt in self.prices:
            for oldAmt in self.lastPrices:
              print("New Price: ", newAmt, '\n')
              print("Old Price: ", oldAmt, '\n')
          # amtChange.append(math.fabs(oldAmt - newAmt))
#           # print(amtChange)

# # displays current holdings
#   def holdings(self):
#     myHoldings = r.build_holdings()
#     for key,value in my_stocks.items():
#       print(key,value)
#
