#coding:utf8

import urllib
import json
import sys

def req(r):
    print r
    q = urllib.urlopen(r)
    s = q.read()
    try:
        l = json.loads(s)
        print l
    except:
        print "error\n"
        sys.stderr.write(r+'\n'+s+'\n')
    return l

BASE = 'http://localhost:5000/'

r = BASE+'updateScore?uid=%d&newScore=%d' % (0, 30)
l = req(r)

r = BASE+'getRank?score=50'
l = req(r)

r = BASE+'getUser?rank=1'
l = req(r)

r = BASE+'getRange?start=10&end=20'
l = req(r)

