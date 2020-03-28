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
    self.stockData = {} # dictionary for working with positions
    self.myHoldings = {} # dictionary for displaying positions


  def readData(self):
    # reading in current data
    for file in os.listdir('.'):
      if fnmatch.fnmatch(file, 'stockData.json'):
        f = open(file, 'r')
        self.stockData = json.load(f)
        f.close()

    for file in os.listdir('.'):
      if fnmatch.fnmatch(file, 'myHoldings.json'):
        f = open(file, 'r')
        self.myHoldings = json.load(f)
        f.close()


  # Adds a position to holdings
  def addPosition(self, symb, quanity, price):
    self.readData()
    lot = (quanity, price)
    position = self.stockData.get(symb)

    # check to see if position currently exists
    # append if exists, create new if not
    if symb in self.stockData:
      print(symb, ': found! Adding lot to current holding...')
      position.append(lot)
      self.stockData[symb] = position
      print(self.stockData)
    else:
      print(symb, ': Not found! Creating new holding...')
      self.stockData[symb] = [lot]
      print(self.stockData)


  # Removes a position from holdings
  def removeHolding(self, symb):
    self.readData()
    print('Searching your holdings for: ', symb)

    # check to see if position exists
    if symb in self.stockData:
      print(symb, '- found! removing...')
      del self.stockData[symb]
      print(symb, ': Holding removed!\n', self.stockData)
    else:
      print(symb, ': Position not found!')


    # remove a lot from position
  def removePosition(self, symb, quanity, price):
    self.readData()
    lot = [quanity, price]
    position = self.stockData.get(symb)
    removeLot = position.index(lot)
    print('Searching your holdings for: ', symb)

    # check for symbol in holdings
    if symb in self.stockData:
      print(symb, '- found!')

      position.pop(removeLot)
      self.stockData[symb] = position
      print(symb, 'position updated: \n', position)

    else:
      print(symb, 'Symbol not found!')
      
    return len(position)


  # calculates the net price of each position
  def netPrice(self):
    position = self.stockData.values()
    lots = [i for i in position]
    netPrice = []

    for lot in position:
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

    # building a dictionary for pretty printing
    symb = [i for i in self.stockData.keys()]
    self.myHoldings = {'ticker': symb, 'lot': lots, 'netPrice': netPrice}



  # writes both dictionaries to json file
  # myHoldings.json contains dict for pretty printing
  # stockData.json contains bict for operations
  def writeData(self):
    with open('myHoldings.json', 'w') as f:
      json.dump(self.myHoldings, f)
    f.close()

    with open('stockData.json', 'w') as f:
      json.dump(self.stockData, f)
    f.close()


  # write stock data into a human readable format
  def formatData(self):
    self.readData()
    fin = self.myHoldings

    dataLine = zip_longest(fin.get('ticker'), fin.get('lot'), fin.get('netPrice'), fillvalue=' - ')
    fout = open('myHoldings.txt', "w")
    fout.write('Position \t|\t Lot: \t|\t Net Price: \t\n')
    for data in dataLine:
      fout.write(str(data) + "\n")
    fout.close()


  def displayHoldings(self):
    self.readData()
    fin = self.myHoldings

    if len(fin) != 0:
      dataLine = zip_longest(fin.get('ticker'), fin.get('lot'), fin.get('netPrice'), fillvalue=' - ')
      print('Position \t|\t Lot: \t|\t Net Price: \t\n')
      for data in dataLine:
        print(str(data) + "")
    else:
      print('No holdings found!')


  def displayMenu(self):
    print('Make your selection: ')
    selection = input('1. Add position \n 2. Remove position \n 3. Update position \n 4. Display holdings \n 5. Exit\n')

    return selection


if __name__ == "__main__":
  mh = MyHoldings()


  option = mh.displayMenu()
  while True:
    if option == '1':
      while True:
        try:
          symb = input("Enter stock ticker: ").upper()
          quanity = int(input('Enter the number of shares: '))
          price = float(input('Enter the purchase price: '))

          mh.addPosition(symb, quanity, price)
          mh.netPrice()
          print('Writing data')
          mh.writeData()
          print('Formating data')
          mh.formatData()
          break

        except ValueError as ve:
          print('Error! ', type(ve), ': ', ve)

    elif option == '2':
      while True:
        try:
          symb = input("Enter stock ticker: ").upper()
          mh.removeHolding(symb)
          mh.netPrice()
          mh.writeData()
          break

        except ValueError as ve:
          print('Error! ', type(ve), ': ', ve)

    elif option == '3':
      while True:
        try:
          symb = input("Enter stock ticker: ").upper()
          sd = mh.stockData.get(symb)
          print('Here is your current holding: ', sd)
          
          quanity = int(input('Enter quanity to remove'))
          price = float(input('Enter price to remove'))
          position = mh.removePosition(symb, quanity, price)
          if position == 0:
            print('Holding is empty, removing holding!')
            mh.removeHolding(symb)
            mh.writeData()
            break
          else:
            mh.netPrice()
            mh.writeData()
            break

        except ValueError as ve:
          print('error: ', type(ve), ve)

    elif option == '4':
      mh.displayHoldings()
    elif option == '5':
      print('Exiting...')
      print("Done!")
      break
    else:
      print(option, "is an invalid option! Enter 1, 2, 3, 4, or 5\n")

    option = mh.displayMenu()


