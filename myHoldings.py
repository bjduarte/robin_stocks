#!/usr/bin/python3

import numpy as np
import io
import sys
import os
import fnmatch
import datetime
import time
import json

class MyHoldings:

  def __init__(self):
    # self.holdings = []
    # self.batch = ()
    self.myHoldings = {}


  def addBatch(self, symb, quanity, price):
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

    for i in holdings:
      # split shares into individual list
      getShares = [j[0] for j in i]

      # split prices into individual list
      getPrice = [j[1] for j in i]

      # computing the total price of each batch of shares purchased 
      products = [share * price for share, price in zip(getShares, getPrice)]

      # calculating the sum of shares purchased
      numOfShares = np.sum(getShares)

      # calculating the total of prices
      totalPrice = np.sum(products)

      # calculating the netPrice of each stock holding
      netPrice = (totalPrice / numOfShares)
      print('Net Price: ', netPrice)



if __name__ == "__main__":
  mh = MyHoldings()

  mh.addBatch('AAPL', 2, 200)
  mh.addBatch('AAPL', 3, 300)
  mh.addBatch('AAPL', 4, 400)

  mh.addBatch('AMD', 5, 50)
  mh.addBatch('AMD', 6, 60)

  mh.addBatch('AMZN', 1, 1900)

  mh.netPrice()
