#!/usr/bin/python3

import io
import time
import datetime
import json
from pprint import pprint
from aggregator import Aggregator
from analyzer import Analyzer

def main():
  '''main class to handle stock data'''
  
  anal = Analyzer()

  print("Reading in JSON")
  anal.readInData()
  print("Data has been read into dictionary")


if __name__ == '__main__':
  main()