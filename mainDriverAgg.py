#!/usr/bin/python3

import io
import time
import os, sys
import json
from pprint import pprint
from aggregator import Aggregator
from analyzer import Analyzer

def main():
  '''main class to handle stock data'''
  print ("Adding tickers")
  stk = Aggregator()
  # anal = Analyzer()

  stk.addTicker('AMD', True)
  stk.addTicker('AAPL', True)
  stk.addTicker('BABA', True)
  stk.addTicker('AMZN', True)
  stk.addTicker('NVDA', True)
  stk.addTicker('FIVN', True)
  stk.addTicker('VZ', True)
  stk.addTicker('T', True)
  stk.addTicker('ZM', True)
  stk.addTicker('WORK', True)
  stk.addTicker('TSLA')


  # build stock data
  print("Building stock data")
  stk.buildStockData()

  # Write stock data to JSON file
  print("Writing data")
  stk.writeToJSON()
  print ("Data has been written!")
  time.sleep(2)

  print('Formatting data')
  stk.formatData()
  print('Data has been Formatted')
  

if __name__ == '__main__':
  main()