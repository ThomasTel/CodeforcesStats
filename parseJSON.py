#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals
import io
import sys
import json
from operator import itemgetter
 
with io.open('ratings.json', 'r', encoding='utf8') as f:
   data = json.loads(f.readline().encode('utf8'))
   data_ = {}
   for x in data['result']:
      if 'country' in x and 'maxRating' in x :
         if not x['country'] in data_:
            data_[x['country']] = []
         data_[x['country']].append(x['maxRating'])
   data = []
   for x, y in data_.items():
      data.append((x, sum(y) / len(y), len(y)))
   for x, y, z in sorted(data, key = itemgetter(1), reverse=True):
      print x + ';' + str(y) + ';' + str(z)
   