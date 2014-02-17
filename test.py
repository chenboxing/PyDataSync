#__author__ = 'chenbox'
##import datetime
#import time
#
#s = '20110811'
#fmt = '%Y%m%d'
#t = time.strptime(s, fmt)
#print(t.strftime('%b %d %Y',t))

import sqlite3
import sys
import os

def connect_db():
    """Returns a new connection to the sqlite database"""
    return sqlite3.connect(app.config['DATABASE'], detect_types=sqlite3.PARSE_DECLTYPES)


