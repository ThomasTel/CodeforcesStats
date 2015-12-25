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
   s = 255*s/maxi
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
   x[2] = int(x[2])/float(pop[x[0]])
   d[x[0]] = x[1], x[2]
   ratings.append(x[1])
   people.append(x[2])
   print x[0], people[-1]
fr.close()
minPeople = min(people)
maxPeople = max(people)

tree = etree.parse('Codeforces_rating.svg')
root = tree.getroot()[0]
for child in root:
   if 'id' in child.attrib and (child.attrib['id'] in d or not child.attrib['id'] in ['lakes', 'gl']):
      s = d[child.attrib['id']][1] if child.attrib['id'] in d else 0
      color = scolor(minPeople, maxPeople, s)
      for path in child.iter('{http://www.w3.org/2000/svg}path'):
         path.attrib['fill'] = color

tree.write('geek.svg')