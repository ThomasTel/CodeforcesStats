#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals
import io
import sys

d = {}
fr = io.open('code.csv', 'r', encoding='utf8')
for s in fr.read().splitlines():
   x = s.split(';')
   d[x[0].lower()] = x[1].lower()
fr.close()
fr = io.open('ratings_treated.csv', 'r', encoding='utf8')
fw = io.open('ratings_treated_code.csv', 'w', encoding='utf8')
for s in fr.read().splitlines():
   x = s.split(';')
   if not x[0].lower() in d:
      print x[0]
   else:
      fw.write(d[x[0].lower()] + ';' + str(x[1]) + ';' + str(x[2]) + '\n')
fr.close()
fw.close()