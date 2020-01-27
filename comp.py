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
    self.prices = []
    self.lastPrice = []
    self.numOfFiles = 0
    self.numOfTickers = 0

    # Login to Robin Hood Account
    username = 'bryanduarte@me.com'
    password = 'Masterman1$'
    login = r.login(username,password)


# reads in stock data from JSON into a dictionary of lists
  def readInData(self):
    p = ''
    for file in os.listdir('./stockData'):
      if fnmatch.fnmatch(file, '*.json'):
        self.numOfFiles += 1 
        path = p.join(("./stockData/",file))
        f = open(path, 'r')
        self.stocks = json.load(f)

        k = 3
        if self.numOfFiles == 1:
          temp = self.stocks.get('current price')

          for i in temp:
            for j in i:
              self.lastPrice.append(float(j))
        elif self.numOfFiles == 2:
          temp = self.stocks.get('current price')

          for i in temp:
            for j in i:
              self.prices.append(float(j))

        if k <= self.numOfFiles:
          self.lastPrice = self.temp
          temp = self.stocks.get('current price')
          
          for i in temp:
            for j in i:
              self.prices.append(float(j))

        f.close()


# computes the change of stocks
  def computeChange(self):

    for i in range(2, self.numOfFiles):
      res = np.subtract(np.array(self.lastPrice), np.array(self.prices))
      print('List 1, list 2: ', res)




if __name__ == '__main__':
  test = Comp()
  print('Reading data')
  test.readInData()
  print('Data read')
  print('Computing Change')
  test.computeChange()
  print('Change Computed')  

