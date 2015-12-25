#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals
import io
import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

with io.open('ratings.json', 'r', encoding='utf8') as f:
   data = json.loads(f.readline().encode('utf8'))
   ratings = []
   for x in data['result']:
      if 'country' in x and 'maxRating' in x :
         ratings.append(int(x['maxRating']))
   d = {}
   for x in ratings:
      if not x in d:
         d[x] = 0
      d[x] += 1
   items = zip(*sorted(d.items()))
   plt.plot(items[0], items[1], linewidth=0.2)
   plt.xlabel('maxRating')
   plt.ylabel('number')
   plt.axis([0, 4000, 0, 100])
   plt.show()
   