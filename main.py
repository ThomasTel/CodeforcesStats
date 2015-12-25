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

def random_color():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())

d = {}
fr = io.open('ratings_treated_code.csv', 'r', encoding='utf8')
ratings = []
people = []
for s in fr.read().splitlines():
   x = s.split(';')
   x[1] = int(x[1])
   x[2] = int(x[2])
   d[x[0]] = [x[1], x[2]]
   ratings.append(x[1])
   people.append(x[2])
print np.mean(ratings), np.std(ratings)
fr.close()

tree = etree.parse('Codeforces_rating.svg')
root = tree.getroot()[0]
for child in root:
   if 'id' in child.attrib and child.attrib['id'] in d:
      color = random_color()
      for path in child.iter('{http://www.w3.org/2000/svg}path'):
         path.attrib['fill'] = color

tree.write('Codeforces_rating_treated.svg')