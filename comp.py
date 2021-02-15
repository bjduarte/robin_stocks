#!/usr/bin/python3

import robin_stocks as r
import numpy as np
import math
import io
import sys
import os
import fnmatch
import datetime
import time
import json


class Comp:

  def __init__(self):
    self.stocks = {} # dictionary of stock data sorted by symbol
    self.currentValues = []
    self.previousValues = []
    self.numOfFiles = 0
    self.numOfTickers = 0

    # Login to Robin Hood Account
    username = 'bryanduarte@me.com'
    password = 'Masterman1$'
    login = r.login(username,password)


# reads in stock data from JSON into a dictionary of lists
  def readInData(self):
    listOfStocks = []
    p = ''
    for file in os.listdir('./stockData'):
      if fnmatch.fnmatch(file, '*.json'):
        self.numOfFiles += 1 
        path = p.join(("./stockData/",file))
        # print('Files: ', path)
        f = open(path, 'r')
        self.stocks = json.load(f)
        listOfStocks.append(self.stocks)

# extracts a single dictionary
#  gets the current price from the most recent query
    for price in listOfStocks[0].get('current price'):
      self.currentValues.append(float(price[0]))
    print('Current Values: ', len(self.currentValues))

# extracts a single dictionary
# gets the current price from the previous query
    for price in listOfStocks[1].get('current price'):
      self.previousValues.append(float(price[0]))
    print('Previous values: ', len(self.previousValues))

    f.close()


# computes the change between the last two querys  for each holding
  def computeChange(self):
    # computes the difference between each value in the current and previous lists
    # rounds the result to 2 decimal places
    # produces a list of tuples containing the stocks above or below 3.00
    amountChanged = [(a, round(i - j, 2)) for a, i, j in zip(self.stocks.get('stock ticker'), self.previousValues, self.currentValues) if (i-j) <= -3.00 or (i-j) >= 3.00]

    print('Stocks above or below 3.00: ')
    for val in amountChanged:
      print(val, '\n')



if __name__ == '__main__':
  test = Comp()
  print('Reading data')
  test.readInData()
  print('Data read')
  print('Computing Change')
  test.computeChange()
  print('Change Computed')  

