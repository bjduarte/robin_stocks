#!/usr/bin/python3

import numpy as np
import io
import sys
import os
import fnmatch
import datetime
import time
import json
from itertools import zip_longest

class MyHoldings:

  def __init__(self):
    # self.holdings = []
    # self.batch = ()
    self.myHoldings = {}
    self.stockData = {}


  def addPosition(self, symb, quanity, price):
    batch = (quanity, price)
    holdings = self.myHoldings.get(symb)

    if symb in self.myHoldings:
      holdings.append(batch)
      self.myHoldings[symb] = holdings
      # print('Updating: ', batch)
      # print('Current: ', self.myHoldings.get(symb))
    else:
      self.myHoldings[symb] = [batch]
      # print('Adding: ', batch)
      # print('Current: ', self.myHoldings.get(symb))


  def netPrice(self):
    holdings = self.myHoldings.values()
    netPrice = []
    lots = [i for i in holdings]

    for lot in holdings:
      # split shares into individual list
      getShares = [j[0] for j in lot]

      # split prices into individual list
      getPrice = [j[1] for j in lot]

      # computing the total price of each batch of shares purchased 
      products = [share * price for share, price in zip(getShares, getPrice)]

      # calculating the total number of shares purchased
      numOfShares = np.sum(getShares)

      # calculating the total price for all shares
      totalPrice = np.sum(products)

      # calculating the netPrice of each stock holding
      netPrice.append((totalPrice / numOfShares))
      # print('netprice: ', netPrice)

    # building the dictionary to be written
    symb = [i for i in self.myHoldings.keys()]
    self.stockData = {'ticker': symb, 'lot': lots, 'netPrice': netPrice}


  def writeData(self):
    with open('myHoldings.json', 'w') as f:
      json.dump(self.stockData, f)
    f.close()


# format stock data into human readable text
  def formatData(self):
    for file in os.listdir('.'):
      if fnmatch.fnmatch(file, 'myHoldings.json'):
        f = open(file, 'r')
        fin = json.load(f)
        f.close()

        line1 = zip_longest(fin.get('ticker'), fin.get('lot'), fin.get('netPrice'), fillvalue=' - ')
        fout = open('myHoldings.txt', "w")
        fout.write('Stock Ticker: \t|\t Lot: \t|\t Net Price: \t\n')
        for data in line1:
          fout.write(str(data) + "\n")
        fout.close()


if __name__ == "__main__":
  mh = MyHoldings()

  flag = True
  print("Enter your position: ")
  while flag:
    try:
      symb = input("Enter stock ticker: ")
      quanity = int(input('Enter the number of shares: '))
      price = float(input('Enter the purchase price: '))
      mh.addPosition(symb, quanity, price)
    except ValueError:
      print('Sorry! Invalid value! Please re-enter your position')
      symb = input("Enter stock ticker: ")
      quanity = int(input('Enter the number of shares: '))
      price = float(input('Enter the purchase price: '))
    else:
      exit = input("Enter another? (y or n)")
      if exit == 'n':
        flag = False
      else:
        continue

      mh.netPrice()
  print('Writing data')
  mh.writeData()

  print('Formating data')
  mh.formatData()

  print("Done!")


