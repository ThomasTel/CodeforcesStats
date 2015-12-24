#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals
import io
import sys
import json

with io.open('ratings.json', 'r', encoding='utf8') as f:
   data = json.loads(f.readline().encode('utf8'))
   data_ = {}
   for x in data['result']:
      if 'country' in x and 'maxRating' in x :
         if not x['country'] in data_:
            data_[x['country']] = []
         data_[x['country']].append(x['maxRating'])
   for x, y in data_.items():
      print x, 
      for a in y:
         print a,
      print ''