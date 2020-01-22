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
    self.allData = []
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


# reads in stock data from JSON into a dictionary of lists
  def readInData(self):
    p = ''
    for file in os.listdir('./stockData'):
      if fnmatch.fnmatch(file, '*.json'):
        path = p.join(("./stockData/",file))
        f = open(path, 'r')
        self.stocks = json.load(f)
        self.allData.append(self.stocks)
        f.close()


# computes the change of stocks
  def computeChange(self):
    numOfFiles = len(self.allData)
    numOfTickers = len(self.allData[0].get('current price'))
    # files = 0
    # j = 1
    tempList = []
    tempList2 = []
    for data in range(0, numOfTickers):
      for files in range(0, numOfFiles):
        if data < numOfTickers and files == 0:
          tempList.append(float(self.allData[files].get('current price')[data][0]))
          print('Temp List1: ', tempList[data])
        elif data < numOfTickers and files > 0:
          tempList2.append(float(self.allData[files].get('current price')[data][1]))
          print('Temp list2: ', tempList2[data])

    res = [list(math.fabs(a - z) for a in tempList2) for z in tempList]
    # print(tempList[0])
    # print(tempList2[0])
    # print(res[0][0])

    if len(tempList2) > numOfTickers:
      amtChange = [list(math.fabs(a - z) for a in tempList2) for z in res[0]]
      print(amtChange[0][0])

# Output = [Input1[i]-Input2[i] if Input1[i] > Input2[i] \
          # else Input1[i] for i in range(len(Input1))]



# tempList = [list(map(lambda ele - ele, sub)) for sub in test_list]


# keeps iterator from exceeding number of files
        # num2 = self.allData[j].get('current price')[data]
        # if j >= (numOfFiles-1):
        #   j = 1
        # else:
        #   j += 1




# # displays current holdings
#   def holdings(self):
#     myHoldings = r.build_holdings()
#     for key,value in my_stocks.items():
#       print(key,value)

