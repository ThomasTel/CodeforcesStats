#!/usr/bin/env python
# coding: utf-8 
from __future__ import unicode_literals
from lxml import etree
from bs4 import BeautifulSoup
import re
import unicodedata
import sys  
import random
import io
import numpy as np

def scolor(mini, maxi, s):
   r = lambda x : min(255, 2*x)
   g = lambda x : r(255-x)
   s = 255*(s-mini)/(maxi-mini)
   return '#%02X%02X%02X' % (r(s),g(s),0)

fr = io.open('POP.csv', 'r', encoding='utf8')
pop = {}
for s in fr.read().splitlines():
   x = s.split(';')
   pop[x[0].lower()] = int(x[1])
fr.close()

d = {}
fr = io.open('ratings_treated_code.csv', 'r', encoding='utf8')
ratings = []
people = []
for s in fr.read().splitlines():
   x = s.split(';')
   x[1] = int(x[1])
   x[2] = int(x[2])
   d[x[0]] = x[1], x[2]
   ratings.append(x[1])
   people.append(x[2])
fr.close()
for k, (a, b) in d.items():
   if b < pop[k] / 5000000:
      del d[k]
minRating = min(ratings) - 50
maxRating = max(ratings)

tree = etree.parse('Codeforces_rating.svg')
root = tree.getroot()[0]
for child in root:
   if 'id' in child.attrib and (child.attrib['id'] in d or not child.attrib['id'] in ['lakes', 'gl']):
      s = int(d[child.attrib['id']][0]) if child.attrib['id'] in d else minRating
      color = scolor(minRating, maxRating, s)
      for path in child.iter('{http://www.w3.org/2000/svg}path'):
         path.attrib['fill'] = color

tree.write('Codeforces_rating_treated.svg')