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


p = ''
for file in os.listdir('./stockData'):
  if fnmatch.fnmatch(file, '*.json'):
    path = p.join(("./stockData/",file))
    print(path)
    f = open(path, 'r')
    fin = json.load(f)
    f.close()


    line1 = zip(fin.get('stock ticker'), fin.get('current price'),fin.get('days open'))
    line2 = zip(fin.get('days high'), fin.get('days low'), fin.get('days volume'))
    line3 = zip(fin.get('52 week high'), fin.get('52 week low'), fin.get('average volume'), fin.get('2 week volume'))


# breaking stock data into separate lines for displaying output
    pp = ''
    today = datetime.datetime.today()
    filename = ('data-{:%a %b %d,%Y-%H-%M}'.format(today))
    pathToFile = pp.join(('stockData/',filename))
    fout = open(pathToFile, "w+")

    fout.write('stock ticker \t| current price \t| days open\n')
    for data1 in line1:
      fout.write(str(data1) + "\n")

    fout.write('days high \t| days low \t| days volume\n')
    for data2 in line2:
      fout.write(str(data2) + "\n")

    fout.write('52 week high \t| 52 week low \t| average volume \t| 2 week volume\n')
    for data3 in line3:
      fout.write(str(data3) + "\n")
    fout.close()
print('Data written')
